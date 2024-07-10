from __future__ import annotations

import logging
import os
import warnings
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
    cast,
)

import numpy as np
from langchain_core._api.deprecation import deprecated
from langchain_core.embeddings import Embeddings
from langchain_core.pydantic_v1 import BaseModel, Extra, Field, root_validator
from langchain_core.utils import get_from_dict_or_env, get_pydantic_field_names
from tenacity import (
    AsyncRetrying,
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from langchain_community.utils.openai import is_openai_v1

logger = logging.getLogger(__name__)


from langchain_huggingface import HuggingFaceEmbeddings
from typing import List    

class HFEmbeddings(HuggingFaceEmbeddings):
    def embed_query(self, text: str) -> List[float]:
        task = 'Given a question, retrieve passages that answer the question'
        prompt = f"Instruct: {task}\nQuery: "
        """Compute query embeddings using a HuggingFace transformer model.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        return self.embed_documents([text])[0]
from typing import Any, Dict, List, Optional

from langchain_core.embeddings import Embeddings


class LlamaCppEmbeddings(BaseModel, Embeddings):
    """llama.cpp embedding models.

    To use, you should have the llama-cpp-python library installed, and provide the
    path to the Llama model as a named parameter to the constructor.
    Check out: https://github.com/abetlen/llama-cpp-python

    Example:
        .. code-block:: python

            from langchain_community.embeddings import LlamaCppEmbeddings
            llama = LlamaCppEmbeddings(model_path="/path/to/model.bin")
    """

    client: Any  #: :meta private:
    model_path: str

    n_ctx: int = Field(8192, alias="n_ctx")
    """Token context window."""

    n_parts: int = Field(-1, alias="n_parts")
    """Number of parts to split the model into. 
    If -1, the number of parts is automatically determined."""

    seed: int = Field(-1, alias="seed")
    """Seed. If -1, a random seed is used."""

    f16_kv: bool = Field(False, alias="f16_kv")
    """Use half-precision for key/value cache."""

    logits_all: bool = Field(False, alias="logits_all")
    """Return logits for all tokens, not just the last token."""

    vocab_only: bool = Field(False, alias="vocab_only")
    """Only load the vocabulary, no weights."""

    use_mlock: bool = Field(False, alias="use_mlock")
    """Force system to keep model in RAM."""

    n_threads: Optional[int] = Field(None, alias="n_threads")
    """Number of threads to use. If None, the number 
    of threads is automatically determined."""

    n_batch: Optional[int] = Field(512, alias="n_batch")
    """Number of tokens to process in parallel.
    Should be a number between 1 and n_ctx."""

    n_gpu_layers: Optional[int] = Field(None, alias="n_gpu_layers")
    """Number of layers to be loaded into gpu memory. Default None."""

    verbose: bool = Field(True, alias="verbose")
    """Print verbose output to stderr."""

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator(allow_reuse=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that llama-cpp-python library is installed."""
        model_path = values["model_path"]
        model_param_names = [
            "n_ctx",
            "n_parts",
            "seed",
            "f16_kv",
            "logits_all",
            "vocab_only",
            "use_mlock",
            "n_threads",
            "n_batch",
            "verbose",
        ]
        model_params = {k: values[k] for k in model_param_names}
        # For backwards compatibility, only include if non-null.
        if values["n_gpu_layers"] is not None:
            model_params["n_gpu_layers"] = values["n_gpu_layers"]

        try:
            from llama_cpp import Llama
            import llama_cpp

            values["client"] = Llama(model_path, embedding=True, rope_freq_base=0, pooling_type=llama_cpp.LLAMA_POOLING_TYPE_NONE, **model_params)
        except ImportError:
            raise ImportError(
                "Could not import llama-cpp-python library. "
                "Please install the llama-cpp-python library to "
                "use this embedding model: pip install llama-cpp-python"
            )
        except Exception as e:
            raise ValueError(
                f"Could not load Llama model from path: {model_path}. "
                f"Received error {e}"
            )

        return values

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents using the Llama model.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        embeddings = [self.client.embed(text)[-1] for text in texts]
        return [list(map(float, e)) for e in embeddings]


    def embed_query(self, text: str) -> List[float]:
        """Embed a query using the Llama model.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        task = 'Given a question, retrieve passages that answer the question'
        prompt = f"Instruct: {task}\nQuery: "
        if type(text) == dict:
            text = text['input']
        embedding = self.client.embed(prompt+text)[-1]
        return list(map(float, embedding))


def _create_retry_decorator(embeddings: OpenAIEmbeddings) -> Callable[[Any], Any]:
    import openai

    # Wait 2^x * 1 second between each retry starting with
    # retry_min_seconds seconds, then up to retry_max_seconds seconds,
    # then retry_max_seconds seconds afterwards
    # retry_min_seconds and retry_max_seconds are optional arguments of
    # OpenAIEmbeddings
    return retry(
        reraise=True,
        stop=stop_after_attempt(embeddings.max_retries),
        wait=wait_exponential(
            multiplier=1,
            min=embeddings.retry_min_seconds,
            max=embeddings.retry_max_seconds,
        ),
        retry=(
            retry_if_exception_type(openai.error.Timeout)
            | retry_if_exception_type(openai.error.APIError)
            | retry_if_exception_type(openai.error.APIConnectionError)
            | retry_if_exception_type(openai.error.RateLimitError)
            | retry_if_exception_type(openai.error.ServiceUnavailableError)
        ),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )


def _async_retry_decorator(embeddings: OpenAIEmbeddings) -> Any:
    import openai

    # Wait 2^x * 1 second between each retry starting with
    # retry_min_seconds seconds, then up to retry_max_seconds seconds,
    # then retry_max_seconds seconds afterwards
    # retry_min_seconds and retry_max_seconds are optional arguments of
    # OpenAIEmbeddings
    async_retrying = AsyncRetrying(
        reraise=True,
        stop=stop_after_attempt(embeddings.max_retries),
        wait=wait_exponential(
            multiplier=1,
            min=embeddings.retry_min_seconds,
            max=embeddings.retry_max_seconds,
        ),
        retry=(
            retry_if_exception_type(openai.error.Timeout)
            | retry_if_exception_type(openai.error.APIError)
            | retry_if_exception_type(openai.error.APIConnectionError)
            | retry_if_exception_type(openai.error.RateLimitError)
            | retry_if_exception_type(openai.error.ServiceUnavailableError)
        ),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )

    def wrap(func: Callable) -> Callable:
        async def wrapped_f(*args: Any, **kwargs: Any) -> Callable:
            async for _ in async_retrying:
                return await func(*args, **kwargs)
            raise AssertionError("this is unreachable")

        return wrapped_f

    return wrap


# https://stackoverflow.com/questions/76469415/getting-embeddings-of-length-1-from-langchain-openaiembeddings
def _check_response(response: dict, skip_empty: bool = False) -> dict:
    if any(len(d["embedding"]) == 1 for d in response["data"]) and not skip_empty:
        import openai

        raise openai.error.APIError("OpenAI API returned an empty embedding")
    return response


def embed_with_retry(embeddings: OpenAIEmbeddings, **kwargs: Any) -> Any:
    """Use tenacity to retry the embedding call."""
    if is_openai_v1():
        return embeddings.client.create(**kwargs)
    retry_decorator = _create_retry_decorator(embeddings)

    @retry_decorator
    def _embed_with_retry(**kwargs: Any) -> Any:
        response = embeddings.client.create(**kwargs)
        return _check_response(response, skip_empty=embeddings.skip_empty)

    return _embed_with_retry(**kwargs)


async def async_embed_with_retry(embeddings: OpenAIEmbeddings, **kwargs: Any) -> Any:
    """Use tenacity to retry the embedding call."""

    if is_openai_v1():
        return await embeddings.async_client.create(**kwargs)

    @_async_retry_decorator(embeddings)
    async def _async_embed_with_retry(**kwargs: Any) -> Any:
        response = await embeddings.client.acreate(**kwargs)
        return _check_response(response, skip_empty=embeddings.skip_empty)

    return await _async_embed_with_retry(**kwargs)


@deprecated(
    since="0.0.9",
    removal="0.3.0",
    alternative_import="langchain_openai.OpenAIEmbeddings",
)
class OpenAIEmbeddings(BaseModel, Embeddings):
    """OpenAI embedding models.

    To use, you should have the ``openai`` python package installed, and the
    environment variable ``OPENAI_API_KEY`` set with your API key or pass it
    as a named parameter to the constructor.

    Example:
        .. code-block:: python

            from langchain_community.embeddings import OpenAIEmbeddings
            openai = OpenAIEmbeddings(openai_api_key="my-api-key")

    In order to use the library with Microsoft Azure endpoints, you need to set
    the OPENAI_API_TYPE, OPENAI_API_BASE, OPENAI_API_KEY and OPENAI_API_VERSION.
    The OPENAI_API_TYPE must be set to 'azure' and the others correspond to
    the properties of your endpoint.
    In addition, the deployment name must be passed as the model parameter.

    Example:
        .. code-block:: python

            import os

            os.environ["OPENAI_API_TYPE"] = "azure"
            os.environ["OPENAI_API_BASE"] = "https://<your-endpoint.openai.azure.com/"
            os.environ["OPENAI_API_KEY"] = "your AzureOpenAI key"
            os.environ["OPENAI_API_VERSION"] = "2023-05-15"
            os.environ["OPENAI_PROXY"] = "http://your-corporate-proxy:8080"

            from langchain_community.embeddings.openai import OpenAIEmbeddings
            embeddings = OpenAIEmbeddings(
                deployment="your-embeddings-deployment-name",
                model="your-embeddings-model-name",
                openai_api_base="https://your-endpoint.openai.azure.com/",
                openai_api_type="azure",
            )
            text = "This is a test query."
            query_result = embeddings.embed_query(text)

    """

    client: Any = Field(default=None, exclude=True)  #: :meta private:
    async_client: Any = Field(default=None, exclude=True)  #: :meta private:
    model: str = "text-embedding-ada-002"
    # to support Azure OpenAI Service custom deployment names
    deployment: Optional[str] = model
    # TODO: Move to AzureOpenAIEmbeddings.
    openai_api_version: Optional[str] = Field(default=None, alias="api_version")
    """Automatically inferred from env var `OPENAI_API_VERSION` if not provided."""
    # to support Azure OpenAI Service custom endpoints
    openai_api_base: Optional[str] = Field(default=None, alias="base_url")
    """Base URL path for API requests, leave blank if not using a proxy or service 
        emulator."""
    # to support Azure OpenAI Service custom endpoints
    openai_api_type: Optional[str] = None
    # to support explicit proxy for OpenAI
    openai_proxy: Optional[str] = None
    embedding_ctx_length: int = 8191
    """The maximum number of tokens to embed at once."""
    openai_api_key: Optional[str] = Field(default=None, alias="api_key")
    """Automatically inferred from env var `OPENAI_API_KEY` if not provided."""
    openai_organization: Optional[str] = Field(default=None, alias="organization")
    """Automatically inferred from env var `OPENAI_ORG_ID` if not provided."""
    allowed_special: Union[Literal["all"], Set[str]] = set()
    disallowed_special: Union[Literal["all"], Set[str], Sequence[str]] = "all"
    chunk_size: int = 1000
    """Maximum number of texts to embed in each batch"""
    max_retries: int = 2
    """Maximum number of retries to make when generating."""
    request_timeout: Optional[Union[float, Tuple[float, float], Any]] = Field(
        default=None, alias="timeout"
    )
    """Timeout for requests to OpenAI completion API. Can be float, httpx.Timeout or 
        None."""
    headers: Any = None
    tiktoken_enabled: bool = True
    """Set this to False for non-OpenAI implementations of the embeddings API, e.g.
    the `--extensions openai` extension for `text-generation-webui`"""
    tiktoken_model_name: Optional[str] = None
    """The model name to pass to tiktoken when using this class. 
    Tiktoken is used to count the number of tokens in documents to constrain 
    them to be under a certain limit. By default, when set to None, this will 
    be the same as the embedding model name. However, there are some cases 
    where you may want to use this Embedding class with a model name not 
    supported by tiktoken. This can include when using Azure embeddings or 
    when using one of the many model providers that expose an OpenAI-like 
    API but with different models. In those cases, in order to avoid erroring 
    when tiktoken is called, you can specify a model name to use here."""
    show_progress_bar: bool = False
    """Whether to show a progress bar when embedding."""
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Holds any model parameters valid for `create` call not explicitly specified."""
    skip_empty: bool = False
    """Whether to skip empty strings when embedding or raise an error.
    Defaults to not skipping."""
    default_headers: Union[Mapping[str, str], None] = None
    default_query: Union[Mapping[str, object], None] = None
    # Configure a custom httpx client. See the
    # [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
    retry_min_seconds: int = 4
    """Min number of seconds to wait between retries"""
    retry_max_seconds: int = 20
    """Max number of seconds to wait between retries"""
    http_client: Union[Any, None] = None
    """Optional httpx.Client."""

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid
        allow_population_by_field_name = True

    @root_validator(pre=True, allow_reuse=True)
    def build_extra(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Build extra kwargs from additional params that were passed in."""
        all_required_field_names = get_pydantic_field_names(cls)
        extra = values.get("model_kwargs", {})
        for field_name in list(values):
            if field_name in extra:
                raise ValueError(f"Found {field_name} supplied twice.")
            if field_name not in all_required_field_names:
                warnings.warn(
                    f"""WARNING! {field_name} is not default parameter.
                    {field_name} was transferred to model_kwargs.
                    Please confirm that {field_name} is what you intended."""
                )
                extra[field_name] = values.pop(field_name)

        invalid_model_kwargs = all_required_field_names.intersection(extra.keys())
        if invalid_model_kwargs:
            raise ValueError(
                f"Parameters {invalid_model_kwargs} should be specified explicitly. "
                f"Instead they were passed in as part of `model_kwargs` parameter."
            )

        values["model_kwargs"] = extra
        return values

    @root_validator(allow_reuse=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        values["openai_api_key"] = get_from_dict_or_env(
            values, "openai_api_key", "OPENAI_API_KEY"
        )
        values["openai_api_base"] = values["openai_api_base"] or os.getenv(
            "OPENAI_API_BASE"
        )
        values["openai_api_type"] = get_from_dict_or_env(
            values,
            "openai_api_type",
            "OPENAI_API_TYPE",
            default="",
        )
        values["openai_proxy"] = get_from_dict_or_env(
            values,
            "openai_proxy",
            "OPENAI_PROXY",
            default="",
        )
        if values["openai_api_type"] in ("azure", "azure_ad", "azuread"):
            default_api_version = "2023-05-15"
            # Azure OpenAI embedding models allow a maximum of 16 texts
            # at a time in each batch
            # See: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#embeddings
            values["chunk_size"] = min(values["chunk_size"], 16)
        else:
            default_api_version = ""
        values["openai_api_version"] = get_from_dict_or_env(
            values,
            "openai_api_version",
            "OPENAI_API_VERSION",
            default=default_api_version,
        )
        # Check OPENAI_ORGANIZATION for backwards compatibility.
        values["openai_organization"] = (
            values["openai_organization"]
            or os.getenv("OPENAI_ORG_ID")
            or os.getenv("OPENAI_ORGANIZATION")
        )
        try:
            import openai
        except ImportError:
            raise ImportError(
                "Could not import openai python package. "
                "Please install it with `pip install openai`."
            )
        else:
            if is_openai_v1():
                if values["openai_api_type"] in ("azure", "azure_ad", "azuread"):
                    warnings.warn(
                        "If you have openai>=1.0.0 installed and are using Azure, "
                        "please use the `AzureOpenAIEmbeddings` class."
                    )
                client_params = {
                    "api_key": values["openai_api_key"],
                    "organization": values["openai_organization"],
                    "base_url": values["openai_api_base"],
                    "timeout": values["request_timeout"],
                    "max_retries": values["max_retries"],
                    "default_headers": values["default_headers"],
                    "default_query": values["default_query"],
                    "http_client": values["http_client"],
                }
                if not values.get("client"):
                    values["client"] = openai.OpenAI(**client_params).embeddings
                if not values.get("async_client"):
                    values["async_client"] = openai.AsyncOpenAI(
                        **client_params
                    ).embeddings
            elif not values.get("client"):
                values["client"] = openai.Embedding
            else:
                pass
        return values

    @property
    def _invocation_params(self) -> Dict[str, Any]:
        if is_openai_v1():
            openai_args: Dict = {"model": self.model, **self.model_kwargs}
        else:
            openai_args = {
                "model": self.model,
                "request_timeout": self.request_timeout,
                "headers": self.headers,
                "api_key": self.openai_api_key,
                "organization": self.openai_organization,
                "api_base": self.openai_api_base,
                "api_type": self.openai_api_type,
                "api_version": self.openai_api_version,
                **self.model_kwargs,
            }
            if self.openai_api_type in ("azure", "azure_ad", "azuread"):
                openai_args["engine"] = self.deployment
            # TODO: Look into proxy with openai v1.
            if self.openai_proxy:
                try:
                    import openai
                except ImportError:
                    raise ImportError(
                        "Could not import openai python package. "
                        "Please install it with `pip install openai`."
                    )

                openai.proxy = {
                    "http": self.openai_proxy,
                    "https": self.openai_proxy,
                }  # type: ignore[assignment]
        return openai_args

    # please refer to
    # https://github.com/openai/openai-cookbook/blob/main/examples/Embedding_long_inputs.ipynb
    def _get_len_safe_embeddings(
        self, texts: List[str], *, engine: str, chunk_size: Optional[int] = None
    ) -> List[List[float]]:
        """
        Generate length-safe embeddings for a list of texts.

        This method handles tokenization and embedding generation, respecting the
        set embedding context length and chunk size. It supports both tiktoken
        and HuggingFace tokenizer based on the tiktoken_enabled flag.

        Args:
            texts (List[str]): A list of texts to embed.
            engine (str): The engine or model to use for embeddings.
            chunk_size (Optional[int]): The size of chunks for processing embeddings.

        Returns:
            List[List[float]]: A list of embeddings for each input text.
        """

        tokens = []
        indices = []
        model_name = self.tiktoken_model_name or self.model
        _chunk_size = chunk_size or self.chunk_size

        # If tiktoken flag set to False
        if not self.tiktoken_enabled:
            try:
                from transformers import AutoTokenizer
            except ImportError:
                raise ImportError(
                    "Could not import transformers python package. "
                    "This is needed in order to for OpenAIEmbeddings without "
                    "`tiktoken`. Please install it with `pip install transformers`. "
                )

            tokenizer = AutoTokenizer.from_pretrained(
                pretrained_model_name_or_path=model_name, use_fast=False
            )
            for i, text in enumerate(texts):
                # Tokenize the text using HuggingFace transformers
                tokenized = tokenizer.encode(text, add_special_tokens=False)

                # Split tokens into chunks respecting the embedding_ctx_length
                for j in range(0, len(tokenized), self.embedding_ctx_length):
                    token_chunk = tokenized[j : j + self.embedding_ctx_length]

                    # Convert token IDs back to a string
                    chunk_text = tokenizer.decode(token_chunk)
                    tokens.append(chunk_text)
                    indices.append(i)
        else:
            try:
                import tiktoken
            except ImportError:
                raise ImportError(
                    "Could not import tiktoken python package. "
                    "This is needed in order to for OpenAIEmbeddings. "
                    "Please install it with `pip install tiktoken`."
                )

            try:
                encoding = tiktoken.encoding_for_model(model_name)
            except KeyError:
                logger.warning("Warning: model not found. Using cl100k_base encoding.")
                model = "cl100k_base"
                encoding = tiktoken.get_encoding(model)
            for i, text in enumerate(texts):
                if self.model.endswith("001"):
                    # See: https://github.com/openai/openai-python/
                    #      issues/418#issuecomment-1525939500
                    # replace newlines, which can negatively affect performance.
                    text = text.replace("\n", " ")

                token = encoding.encode(
                    text=text,
                    allowed_special=self.allowed_special,
                    disallowed_special=self.disallowed_special,
                )

                # Split tokens into chunks respecting the embedding_ctx_length
                for j in range(0, len(token), self.embedding_ctx_length):
                    tokens.append(token[j : j + self.embedding_ctx_length])
                    indices.append(i)

        if self.show_progress_bar:
            try:
                from tqdm.auto import tqdm

                _iter = tqdm(range(0, len(tokens), _chunk_size))
            except ImportError:
                _iter = range(0, len(tokens), _chunk_size)
        else:
            _iter = range(0, len(tokens), _chunk_size)

        batched_embeddings: List[List[float]] = []
        print(tokens)
        for i in _iter:
            response = embed_with_retry(
                self,
                input=tokens[i : i + _chunk_size],
                **self._invocation_params,
            )
            if not isinstance(response, dict):
                response = response.dict()
            batched_embeddings.extend(r["embedding"] for r in response["data"])

        results: List[List[List[float]]] = [[] for _ in range(len(texts))]
        num_tokens_in_batch: List[List[int]] = [[] for _ in range(len(texts))]
        for i in range(len(indices)):
            if self.skip_empty and len(batched_embeddings[i]) == 1:
                continue
            results[indices[i]].append(batched_embeddings[i])
            num_tokens_in_batch[indices[i]].append(len(tokens[i]))

        embeddings: List[List[float]] = [[] for _ in range(len(texts))]
        for i in range(len(texts)):
            _result = results[i]
            if len(_result) == 0:
                average_embedded = embed_with_retry(
                    self,
                    input="",
                    **self._invocation_params,
                )
                if not isinstance(average_embedded, dict):
                    average_embedded = average_embedded.dict()
                average = average_embedded["data"][0]["embedding"]
            else:
                average = np.average(_result, axis=0, weights=num_tokens_in_batch[i])
            embeddings[i] = (average / np.linalg.norm(average)).tolist()

        return embeddings

    # please refer to
    # https://github.com/openai/openai-cookbook/blob/main/examples/Embedding_long_inputs.ipynb
    async def _aget_len_safe_embeddings(
        self, texts: List[str], *, engine: str, chunk_size: Optional[int] = None
    ) -> List[List[float]]:
        """
        Asynchronously generate length-safe embeddings for a list of texts.

        This method handles tokenization and asynchronous embedding generation,
        respecting the set embedding context length and chunk size. It supports both
        `tiktoken` and HuggingFace `tokenizer` based on the tiktoken_enabled flag.

        Args:
            texts (List[str]): A list of texts to embed.
            engine (str): The engine or model to use for embeddings.
            chunk_size (Optional[int]): The size of chunks for processing embeddings.

        Returns:
            List[List[float]]: A list of embeddings for each input text.
        """

        tokens = []
        indices = []
        model_name = self.tiktoken_model_name or self.model
        _chunk_size = chunk_size or self.chunk_size

        # If tiktoken flag set to False
        if not self.tiktoken_enabled:
            try:
                from transformers import AutoTokenizer
            except ImportError:
                raise ImportError(
                    "Could not import transformers python package. "
                    "This is needed in order to for OpenAIEmbeddings without "
                    " `tiktoken`. Please install it with `pip install transformers`."
                )

            tokenizer = AutoTokenizer.from_pretrained(
                pretrained_model_name_or_path=model_name, use_fast=False
            )
            for i, text in enumerate(texts):
                # Tokenize the text using HuggingFace transformers
                tokenized = tokenizer.encode(text, add_special_tokens=False)

                # Split tokens into chunks respecting the embedding_ctx_length
                for j in range(0, len(tokenized), self.embedding_ctx_length):
                    token_chunk = tokenized[j : j + self.embedding_ctx_length]

                    # Convert token IDs back to a string
                    chunk_text = tokenizer.decode(token_chunk)
                    tokens.append(chunk_text)
                    indices.append(i)
        else:
            try:
                import tiktoken
            except ImportError:
                raise ImportError(
                    "Could not import tiktoken python package. "
                    "This is needed in order to for OpenAIEmbeddings. "
                    "Please install it with `pip install tiktoken`."
                )

            try:
                encoding = tiktoken.encoding_for_model(model_name)
            except KeyError:
                logger.warning("Warning: model not found. Using cl100k_base encoding.")
                model = "cl100k_base"
                encoding = tiktoken.get_encoding(model)
            for i, text in enumerate(texts):
                if self.model.endswith("001"):
                    # See: https://github.com/openai/openai-python/
                    #      issues/418#issuecomment-1525939500
                    # replace newlines, which can negatively affect performance.
                    text = text.replace("\n", " ")

                token = encoding.encode(
                    text=text,
                    allowed_special=self.allowed_special,
                    disallowed_special=self.disallowed_special,
                )

                # Split tokens into chunks respecting the embedding_ctx_length
                for j in range(0, len(token), self.embedding_ctx_length):
                    tokens.append(token[j : j + self.embedding_ctx_length])
                    indices.append(i)

        batched_embeddings: List[List[float]] = []
        _chunk_size = chunk_size or self.chunk_size
        for i in range(0, len(tokens), _chunk_size):
            response = await async_embed_with_retry(
                self,
                input=texts,
                **self._invocation_params,
            )

            if not isinstance(response, dict):
                response = response.dict()
            batched_embeddings.extend(r["embedding"] for r in response["data"])

        results: List[List[List[float]]] = [[] for _ in range(len(texts))]
        num_tokens_in_batch: List[List[int]] = [[] for _ in range(len(texts))]
        for i in range(len(indices)):
            results[indices[i]].append(batched_embeddings[i])
            num_tokens_in_batch[indices[i]].append(len(tokens[i]))

        embeddings: List[List[float]] = [[] for _ in range(len(texts))]
        for i in range(len(texts)):
            _result = results[i]
            if len(_result) == 0:
                average_embedded = await async_embed_with_retry(
                    self,
                    input="",
                    **self._invocation_params,
                )
                if not isinstance(average_embedded, dict):
                    average_embedded = average_embedded.dict()
                average = average_embedded["data"][0]["embedding"]
            else:
                average = np.average(_result, axis=0, weights=num_tokens_in_batch[i])
            embeddings[i] = (average / np.linalg.norm(average)).tolist()

        return embeddings

    def embed_documents(
        self, texts: List[str], chunk_size: Optional[int] = 0
    ) -> List[List[float]]:
        """Call out to OpenAI's embedding endpoint for embedding search docs.

        Args:
            texts: The list of texts to embed.
            chunk_size: The chunk size of embeddings. If None, will use the chunk size
                specified by the class.

        Returns:
            List of embeddings, one for each text.
        """
        # NOTE: to keep things simple, we assume the list may contain texts longer
        #       than the maximum context and use length-safe embedding function.
        engine = cast(str, self.deployment)
        return self._get_len_safe_embeddings(texts, engine=engine)

    async def aembed_documents(
        self, texts: List[str], chunk_size: Optional[int] = 0
    ) -> List[List[float]]:
        """Call out to OpenAI's embedding endpoint async for embedding search docs.

        Args:
            texts: The list of texts to embed.
            chunk_size: The chunk size of embeddings. If None, will use the chunk size
                specified by the class.

        Returns:
            List of embeddings, one for each text.
        """
        # NOTE: to keep things simple, we assume the list may contain texts longer
        #       than the maximum context and use length-safe embedding function.
        engine = cast(str, self.deployment)
        return await self._aget_len_safe_embeddings(texts, engine=engine)

    def embed_query(self, text: str) -> List[float]:
        """Call out to OpenAI's embedding endpoint for embedding query text.

        Args:
            text: The text to embed.

        Returns:
            Embedding for the text.
        """
        return self.embed_documents([text])[0]

    async def aembed_query(self, text: str) -> List[float]:
        """Call out to OpenAI's embedding endpoint async for embedding query text.

        Args:
            text: The text to embed.

        Returns:
            Embedding for the text.
        """
        embeddings = await self.aembed_documents([text])
        return embeddings[0]
# llama = LlamaCppEmbeddings(model_path="Model/gte-qwen2-7b-instruct-q5_k_m.gguf", n_gpu_layers=9999)
# print(llama.embed_query('What is it?'))
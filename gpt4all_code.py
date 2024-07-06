# from functools import partial
# from typing import Any, Dict, List, Mapping, Optional, Set

# from langchain_core.callbacks import CallbackManagerForLLMRun
# from langchain_core.language_models.llms import LLM
# from langchain_core.pydantic_v1 import Extra, Field, root_validator

# from langchain_community.llms.utils import enforce_stop_tokens


# class GPT4All(LLM):
#     """GPT4All language models.

#     To use, you should have the ``gpt4all`` python package installed, the
#     pre-trained model file, and the model's config information.

#     Example:
#         .. code-block:: python

#             from langchain_community.llms import GPT4All
#             model = GPT4All(model="./models/gpt4all-model.bin", n_threads=8)

#             # Simplest invocation
#             response = model.invoke("Once upon a time, ")
#     """

#     model: str
#     """Path to the pre-trained GPT4All model file."""

#     backend: Optional[str] = Field(None, alias="backend")

#     max_tokens: int = Field(200, alias="max_tokens")
#     """Token context window."""

#     n_parts: int = Field(-1, alias="n_parts")
#     """Number of parts to split the model into. 
#     If -1, the number of parts is automatically determined."""

#     seed: int = Field(0, alias="seed")
#     """Seed. If -1, a random seed is used."""

#     f16_kv: bool = Field(False, alias="f16_kv")
#     """Use half-precision for key/value cache."""

#     logits_all: bool = Field(False, alias="logits_all")
#     """Return logits for all tokens, not just the last token."""

#     vocab_only: bool = Field(False, alias="vocab_only")
#     """Only load the vocabulary, no weights."""

#     use_mlock: bool = Field(False, alias="use_mlock")
#     """Force system to keep model in RAM."""

#     embedding: bool = Field(False, alias="embedding")
#     """Use embedding mode only."""

#     n_threads: Optional[int] = Field(4, alias="n_threads")
#     """Number of threads to use."""

#     n_predict: Optional[int] = 256
#     """The maximum number of tokens to generate."""

#     temp: Optional[float] = 0.7
#     """The temperature to use for sampling."""

#     top_p: Optional[float] = 0.1
#     """The top-p value to use for sampling."""

#     top_k: Optional[int] = 40
#     """The top-k value to use for sampling."""

#     echo: Optional[bool] = False
#     """Whether to echo the prompt."""

#     stop: Optional[List[str]] = []
#     """A list of strings to stop generation when encountered."""

#     repeat_last_n: Optional[int] = 64
#     "Last n tokens to penalize"

#     repeat_penalty: Optional[float] = 1.18
#     """The penalty to apply to repeated tokens."""

#     n_batch: int = Field(8, alias="n_batch")
#     """Batch size for prompt processing."""

#     streaming: bool = False
#     """Whether to stream the results or not."""

#     allow_download: bool = False
#     """If model does not exist in ~/.cache/gpt4all/, download it."""

#     device: Optional[str] = Field("cpu", alias="device")
#     """Device name: cpu, gpu, nvidia, intel, amd or DeviceName."""

#     client: Any = None  #: :meta private:

#     class Config:
#         """Configuration for this pydantic object."""

#         extra = Extra.forbid

#     @staticmethod
#     def _model_param_names() -> Set[str]:
#         return {
#             "max_tokens",
#             "n_predict",
#             "top_k",
#             "top_p",
#             "temp",
#             "n_batch",
#             "repeat_penalty",
#             "repeat_last_n",
#             "streaming",
#         }

#     def _default_params(self) -> Dict[str, Any]:
#         return {
#             "max_tokens": self.max_tokens,
#             "n_predict": self.n_predict,
#             "top_k": self.top_k,
#             "top_p": self.top_p,
#             "temp": self.temp,
#             "n_batch": self.n_batch,
#             "repeat_penalty": self.repeat_penalty,
#             "repeat_last_n": self.repeat_last_n,
#             "streaming": self.streaming,
#         }

#     @root_validator()
#     def validate_environment(cls, values: Dict) -> Dict:
#         """Validate that the python package exists in the environment."""
#         try:
#             from gpt4all import GPT4All as GPT4AllModel
#         except ImportError:
#             raise ImportError(
#                 "Could not import gpt4all python package. "
#                 "Please install it with `pip install gpt4all`."
#             )

#         full_path = values["model"]
#         model_path, delimiter, model_name = full_path.rpartition("/")
#         model_path += delimiter

#         values["client"] = GPT4AllModel(
#             model_name,
#             model_path=model_path or None,
#             model_type=values["backend"],
#             allow_download=values["allow_download"],
#             device=values["device"],
#             n_ctx=4096,
#         )
#         if values["n_threads"] is not None:
#             # set n_threads
#             values["client"].model.set_thread_count(values["n_threads"])

#         try:
#             values["backend"] = values["client"].model_type
#         except AttributeError:
#             # The below is for compatibility with GPT4All Python bindings <= 0.2.3.
#             values["backend"] = values["client"].model.model_type

#         return values

#     @property
#     def _identifying_params(self) -> Mapping[str, Any]:
#         """Get the identifying parameters."""
#         return {
#             "model": self.model,
#             **self._default_params(),
#             **{
#                 k: v for k, v in self.__dict__.items() if k in self._model_param_names()
#             },
#         }

#     @property
#     def _llm_type(self) -> str:
#         """Return the type of llm."""
#         return "gpt4all"

#     def _call(
#         self,
#         prompt: str,
#         stop: Optional[List[str]] = None,
#         run_manager: Optional[CallbackManagerForLLMRun] = None,
#         **kwargs: Any,
#     ) -> str:
#         r"""Call out to GPT4All's generate method.

#         Args:
#             prompt: The prompt to pass into the model.
#             stop: A list of strings to stop generation when encountered.

#         Returns:
#             The string generated by the model.

#         Example:
#             .. code-block:: python

#                 prompt = "Once upon a time, "
#                 response = model.invoke(prompt, n_predict=55)
#         """
#         text_callback = None
#         if run_manager:
#             text_callback = partial(run_manager.on_llm_new_token, verbose=self.verbose)
#         text = ""
#         params = {**self._default_params(), **kwargs}
#         for token in self.client.generate(prompt, **params):
#             if text_callback:
#                 text_callback(token)
#             text += token
#         if stop is not None:
#             text = enforce_stop_tokens(text, stop)
#         return text

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

template = """System: You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Attention: If your answer relates to any image description given below, you should refer to the image ID in your answer. The image id is in format [image_id.png] . For example [0_image_0.png]
Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
In addition to these main elements, there are other small boxes scattered throughout the image, some of which may be part of the same system or represent different components. The diagram appears to provide a clear visual representation of the relationships and connections between these various components within the system.)

## Data Structures

struct

**bl_apdb_

** APDB structure.

struct

**bl_t_can_id_

** CAN ID structure.

struct

**bl_t_date_

** Date structure.

## Macros

\#define APDB_VERSION

**0x00000206UL

**

## Typedefs

typedef struct

**bl_apdb_ BL_APDB

** APDB structure.

typedef struct

**bl_t_can_id_ BL_T_CAN_ID

** CAN ID structure.

typedef struct bl_t_date_ BL_T_DATE Date structure.

## Apdb Flags

Defined APDB flags.

\#define APDB_FLAGS_ABRD_ENABLE

**0x00000001UL

**

\#define APDB_FLAGS_CRC64_ENABLE

**0x40000000UL

**

\#define APDB_FLAGS_MULTI_APP

**0x80000000UL

**

## Application Descriptor Block (Apdb)

The APDB, which is defined by the user.

Within this time, the application needs to shut down and all non-volatile memories need to be stored.

With a call to IO_DOWNLOAD_Launch()**, the ECU restarts in Ethernet download mode. If the download mode is not launched during this time, the request becomes invalid and a new request is** necessary. The configuration for setting up the download capability is taken from the APDB. There, the fields - **TargetIPAddress** - **SubnetMask** - **DLMulticastIPAddress** are used. If an enforcement to default settings has been detected during startup, the bootloader's default settings will be applied. DOWNLOAD-API Usage: - **Examples for DOWNLOAD API functions**

## 7.8.2 Download Code Examples

Examples for using the DOWNLOAD API // initialize Ethernet interface for handling download requests IO_DOWNLOAD_Init(); // application cycle while (1): ...

``` // check, if a download request is pending if (IO_DOWNLOAD_CheckRequest() == IO_E_OK) ( // shut down application ...

```

// save memories

For code examples see the section **Example for flash initialization. ** Returns IO_ErrorType Return values

| IO_E_OK                     | Everything fine                                            | |-----------------------------|------------------------------------------------------------| | IO_E_FLASH_WRONG_DEVICE_ID  | The flash chip did not return the expected device ID       | | IO_E_INVALID_CHANNEL_ID     | The flash module is not available on the used ECU variant  | | IO_E_CHANNEL_BUSY           | Module has been initialized before                         | | IO_E_DRIVER_NOT_INITIALIZED | The common driver init function has not been called before | | IO_E_OPTION_NOT_SUPPORTED   | The type of the flash chip is not supported                |

IO_E_INTERNAL_CSM **Internal error** IO_E_BUSY **Driver is busy, last operation is still ongoing** IO_E_FLASH_OP_FAILED **Driver is idle, the last operation has failed**

Remarks

If the flash driver needs to be re

For the safety configuration of a 3 mode ADC channel, the following rules need to be fulfilled: - The channel must have IO_PIN_NONE in the redundant_channel **field. ** - If the ratiometric measurement mode is used, the channel must not use **IO_SENSOR_** SUPPLY_2.

## 7.4.6 Function Documentation 7.4.6.1 Float4 Io_Adc_Boardtempfloat ( Ubyte4 **Raw_Value** )

Calculates the board temperature in degree Celsius.

The function converts the raw ADC value (retrieved from IO_ADC_Get()**) to a temperature in degree** Celsius and returns it as a float value.

Parameters raw_value raw adc board temperature returned from the IO_ADC_Get() **function** Returns the board temperature in degree Celsius ( -63.00 .. 152.50 degree C ) Remarks Usage: 1 IO_ADC_Get(IO_ADC_BOARD_TEMP, 2 &raw_value, 3 &fresh); 4 5 temp = IO_ADC_BoardTempFloat(raw_value);

## 7.4.6.2 Sbyte2 Io_Adc_Boardtempsbyte ( Ubyte4 **Raw_Value** )

Calculates the board temperature in degree Celsius.

For any further error the diagnostic state machine will enter the safe state. Definition at line 549 of file IO_Driver.h.

## 7.9.5.8 #Define Safety_Conf_Resets_5 ( 5U )

5 Resets allowed.

This means that the watchdog CPU can reset the device and try to restart the device for 5 times.

For any further error the diagnostic state machine will enter the safe state.

Definition at line 555 of file IO_Driver.h.

## 7.9.5.9 #Define Safety_Conf_Resets_6 ( 6U )

6 Resets allowed. This means that the watchdog CPU can reset the device and try to restart the device for 6 times. For any further error the diagnostic state machine will enter the safe state.

Definition at line 561 of file IO_Driver.h.

## 7.9.5.10 #Define Safety_Conf_Resets_7 ( 7U )

7 Resets allowed.

This means that the watchdog CPU can reset the device and try to restart the device for 7 times. For any further error the diagnostic state machine will enter the safe state. Definition at line 567 of file IO_Driver.h.

For the safety configuration of a 3 mode ADC channel, the following rules need to be fulfilled: - The channel must have IO_PIN_NONE in the redundant_channel **field. ** - If the ratiometric measurement mode is used, the channel must not use **IO_SENSOR_** SUPPLY_2.

Definition at line 238 of file IO_ADC.h.

## 6.5.2 Field Documentation

6.5.2.1 ubyte1 io_adc_safety_conf_::adc_val_lower Lower ADC limit in % [4..96] Definition at line 240 of file IO_ADC.h. 6.5.2.2 ubyte1 io_adc_safety_conf_::adc_val_upper Upper ADC limit in % [4..96] Definition at line 241 of file IO_ADC.h.

6.5.2.3 ubyte1 io_adc_safety_conf_::redundant_channel Redundant channel for 2 mode inputs.

Definition at line 242 of file IO_ADC.h.

## 6.6 Io_Can_Data_Frame_ Struct Reference

CAN data frame.

## Data Fields

ubyte1 data [8]

**ubyte4 id

**

**ubyte1 id_format

**

**ubyte1 length

**

## 6.6.1 Detailed Description

CAN data frame.

Stores a data frame for the CAN communication.

With the polling method, the speed of reading the EEPROM or FRAM is limited by the bandwidth of the SPI bus. The read **data rate that can be achieved is 267000 B/s and higher. ** The write speed achievable for the FRAM is 247000 B/s. The EEPROM write **speed cannot be** significantly improved by the polling because it is limited by the internal 5 ms programming delay (max), i.e. to 12800 B/s. The data rates for the polling method are not guaranteed because they depend on the frequency of the polling. The desired polling period is 1.6 us and shorter: If this is fulfilled, the specified data rates will surely be exceeded. In practice, however, the polling frequency depends on various CPU load conditions (such as the background interrupts) that are difficult to control. The given data rates are typical values verified by measurements in a test application. They should be met with a high degree of confidence in the majority of customer applications.

## 7.10.3 Eeprom Code Examples

and will remain the sole property of TTControl GmbH or the respective **right holder. Nothing contained** in this legal notice, the document or in any web site of TTControl GmbH shall be construed as conferring to the recipient any license under any intellectual property rights, whether explicit, by estoppel, implication, or otherwise. The product or Sample is only allowed to be used in the scope as **described in this document. ** TTControl GmbH provides this document "as is" and disclaims **all warranties of any kind. The entire** risk, as to quality, use or performance of the document remains with the recipient.

and 3000-5000mV** as valid high-level. Note If no limits will be specified by the application, the following default limits will be applied: \( 0, 2500, 2500, 32000 ) Definition at line 148 of file IO_DIO.h.

If safety_conf != NULL, the parameter diag_margin is forced to TRUE

**to allow diagnostics

**

Static friction and stiction can cause a hysteresis and make

**the control of a hydraulic

** valve erratic and unpredictable. In order to counteract these hysteresis effects, small vibrations about the desired position shall be created in the valve. This constantly breaks the static friction ensuring that it will move even with small input changes, and the effects of hysteresis are average out. A proper setting of PWM frequency according to the resonance frequency of the actuator allows to adjust this desired small vibration, low enough in amplitude to prevent noticeable oscillations on the hydraulic output but sufficient high to prevent friction. The PWM frequency can be set in the range

**of 50 .. 1000Hz, a typical

** range for hydraulic valves to operate without friction is 90

**.. 160Hz.

**
User: How to init and get data from analog inputs on TTC 500 in C

Assistant:"""
template = """<|im_start|>system
You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. The context is in markdown format.
If you don't know the answer, just say that you don't know. 
Attention: If your answer relates to any image description given below, you should refer to the image ID in your answer. The image id is in format [image_id.png] . For example [0_image_0.png]
Use the maximum sentences you need to provide accurate and detailed answers to diverse queries.
Context:
In addition to these main elements, there are other small boxes scattered throughout the image, some of which may be part of the same system or represent different components. The diagram appears to provide a clear visual representation of the relationships and connections between these various components within the system.)

## Data Structures

struct

**bl_apdb_

** APDB structure.

struct

**bl_t_can_id_

** CAN ID structure.

struct

**bl_t_date_

** Date structure.

## Macros

\#define APDB_VERSION

**0x00000206UL

**

## Typedefs

typedef struct

**bl_apdb_ BL_APDB

** APDB structure.

typedef struct

**bl_t_can_id_ BL_T_CAN_ID

** CAN ID structure.

typedef struct bl_t_date_ BL_T_DATE Date structure.

## Apdb Flags

Defined APDB flags.

\#define APDB_FLAGS_ABRD_ENABLE

**0x00000001UL

**

\#define APDB_FLAGS_CRC64_ENABLE

**0x40000000UL

**

\#define APDB_FLAGS_MULTI_APP

**0x80000000UL

**

## Application Descriptor Block (Apdb)

The APDB, which is defined by the user.

Within this time, the application needs to shut down and all non-volatile memories need to be stored.

With a call to IO_DOWNLOAD_Launch()**, the ECU restarts in Ethernet download mode. If the download mode is not launched during this time, the request becomes invalid and a new request is** necessary. The configuration for setting up the download capability is taken from the APDB. There, the fields - **TargetIPAddress** - **SubnetMask** - **DLMulticastIPAddress** are used. If an enforcement to default settings has been detected during startup, the bootloader's default settings will be applied. DOWNLOAD-API Usage: - **Examples for DOWNLOAD API functions**

## 7.8.2 Download Code Examples

Examples for using the DOWNLOAD API // initialize Ethernet interface for handling download requests IO_DOWNLOAD_Init(); // application cycle while (1): ...

``` // check, if a download request is pending if (IO_DOWNLOAD_CheckRequest() == IO_E_OK) ( // shut down application ...

```

// save memories

For code examples see the section **Example for flash initialization. ** Returns IO_ErrorType Return values

| IO_E_OK                     | Everything fine                                            | |-----------------------------|------------------------------------------------------------| | IO_E_FLASH_WRONG_DEVICE_ID  | The flash chip did not return the expected device ID       | | IO_E_INVALID_CHANNEL_ID     | The flash module is not available on the used ECU variant  | | IO_E_CHANNEL_BUSY           | Module has been initialized before                         | | IO_E_DRIVER_NOT_INITIALIZED | The common driver init function has not been called before | | IO_E_OPTION_NOT_SUPPORTED   | The type of the flash chip is not supported                |

IO_E_INTERNAL_CSM **Internal error** IO_E_BUSY **Driver is busy, last operation is still ongoing** IO_E_FLASH_OP_FAILED **Driver is idle, the last operation has failed**

Remarks

If the flash driver needs to be re

For the safety configuration of a 3 mode ADC channel, the following rules need to be fulfilled: - The channel must have IO_PIN_NONE in the redundant_channel **field. ** - If the ratiometric measurement mode is used, the channel must not use **IO_SENSOR_** SUPPLY_2.

## 7.4.6 Function Documentation 7.4.6.1 Float4 Io_Adc_Boardtempfloat ( Ubyte4 **Raw_Value** )

Calculates the board temperature in degree Celsius.

The function converts the raw ADC value (retrieved from IO_ADC_Get()**) to a temperature in degree** Celsius and returns it as a float value.

Parameters raw_value raw adc board temperature returned from the IO_ADC_Get() **function** Returns the board temperature in degree Celsius ( -63.00 .. 152.50 degree C ) Remarks Usage: 1 IO_ADC_Get(IO_ADC_BOARD_TEMP, 2 &raw_value, 3 &fresh); 4 5 temp = IO_ADC_BoardTempFloat(raw_value);

## 7.4.6.2 Sbyte2 Io_Adc_Boardtempsbyte ( Ubyte4 **Raw_Value** )

Calculates the board temperature in degree Celsius.

For any further error the diagnostic state machine will enter the safe state. Definition at line 549 of file IO_Driver.h.

## 7.9.5.8 #Define Safety_Conf_Resets_5 ( 5U )

5 Resets allowed.

This means that the watchdog CPU can reset the device and try to restart the device for 5 times.

For any further error the diagnostic state machine will enter the safe state.

Definition at line 555 of file IO_Driver.h.

## 7.9.5.9 #Define Safety_Conf_Resets_6 ( 6U )

6 Resets allowed. This means that the watchdog CPU can reset the device and try to restart the device for 6 times. For any further error the diagnostic state machine will enter the safe state.

Definition at line 561 of file IO_Driver.h.

## 7.9.5.10 #Define Safety_Conf_Resets_7 ( 7U )

7 Resets allowed.

This means that the watchdog CPU can reset the device and try to restart the device for 7 times. For any further error the diagnostic state machine will enter the safe state. Definition at line 567 of file IO_Driver.h.

For the safety configuration of a 3 mode ADC channel, the following rules need to be fulfilled: - The channel must have IO_PIN_NONE in the redundant_channel **field. ** - If the ratiometric measurement mode is used, the channel must not use **IO_SENSOR_** SUPPLY_2.

Definition at line 238 of file IO_ADC.h.

## 6.5.2 Field Documentation

6.5.2.1 ubyte1 io_adc_safety_conf_::adc_val_lower Lower ADC limit in % [4..96] Definition at line 240 of file IO_ADC.h. 6.5.2.2 ubyte1 io_adc_safety_conf_::adc_val_upper Upper ADC limit in % [4..96] Definition at line 241 of file IO_ADC.h.

6.5.2.3 ubyte1 io_adc_safety_conf_::redundant_channel Redundant channel for 2 mode inputs.

Definition at line 242 of file IO_ADC.h.

## 6.6 Io_Can_Data_Frame_ Struct Reference

CAN data frame.

## Data Fields

ubyte1 data [8]

**ubyte4 id

**

**ubyte1 id_format

**

**ubyte1 length

**

## 6.6.1 Detailed Description

CAN data frame.

Stores a data frame for the CAN communication.

With the polling method, the speed of reading the EEPROM or FRAM is limited by the bandwidth of the SPI bus. The read **data rate that can be achieved is 267000 B/s and higher. ** The write speed achievable for the FRAM is 247000 B/s. The EEPROM write **speed cannot be** significantly improved by the polling because it is limited by the internal 5 ms programming delay (max), i.e. to 12800 B/s. The data rates for the polling method are not guaranteed because they depend on the frequency of the polling. The desired polling period is 1.6 us and shorter: If this is fulfilled, the specified data rates will surely be exceeded. In practice, however, the polling frequency depends on various CPU load conditions (such as the background interrupts) that are difficult to control. The given data rates are typical values verified by measurements in a test application. They should be met with a high degree of confidence in the majority of customer applications.

## 7.10.3 Eeprom Code Examples

and will remain the sole property of TTControl GmbH or the respective **right holder. Nothing contained** in this legal notice, the document or in any web site of TTControl GmbH shall be construed as conferring to the recipient any license under any intellectual property rights, whether explicit, by estoppel, implication, or otherwise. The product or Sample is only allowed to be used in the scope as **described in this document. ** TTControl GmbH provides this document "as is" and disclaims **all warranties of any kind. The entire** risk, as to quality, use or performance of the document remains with the recipient.

and 3000-5000mV** as valid high-level. Note If no limits will be specified by the application, the following default limits will be applied: \( 0, 2500, 2500, 32000 ) Definition at line 148 of file IO_DIO.h.

If safety_conf != NULL, the parameter diag_margin is forced to TRUE

**to allow diagnostics

**

Static friction and stiction can cause a hysteresis and make

**the control of a hydraulic

** valve erratic and unpredictable. In order to counteract these hysteresis effects, small vibrations about the desired position shall be created in the valve. This constantly breaks the static friction ensuring that it will move even with small input changes, and the effects of hysteresis are average out. A proper setting of PWM frequency according to the resonance frequency of the actuator allows to adjust this desired small vibration, low enough in amplitude to prevent noticeable oscillations on the hydraulic output but sufficient high to prevent friction. The PWM frequency can be set in the range

**of 50 .. 1000Hz, a typical

** range for hydraulic valves to operate without friction is 90

**.. 160Hz.

**<|im_end|>
<|im_start|>user
How to init and get data from analog inputs on TTC 500 in C<|im_end|>
<|im_start|>assistant
"""
prompt = PromptTemplate.from_template(template)

# llm = LlamaCpp(model_path='./Model/Llama3-ChatQA-1.5-8B-Q6_K.gguf', n_gpu_layers=999, n_ctx=5000, verbose=True, stop=['<|eot_id|>', "<|end_of_text|>", "<|im_end|>"], 
#                max_tokens=2000,
#                # temperature=1.5,
#               rope_freq_base=0)
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name='MaziyarPanahi/Meta-Llama-3-70B-Instruct-GPTQ', openai_api_key='BVJD4F99OBYPLI0PTM46PI5VK5D09HUD2B404UT6', model_kwargs={'stop': ['<|eot_id|>']}, openai_api_base='https://api.runpod.ai/v2/vllm-svgd8vjj76vhwf/openai/v1/')

# from langchain_huggingface import HuggingFacePipeline
# from transformers import BitsAndBytesConfig

# quantization_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype="float16",
#     bnb_4bit_use_double_quant=True
# )
# llm = HuggingFacePipeline.from_model_id(
#     # model_id="nvidia/Llama3-ChatQA-1.5-8B",
#     model_id='Qwen/Qwen2-7B-Instruct',
#     task="text-generation",
#     model_kwargs={"quantization_config": quantization_config},
#     device=0,
#     pipeline_kwargs=dict(
#         max_new_tokens=512,
#         do_sample=False,
#         repetition_penalty=1.03,
#     ),
# )

# llm_chain = prompt | llm
# question = "How to init and get data from analog inputs on TTC 500 in C"

# from langchain_community.llms import VLLM

# llm = VLLM(
#     model="Qwen/Qwen2-7B-Instruct-GPTQ-Int4",
#     trust_remote_code=True,  # mandatory for hf models
#     max_new_tokens=1000,

#     temperature=0,
#     vllm_kwargs={"max_model_len": 5000, 'quantization': 'gptq'}
# )
response = llm.invoke(template)
print(response)
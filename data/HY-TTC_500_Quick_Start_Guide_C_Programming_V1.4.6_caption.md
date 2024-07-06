# Hy-Ttc 500

![0_image_0.Png](0_image_0.Png)

![0_image_1.Png](0_image_1.Png)

![0_image_2.Png](0_image_2.Png)

Quick Start Guide - C Programming Programmable ECU for Sensor-Actuator Management Product Version 01.08

| Document Number:   | D-TTC5F-G-20-004   |
|--------------------|--------------------|
| Document Version:  | 1.4.6              |
| Date:              | 07-May-2020        |
| Status:            | Released           |

TTControl GmbH Schoenbrunner Str. 7, A-1040 Vienna, Austria,Tel. +43 1 585 34 34–0, Fax +43 1 585 34 34–90, office@ttcontrol.com No part of the document may be reproduced or transmitted in any form or by any means, electronic or mechanical, for any purpose, without the written permission of TTControl GmbH. Company or product names mentioned in this document may be trademarks or registered trademarks of their respective holders. TTControl GmbH undertakes no further obligation or relation to this document.

Copyright  2020 TTControl GmbH. All rights reserved. Subject to changes and corrections TTControl GmbH Confidential and Proprietary Information

## Legal Notice Document Number: D-Ttc5F-G-20-004

The data in this document may not be altered or amended without special notification from TTControl GmbH. TTControl GmbH undertakes no further obligation in relation to this document. The software described in it can only be used if the customer is in possession of a general license agreement or single license. The information contained in this document does not affect or change any General Terms and Conditions of TTControl GmbH and/or any agreements existing between TTControl GmbH and the recipient regarding the product or Sample concerned. The reader acknowledges that this document may not be reproduced, stored in a retrieval system, transmitted, changed, or translated, in whole or in part, without the express prior written consent of TTControl GmbH. The reader acknowledges that any and all of the copyrights, trademarks, trade names, patents (whether registrable or not) and other intellectual property rights embodied in or in connection with this document are and will remain the sole property of TTControl GmbH or the respective right holder. Nothing contained in this legal notice, the document or in any web site of TTControl GmbH shall be construed as conferring to the recipient any license under any intellectual property rights, whether explicit, by estoppel, implication, or otherwise. The product or Sample is only allowed to be used in the scope as described in this document.

TTControl GmbH provides this document "as is" and disclaims all warranties of any kind. The entire risk, as to quality, use or performance of the document remains with the recipient.

All trademarks mentioned in this document belong to their respective owners.

Copyright  2020 TTControl GmbH. All rights reserved.

## Contents

| Table of Contents    | ii                                          |    |    |
|----------------------|---------------------------------------------|----|----|
| List of Figures      | 1                                           |    |    |
| I                    | Quick Start Guide                           | 2  |    |
| 1                    | Overview                                    |    | 3  |
| 2                    | Information and latest version of software  |    | 4  |
| 3                    | Getting Started                             | 5  |    |
| 4                    | Using the Interface Board                   |    | 7  |
| 4.1                  | HY-TTC 500 Cable Harness                    |    | 7  |
| 4.2                  | HY-TTC 500 CAN Termination                  | 8  |    |
| 4.3                  | HY-TTC 500 Power Supply                     | 9  |    |
| 4.4                  | HY-TTC 500 Terminal 15 (KL15) Modes         |    | 11 |
| 4.5                  | Status LEDs                                 |    | 12 |
| 4.6                  | Selecting BroadR-Reach®or Ethernet mode     |    | 13 |
| 4.7                  | HY-TTC 500 Download and Debugging           |    | 14 |
| 5                    | C Programming Howto for HY-TTC 500          |    | 15 |
| 5.1                  | Overview                                    |    | 15 |
| 5.2                  | Endianess                                   |    | 15 |
| 5.3                  | Tool Chain                                  |    | 15 |
| 5.4                  | File Structure                              | 20 |    |
| 5.5                  | Development Environment                     | 22 |    |
| 5.6                  | Settings.mk                                 | 22 |    |
| 5.7                  | Application Examples                        | 24 |    |
| 5.7.1                | Build Application                           |    | 24 |
| 5.7.2                | General                                     |    | 27 |
| 5.7.3                | Help for C Driver Functions                 |    | 30 |
| 5.7.4                | Linking Constant Data                       |    | 30 |
| 5.7.5                | Safety Configuration                        |    | 32 |
| 5.7.6                | Debugging of a safety-critical Application  |    | 32 |
| 5.8                  | Flashing the HY-TTC 500                     | 32 |    |
| 5.8.1                | The Lauterbach Debugging Device and Trace32 |    | 32 |
| 5.8.2                | The TTC-Downloader Tool                     |    | 45 |
| 6                    | Memory Mapping                              |    | 48 |
| 6.1                  | Memory Map for Internal Flash and RAM       |    | 48 |
| 6.2                  | Memory Map for External Flash and RAM       | 49 |    |
| References           | 50                                          |    |    |
| Legal Disclaimer     |                                             | 51 |    |

ii Contents

## List Of Figures

| 3.1   | HY-TTC 500 Starter Kit                                                            |     | 5   |
|-------|-----------------------------------------------------------------------------------|-----|-----|
| 3.2   | HY-TTC 500 Starter Kit for C programming                                          |     | 6   |
| 4.1   | HY-TTC 500 Interface Board                                                        |     | 7   |
| 4.2   | HY-TTC 500 Interface Board CAN Termination                                        |     | 8   |
| 4.3   | HY-TTC 500 Interface Board CAN Termination                                        |     | 9   |
| 4.4   | HY-TTC 500 Interface Board Power Supply                                           | 10  |     |
| 4.5   | HY-TTC 500 Interface Board Power Supply                                           | 10  |     |
| 4.6   | HY-TTC 500 Interface Board Terminal 15 (KL15)                                     | 11  |     |
| 4.7   | HY-TTC 500 Interface Board Terminal 15 (KL15)                                     | 11  |     |
| 4.8   | Status LEDs                                                                       |     | 12  |
| 4.9   | Status LEDs                                                                       |     | 13  |
| 4.10  | Jumpers for Ethernet or BroadR-Reach®mode                                         | 13  |     |
| 5.1   | CCS Edit - Code Composer Studio                                                   |     | 16  |
| 5.2   | Show only. . . check box                                                          |     | 16  |
| 5.3   | Work with field                                                                   | 17  |     |
| 5.4   | Add button                                                                        | 17  |     |
| 5.5   | Add Repository dialog                                                             | 18  |     |
| 5.6   | TI Compiler Updates branch                                                        |     | 19  |
| 5.7   | ARM Compiler Tools 5.1.6                                                          |     | 19  |
| 5.8   | Contents of the Get_Started directory                                             |     | 20  |
| 5.9   | The examples and template directories                                             |     | 21  |
| 5.10  | Settings.mk                                                                       | 23  |     |
| 5.11  | Select new wizard page                                                            |     | 25  |
| 5.12  | Import Existing Code page                                                         |     | 25  |
| 5.13  | Browse For Folder dialog                                                          |     | 26  |
| 5.14  | Console pane with successful build                                                | 26  |     |
| 5.15  | Includes                                                                          | 27  |     |
| 5.16  | Application Descriptor Block (APDB)                                               |     | 28  |
| 5.17  | Application initialization                                                        |     | 29  |
| 5.18  | Application loop                                                                  |     | 30  |
| 5.19  | Linking constant data to the external flash and/or application configuration data | .   | 31  |
| 5.20  | Lauterbach Base Station                                                           |     | 33  |
| 5.21  | Trace32 Software                                                                  |     | 33  |
| 5.22  | Chosse Destination Location page                                                  |     | 33  |
| 5.23  | Installation Type page                                                            |     | 34  |
| 5.24  | Setup Type page                                                                   |     | 34  |
| 5.25  | TRACE32 Product Type page                                                         | 35  |     |
| 5.26  | Maintenance Notice page                                                           |     | 35  |
| 5.27  | Debugger Interface Type page                                                      |     | 36  |
| 5.28  | OS Selection page                                                                 |     | 36  |
| 5.29  | CPU selection page                                                                |     | 37  |
| 5.30  | TRACE32 executable type dialog                                                    | 37  |     |

| 5.31   | Environment variable T32ID page                  |     | 37   |
|--------|--------------------------------------------------|-----|------|
| 5.32   | Device software installation                     | 38  |      |
| 5.33   | Environment variable T32TMP page                 | 38  |      |
| 5.34   | Prepare TRACE32 for Integration. . . page        | 39  |      |
| 5.35   | Select way to submit registration page           | 39  |      |
| 5.36   | TRACE32 software is successfully finished page   | 40  |      |
| 5.37   | JTAG Adapter Board                               | 40  |      |
| 5.38   | JTAG Cable                                       | 40  |      |
| 5.39   | HY-TTC 500 with JTAG connector and LEDs          |     | 41   |
| 5.40   | Lauterbach connection to HY-TTC 580 (1)          |     | 42   |
| 5.41   | Lauterbach connection to HY-TTC 580 (2)          |     | 42   |
| 5.42   | HY-TTC 500 with LEDs                             |     | 43   |
| 5.43   | HY-TTC 500 with JTAG connector and signal pins   |     | 44   |
| 5.44   | Trace32 and .cmm batch file                      |     | 44   |
| 5.45   | Flash application dialog                         | 45  |      |
| 5.46   | Reset Trace32 windows dialog                     | 45  |      |
| 5.47   | Trace32 Window after flashing                    |     | 46   |
| 5.48   | TTC-Downloader                                   | 47  |      |
| 6.1    | Memory map for HY-TTC 500 internal Flash         |     | 48   |
| 6.2    | Memory map for HY-TTC 500 external RAM and Flash |     | 49   |

HY-TTC 500 Quick Start Guide - C Programming V 1.4.6 2 Part I

# Quick Start Guide

## 1 Overview

The purpose of this document is to give a short overview of how to setup the HY-TTC 500 Starter Kit for C programming.

In case of errors or bugs in documents or workshop examples, please send a feedback to our support team (support@ttcontrol.com).

## 2 Information And Latest Version Of Software

Get the latest version of the Quick Start Guide and information about new product features, improvements and bug fixes from our Service Area at **http://www.ttcontrol.com/service-area/**.

Download the latest files as follows:
1. Enter the **Service Area** page.

2. Then click Controller > HY-TTC 500 Family > IO Driver Release > **IO Driver Release <latest version>**.

3. From the page with the latest IO Driver Release, download Installer - C Programming Environment for HY-TTC 500 <version and build>.

## 3 Getting Started

TTControl GmbH recommends using the HY-TTC 500 Starter Kit, because it includes all components required for smooth development. There are two variants of the HY-TTC 500 Starter Kit available: one for C programming (with JTAG-Adapter and open housing) and one for CODESYS programming. This Quick Start Guide is for the C programming variant (see Figure 3.2 on the following page). For the CODESYS programming variant, see [5]. Note that the Ethernet USB adapter is only part of the starter kit if the corresponding HY-TTC 500 ECU is equipped with an Ethernet interface.

| Nr.   | Starter Kit Components                        |
|-------|-----------------------------------------------|
| 1     | HY-TTC 500 ECU open housing                   |
| 2     | JTAG adapter                                  |
| 3     | JTAG adapter cable                            |
| 4     | Interface board                               |
| 5     | Cable harness 1.5 m                           |
| 6     | Installation CD C-Programming                 |
| 7     | Ethernet USB adapter with driver and software |
| 8     | PCAN USB adapter with driver and software     |
| 9     | Datacable 2m                                  |
| 10    | Quick Start Guide                             |

![8_image_0.png]( The image features a white box with a blue handle and a picture of a man on it. Inside the box, there is an assortment of electronic equipment, including several cords and wires. These items are neatly arranged in the box, creating an organized appearance.

The scene also includes a person standing next to the box, possibly admiring or working with the electronics inside. The combination of the white box, blue handle, and assorted electronics creates a visually appealing image that showcases both the contents and the overall design of the box.)

![9_image_0.png]( The image features a black case with various electronic equipment and accessories inside it. There are two cords placed next to each other on the left side of the case, while another cord is located towards the right side. A pair of scissors can be seen near the top-right corner of the case.

There are several books scattered around the case, with one book lying horizontally across the middle section and two more books placed vertically on the left side. Additionally, a remote control is located towards the bottom right area of the case. The assortment of items in the case suggests that it may be used for transporting or storing electronic equipment and accessories.)

| 6

## 4 Using The Interface Board

![10_image_0.Png](10_image_0.Png) 4.1 Hy-Ttc 500 Cable Harness

Connect the HY-TTC 500 to the connector interface board with the provided cable harness. Note: Do not use a cable harness from a different HY-TTC 500 variant! The HY-TTC 500 variants use different cable harnesses and the usage of the wrong cable harness may damage the HY-TTC 500 device.

## 4.2 Hy-Ttc 500 Can Termination

If termination of a CAN interface (2 x 60 Ωsplit termination) is required, then connect the jumper pins for the CAN interface as follows:

| CAN Interface   | Connect Jumper Pins           |
|-----------------|-------------------------------|
| CAN0            | 235 with 209 and 222 with 248 |
| CAN1            | 236 with 210 and 223 with 249 |
| CAN2            | 237 with 211 and 224 with 250 |
| CAN3            | 216 with 212 and 225 with 229 |

Figure 4.3 on the next page shows the jumper setting for CAN0 as example.

![11_image_0.png]( The image features a blue circuit board with various electronic components and wires on it. There are several rows of chips placed across the board, which appear to be part of a computer system or other electronic device.

The circuit board is filled with numerous small parts, including multiple chips in different positions. Some of these chips are located near the center of the board, while others can be found closer to the edges. The components on the board create an intricate and complex network that enables the functioning of electronic devices.)

![12_image_0.png]( The image displays a blue circuit board with several electronic components attached to it. There are two rows of numbers on the board, one row displaying numbers from 10 to 25 and another row showing numbers from 30 to 45. These numbers seem to be related to the functioning or configuration of the electronic device.

The circuit board is filled with various components, including a total of sixteen buttons arranged in different positions on the board. Some of these buttons are located near the top left corner, while others can be found scattered across the middle and right side of the board. The presence of multiple buttons suggests that this electronic device may have complex functions or require user input for its operation.)

## 4.3 Hy-Ttc 500 Power Supply

- Connect the power supply GND to the black socket named **BAT-**.

- Connect the positive power supply to the red socket named **BAT+ Power** and to **BAT+ CPU**
on the connector terminal block, e.g. by short-circuit of BAT+ CPU to **BAT+ Power**.

See also Figure 4.4 on the following page and Figure 4.5 on the next page.

![13_image_0.png]( The image features a close-up of an electronic circuit board with several components and wires. There are multiple chips on the board, including one that has been highlighted by a red circle. The board is filled with various parts, making it appear quite complex.

In addition to the main board, there are two other smaller boards visible in the scene, one located towards the top left corner and another at the bottom right corner of the image. These smaller boards seem to be part of the larger electronic circuitry setup.)

![13_image_1.png]( The image displays a blue circuit board with various electronic components on it. There are multiple switches and connectors, including a BAT+ connector, which is likely used for power supply purposes. The circuit board also features a number of red knobs that control the settings or functions of the device.

In addition to these components, there are two white plastic pieces on the circuit board, possibly serving as protective covers or guards. Overall, the image showcases an intricate and complex electronic component setup.)

## 4.4 Hy-Ttc 500 Terminal 15 (Kl15) Modes

- **Always on Mode**:

![14_image_0.png]( The image features a close-up of an electronic circuit board with a red arrow pointing to a small part on it. This part is likely a crucial component or a problematic area that needs attention. The rest of the circuit board consists of various components, including multiple rows of chips and wires.

In addition to the main focus on the electronic device, there are two other smaller objects in the scene: one located near the top left corner and another at the bottom right corner. These objects might be related to the electronic component or serve as a reference for the viewer.)

Put the jumper to **Always on** mode if the HY-TTC 500 shall be in active state independent of Terminal 15.

- **Normal Mode**:
Put the jumper to **Normal** mode if the HY-TTC 500 power-up shall depend on **Terminal 15**.

![14_image_1.png]( The image displays a blue circuit board with various electronic components and labels attached to it. There are several small switches on the board, which appear to be used for controlling different functions of the device. A prominent label is visible that reads "Terminal 15."

In addition to the switches, there are two knobs located towards the center of the circuit board. These knobs likely serve as adjustable settings or controls for the electronic components on the board. The overall appearance suggests a complex and intricate device with multiple functions controlled by these various switches and knobs.)

## 4.5 Status Leds

There are status LEDs for
- BAT+ Power

![15_image_0.png]( The image features a close-up of an electronic circuit board with several components and wires. There are multiple chips on the board, including one that is highlighted by a red circle. A small blue box can be seen towards the left side of the image, possibly indicating a specific component or area of interest.

The circuit board has various connectors and ports, such as two USB ports located near the center-left part of the board. The overall composition of the image suggests that it is an intricate electronic device with numerous components and connections.)

- BAT+ CPU
- Terminal 15
- Wake-Up See Figure 4.8 on this page and Figure 4.9 on the next page. A status LED is on, when the corresponding input voltage is above the lower voltage limit (8V) for safe operation of the ECU. The switching threshold of the LEDs is min. 8 V and max. 8.9 V (to guarantee a voltage >8 V over all parts tolerances).

![16_image_0.png]( The image features a blue circuit board with several components and labels on it. A red circle is placed over the label "Wake Up," indicating that this part of the circuit is important or needs attention. There are also other labels visible on the board, including one labeled "Terminal 15."

The circuit board contains multiple chips and connectors, with some located near the center and others towards the edges. The presence of these components suggests that the board may be part of a larger electronic device or system.)

## 4.6 Selecting Broadr-Reach® **Or Ethernet Mode**

For Ethernet mode, set all six jumpers as shown in Figure 4.10(a) on this page. Note: The Ethernet mode is only available for HY-TTC 580.

For BroadR-Reach® mode (also known as 100BASE-T1 Ethernet), set all six jumpers as shown in Figure 4.10(b) on the current page.

Note: The BroadR-Reach® mode is available on HY-TTC 590E, HY-TTC 590, and HY-TTC 508.

![16_image_1.png](1. A close-up of a blue circuit board with several red dots on it is shown.
2. The same blue circuit board is displayed again, but this time with the red dots highlighted by a circle around them.)

Figure 4.10: Jumpers for Ethernet or BroadR-Reach® mode

## 4.7 Hy-Ttc 500 Download And Debugging

For application download to and debugging of HY-TTC 500 there are the following options:
- For download and debugging via **JTAG** it is possible to use the **Lauterbach Power Debug**
Module with the **TTControl JTAG Adapter Board** and Lauterbach Batch files (***.cmm**).

- For download via CAN it is possible to use the **TTControl Downloader (TTC-Downloader)**
and the **Peak PCAN-USB Adapter**.

- For download via **Ethernet** it is possible to use the **TTControl Downloader** and an Ethernet Interface.

Note: For unexperienced users of the HY-TTC 500 it is recommended to use the CAN or JTAG
option. If you use Ethernet and an application is already flashed to the target, then you have to make sure that the application listens to download requests on the Ethernet. The example application of the Quick Start Guide does not listen to download requests.

## 5 C Programming Howto For Hy-Ttc 500 5.1 Overview

The following C programming Howto gives customers who purchase a product of the HY-TTC 500 family a quick overview of how to program these devices in C. This Howto also lists basic C code to demonstrate how to implement main functions and safety-relevant functions of the device. Finally, this Howto provides a step-by-step guide on how to flash the software with a Lauterbach Debugging Device.

## 5.2 Endianess

The endianess of the ARM®Cortex™-R4F core of the TI TMS570 CPU is configured to BE32.

Big-endian systems store the most-significant byte of a multi-byte data field in the lowest memory address. Also, the address of the multi-byte data field is the lowest address. The endianess of the HY-TTC 500 controllers can not be changed.

## 5.3 Tool Chain

The required tool chain is **TI ARM Code Generation Tools**, version 5.1.6. It conforms to the ISO/IEC 9899:1990 C standard [1], which was previously ratified as ANSI X3.159-1989 (ANSI C89).

An integrated development environment (IDE) named **TI Code Composer Studio (TI CCS)**, is available online from **http://processors.wiki.ti.com/index.php/Download_CCS\#** or from your local distributor.

Upgrade or downgrade the tool chain of your TI CCS installation to a specific version as described in the following instruction list:
Note: It might be necessary to turn off the antivirus protection in Windows Security for Windows 10 before starting with upgrade or downgrade.

1. Click Help > **Install New Software** (see Figure 5.1 on the following page) to open the **Install**
dialog.

2. Clear the check box **Show only the latest versions of available software** in the **Install**
dialog (see Figure 5.2 on the next page).

3. From the **Work with** list, select **Code Generation Tools Updates** (see Figure 5.3 on page 17).

If this option is not available, then you need to perform the following sub-steps, otherwise continue with step 4 on page 18.

a) Click Add (see Figure 5.4 on page 17) to open the **Add Repository** dialog. b) In the dialog (see Figure 5.5 on page 18):
- for **Name**, enter **Code Generation Tools Updates**
- for **Location**, enter **http://software-dl.ti.com/dsps/dsps_public_sw/**
sdo_ccstudio/codegen/Updates/p2win32/

![19_image_0.png]( The image displays a computer screen with a window open to a code editor. There are multiple options and buttons available on this screen, including "Code Composer Studio," which is likely used for programming or software development purposes. A red arrow is pointing towards the bottom right corner of the screen, possibly indicating an important button or action to be taken. The overall layout suggests that the user might be working with a specific program or tool related to coding and software development.)

![19_image_1.png]( The image displays a computer screen with a software installation window open. There is a red arrow pointing to the word "select" on the screen, indicating that it is currently selected. The software appears to be related to installing additional versions of a particular software program.

Apart from the main software installation window, there are two other windows visible in the image: one located at the top left corner and another at the bottom right corner. These windows might provide additional information or options during the installation process.)

![20_image_0.png](5.6 Work with files)

![20_image_1.png]( The image displays a computer screen with a software installation wizard open on it. There are several options available for selecting and installing different software packages. A mouse pointer is located near the bottom right corner of the screen, indicating that the user can interact with these options by clicking or dragging the cursor.

The screen features multiple buttons, including one at the top left corner, another in the middle-left area, and a third one towards the lower part of the screen. These buttons likely provide additional information or control settings for the software installation process.)

![21_image_0.png]( The image displays a computer screen with a software installation process underway. A window is open on the screen, and there are two buttons visible - one at the top left corner of the screen and another towards the right side. Additionally, there is a red circle highlighting the text "CodeGen Tools Updates" in the middle of the screen.

The computer screen also features a mouse cursor located near the bottom left corner of the image. The overall scene suggests that the user is installing or updating software on their computer system.)

c) From the **Work with** field, select **Code Generation Tools Updates**.

d) Continue with step 4 below.

4. From the list of tools, expand the **TI Compiler Updates** branch (see Figure 5.6 on the next page) and then select **ARM Compiler Tools 5.1.6** (see Figure 5.7 on the facing page)
5. Click **Next** and follow the instructions of the installation wizard.

![22_image_0.png]( The image displays a computer screen with an installation wizard open on it. There are several options available for the user to choose from, including "Compile Updates," "Install Software," and "Add/Remove Programs." A red arrow is pointing towards the "Compile Updates" option, which seems to be the primary focus of the screen at the moment. The installation wizard appears to guide users through the process of updating or installing software on their computer.) ![22_image_1.png]( The image displays a computer screen with a software installation wizard open on it. There are several options available for the user to choose from, including "Compile All" and "Find Environment." A red arrow is pointing towards the option that reads "AMM Compile Tools," indicating its importance or relevance in the context of the software installation process. The screen appears to be a part of an operating system setup, with various options laid out for the user to select and proceed with their desired actions.)

## 5.4 File Structure

The developer package is extracted into five directories:
- **Bootloader**

![23_image_0.png]( The image displays a computer screen with various windows open on it. One of the windows is focused on a file that has been downloaded and saved to the computer's hard drive. The file appears to be a Microsoft Word document, which can be seen in the lower-left corner of the screen.

In addition to the main window, there are other smaller windows visible across the screen, likely containing different applications or tools used for various tasks on the computer.)

- **Documentation**
- **FPGA_Bitstream**
- **Get_Started**
- **Release_Notes**
Figure 5.8 on the current page shows the contents of the **Get_Started** directory.

![23_image_1.png](100% of the cat's stomach is visible on this image. The cat appears to be well-fed and healthy, with a full stomach.)

Figure 5.9(a) on the facing page shows the contents of the **examples** directory. The **examples** directory has some prebuilt projects to explain the usage of certain functions. Figure 5.9(b) on the next page shows the contents of the **template** directory, which contains a template for starting a new project.

![24_image_0.png](1. The image displays a computer screen with two windows open side by side. One window is showing a folder view of files, while the other window is displaying a list of folders and files.
2. Both windows have a blue background, which adds to their visual appeal. A total of nine files can be seen in the folder view, each occupying different positions within the screen. The list of folders and files contains 14 items, with some overlapping or partially visible due to their positioning.
3. The two windows are placed next to each other, allowing for easy comparison between the folder view and the list of files.)

The template should help you getting started. Every new project should start with a copy of this folder as base. The **template** directory contains several subdirectories that are necessary for a project:
- bsp: Subdirectory bsp (Board Support Package) contains files for the linker and board specific objects.

- **build**: Subdirectory **build** is an empty folder in which the generated files are put during the compile process.

- env: Subdirectory env (Environment) contains auxiliary tools like these two:
- File **AddAPDB.exe** patches the **.hex** files with the CRC checksum, application size and build date.

- File **nowECC.exe** generates a second file which contains the corresponding ECC data if the Lauterbach Device is used for flashing the device.

- inc: Subdirectory inc (Include) contains all the header files that are necessary to create a project with the C programming language.

- lib: Subdirectory lib (Libraries) contains the libraries **ttc500.lib** (for the hardware driver)
and **bsp.lib** (for the startup code).

- src: Subdirectory src (Source) contains the source code files to create a project with the C
programming language.

## 5.5 Development Environment

TTControl GmbH recommends the **TI Code Composer Studio (TI CCS)** as your primary development environment.

## 5.6 Settings.Mk

The **Settings.mk** is needed to tell the **Makefile** what settings to use. Some basic settings can be modified in this file.

\# TTC-Downloader hardware type DOWNLOADER_HW_TYPE = 0x00400807 \# Bootloader version BOOTLOADER_VERSION = 3.0 \# path with C compiler ifndef C COMP PATH
C_COMP_PATH = C:\TI\ccsv6\tools\compiler\arm_5.1.6\bin endif \#--
\#
\#=
\# compile code for profiling or debugging 0 ... profiling
\#
1 ... debugging
\#
\#  2 ... release OPT_TYPE = 1 ifeq ($(OPT_TYPE), 0)
\# optimize for profiling OPT_STR := PROFILING
endif ifeq ($(OPT_TYPE), 1)
\# optimize for debugging OPT_STR := DEBUGGING
endif ifeq ($(OPT_TYPE), 2)
\# optimize for release OPT_STR := RELEASE
endif

## Figure 5.10: Settings.Mk

- DOWNLOADER_HW_TYPE tells AddAPDB.exe for which HW type to compile.

- 0x00400807 compiles for a 1st generation¹ HY-TTC 580.

- 0x00600807 compiles for a 1st generation¹ HY-TTC 540.

- 0x00A00807 compiles for a 1st generation¹ HY-TTC 520 ³
- 0x00C00807 compiles for a 1st generation¹ HY-TTC 510. - 0x00201007 compiles for a 2 nd generation² HY-TTC 580.

- 0x00402007 compiles for a 2 nd generation² HY-TTC 540.

- 0x00602007 compiles for a 2 nd generation² HY-TTC 520 3 . - 0x00802007 compiles for a 2 nd generation² HY-TTC 510.

- 0x00201C07 compiles for a HY-TTC 590.

- 0x00401C07 compiles for a HY-TTC 590E 3.

- 0x00201807 compiles for a HY-TTC 508.

- **C_COMP_PATH** tells the **Makefile** what compiler to use. **TI ARM Code Generation** tools are the only ones recommended by TTControl GmbH. Note: Make sure the path is the one you selected as installation folder for the installation of TI CCS.

- **OPT_TYPE** configures the compiler options to predefined values, for code optimizations and debugging symbols. Select 1 for **debugging** and 2 for a **release build**. If any other compiler or linker options are needed, please refer to the **TI ARM Code Generation Tools manuals** [2] and [3].
Additionally all the paths for the different folders are specified in **Settings.mk**. They must be adjusted if any of the folders are moved.

## 5.7 Application Examples

This section shows a basic example. Section 5.7.1 on this page shows how to build the application with CCS. Section 5.7.2 on page 27 shows the code with some overview comments about the code structure. For more information, see Section 5.7.3 on page 30, Section 5.7.4 on page 30, and Section 5.7.5 on page 32.

## 5.7.1 Build Application

1. Open the Code Composer Studio. 2. Click File > New > **Project...** to open the **New Project** dialog (see Figure 5.11 on the next page).

3. On the **Select a wizard** page, select **Makefile Project with Existing Code** (see Figure 5.11 on the facing page) and then click **Next**.

4. On the **Import Existing Code** page, fill the fields as follows (see Figure 5.12 on the next page):
- for **Project Name**, enter any name (**HY-TTC_500_Demo** in our example) - for **Existing Code Location**, select the **template** folder as shown in Figure 5.13 on page 26
- for **Languages**, select C and C++
- for **Toolchain for Indexer Settings**, select **<none>**
Then click **Finish**.

5. From the menue, select Project > **Build All**. The **Console** pane opens and shows the build process (see Figure 5.14 on page 26).

6. After successful building, the **Console** pane shows **No errors** (see Figure 5.14 on page 26).

![28_image_0.png]( The image displays a computer screen with a window open to a software program. In this particular window, there is an option for creating a new project called "Malefele Project." A red arrow points towards the word "with" on the screen, indicating that it is being highlighted or selected.

The computer screen also has other windows visible in the background, suggesting that multiple applications are running simultaneously. The focus of this particular window, however, remains on creating a new project with an existing code.)

![28_image_1.png](1. The image displays a computer screen with a blue window open, likely related to importing code or working on a project.
2. There is a red arrow pointing towards the word "importing" within the window.)

![29_image_0.png](13. Browse for Folder Dialog Box)

![29_image_1.png]( The image shows a computer screen with a blue background and white text. There is an open window displaying a program that appears to be related to file management or data processing. A red arrow is pointing towards the word "build" on the screen, indicating that it might be a command or action related to the software being used. The overall scene suggests that someone is working with files or data using this particular application.)

## 5.7.2 General

Every program must include at least the header files **IO_Driver.h** and **APDB.h** (see Figure 5.15 on the current page). The Application Descriptor Block (APDB) is a 128-byte structure that is used by download tools and the bootloader to update the application and do CRC checks. The structure Apdb_t must be defined (see Figure 5.16 on the following page).

| /******************************************************************************  * Includes  ******************************************************************************/ #include "APDB.h" #include "IO_Driver.h" #include "IO_DIO.h" #include "IO_POWER.h" #include "IO_RTC.h" Main include files for I/O driver and APDB Other includes Figure 5.15: Includes   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![31_image_0.png]( The image displays a computer screen with a lot of text and code written on it. There are multiple lines of code that appear to be related to an application or software development process. Some of these lines include "application descriptor block" and "application decoder."

The screen also features a few numbers scattered throughout the text, which might indicate specific values or measurements within the code. Overall, it seems like a complex technical document that requires careful attention and understanding to decipher its meaning.)

The first step is to initialize the **IO_Driver** in the **main()** function. After that, every channel, function or interface can be initialized with individual parameters (Figure 5.17 on the current page).

/******************************************************************************
 * **Main Task**
 ******************************************************************************/
\#pragma TASK( main ); void main(void)
{ volatile IO_ErrorType io_error = IO_E_OK;
 ubyte4 timestamp = 0; ubyte2 pwm0_current = 0; bool pwm0_fresh = FALSE;
 /* safety configuration */
 IO_DRIVER_SAFETY_CONF safety_conf;
 /* 10ms cycle period with 25% window size,
 * no resets,
 * 30ms glitch filter, * no callbacks */
 safety_conf.command_period = 10000; safety_conf.windows_size = SAFETY_CONF_WINDOW_SIZE_25_PERCENT;
 safety_conf.reset_behavior = SAFETY_CONF_RESETS_DISABLED;
 safety_conf.glitch_filter_time = 30; safety_conf.error_callback = NULL;
 safety_conf.notify_callback = NULL;
 
 /* initialize I/O driver with safety configuration */
 io_error = IO_Driver_Init(&safety_conf);
1) Initialize I/O driver
 /* setup a PWM output with current measurement */
 io_error = IO_PWM_Init( IO_PWM_00 /* PWM channel 0 */
 , 100 /* frequency is 100Hz */
 , TRUE /* positive polarity */ , FALSE /* no diagnostic margin */
 , NULL /* not safety critical */ );
2) Initialize I/Os
 /* turn on power stage */
 io_error = IO_POWER_Set( IO_INT_POWERSTAGE_ENABLE , IO_POWER_ON
 );
 /* turn on safety switch 0 */ io_error = IO_POWER_Set( IO_INT_SAFETY_SW_0
 , IO_POWER_ON
 );
 /* start the RTC */
 IO_RTC_StartTime(&timestamp); 

| 3) Enable outputs 4) Start timestamp   |
|----------------------------------------|

Figure 5.17: Application initialization After initializiation, typically a while loop (**while (1)**) is executed. This is the main loop of the application, and it will be executed each cycle time ms. See Figure 5.18 on this page.

![33_image_0.png]( The image displays a white paper with a diagram that appears to be a flowchart or a representation of a computer program. There are several lines and boxes on the paper, indicating different steps within the process.

In addition to the main diagram, there is also a table located towards the bottom right corner of the page. The table contains various numbers and text, possibly providing more context or details about the flowchart.)

Be aware that the duration of each cycle is 10000 µs in this case. See also Figure 5.17 on the previous page, parameter **safety_conf.command_period**.

## 5.7.3 Help For C Driver Functions

The I/O driver API documentation (**HY-TTC_500_IO_Driver_Manual_V3.1.0.chm** [4]) is available in the compiled HTML format and can be found in **Documentation > Manuals**. It provides a short overview of the available I/O driver functions as well as detailed descriptions of those functions, including parameters, return values and examples.

## 5.7.4 Linking Constant Data

Constant data is linked to the application region by default. However, it can also be linked to the external flash memory (if available) or to the application configuration data region. The major difference is the integrity protection of their respective contents. While constant data linked to the external flash memory is protected by the application CRC, the application configuration data region's integrity must be ensured by the application itself. Figure 5.19 on the facing page depicts an example of how to link constant data to the external flash memory as well as to the application configuration data region.

/******************************************************************************
 * **Global data**
 ******************************************************************************/

```
#pragma SET_DATA_SECTION("#$% &
                             'FLA(
                                   )
                                             
                                    ")
/*
 * After setting the active data section to " #$%&_FLASH"* the linker places
 * ALL of the subsequently defined variables to the +
                                                    ,-
                                                      ernal flash memory.
 * 
 * Attention: Be aware that the constant data linked to the e,-
                                                               +
                                                                         
                                                                .
                                                                          
                                                                nal flash
 * memory is protected by the application CR/0 Thus, any modification
 * will lead to an invalid application CRC.
 */
const ubyte1 foo = 1
                   2
                             
                     1; /* foo is linked to e,-
                                                  +
                                                            
                                                   .
                                                             
                                                   nal flash */
const uby-
          +
                    
          3
                    
            bar = 124
                     3567 /* bar is also linked to +
                                                    ,
                                                              
                                                     ternal flash */

```

#pragma SET_DATA_SECTION("#/**FG_FLA**(
)

## ")

/*
 * After setting the active data section to " \#CFG_FLASH"* **the linker places**
 * ALL of the subsequently defined variables to the configuration flash memory.

 * 
 * Attention: Be aware that the content of the configuration flash memory is
 * NOT protected by the application CR/0 **This means that the data**
 * integrity of the configuration flash memory must be ensured by
 * the application itself.

 */
const ubyte2 wayne = 8 5 6**; /* wayne is linked to configuration flash */**

#pragma SET_DATA_SECTION()
/*
 * After placing the respective global variables to the +
,

ternal and
 * configuration flash memory, the active data section needs to be reset
 * to its default value.

 */

## Figure 5.19: Linking Constant Data To The External Flash And/Or Application Configuration Data 5.7.5 Safety Configuration

For safety-critical applications, every safety-critical IO pin can be initialized with a safety configuration. Please refer to **HY-TTC_500_Series_C_API_Manual.chm** [4] for further details.

To enable any outputs, the I/O Driver has to be configured with a valid safety configuration. The I/O Driver safety configuration consists of several elements:
- **command_period [**µs]: Sets the period at which the application cycle is executed.

Important: The **command_period** is checked by the watchdog and has to meet the window configuration.

- **window_size [%]**: Configures the size of the window for the watchdog which checks the command_period. The application cycle has to fulfill those timing requirements.

- **reset_behavior**: Configures how often the watchdog can restart the CPU in case of an error. If a safety-critical error occurs, the watchdog will reset the CPU and start again. After the maximum number of resets, a permanent safe state will be entered.

- **glitch_filter_time [ms]**: Sets the time a temporary error condition must persist to cause an error reaction by the safety function.

- **error_callback**: Configures the error callback for the application. It can be set to **NULL** to disable the error callback.

- **notify_callback**: Configures the notification callback for the application. It can be set to NULL to disable the notification callback.

## 5.7.6 Debugging Of A Safety-Critical Application

The **DebugKey** field of the APDB can be set to **0xC0FFEE** to enable debugging of a safety-critical I/O Driver. This can be done directly in the definition of the APDB (Figure 5.16 on page 28).

## 5.8 Flashing The Hy-Ttc 500

There are two ways how to flash a HY-TTC 500 device: Using the Lauterbach Debugging Device or the TTC-Downloader Tool via CAN or Ethernet. Both ways will be described step by step. For further information on each product, please refer to the respective manual.

## 5.8.1 The Lauterbach Debugging Device And Trace32 5.8.1.1 Overview

The Lauterbach product TRACE32-ICD supports a wide range of on-chip debug interfaces. The hardware for the debugger is universal and allows interfacing different target processors by simply changing the debug cable and the software.

## 5.8.1.2 Installation

The installation is started automatically or by executing **setup.bat** on the installation DVD.

![36_image_0.png]( The image features a computer setup with a laptop and a desktop computer placed next to each other. On the laptop screen, there is an open program displaying data related to the Laubertbach Base Station. A mouse can be seen on the desk near the laptop, indicating that it's being used for input or navigation within the software.

In addition to the main setup, a keyboard and two TV screens are also visible in the scene. The TV screens seem to be displaying different information related to the computer system. Overall, this image showcases a well-equipped workspace with various devices and screens to facilitate efficient data processing and analysis.)

The installation wizard guides you trough the installation process:

1. After the Welcome page, confirm the licensing agreements on the **License Software Agreement** page.

![36_image_1.png]( The image displays a computer screen with a window open to a folder selection page. There are multiple folders displayed on the screen, and one of them is labeled "TRACE." Above this folder, there is a message that reads "Select Destination Location." This indicates that the user has been prompted to choose where they would like to save or install the file. The computer screen takes up most of the image, with no other objects visible in the frame.)

2. On the **Choose Destination Location** page, set the installation path (see Figure 5.22 on this page).

3. On the **Installation Type** page, select **Custom Installation** (see Figure 5.23 on the next page).

4. On the **Setup Type** page, select **New Installation** (see Figure 5.24 on the following page).

5. On the **TRACE32 Product Type** page, select **Debugger** (see Figure 5.25 on page 35). 6. On the **Maintenance Notice** page and click **Next** (see Figure 5.26 on page 35). 7. On the **Debugger Interface Type** page, select **USB Interface** (see Figure 5.27 on page 36).

![37_image_0.png]( The image displays a computer screen with a software installation wizard open on it. There are two buttons visible on the screen, one of which is labeled "Custom Installation." A red circle is placed over this button, drawing attention to its importance.

In addition to these buttons, there are several other elements present in the image. These include a keyboard and a mouse located near the bottom left corner of the screen, as well as two more buttons situated towards the top right side. The overall scene suggests that the user is about to install or configure software on their computer system.)

![37_image_1.png]( The image shows a computer screen displaying a software installation process for an operating system. There is a message on the screen that reads "Please select setup type for installation." A button labeled "New Installation" can be seen below this message.

In addition to the main text, there are two smaller buttons located at the bottom right corner of the screen. The first one is labeled "Back," and the second one is labeled "Cancel." These buttons likely allow the user to navigate through different options or cancel the installation process if needed.)

![38_image_0.png]( The image displays a computer screen with several options and settings for a software program. There are multiple windows open on the screen, each containing different information or instructions related to the program. A red highlight is placed over one of the windows, drawing attention to it.

In addition to these windows, there are two clocks visible in the image – one located near the top left corner and another towards the bottom right side. The presence of these clocks suggests that the user might be monitoring time-sensitive tasks or events related to the software program.)

![38_image_1.png]( The image displays a computer screen with a blue background and white text. On the screen, there is an advertisement for a software product called TRADE, which appears to be related to trading or finance. The advertisement includes a picture of money and a description of how to check the software's features.

In addition to the main advertisement, there are two smaller images on the screen: one located at the top left corner and another in the lower right area. These images might be related to the product or serve as visual elements for the advertisement.)

![39_image_0.png]( The image displays a computer screen with a message on it, likely related to debugging or troubleshooting an issue. There are two buttons visible on the screen, one towards the left side and another at the top right corner. A window is open in the background, possibly containing more information about the problem being addressed.)

8. On the **OS Selection** page, select **PC Windows XP/VISTA/7/8/10** (see Figure 5.28 on this

![39_image_1.png]( The image displays a computer screen with a blue background and a message on it. There is a window that says "OS Selection" at the top left corner of the screen. Below this text, there are several options to choose from, including "Windows," "Mac OS X," and "Linux."

In addition to these choices, there are two more windows visible in the image: one on the right side with a message that reads "The selected operating system is Windows," and another window at the bottom left corner of the screen. The latter appears to be related to selecting an installation type.)

page).

9. On the **CPU selection** page, select **ICD ARM 32-bit** (see Figure 5.29 on the next page).

10. In the **TRACE32 executable type** dialog, click Yes for a 64-bit OS (see Figure 5.30 on the facing page).

11. On the **Environment variable T32ID** page, choose the default value T32 (see Figure 5.31 on the next page).

12. If you are asked to install the Lauterbach device software, click **Install** (see Figure 5.32 on page 38). Use the suggested default settings for the device software installation process.

13. On the **Environment variable T32TMP** page, set the destination folder (see Figure 5.33 on page 38).

![40_image_0.png]( The image displays a computer screen with a selection page for CPUs. There are multiple options available to choose from, including different types of processors and their corresponding prices. A total of sixteen CPUs can be seen on the screen, each accompanied by its respective price.

The selection page is organized in such a way that it allows users to easily view and compare the various CPU options based on their specific needs and preferences. The layout provides an accessible and user-friendly experience for those looking to purchase or upgrade their computer components.)

![40_image_1.png]( The image displays a computer screen with a message on it that reads "For your 64-bit host operating system are bit and bit." This message is likely related to a software installation or configuration process. There is also a question mark displayed next to the message, possibly indicating an error or asking for input from the user. The overall setting suggests that this is a technical support page or a troubleshooting guide for a specific software application.)

![40_image_2.png]( The image displays a computer screen with a message on it that reads "Please enter your environment variable TD32E executable type dialog." There is also a button labeled "OK" located at the bottom of the screen.)

![41_image_0.png]( The image displays a computer screen with a software installation process underway. A message is displayed on the screen asking if you would like to install this device's software. There are two buttons visible on the screen - one that says "Yes" and another that reads "No."

In addition, there is a person's name in the top left corner of the screen, possibly indicating who the installation is for or who set up the system. The computer setup process seems to be well underway, with the user likely deciding whether to proceed with the installation.)

![41_image_1.png]( The image displays a computer screen with an open folder and a message that reads "Environment Variable TMTP." There is also a blue background on the screen, which adds to the overall appearance of the display.)

14. On the next pages related to screen configuration, use the default settings.

![42_image_0.png]( The image displays a computer screen with a message that reads "Prepare TRACEE for Integrations with Other Products." There are several options and instructions displayed on the screen, including a list of products like Eclipse, LabVIEW, and other tools.

The screen also contains a button labeled "Any integration done with TRACEE API," which is likely related to the integration process. The overall context suggests that this message might be related to software development or integration tasks involving these specific products.) 15. On the **Prepare TRACE32 for Integration with other products** page, select **No Integration**
(see Figure 5.34 on this page).

![42_image_1.png]( The image displays a computer screen with a blue background and white text. On the screen, there is a window open that says "Select Way to Submit Registrations." Below this message, there are several options for submitting registration forms, including online, by mail, or in person.

The computer screen also has a button labeled "Register Online" with an arrow pointing towards it. The image appears to be from the perspective of someone looking at the computer screen, possibly preparing to submit their registration information.)

16. For the pages **Folder Selection** and **Folder program group type**, use the default settings.

17. On the **Select way to submit registration** page, select **Register later** (see Figure 5.35 on the current page).

18. The last page **TRACE32 software is successfully finished** shows the installation path and how to start the software (see Figure 5.36 on the following page). Click **Finish** to complete the installation.

![43_image_0.png]( The image displays a computer screen with a software installation process underway. A message is displayed on the screen stating that the TRACE software has been successfully installed. There are two buttons visible on the screen, one located at the bottom left corner and another towards the right side of the screen.

The computer monitor occupies most of the image, with a blue background and white text providing information about the installation process.)

![43_image_1.png]( The image features a close-up view of a black cable with multiple connectors on it. There are two main cables visible, one extending from the top left corner to the bottom right corner and another smaller cable running horizontally across the middle of the scene.

In addition to these cables, there is also a small connector located near the center-left side of the image. The overall composition suggests that this could be an electronic component or a part of a larger electrical system.)

## 5.8.1.3 Usage 5.8.1.3.1 Hardware

The HY-TTC 580 Starter Kit comes with the following components:
- JTAG Adapter Board (Figure 5.37 on the current page) and JTAG Cable (Figure 5.38 on this

![43_image_2.png]( The image features a close-up of an electronic device with several components attached to it. There are multiple cables and connectors visible on the device, which appears to be a computer or communication system.

In addition to the main device, there is another smaller object located towards the right side of the image. This object seems to be part of the same electronic device as well. Overall, the scene showcases an intricate and complex electronic setup.)

page)

- open housing of the HY-TTC 500 ECU to enable a connection with the JTAG interface (Figure 5.39 on the next page)

![44_image_0.png]( The image displays a close-up view of an electronic circuit board with various components and connections. There are multiple wires running through the board, connecting different parts together. A few LEDs can be seen on the board, along with other electronic components.

A yellow arrow is pointing towards one of the LEDs, indicating its location or function within the circuit. The image also includes a bar graph that provides additional information about the components and their arrangement on the board.)

The following components from Lauterbach are required:
- Lauterbach Base Station. For example, **Power Debug Interface USB 3 LA-3500** - Lauterbach Debug Cable **JTAG-CORTEX-A/R LA-7843** - Lauterbach AC/DC power supply adapter
- USB connector to connect Lauterbach and PC
Please refer to Figure 5.40 and Figure 5.41 on the following page for how to connect, for example, a HY-TTC 580 with Lauterbach debugger.

![45_image_0.png]( The image displays a white table with various electronic components on it. There are two computer boards placed side by side, one of which is larger and occupies most of the space on the table. A smaller board can be seen towards the right edge of the table.

In addition to the computer boards, there are several cords scattered across the table. Two cords are located near the left side of the table, while another one is positioned closer to the center. The last two cords are placed on the right side of the table, with one being longer and extending towards the edge.

A cell phone can also be seen resting on the table, slightly above the middle-right area.)

![45_image_1.png]( The image features a computer circuit board with various electronic components attached to it. A blue and white device is connected to the board through a series of wires, which are visible on the surface of the board. There are two main cords in the scene, one running horizontally across the middle of the board and another vertically down the right side.

In addition to these primary components, there are several smaller electronic parts scattered around the circuit board, including a few near the top left corner and others at various points along the horizontal wire. The overall composition suggests that this is an intricate electronic device being assembled or worked on.)

## 5.8.1.3.2 Led Description Done Led

The DONE LED (see Figure 5.42 on the current page) indicates the configuration status: If the DONE LED is ON, the FPGA is not configured. If the DONE LED is OFF, the FPGA is configured.

![46_image_0.png]( The image displays a close-up of an electronic component, likely a computer chip or a part of a circuit board. There are several LEDs (light emitting diodes) on the surface of the component, with some located closer to the center and others towards the edges.

The image is accompanied by a text description that highlights the different LEDs in various positions across the component. The text also indicates that there are four LEDs in total, with one positioned at the top left corner, another on the right side of the component, and two more located near the center.) 

Debug LEDs The LEDs LED0. . . LED2 shown in Figure 5.42 on this page are for debugging. They are controlled by the **IO_DEBUG_SetOutputPin()** function. See [4] for details. They are completely controllable by the application.

Signal pins The signal pins on the JTAG adapter board (see Figure 5.43 on the next page) indicate the inverted status of the DONE LED and the Debug LEDs. That is, if a LED is ON, the corresponding signal pin has low voltage (0).

Note: The signal pins shown in Figure 5.43 on the following page are unprotected CMOS outputs.

Any external voltage applied on these pins can damage the ECU.

![47_image_0.png]( The image features a close-up of an electronic device with many small parts and components. There are several blue connectors on the board, which seem to be part of the circuitry. A red circle is highlighted on one of these connectors, possibly indicating a specific component or function.

In addition to the connectors, there are two screws visible in the image, one located near the top left corner and another towards the bottom right corner. The close-up view allows for detailed examination of the electronic device's internal structure and components.)

## 5.8.1.3.3 Software

1. Connect the Lauterbach Base Station and Debug Cable to the PC and power supply and

![47_image_1.png]( The image displays a computer screen with various windows open on it. One of the windows is focused on a search for "trace32.exe." There are multiple options available to choose from within this window, including "File," "Edit," and "View."

In addition to the main window, there are other smaller windows visible in the background, possibly containing more information or tools related to the trace32.exe search. The overall scene suggests a computer-related task being performed on the screen.)

install the necessary drivers.

2. Make the connections as described in Section 4.3 on page 9 and in Section 5.8.1.3.1 on page 40.

3. Perform a power cycle.

4. Click **Start > Trace32 ICD ARM32 USB** on the Windows start menu to start the Lauterbach debugger software.

5. The HY-TTC 500 template comes with a predefined ***.cmm** script. Start the script by clicking File > Run Script (Figure 5.44 on the current page).

6. A dialog asks whether you want to flash the application or not (Figure 5.45 on the facing page).

If you click Yes, the flashing process starts.

7. When the flashing process has finished, the next dialog asks whether you want to keep the current Trace32 window configuration or reset to a default configuration (Figure 5.46 on the next page).

![48_image_0.png]( The image displays a computer screen with an application that allows users to program flash memory. There is a blue button on the screen labeled "Yes," and another one labeled "No." Above these buttons, there are two more buttons, one of which says "Program Application to Flash Memory?" and the other reads "Flash Memory." The computer screen appears to be open to this specific application.)

![48_image_1.png](6.54 Flash Application Applicaiton Dialogue)

![48_image_2.png]( The image displays a computer screen with an error message displayed on it. The message reads "Restart Window Configuration?" and has two buttons below it - one labeled "Yes" and another labeled "No." This indicates that the user might be facing some issues related to their window configuration, and they are prompted to either restart or not restart the process.)

8. After the flashing procedure, you return to the Trace32 window (Figure 5.47 on the following page). Its appearance depends on the chosen windows configuration.

## 5.8.2 The Ttc-Downloader Tool 5.8.2.1 Tool Download

You can download the TTC-Downloader tool from our Service Area:
1. Enter the **HY-TTC Downloader** page. 2. From there, enter the page with the latest release.

3. Download **Installer - TTC-Downloader <version>.zip**. 4. Extract the **.zip** file on your computer.

The tool comes with a documentation file **help.chm**.

## 5.8.2.2 Device Connection

A connection with the HY-TTC 500 can be established either via CAN or via Ethernet as described in Section 5.8.2.2.1 on the current page and Section 5.8.2.2.2 on the following page.

## 5.8.2.2.1 Connecting Via Can

To connect to the device via CAN, use a CAN connector (e.g., **Peak PCAN-USB**) and connect it to CAN0 of the HY-TTC 500. Then power off the device and open the TTC-Downloader.

If the correct CAN settings are not known, then force the default connection settings by connecting the pin sensor supply 0 and sensor supply 1 of the HY-TTC 500 to ground. For variants without

![49_image_0.png]( The image displays a computer screen with four different windows open, each showing various types of data or information. In one window, there is a list of numbers and words arranged vertically, while another window shows a spreadsheet with multiple columns of data. A third window features a graph displaying numerical values in a bar chart format, and the fourth window displays a series of text files.

The computer screen appears to be part of a larger system, possibly for managing or analyzing data related to finance, business, or other fields that require organized information.)

pin sensor supply 1, the default connection can be set by connecting the pin sensor supply 0 to ground. See the TTC-Downloader documentation **help.chm**, Section **Advanced Features > The** CAN Fallback Mode for the HY-TTC 500 variant specific default CAN channel. Note: If you have changed the TTC-Downloader settings in previous applications of the HY-TTC 500, then make sure that you reset them to the default values.

To start connecting press F2 and quickly power on the device, while the Downloader progress bar appears (see Figure 5.48(a) on the next page).

After successful connection, the downloader will identify the device and prepare the flashing process (see Figure 5.48(b) on the facing page).

## 5.8.2.2.2 Connecting Via Ethernet

Note: For unexperienced users of the HY-TTC 500 it is recommended to use the CAN option. If you use Ethernet and an application is already flashed to the target, then you have to make sure that the application listens to download requests on the Ethernet. The example application of the Quick Start Guide does not listen to download requests.

To connect to the device via Ethernet, use the Ethernet port of your computer and connect it to the Ethernet port of the HY-TTC 500. Note that a point-to-point Ethernet connection is mandatory. Open the TTC-Downloader.

The next step depends on the content of the flash memory:

![50_image_0.png](​The image displays two screens side by side, each showing a different stage of installing software on a computer. The first screen shows an error message, while the second one indicates that the installation is progressing. There are also several icons and files visible in both screens, including a "connect to TC downloader" option.

In addition to these screens, there are multiple windows open on each screen, with some of them displaying information about the software installation process. The presence of various icons and files suggests that this is an active installation process taking place on the computer.)

- If the target has no application and no CODESYS runtime system flashed, then use the default connection settings. To set the default settings, open the **Preferences** dialog box (e.g. with Ctrl + P) and click **Default**.

- If the target has an application or CODESYS runtime system flashed, then enter the correct Ethernet settings. If you do not know the correct Ethernet settings, please use CAN to connect with the target as described in Section 5.8.2.2.1 on page 45. To set the correct Ethernet settings, open the **Preferences** dialog box (e.g. with **Ctrl + P**), enter the values, and click **Apply**.

In the **Preferences** dialog box, open the **Ethernet** tab, select the used Ethernet adapter in the Network Adapter dropdown menu, and click **Apply**.

Close the **Preferences** dialog box. Now power on the target. Start the connection procedure by pressing F5. After successful connection, the downloader will identify the device and prepare the flashing process (see Figure 5.48(b) on this page).

## 5.8.2.3 Flashing To Hy-Ttc 500

After successful connection via CAN or Ethernet, you can open your **.hex**-file and flash the device with the Download icon in the **Application Download** group in the Node area. For further information about how to update the bootloader/FPGA IP, read/write from/to EEPROM, and other features of the TTC-Downloader, please refer to the documentation **help.chm** for the tool.

## 6 Memory Mapping 6.1 Memory Map For Internal Flash And Ram

The following table specifies the start address and size of the bootloader, FPGA IP, APDB, **application** and **application configuration data** for the HY-TTC 500 controllers. See also the file mem_ttc500_bl.lsf, which is delivered with the package.

Note: A compatible FPGA is delivered with the package. Note: The application configuration data region is not protected by the application CRC and thus, its integrity must be ensured by the application itself. For detailed information about modifying the flash memory, refer to the documentation **help.chm** for the TTC-Downloader, page **Modifying Flash/EEPROM Memory**.

HY-TTC 500 Start Address **Size**

![51_image_0.png]( The image displays a diagram that illustrates various layers of data storage and processing. There are four main sections within this diagram, each representing different levels of data handling.

The first section is labeled "Application," which likely refers to the application software or program that utilizes the data stored in the other sections. This layer is situated at the top left corner of the image.

The second section is labeled "Data," indicating the storage and organization of raw data within the system. This layer occupies a large portion of the middle area of the image, extending from the top right to the bottom left.

The third section is labeled "Application Layer," which likely refers to the communication between the application software and the data storage layer. It spans across the entire width of the image, from the top left corner to the bottom right corner.

Finally, the fourth section is labeled "Bootloader," representing the initial stage of the system's operation where the bootloader loads the operating system into memory. This layer occupies a small portion of the lower-left area of the image.) Application Cfg. Data 0xF0200000 65536 Bytes Application 0x000A0100 2490112 Bytes

APDB + CRC 0x000A0000 256 Bytes

FPGA IP 0x00020000 524288 Bytes

Bootloader 0x00000000 131072 Bytes

The following table specifies the start address and size of the **internal RAM** for the HY-TTC 500 controllers.

| HY-TTC 500   | Start Address   | Size         |
|--------------|-----------------|--------------|
| Int. RAM     | 0x08003000      | 217088 Bytes |

## 6.2 Memory Map For External Flash And Ram

The following tables specify the start address of the **external RAM** and **Flash** for the HY-TTC 500 controllers.

![52_image_0.png]( The image displays a computer screen with various information and data displayed on it. There are several lines of text that provide details about the system's RAM, including the size (2060 MB), the number of bytes (10736000), and the type of memory (Extended Data Memory). The screen also shows a diagram with multiple bars, possibly representing data transfer rates or other technical information.

The image is quite detailed, making it easy to understand the system's specifications and performance.)

| HY-TTC 580   | Start Address   | Size          |
|--------------|-----------------|---------------|
| Ext. RAM     | 0x60000000      | 2097152 Bytes |
| Ext. Flash   | 0x64000000      | 8388608 Bytes |
| HY-TTC 540   | Start Address   | Size          |
| Ext. RAM     | 0x60000000      | 2097152 Bytes |
| HY-TTC 520   | Start Address   | Size          |
| Ext. RAM     | 0x60000000      | 2097152 Bytes |

## Bibliography

[1] ISO/IEC. ISO/IEC 9899. International Standard, International Organization for Standardization (ISO),
International Electrotechnical Commission (IEC), 12 1990.

[2] Texas Instruments. ARM Assembly Language Tools, 06 2013. SPNU118L, v5.1. [3] Texas Instruments. ARM Optimizing C/C++ Compiler, 06 2013. SPNU151I, v5.1. [4] TTControl GmbH. HY-TTC 500 I/O Driver Manual. S-TTC5F-G-20-001. [5] TTControl GmbH. HY-TTC 500 Quick Start Guide - CODESYS. User Documentation D-TTC5F-G-20-014, TTTech, BU Off-Highway, Services & Operations.

## Legal Disclaimer

THE INFORMATION GIVEN IN THIS DOCUMENT IS GIVEN AS A SUPPORT FOR THE USAGE OF THE PRODUCT AND SHALL NOT BE REGARDED AS ANY DESCRIPTION OR WARRANTY
OF A CERTAIN FUNCTIONALITY, CONDITION OR QUALITY OF THE PRODUCT. THE RECIPIENT OF THIS DOCUMENT MUST VERIFY ANY FUNCTION DESCRIBED HEREIN IN THE REAL
APPLICATION. THIS DOCUMENT WAS MADE TO THE BEST OF KNOWLEDGE OF TTCONTROL GMBH. NEVERTHELESS AND DESPITE GREATEST CARE, IT CANNOT BE EXCLUDED
THAT MISTAKES COULD HAVE CREPT IN. TTCONTROL GMBH PROVIDES THE DOCUMENT
FOR THE PRODUCT "AS IS" AND WITH ALL FAULTS AND HEREBY DISCLAIMS ALL WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, ACCURACY OR COMPLETENESS, OR OF RESULTS TO THE EXTENT PERMITTED
BY APPLICABLE LAW. THE ENTIRE RISK, AS TO THE QUALITY, USE OR PERFORMANCE OF THE DOCUMENT, REMAINS WITH THE RECIPIENT. TO THE MAXIMUM EXTENT PERMITTED
BY APPLICABLE LAW TTCONTROL GMBH SHALL IN NO EVENT BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES WHATSOEVER (INCLUDING
BUT NOT LIMITED TO LOSS OF DATA, DATA BEING RENDERED INACCURATE, BUSINESS INTERRUPTION OR ANY OTHER PECUNIARY OR OTHER LOSS WHATSOEVER) ARISING OUT
OF THE USE OR INABILITY TO USE THE DOCUMENT EVEN IF TTCONTROL GMBH HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

IF THE PRODUCT IS MARKED AS "PROTOTYPE", THE DELIVERED PRODUCT IS A DEVELOPMENT SAMPLE ("SAMPLE"). THE RECIPIENT ACKNOWLEDGES THAT THEY ARE ALLOWED
TO USE THE SAMPLE ONLY IN A LABORATORY FOR THE PURPOSE OF DEVELOPMENT. IN
NO EVENT IS THE RECIPIENT ALLOWED TO USE THE SAMPLE FOR THE PURPOSE OF SERIES MANUFACTURING.

TTCONTROL GMBH PROVIDES NO WARRANTY FOR ITS PRODUCTS OR ITS SAMPLES, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE AND TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW DISCLAIMS ALL LIABILITIES FOR DAMAGES RESULTING FROM OR ARISING
OUT OF THE APPLICATION OR USE OF THESE PRODUCTS OR SAMPLES. THE EXCLUSION
OF LIABILITY DOES NOT APPLY IN CASES OF INTENT AND GROSS NEGLIGENCE. MOREOVER, IT DOES NOT APPLY TO DEFECTS WHICH HAVE BEEN DECEITFULLY CONCEALED
OR WHOSE ABSENCE HAS BEEN GUARANTEED, NOR IN CASES OF CULPABLE HARM TO
LIFE, PHYSICAL INJURY AND DAMAGE TO HEALTH. CLAIMS DUE TO STATUTORY PROVISIONS OF PRODUCT LIABILTY SHALL REMAIN UNAFFECTED.

ANY DISPUTES ARISING OUT OF OR IN CONNECTION WITH THIS DOCUMENT SHALL BE GOVERNED SOLELY BY AUSTRIAN LAW, EXCLUDING ITS CONFLICT OF LAW RULES AND THE UNITED NATIONS CONVENTION ON CONTRACTS FOR THE INTERNATIONAL SALE OF GOODS. SUCH DISPUTES SHALL BE DECIDED EXCLUSIVELY BY THE COURTS OF VIENNA,
AUSTRIA.
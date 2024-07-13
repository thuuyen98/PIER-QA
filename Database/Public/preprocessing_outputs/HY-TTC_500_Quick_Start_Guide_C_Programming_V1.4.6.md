# Hy-Ttc 500

![0_image_0_7674.png](The image features a blue sign with white letters that reads "TTC Control." It is likely an advertisement for a company or service related to control systems. The sign appears to be prominently displayed on a wall, drawing attention to its message.)

![0_image_1_7674.png](The image is a close-up of a white wall with a gray background. There are two distinct lines on the wall, one running horizontally across the middle and another vertically down the center. These lines create an interesting visual effect that adds depth to the otherwise plain surface.)

![0_image_2_7674.png](The image is a close-up of a gray square with a white background. It appears to be an artistic representation of a wall or a building's corner. The square has a slightly darker shade on one side, giving it a more textured appearance.)

Quick Start Guide - C Programming Programmable ECU for Sensor-Actuator Management Product Version 01.08

[table_0][{0: 'Document Number:', 1: 'D-TTC5F-G-20-004'}, {0: 'Document Version:', 1: '1.4.6'}, {0: 'Date:', 1: '07-May-2020'}, {0: 'Status:', 1: 'Released'}][/table_0]

TTControl GmbH Schoenbrunner Str. 7, A-1040 Vienna, Austria,Tel. +43 1 585 34 34–0, Fax +43 1 585 34 34–90, office@ttcontrol.com No part of the document may be reproduced or transmitted in any form or by any means, electronic or mechanical, for any purpose, without the written permission of TTControl GmbH. Company or product names mentioned in this document may be trademarks or registered trademarks of their respective holders. TTControl GmbH undertakes no further obligation or relation to this document.

Copyright  2020 TTControl GmbH. All rights reserved. Subject to changes and corrections TTControl GmbH Confidential and Proprietary Information

## Legal Notice Document Number: D-Ttc5F-G-20-004

The data in this document may not be altered or amended without special notification from TTControl GmbH. TTControl GmbH undertakes no further obligation in relation to this document. The software described in it can only be used if the customer is in possession of a general license agreement or single license. The information contained in this document does not affect or change any General Terms and Conditions of TTControl GmbH and/or any agreements existing between TTControl GmbH and the recipient regarding the product or Sample concerned. The reader acknowledges that this document may not be reproduced, stored in a retrieval system, transmitted, changed, or translated, in whole or in part, without the express prior written consent of TTControl GmbH. The reader acknowledges that any and all of the copyrights, trademarks, trade names, patents (whether registrable or not) and other intellectual property rights embodied in or in connection with this document are and will remain the sole property of TTControl GmbH or the respective right holder. Nothing contained in this legal notice, the document or in any web site of TTControl GmbH shall be construed as conferring to the recipient any license under any intellectual property rights, whether explicit, by estoppel, implication, or otherwise. The product or Sample is only allowed to be used in the scope as described in this document.

TTControl GmbH provides this document "as is" and disclaims all warranties of any kind. The entire risk, as to quality, use or performance of the document remains with the recipient.

All trademarks mentioned in this document belong to their respective owners.

Copyright  2020 TTControl GmbH. All rights reserved.

## Contents

[table_1][{0: 'Table of Contents', 1: 'ii', 2: '', 3: ''}, {0: 'List of Figures', 1: '1', 2: '', 3: ''}, {0: 'I', 1: 'Quick Start Guide', 2: '2', 3: ''}, {0: '1', 1: 'Overview', 2: '', 3: '3'}, {0: '2', 1: 'Information and latest version of software', 2: '', 3: '4'}, {0: '3', 1: 'Getting Started', 2: '5', 3: ''}, {0: '4', 1: 'Using the Interface Board', 2: '', 3: '7'}, {0: '4.1', 1: 'HY-TTC 500 Cable Harness', 2: '', 3: '7'}, {0: '4.2', 1: 'HY-TTC 500 CAN Termination', 2: '8', 3: ''}, {0: '4.3', 1: 'HY-TTC 500 Power Supply', 2: '9', 3: ''}, {0: '4.4', 1: 'HY-TTC 500 Terminal 15 (KL15) Modes', 2: '', 3: '11'}, {0: '4.5', 1: 'Status LEDs', 2: '', 3: '12'}, {0: '4.6', 1: 'Selecting BroadR-Reach®or Ethernet mode', 2: '', 3: '13'}, {0: '4.7', 1: 'HY-TTC 500 Download and Debugging', 2: '', 3: '14'}, {0: '5', 1: 'C Programming Howto for HY-TTC 500', 2: '', 3: '15'}, {0: '5.1', 1: 'Overview', 2: '', 3: '15'}, {0: '5.2', 1: 'Endianess', 2: '', 3: '15'}, {0: '5.3', 1: 'Tool Chain', 2: '', 3: '15'}, {0: '5.4', 1: 'File Structure', 2: '20', 3: ''}, {0: '5.5', 1: 'Development Environment', 2: '22', 3: ''}, {0: '5.6', 1: 'Settings.mk', 2: '22', 3: ''}, {0: '5.7', 1: 'Application Examples', 2: '24', 3: ''}, {0: '5.7.1', 1: 'Build Application', 2: '', 3: '24'}, {0: '5.7.2', 1: 'General', 2: '', 3: '27'}, {0: '5.7.3', 1: 'Help for C Driver Functions', 2: '', 3: '30'}, {0: '5.7.4', 1: 'Linking Constant Data', 2: '', 3: '30'}, {0: '5.7.5', 1: 'Safety Configuration', 2: '', 3: '32'}, {0: '5.7.6', 1: 'Debugging of a safety-critical Application', 2: '', 3: '32'}, {0: '5.8', 1: 'Flashing the HY-TTC 500', 2: '32', 3: ''}, {0: '5.8.1', 1: 'The Lauterbach Debugging Device and Trace32', 2: '', 3: '32'}, {0: '5.8.2', 1: 'The TTC-Downloader Tool', 2: '', 3: '45'}, {0: '6', 1: 'Memory Mapping', 2: '', 3: '48'}, {0: '6.1', 1: 'Memory Map for Internal Flash and RAM', 2: '', 3: '48'}, {0: '6.2', 1: 'Memory Map for External Flash and RAM', 2: '49', 3: ''}, {0: 'References', 1: '50', 2: '', 3: ''}, {0: 'Legal Disclaimer', 1: '', 2: '51', 3: ''}][/table_1]

ii Contents

## List Of Figures

[table_2][{0: '3.1', 1: 'HY-TTC 500 Starter Kit', 2: '', 3: '5'}, {0: '3.2', 1: 'HY-TTC 500 Starter Kit for C programming', 2: '', 3: '6'}, {0: '4.1', 1: 'HY-TTC 500 Interface Board', 2: '', 3: '7'}, {0: '4.2', 1: 'HY-TTC 500 Interface Board CAN Termination', 2: '', 3: '8'}, {0: '4.3', 1: 'HY-TTC 500 Interface Board CAN Termination', 2: '', 3: '9'}, {0: '4.4', 1: 'HY-TTC 500 Interface Board Power Supply', 2: '10', 3: ''}, {0: '4.5', 1: 'HY-TTC 500 Interface Board Power Supply', 2: '10', 3: ''}, {0: '4.6', 1: 'HY-TTC 500 Interface Board Terminal 15 (KL15)', 2: '11', 3: ''}, {0: '4.7', 1: 'HY-TTC 500 Interface Board Terminal 15 (KL15)', 2: '11', 3: ''}, {0: '4.8', 1: 'Status LEDs', 2: '', 3: '12'}, {0: '4.9', 1: 'Status LEDs', 2: '', 3: '13'}, {0: '4.10', 1: 'Jumpers for Ethernet or BroadR-Reach®mode', 2: '13', 3: ''}, {0: '5.1', 1: 'CCS Edit - Code Composer Studio', 2: '', 3: '16'}, {0: '5.2', 1: 'Show only. . . check box', 2: '', 3: '16'}, {0: '5.3', 1: 'Work with field', 2: '17', 3: ''}, {0: '5.4', 1: 'Add button', 2: '17', 3: ''}, {0: '5.5', 1: 'Add Repository dialog', 2: '18', 3: ''}, {0: '5.6', 1: 'TI Compiler Updates branch', 2: '', 3: '19'}, {0: '5.7', 1: 'ARM Compiler Tools 5.1.6', 2: '', 3: '19'}, {0: '5.8', 1: 'Contents of the Get_Started directory', 2: '', 3: '20'}, {0: '5.9', 1: 'The examples and template directories', 2: '', 3: '21'}, {0: '5.10', 1: 'Settings.mk', 2: '23', 3: ''}, {0: '5.11', 1: 'Select new wizard page', 2: '', 3: '25'}, {0: '5.12', 1: 'Import Existing Code page', 2: '', 3: '25'}, {0: '5.13', 1: 'Browse For Folder dialog', 2: '', 3: '26'}, {0: '5.14', 1: 'Console pane with successful build', 2: '26', 3: ''}, {0: '5.15', 1: 'Includes', 2: '27', 3: ''}, {0: '5.16', 1: 'Application Descriptor Block (APDB)', 2: '', 3: '28'}, {0: '5.17', 1: 'Application initialization', 2: '', 3: '29'}, {0: '5.18', 1: 'Application loop', 2: '', 3: '30'}, {0: '5.19', 1: 'Linking constant data to the external flash and/or application configuration data', 2: '.', 3: '31'}, {0: '5.20', 1: 'Lauterbach Base Station', 2: '', 3: '33'}, {0: '5.21', 1: 'Trace32 Software', 2: '', 3: '33'}, {0: '5.22', 1: 'Chosse Destination Location page', 2: '', 3: '33'}, {0: '5.23', 1: 'Installation Type page', 2: '', 3: '34'}, {0: '5.24', 1: 'Setup Type page', 2: '', 3: '34'}, {0: '5.25', 1: 'TRACE32 Product Type page', 2: '35', 3: ''}, {0: '5.26', 1: 'Maintenance Notice page', 2: '', 3: '35'}, {0: '5.27', 1: 'Debugger Interface Type page', 2: '', 3: '36'}, {0: '5.28', 1: 'OS Selection page', 2: '', 3: '36'}, {0: '5.29', 1: 'CPU selection page', 2: '', 3: '37'}, {0: '5.30', 1: 'TRACE32 executable type dialog', 2: '37', 3: ''}][/table_2]

[table_3][{0: '5.31', 1: 'Environment variable T32ID page', 2: '', 3: '37'}, {0: '5.32', 1: 'Device software installation', 2: '38', 3: ''}, {0: '5.33', 1: 'Environment variable T32TMP page', 2: '38', 3: ''}, {0: '5.34', 1: 'Prepare TRACE32 for Integration. . . page', 2: '39', 3: ''}, {0: '5.35', 1: 'Select way to submit registration page', 2: '39', 3: ''}, {0: '5.36', 1: 'TRACE32 software is successfully finished page', 2: '40', 3: ''}, {0: '5.37', 1: 'JTAG Adapter Board', 2: '40', 3: ''}, {0: '5.38', 1: 'JTAG Cable', 2: '40', 3: ''}, {0: '5.39', 1: 'HY-TTC 500 with JTAG connector and LEDs', 2: '', 3: '41'}, {0: '5.40', 1: 'Lauterbach connection to HY-TTC 580 (1)', 2: '', 3: '42'}, {0: '5.41', 1: 'Lauterbach connection to HY-TTC 580 (2)', 2: '', 3: '42'}, {0: '5.42', 1: 'HY-TTC 500 with LEDs', 2: '', 3: '43'}, {0: '5.43', 1: 'HY-TTC 500 with JTAG connector and signal pins', 2: '', 3: '44'}, {0: '5.44', 1: 'Trace32 and .cmm batch file', 2: '', 3: '44'}, {0: '5.45', 1: 'Flash application dialog', 2: '45', 3: ''}, {0: '5.46', 1: 'Reset Trace32 windows dialog', 2: '45', 3: ''}, {0: '5.47', 1: 'Trace32 Window after flashing', 2: '', 3: '46'}, {0: '5.48', 1: 'TTC-Downloader', 2: '47', 3: ''}, {0: '6.1', 1: 'Memory map for HY-TTC 500 internal Flash', 2: '', 3: '48'}, {0: '6.2', 1: 'Memory map for HY-TTC 500 external RAM and Flash', 2: '', 3: '49'}][/table_3]

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

[table_4][{0: 'Nr.', 1: 'Starter Kit Components'}, {0: '1', 1: 'HY-TTC 500 ECU open housing'}, {0: '2', 1: 'JTAG adapter'}, {0: '3', 1: 'JTAG adapter cable'}, {0: '4', 1: 'Interface board'}, {0: '5', 1: 'Cable harness 1.5 m'}, {0: '6', 1: 'Installation CD C-Programming'}, {0: '7', 1: 'Ethernet USB adapter with driver and software'}, {0: '8', 1: 'PCAN USB adapter with driver and software'}, {0: '9', 1: 'Datacable 2m'}, {0: '10', 1: 'Quick Start Guide'}][/table_4]

![8_image_0_7674.png](The image features a white box with blue handles, which is labeled "TTC Control." Inside the box, there are several electronic components, including a computer mouse and a keyboard. These items are arranged neatly within the container, showcasing their organization and presentation.)

![9_image_0_7674.png](The image features a black case with various items inside, including cords, papers, and other electronics. There are several books placed around the case, some of which are located near the top right corner of the case. A pair of scissors can also be seen in the scene, positioned towards the bottom left side of the image. The assortment of items suggests that this is a collection or storage area for electronics and other materials.)

| 6

## 4 Using The Interface Board

![10_image_0_7674.png](The image features a blue circuit board with numerous electronic components attached to it. There are several rows of small white buttons arranged across the board, as well as multiple wires connecting them. Some of these buttons have red lights on top of them, indicating that they might be used for specific functions or purposes.  In addition to the buttons and wires, there is a keyboard visible in the scene, which could be part of the same electronic device or another related component. The overall composition suggests an intricate and complex system of interconnected components, likely designed for a specific purpose or function.) 4.1 Hy-Ttc 500 Cable Harness

Connect the HY-TTC 500 to the connector interface board with the provided cable harness. Note: Do not use a cable harness from a different HY-TTC 500 variant! The HY-TTC 500 variants use different cable harnesses and the usage of the wrong cable harness may damage the HY-TTC 500 device.

## 4.2 Hy-Ttc 500 Can Termination

If termination of a CAN interface (2 x 60 Ωsplit termination) is required, then connect the jumper pins for the CAN interface as follows:

[table_5][{0: 'CAN Interface', 1: 'Connect Jumper Pins'}, {0: 'CAN0', 1: '235 with 209 and 222 with 248'}, {0: 'CAN1', 1: '236 with 210 and 223 with 249'}, {0: 'CAN2', 1: '237 with 211 and 224 with 250'}, {0: 'CAN3', 1: '216 with 212 and 225 with 229'}][/table_5]

Figure 4.3 on the next page shows the jumper setting for CAN0 as example.

![11_image_0_7674.png](The image features a close-up of an electronic circuit board with several components on it. There are multiple rows of chips placed across the board, some of which have red dots underneath them. These chips are likely part of a computer or other electronic device.  In addition to the chips, there is a row of small white buttons located near the center of the circuit board. The buttons appear to be arranged in a linear fashion and may serve as input controls for the device.)

![12_image_0_7674.png](249 is highlighted on a blue circuit board with many electronic components attached to it. The board appears to be part of an electrical system, possibly related to power generation or distribution. There are several other numbers visible on the board as well, indicating that this could be a complex system involving multiple components and functions.)

## 4.3 Hy-Ttc 500 Power Supply

- Connect the power supply GND to the black socket named **BAT-**.

- Connect the positive power supply to the red socket named **BAT+ Power** and to **BAT+ CPU**
on the connector terminal block, e.g. by short-circuit of BAT+ CPU to **BAT+ Power**.

See also Figure 4.4 on the following page and Figure 4.5 on the next page.

![13_image_0_7674.png](The image features a close-up of an electronic circuit board with several components on display. There are multiple chips placed throughout the board, some of which have red lights shining through them. A few of these chips are located near the center of the board while others can be found closer to the edges.  In addition to the chips, there is a power supply visible in the lower right corner of the image. The circuit board appears to be well-organized and intricately designed, showcasing its complex components and their arrangement.)

![13_image_1_7674.png](15 is written on a blue background with white numbers. The number 15 is located near the top right corner of the image.)

## 4.4 Hy-Ttc 500 Terminal 15 (Kl15) Modes

- **Always on Mode**:

![14_image_0_7674.png](The image features a close-up of an electronic circuit board with several components on it. A red arrow is pointing to one of the components, which appears to be a small square. The rest of the components are arranged around this point of interest, creating a detailed view of the circuitry.)

Put the jumper to **Always on** mode if the HY-TTC 500 shall be in active state independent of Terminal 15.

- **Normal Mode**:
Put the jumper to **Normal** mode if the HY-TTC 500 power-up shall depend on **Terminal 15**.

![14_image_1_7674.png](15 is written on a blue background with white letters. The word "Terminal" is displayed below this number, indicating that it might be related to an electrical system or device.)

## 4.5 Status Leds

There are status LEDs for
- BAT+ Power

![15_image_0_7674.png](The image features a close-up of an electronic circuit board with several components on it. A red circle is placed over one of the components, drawing attention to its location. There are multiple rows of chips on the board, indicating that this is likely a complex electronic device.  In addition to the main component under the red circle, there are other smaller components scattered across the circuit board. These include several chips and wires, which contribute to the overall functionality of the device. The close-up view allows for a detailed examination of these intricate parts that make up the electronic circuit board.)

- BAT+ CPU
- Terminal 15
- Wake-Up See Figure 4.8 on this page and Figure 4.9 on the next page. A status LED is on, when the corresponding input voltage is above the lower voltage limit (8V) for safe operation of the ECU. The switching threshold of the LEDs is min. 8 V and max. 8.9 V (to guarantee a voltage >8 V over all parts tolerances).

![16_image_0_7674.png](247 is written on a blue background with a red circle around it. The image also features a computer board with several wires connected to it. There are two buttons visible in the scene, one located near the top left corner of the image and another towards the bottom right side.)

## 4.6 Selecting Broadr-Reach® **Or Ethernet Mode**

For Ethernet mode, set all six jumpers as shown in Figure 4.10(a) on this page. Note: The Ethernet mode is only available for HY-TTC 580.

For BroadR-Reach® mode (also known as 100BASE-T1 Ethernet), set all six jumpers as shown in Figure 4.10(b) on the current page.

Note: The BroadR-Reach® mode is available on HY-TTC 590E, HY-TTC 590, and HY-TTC 508.

![16_image_1_7674.png](1. A close-up of a blue electronic device with red dots on top of it. 2. The same electronic device as in #1 but with a different angle.)

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

![19_image_0_7674.png](The image displays a computer screen with various options and settings visible on the desktop. There are multiple windows open, including one that says "Code Composer Studio." A red arrow is pointing to the right side of the screen, possibly indicating an important option or setting.  In addition to the main window, there are other smaller windows scattered across the screen, likely providing additional information or options for the user. The overall layout and content of the computer screen suggest that it may be a workspace for software development or programming tasks.)

![19_image_1_7674.png](The image displays a computer screen with a software installation wizard on it. There are several options available for selecting the desired software to install. A red arrow is pointing at the option "Show only the latest versions of software." This indicates that the user can choose from the most recent updates or versions of the software being installed. The image also shows a mouse cursor, suggesting that the user might be interacting with the installation wizard on their computer screen.)

![20_image_0_7674.png](5.6 Work with files)

![20_image_1_7674.png](The image displays a computer screen with a software installation wizard on it. There are several options available for selecting the desired software to install. A mouse pointer is located near the "Add" button, indicating that the user has selected this option.  The screen also features a "Select All" button and an "Unselect All" button, allowing users to choose or remove specific items from their installation list. The available options include "Software," "Environment," and "What is needed." There are also two other buttons on the screen: one labeled "Finish" and another labeled "Cancel.")

![21_image_0_7674.png](The image displays a computer screen with a software installation process underway. A window is open on the screen, prompting the user to select a location for the new site. There are two options available - "Enter the location of the site" and "Select an existing site." The user can choose either option based on their preference.  In addition to this, there is a mouse cursor located near the bottom left corner of the screen, indicating that it's ready for interaction with the computer.)

c) From the **Work with** field, select **Code Generation Tools Updates**.

d) Continue with step 4 below.

4. From the list of tools, expand the **TI Compiler Updates** branch (see Figure 5.6 on the next page) and then select **ARM Compiler Tools 5.1.6** (see Figure 5.7 on the facing page)
5. Click **Next** and follow the instructions of the installation wizard.

![22_image_0_7674.png](The image displays a computer screen with an installation wizard open on the desktop. There are several options available for users to choose from, including "Compile Updates," "Install Software," and "Add/Remove Programs." A highlighted box is present in the middle of the screen, likely indicating the most important or relevant option at that moment. The computer screen appears to be a Windows desktop with various icons and menus visible around it.) ![22_image_1_7674.png](1. A window on a computer screen displays an installation program for software. 2. The window is open to the "Available Software" tab. 3. There are two options available: "Show only the latest versions of all software" and "Show only software that has been installed." 4. The user can choose between these options by clicking on them.)

## 5.4 File Structure

The developer package is extracted into five directories:
- **Bootloader**

![23_image_0_7674.png](The image displays a computer screen with various windows open on it. One of the windows is titled "Get Started," which appears to be an installation wizard for a new program. Another window shows a file that has been downloaded, possibly from Microsoft Office. There are also two other windows visible in the scene, one located at the top left corner and another towards the right side of the screen.)

- **Documentation**
- **FPGA_Bitstream**
- **Get_Started**
- **Release_Notes**
Figure 5.8 on the current page shows the contents of the **Get_Started** directory.

![23_image_1_7674.png](100% of the cat is shown on this image.)

Figure 5.9(a) on the facing page shows the contents of the **examples** directory. The **examples** directory has some prebuilt projects to explain the usage of certain functions. Figure 5.9(b) on the next page shows the contents of the **template** directory, which contains a template for starting a new project.

![24_image_0_7674.png](1. The image displays a computer screen with two windows open. One window is focused on a file explorer, while the other one shows a search result. 2. In the first window, there are multiple folders visible, including "C:\Windows\System32" and "C:\Program Files." A total of 14 folders can be seen in this window. 3. The second window displays a list of files, with a total of 15 items displayed. These files appear to be related to the contents of the first window.)

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
\#  2 ... release OPT_TYPE  =  1 ifeq ($(OPT_TYPE), 0)
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

![28_image_0_7674.png](The image displays a computer screen with a window open to a new project creation wizard. The wizard is designed for creating a new project using an existing code. There are several options available on this screen, including selecting a wizard, creating a new project in directory, and creating a new project with an existing code.  The computer screen also has a mouse cursor located towards the right side of the image. The various options presented on the screen suggest that this is a software application designed for managing projects or creating new ones using pre-existing codes.)

![28_image_1_7674.png](1. The image displays a computer screen with a blue background. 2. On the screen, there is an open window that shows a new project being created. 3. A dialog box appears on the screen, asking for information such as the name of the project and its location. 4. There are several options available in the dialog box, including "browse," which allows users to select a file from their computer's storage.)

![29_image_0_7674.png](1. Select Root Directory of Existing Code 2. Browse for Folder)

![29_image_1_7674.png](The image displays a computer screen with a blue background and white text. There is a window open on the screen that reads "ECSHELL Code Composer Studio." A red arrow is pointing to the word "Build" within this window. This suggests that the user might be working on a project or application related to building code, possibly using an integrated development environment (IDE) like Code Composer Studio.)

## 5.7.2 General

Every program must include at least the header files **IO_Driver.h** and **APDB.h** (see Figure 5.15 on the current page). The Application Descriptor Block (APDB) is a 128-byte structure that is used by download tools and the bootloader to update the application and do CRC checks. The structure Apdb_t must be defined (see Figure 5.16 on the following page).

[table_6][{0: '/******************************************************************************  * Includes  ******************************************************************************/ #include "APDB.h" #include "IO_Driver.h" #include "IO_DIO.h" #include "IO_POWER.h" #include "IO_RTC.h" Main include files for I/O driver and APDB Other includes Figure 5.15: Includes'}][/table_6]

![31_image_0_7674.png](The image displays a computer screen with several lines of code written in green. These lines are organized into different sections, including "Application Descriptor Block" and "Application Descriptor Block." There is also an application descriptor block that has been blocked off by the user.  The code appears to be related to a software development project or a programming task. The presence of multiple lines of code suggests that it could be a complex program or a part of a larger system.)

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

[table_7][{0: '3) Enable outputs 4) Start timestamp'}][/table_7]

Figure 5.17: Application initialization After initializiation, typically a while loop (**while (1)**) is executed. This is the main loop of the application, and it will be executed each cycle time ms. See Figure 5.18 on this page.

![33_image_0_7674.png](16. Application Loop (Figure 6-1)  The image displays a diagram of an application loop with several components labeled. The main components include a "Call" function, which is located at the bottom right corner of the loop, and a "Pass" function situated above it. There are also two "Read" functions, one on the left side and another in the middle of the loop.  In addition to these functions, there are three labels: "Application Loop," "Call," and "Pass." The diagram provides an overview of the application's structure and flow within the loop.)

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

![36_image_0_7674.png](The image features a computer setup with a laptop placed next to a monitor. On the laptop, there is an open program displaying information related to Laubertbach Base Station. A mouse can also be seen on the laptop's surface.  In addition to the laptop and monitor, there are two keyboards in the scene – one near the laptop and another further away from it. The setup appears to be a workspace for analyzing or working with data related to Laubertbach Base Station.)

The installation wizard guides you trough the installation process:

1. After the Welcome page, confirm the licensing agreements on the **License Software Agreement** page.

![36_image_1_7674.png](The image displays a computer screen with a message on it that reads "Choose Destination Location." There is also an option to select a destination location by clicking on the "Select" button. The screen appears to be related to software installation or setup, as indicated by the presence of this message.)

2. On the **Choose Destination Location** page, set the installation path (see Figure 5.22 on this page).

3. On the **Installation Type** page, select **Custom Installation** (see Figure 5.23 on the next page).

4. On the **Setup Type** page, select **New Installation** (see Figure 5.24 on the following page).

5. On the **TRACE32 Product Type** page, select **Debugger** (see Figure 5.25 on page 35). 6. On the **Maintenance Notice** page and click **Next** (see Figure 5.26 on page 35). 7. On the **Debugger Interface Type** page, select **USB Interface** (see Figure 5.27 on page 36).

![37_image_0_7674.png](The image displays a computer screen with a window open to an installation type setup. There are two buttons on the screen, one of which is labeled "Custom Installation." A red circle is placed over this button, drawing attention to its function.  In addition to these buttons, there are several other elements visible in the image. These include a keyboard and a mouse, both located near the bottom left corner of the screen. There's also an icon on the right side of the screen, possibly representing a software application or file.)

![37_image_1_7674.png](The image displays a computer screen with a message on it that reads "Please select setup type for installation." There are two buttons visible on the screen, one of which is labeled "Back" and the other is labeled "Next." A window appears to be open, possibly for setting up or installing software.)

![38_image_0_7674.png](The image displays a computer screen with a software program open on it. The program is likely related to debugging or programming, as there are multiple options displayed on the screen. A red arrow is pointing towards one of these options, which reads "Debugger." This suggests that the user might be working on fixing an issue in their code or testing the functionality of the software.)

![38_image_1_7674.png](The image displays a computer screen with a blue background featuring a software product advertisement for TRADE32. The advertisement is promoting the benefits of using this software, such as support on both TRADE21 and TRADE32 platforms. There are also details about how to check the software's features and download it from their website.)

![39_image_0_7674.png](The image displays a computer screen with a message on it that reads "Please select the heat interface type you will use." There are two options available for selection - USB Interface and Ethernet Interface. The user can choose between these two options to proceed further in their task.)

8. On the **OS Selection** page, select **PC Windows XP/VISTA/7/8/10** (see Figure 5.28 on this

![39_image_1_7674.png](The image displays a computer screen with a blue background and white text. On the screen, there is an error message that reads "OS Selection" at the top left corner. Below this message, there are two more lines of text, one reading "The selected OS is not compatible with your system." The other line says "Please select a different OS." This suggests that the user might be facing compatibility issues or errors related to their computer's operating system.)

page).

9. On the **CPU selection** page, select **ICD ARM 32-bit** (see Figure 5.29 on the next page).

10. In the **TRACE32 executable type** dialog, click Yes for a 64-bit OS (see Figure 5.30 on the facing page).

11. On the **Environment variable T32ID** page, choose the default value T32 (see Figure 5.31 on the next page).

12. If you are asked to install the Lauterbach device software, click **Install** (see Figure 5.32 on page 38). Use the suggested default settings for the device software installation process.

13. On the **Environment variable T32TMP** page, set the destination folder (see Figure 5.33 on page 38).

![40_image_0_7674.png](The image displays a computer screen with a selection page for CPUs. There are several options available to choose from, including ARM Cortex-A9, ARM Cortex-A8, ARM Cortex-A7, ARM Cortex-A5, and others. A total of nine different CPUs can be selected on this page. The selection process is facilitated by a clear button that allows the user to choose their preferred CPU.)

![40_image_1_7674.png](The image displays a computer screen with a message on it that reads "For your 64-bit host operating system are bit and bit." This suggests that the system is designed for use with both 32-bit and 64-bit operating systems, providing compatibility and flexibility.)

![40_image_2_7674.png](The image displays a computer screen with a message on it that reads "Please enter your environment variable TD32E executable type dialog." There is also an error message displayed below this message, which suggests that there might be an issue with the device or software being used.)

![41_image_0_7674.png](The image displays a computer screen with a message asking whether you would like to install this device software. There is a button labeled "Don't Install" on the right side of the screen, which is currently highlighted. Above the button, there is a name and an email address associated with the installation.)

![41_image_1_7674.png](The image displays a computer screen with a message on it that reads "Please enter the path of TIMPE." This message is likely related to a software development process. The screen also has a blue background and appears to be part of an environment setup.)

14. On the next pages related to screen configuration, use the default settings.

![42_image_0_7674.png](The image displays a computer screen with a message that reads "Prepare TRACEE for Integrations with Other Products." There are several options available on the screen, including "No Integration," "Any integration done with TRACEE API," and "Any integration done with TRACEE API." The user can choose from these options based on their preferences.) 15. On the **Prepare TRACE32 for Integration with other products** page, select **No Integration**
(see Figure 5.34 on this page).

![42_image_1_7674.png](The image displays a computer screen with a window open to an online registration form. The form is asking for various personal information such as name, email address, phone number, and date of birth. There are multiple options available for each field, allowing users to select their preferred choices.  The form also includes a section where the user can choose whether they want to receive emails or not. A button labeled "submit" is visible at the bottom right corner of the screen, indicating that the user can submit their information once it has been filled out correctly.)

16. For the pages **Folder Selection** and **Folder program group type**, use the default settings.

17. On the **Select way to submit registration** page, select **Register later** (see Figure 5.35 on the current page).

18. The last page **TRACE32 software is successfully finished** shows the installation path and how to start the software (see Figure 5.36 on the following page). Click **Finish** to complete the installation.

![43_image_0_7674.png](The image displays a computer screen with a message that reads "Trace software is successfully installed." There are two buttons on the screen, one of which says "Finish" and the other has a question mark. Above these buttons, there is a blue background with an orange logo in the upper left corner.)

![43_image_1_7674.png](The image features a close-up of a black cord with multiple connectors on its end. There are two cords visible in the picture, one being longer than the other. The cords are connected to various electronic devices, possibly for data transfer or power supply purposes.)

## 5.8.1.3 Usage 5.8.1.3.1 Hardware

The HY-TTC 580 Starter Kit comes with the following components:
- JTAG Adapter Board (Figure 5.37 on the current page) and JTAG Cable (Figure 5.38 on this

![43_image_2_7674.png](The image features a blue electronic device with several ports on its surface. There are multiple connectors and cables attached to this device, indicating that it is likely used for communication or data transfer purposes. The device appears to be an electronic component or module, possibly related to computer hardware or networking equipment.)

page)

- open housing of the HY-TTC 500 ECU to enable a connection with the JTAG interface (Figure 5.39 on the next page)

![44_image_0_7674.png](The image features a close-up view of an electronic circuit board with various components such as LEDs and resistors. There are multiple LEDs placed throughout the board, some closer to the center while others are positioned towards the edges. A total of nine LEDs can be identified in the scene.  In addition to the LEDs, there are several resistors on the circuit board, with a total of eight visible. These components are distributed across different areas of the board, contributing to its functionality and design. The close-up view allows for an appreciation of the intricate details within this electronic device.)

The following components from Lauterbach are required:
- Lauterbach Base Station. For example, **Power Debug Interface USB 3 LA-3500** - Lauterbach Debug Cable **JTAG-CORTEX-A/R LA-7843** - Lauterbach AC/DC power supply adapter
- USB connector to connect Lauterbach and PC
Please refer to Figure 5.40 and Figure 5.41 on the following page for how to connect, for example, a HY-TTC 580 with Lauterbach debugger.

![45_image_0_7674.png](The image features a white table with various electronic components on top of it. There are two computer boards placed next to each other, along with several cords and wires connected to them. A cell phone is also present on the table, positioned near one of the computer boards.  In addition to these items, there are three books scattered around the table, possibly containing information or instructions related to the electronic components. The overall scene suggests a workspace for assembling or repairing electronic devices.)

![45_image_1_7674.png](The image features a computer circuit board with various electronic components attached to it. There are two main parts of the circuit board: one is located towards the left side of the board, while the other is situated more towards the right side.  In addition to these components, there are several cables and wires connected to the circuit board. Some of them are positioned near the top edge of the board, while others can be found closer to the bottom edge. The arrangement of these electronic parts and cables suggests that this is a complex system designed for computer processing or communication purposes.)

## 5.8.1.3.2 Led Description Done Led

The DONE LED (see Figure 5.42 on the current page) indicates the configuration status: If the DONE LED is ON, the FPGA is not configured. If the DONE LED is OFF, the FPGA is configured.

![46_image_0_7674.png](The image features a close-up of an electronic component with four LEDs labeled "LED1," "LED2," "LED3," and "LED4." These labels are placed on top of each other to indicate their positions within the circuitry. The components appear to be part of a larger electronic device, possibly a computer or a gadget.) 

Debug LEDs The LEDs LED0. . . LED2 shown in Figure 5.42 on this page are for debugging. They are controlled by the **IO_DEBUG_SetOutputPin()** function. See [4] for details. They are completely controllable by the application.

Signal pins The signal pins on the JTAG adapter board (see Figure 5.43 on the next page) indicate the inverted status of the DONE LED and the Debug LEDs. That is, if a LED is ON, the corresponding signal pin has low voltage (0).

Note: The signal pins shown in Figure 5.43 on the following page are unprotected CMOS outputs.

Any external voltage applied on these pins can damage the ECU.

![47_image_0_7674.png](The image features a close-up of an electronic device with several components visible on its surface. There are two main areas of interest: one is a blue box with a red circle pointing to it, while the other is a small square with a green circle around it. These circles indicate that these specific parts might be important or require attention.  In addition to these highlighted areas, there are several other components on the device, including multiple screws and various connectors. The close-up view of the electronic device allows for detailed examination of its internal structure and functioning.)

## 5.8.1.3.3 Software

1. Connect the Lauterbach Base Station and Debug Cable to the PC and power supply and

![47_image_1_7674.png](The image displays a computer screen with various options and settings visible on the desktop. There are multiple windows open, including one that says "Search for script." A menu is also present at the top of the screen, offering different choices such as "File," "Edit," "View," and "Tools."  In addition to these options, there are several icons scattered across the screen, some of which may be related to specific applications or functions. The overall layout suggests that this computer setup is designed for efficient work and organization.)

install the necessary drivers.

2. Make the connections as described in Section 4.3 on page 9 and in Section 5.8.1.3.1 on page 40.

3. Perform a power cycle.

4. Click **Start > Trace32 ICD ARM32 USB** on the Windows start menu to start the Lauterbach debugger software.

5. The HY-TTC 500 template comes with a predefined ***.cmm** script. Start the script by clicking File > Run Script (Figure 5.44 on the current page).

6. A dialog asks whether you want to flash the application or not (Figure 5.45 on the facing page).

If you click Yes, the flashing process starts.

7. When the flashing process has finished, the next dialog asks whether you want to keep the current Trace32 window configuration or reset to a default configuration (Figure 5.46 on the next page).

![48_image_0_7674.png](The image displays a computer screen with a message asking whether to program application to flash memory. There are two buttons on the screen, one labeled "Yes" and another labeled "No." A window is open on the screen, possibly related to the installation or configuration of an ARM processor.)

![48_image_1_7674.png](6.54 Flash Application: Applicaiton  The image displays a diagram with several elements on it. The main focus is on a section of code that reads "Flash Application." This could potentially be related to an application or software development project involving the use of Adobe Flash technology.)

![48_image_2_7674.png](The image displays a computer screen with a window configuration prompt on it. There are two buttons visible on the screen, one labeled "Yes" and another labeled "No." Above these buttons, there is a question asking whether to reset the window configuration or not. This indicates that the user might be configuring their operating system or software settings.)

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

![49_image_0_7674.png](The image displays a computer screen with multiple windows open, showcasing various applications. There are three main windows on the screen, each containing different types of data. One window is filled with rows of numbers, while another has a list of names or addresses. A third window appears to be related to financial calculations or transactions.  In addition to these primary windows, there are several smaller windows scattered across the screen, possibly providing more information or options for the user. The overall scene suggests that this computer is being used for various tasks and purposes, including data analysis, organization, and financial management.)

pin sensor supply 1, the default connection can be set by connecting the pin sensor supply 0 to ground. See the TTC-Downloader documentation **help.chm**, Section **Advanced Features > The** CAN Fallback Mode for the HY-TTC 500 variant specific default CAN channel. Note: If you have changed the TTC-Downloader settings in previous applications of the HY-TTC 500, then make sure that you reset them to the default values.

To start connecting press F2 and quickly power on the device, while the Downloader progress bar appears (see Figure 5.48(a) on the next page).

After successful connection, the downloader will identify the device and prepare the flashing process (see Figure 5.48(b) on the facing page).

## 5.8.2.2.2 Connecting Via Ethernet

Note: For unexperienced users of the HY-TTC 500 it is recommended to use the CAN option. If you use Ethernet and an application is already flashed to the target, then you have to make sure that the application listens to download requests on the Ethernet. The example application of the Quick Start Guide does not listen to download requests.

To connect to the device via Ethernet, use the Ethernet port of your computer and connect it to the Ethernet port of the HY-TTC 500. Note that a point-to-point Ethernet connection is mandatory. Open the TTC-Downloader.

The next step depends on the content of the flash memory:

![50_image_0_7674.png](1. The image displays a computer screen with two windows side by side. In one window, there is an error message that reads "Error: Permission Denied." On the other side of the screen, there are instructions on how to fix this issue. 2. A screenshot of a Windows desktop shows a red button labeled "Power Cycle NCM!" in the middle of the screen. The image also includes a few icons and text boxes around it.)

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

![51_image_0_7674.png](16-bit Application C++ Data X200 FFT (Fast Fourier Transform) is shown in a diagram with several layers of information. The diagram includes labels such as "Application," "C++," "Data," "X200," and "FFT." There are also smaller text boxes that provide additional details about the different components within the image, including "Bootloader" and "Protected." This visual representation helps to understand the relationships between these various elements in a clear and organized manner.) Application Cfg. Data 0xF0200000 65536 Bytes Application 0x000A0100 2490112 Bytes

APDB + CRC 0x000A0000 256 Bytes

FPGA IP 0x00020000 524288 Bytes

Bootloader 0x00000000 131072 Bytes

The following table specifies the start address and size of the **internal RAM** for the HY-TTC 500 controllers.

[table_8][{0: 'HY-TTC 500', 1: 'Start Address', 2: 'Size'}, {0: 'Int. RAM', 1: '0x08003000', 2: '217088 Bytes'}][/table_8]

## 6.2 Memory Map For External Flash And Ram

The following tables specify the start address of the **external RAM** and **Flash** for the HY-TTC 500 controllers.

![52_image_0_7674.png](The image displays a computer screen with various information related to RAM and storage. There are two main sections on the screen, one of which is labeled "HYTC 5100." This section contains details such as the size of the RAM (2048 KB) and the number of bytes (2097152). The other section displays information about the storage capacity, including the amount of free space available.  In addition to these main sections, there are smaller text boxes scattered throughout the screen that provide more details on the RAM and storage. Overall, the image provides a comprehensive view of the computer's memory and storage capabilities.)

[table_9][{0: 'HY-TTC 580', 1: 'Start Address', 2: 'Size'}, {0: 'Ext. RAM', 1: '0x60000000', 2: '2097152 Bytes'}, {0: 'Ext. Flash', 1: '0x64000000', 2: '8388608 Bytes'}, {0: 'HY-TTC 540', 1: 'Start Address', 2: 'Size'}, {0: 'Ext. RAM', 1: '0x60000000', 2: '2097152 Bytes'}, {0: 'HY-TTC 520', 1: 'Start Address', 2: 'Size'}, {0: 'Ext. RAM', 1: '0x60000000', 2: '2097152 Bytes'}][/table_9]

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
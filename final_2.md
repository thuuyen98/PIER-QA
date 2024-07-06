# Hy-Ttc 500

![0_Image_0.Png](0_Image_0.Png)

System Manual Programmable ECU for Sensor-Actuator Management Product Version 02.00 Original Instructions

| Document Number:   | D-TTC5F-G-20-002   |
|--------------------|--------------------|
| Document Version:  | 1.6.0              |
| Date:              | 25-Aug-2022        |
| Status:            | Released           |

TTControl GmbH
Schoenbrunner Str. 7, A-1040 Vienna, Austria,Tel. +43 1 585 34 34–0, Fax +43 1 585 34 34–90, **office@ttcontrol.com** No part of the document may be reproduced or transmitted in any form or by any means, electronic or mechanical, for any purpose, without the written permission of TTControl GmbH. Company or product names mentioned in this document may be trademarks or registered trademarks of their respective holders. TTControl GmbH undertakes no further obligation or relation to this document.

Copyright  2022 TTControl GmbH. All rights reserved. **Subject to changes and corrections**
TTControl GmbH Confidential and Proprietary Information

## Legal Notice **Document Number: D-Ttc5F-G-20-002**

The data in this document may not be altered or amended without special notification from TTControl GmbH. TTControl GmbH undertakes no further obligation in relation to this document. The software described in it can only be used if the customer is in possession of a general license agreement or single license. The information contained in this document does not affect or change any General Terms and Conditions of TTControl GmbH and/or any agreements existing between TTControl GmbH and the recipient regarding the product or Sample concerned. The reader acknowledges that this document may not be reproduced, stored in a retrieval system, transmitted, changed, or translated, in whole or in part, without the express prior written consent of TTControl GmbH. The reader acknowledges that any and all of the copyrights, trademarks, trade names, **patents (whether registrable or not)** and other intellectual property rights embodied in or in connection with this document are and will remain the sole property of TTControl GmbH or the respective **right holder. Nothing contained** in this legal notice, the document or in any web site of TTControl GmbH shall be construed as conferring to the recipient any license under any intellectual property rights, whether explicit, by estoppel, implication, or otherwise. The product or Sample is only allowed to be used in the scope as **described in this document.**
TTControl GmbH provides this document "as is" and disclaims **all warranties of any kind. The entire** risk, as to quality, use or performance of the document remains with the recipient. All trademarks mentioned in this document belong to their respective owners.

Copyright  2022 TTControl GmbH. All rights reserved.

## Contents

| Table of Contents   |                                                     | viii   |    |
|---------------------|-----------------------------------------------------|--------|----|
| List of Figures     |                                                     | x      |    |
| List of Tables      |                                                     | xi     |    |
| 1                   | Introduction                                        |        | 2  |
| 1.1                 | Inputs and Outputs                                  |        | 2  |
| 1.2                 | Communication Interfaces                            |        | 2  |
| 1.3                 | Safety and Certification                            | 2      |    |
| 1.4                 | Programming Options                                 |        | 3  |
| 1.5                 | HY-TTC 500 Variants                                 |        | 3  |
| 1.5.1               | HY-TTC 500 FPGA Variants                            |        | 3  |
| 1.5.2               | HY-TTC 580 Variant                                  |        | 7  |
| 1.5.3               | HY-TTC 540 Variant                                  |        | 11 |
| 1.5.4               | HY-TTC 520 Variant (Customer-specific variant only) |        | 15 |
| 1.5.5               | HY-TTC 510 Variant                                  |        | 19 |
| 1.5.6               | HY-TTC 590E Variant                                 |        | 23 |
| 1.5.7               | HY-TTC 590 Variant                                  |        | 27 |
| 1.5.8               | HY-TTC 508 Variant                                  |        | 31 |
| 1.6                 | Standards and Guidelines                            |        | 35 |
| 1.6.1               | Electrical Capability                               |        | 36 |
| 1.6.2               | Mechanical Capability                               |        | 36 |
| 1.6.3               | Climatic Capability                                 |        | 36 |
| 1.6.4               | Chemical Capability                                 |        | 37 |
| 1.6.5               | Ingress Protection Capability                       |        | 37 |
| 1.6.6               | ESD and EMC Capability for Road Vehicles            |        | 38 |
| 1.6.7               | ESD and EMC Capability for Industrial Applications  |        | 38 |
| 1.6.8               | Functional Safety                                   |        | 38 |
| 1.7                 | Instructions for Safe Operation                     |        | 39 |
| 1.7.1               | General                                             |        | 39 |
| 1.7.2               | Checks to be done before commissioning the ECU      |        | 40 |
| 1.7.3               | Intended use                                        |        | 40 |
| 1.7.4               | Improper use                                        | 40     |    |
| 2                   | Mounting and Label                                  |        | 41 |
| 2.1                 | Mounting Requirements                               |        | 41 |
| 2.2                 | Label Information                                   |        | 41 |
| 3                   | Pinning and Connector                               |        | 42 |
| 3.1                 | Connector                                           | 42     |    |
| 3.2                 | Mating Connector                                    |        | 43 |
| 3.2.1               | KOSTAL Mating Connector                             |        | 44 |
| 3.2.1.1             | Mating Connector 96-positions                       |        | 44 |
| 3.2.1.2             | Mating Connector 58-positions                       |        | 44 |
| 3.2.1.3             | Crimp Contacts                                      |        | 45 |

| 3.2.1.4   | Tools                                               |     | 45   |
|-----------|-----------------------------------------------------|-----|------|
| 3.2.2     | BOSCH Mating Connector                              |     | 46   |
| 3.2.2.1   | Mating Connector 96-positions                       |     | 46   |
| 3.2.2.2   | Mating Connector 58-positions                       |     | 46   |
| 3.2.2.3   | Crimp Contacts                                      |     | 47   |
| 3.2.2.4   | Tools                                               |     | 47   |
| 3.3       | Cable Harness                                       |     | 48   |
| 3.4       | Fuse                                                |     | 48   |
| 3.5       | HY-TTC 500 Family Pinning                           |     | 49   |
| 3.5.1     | HY-TTC 580 Variant                                  |     | 50   |
| 3.5.2     | HY-TTC 540 Variant                                  |     | 57   |
| 3.5.3     | HY-TTC 520 Variant (Customer-specific variant only) |     | 64   |
| 3.5.4     | HY-TTC 510 Variant                                  |     | 70   |
| 3.5.5     | HY-TTC 590E Variant                                 |     | 76   |
| 3.5.6     | HY-TTC 590 Variant                                  |     | 83   |
| 3.5.7     | HY-TTC 508 Variant                                  |     | 90   |
| 4         | Specification of Inputs and Outputs                 |     | 96   |
| 4.1       | BAT+ Power                                          | 96  |      |
| 4.1.1     | Pinout                                              |     | 96   |
| 4.1.2     | Functional Description                              |     | 96   |
| 4.1.3     | Maximum Ratings                                     |     | 97   |
| 4.1.4     | Characteristics                                     |     | 97   |
| 4.2       | BAT+ CPU                                            |     | 98   |
| 4.2.1     | Pinout                                              |     | 98   |
| 4.2.2     | Functional Description                              |     | 99   |
| 4.2.3     | Maximum Ratings                                     |     | 100  |
| 4.2.4     | Characteristics                                     |     | 100  |
| 4.2.5     | Low-Voltage Operation                               |     | 101  |
| 4.2.5.1   | HY-TTC 500 ISO 16750 functional status              |     | 103  |
| 4.2.6     | Voltage Monitoring                                  |     | 103  |
| 4.3       | BAT-                                                |     | 104  |
| 4.3.1     | Pinout                                              |     | 104  |
| 4.3.2     | Functional Description                              |     | 105  |
| 4.3.3     | Maximum Ratings                                     |     | 105  |
| 4.4       | Sensor GND                                          |     | 106  |
| 4.4.1     | Pinout                                              |     | 106  |
| 4.4.2     | Functional Description                              |     | 107  |
| 4.4.3     | Maximum Ratings                                     |     | 107  |
| 4.5       | Terminal 15                                         |     | 108  |
| 4.5.1     | Pinout                                              |     | 108  |
| 4.5.2     | Functional Description                              |     | 109  |
| 4.5.3     | Maximum Ratings                                     |     | 109  |
| 4.5.4     | Characteristics                                     |     | 109  |
| 4.6       | Wake-Up                                             | 110 |      |

| 4.6.1    | Pinout                                     |     | 110   |
|----------|--------------------------------------------|-----|-------|
| 4.6.2    | Functional Description                     |     | 110   |
| 4.6.3    | Maximum Ratings                            |     | 111   |
| 4.6.4    | Characteristics                            |     | 111   |
| 4.7      | Sensor Supplies 5 V                        | 112 |       |
| 4.7.1    | Pinout                                     |     | 112   |
| 4.7.2    | Functional Description                     |     | 112   |
| 4.7.3    | Maximum Ratings                            |     | 113   |
| 4.7.4    | Characteristics                            |     | 113   |
| 4.8      | Sensor Supply Variable                     |     | 114   |
| 4.8.1    | Pinout                                     |     | 114   |
| 4.8.2    | Functional Description                     |     | 114   |
| 4.8.3    | Maximum Ratings                            |     | 115   |
| 4.8.4    | Characteristics                            |     | 115   |
| 4.9      | Analog Input 3 Modes                       | 116 |       |
| 4.9.1    | Pinout                                     |     | 116   |
| 4.9.2    | Functional Description                     |     | 116   |
| 4.9.3    | Maximum Ratings                            |     | 117   |
| 4.9.4    | Analog Voltage Input                       |     | 117   |
| 4.9.4.1  | Characteristics of 5 V Input (Ratiometric) |     | 118   |
| 4.9.4.2  | Characteristics of 5 V Input (Absolute)    |     | 119   |
| 4.9.4.3  | Characteristics of 5 V Digital Input       |     | 119   |
| 4.9.5    | Analog Current Input                       |     | 120   |
| 4.9.5.1  | Characteristics of Analog Current Input    |     | 121   |
| 4.9.6    | Analog Resistance Input                    |     | 121   |
| 4.9.6.1  | Characteristics of Analog Resistance Input |     | 122   |
| 4.10     | Analog Input 2 Modes                       | 124 |       |
| 4.10.1   | Pinout                                     |     | 124   |
| 4.10.2   | Functional Description                     |     | 125   |
| 4.10.3   | Maximum Ratings                            |     | 125   |
| 4.10.4   | Analog Voltage Input                       |     | 126   |
| 4.10.4.1 | Characteristics of 5 V Input (Ratiometric) |     | 126   |
| 4.10.4.2 | Characteristics of 5 V Input (Absolute)    |     | 126   |
| 4.10.4.3 | Characteristics of 10 V Input (Absolute)   |     | 127   |
| 4.10.4.4 | Characteristics of 32 V Input (Absolute)   |     | 127   |
| 4.10.4.5 | Characteristics of 32 V Digital Input      |     | 128   |
| 4.10.5   | Analog Current Input                       |     | 129   |
| 4.10.5.1 | Characteristics of Analog Current Input    |     | 129   |
| 4.11     | Timer Inputs                               |     | 130   |
| 4.11.1   | Pinout                                     |     | 130   |
| 4.11.2   | Functional Description                     |     | 131   |
| 4.11.3   | Maximum Ratings                            |     | 131   |
| 4.11.4   | Timer and Current Loop Inputs              |     | 134   |
| 4.11.4.1 | Characteristics of Timer Input             |     | 134   |

| 4.11.4.2   | Characteristics of Current Loop Input       |     | 134   |
|------------|---------------------------------------------|-----|-------|
| 4.11.5     | Analog and Digital Inputs                   |     | 136   |
| 4.11.5.1   | Characteristics of Analog Voltage Input     |     | 136   |
| 4.11.5.2   | Characteristics of Digital Input            |     | 136   |
| 4.12       | High-Side PWM Outputs                       |     | 137   |
| 4.12.1     | Pinout                                      |     | 137   |
| 4.12.2     | Functional Description                      |     | 138   |
| 4.12.2.1   | Power Stage Pairing                         |     | 140   |
| 4.12.2.2   | Mutual Exclusive Mode                       |     | 140   |
| 4.12.3     | Maximum Ratings                             |     | 140   |
| 4.12.4     | High-Side PWM Outputs                       |     | 141   |
| 4.12.4.1   | Characteristics of High-Side PWM Output     |     | 141   |
| 4.12.4.2   | Diagnostic Functions                        |     | 141   |
| 4.12.4.3   | Current Measurement                         |     | 142   |
| 4.12.5     | High-Side Digital Outputs                   |     | 144   |
| 4.12.5.1   | Characteristics of High-Side Digital Output |     | 144   |
| 4.12.6     | Digital and Frequency Inputs                |     | 144   |
| 4.12.6.1   | Characteristics of Digital Input            |     | 145   |
| 4.12.6.2   | Characteristics of Timer Input              |     | 145   |
| 4.12.7     | Secondary Shut-off Paths                    |     | 146   |
| 4.12.8     | External Shut-off Groups                    |     | 147   |
| 4.12.8.1   | Characteristics of External Shut-off        | 147 |       |
| 4.12.9     | Tertiary Shut-off Path                      | 148 |       |
| 4.12.9.1   | Functional description                      |     | 148   |
| 4.13       | High-Side Digital Outputs                   |     | 149   |
| 4.13.1     | Pinout                                      |     | 149   |
| 4.13.2     | Functional Description                      |     | 150   |
| 4.13.2.1   | Power Stage Pairing                         |     | 151   |
| 4.13.2.2   | Mutual Exclusive Mode                       |     | 151   |
| 4.13.3     | Diagnostic Functions                        | 151 |       |
| 4.13.4     | Maximum Ratings                             |     | 151   |
| 4.13.5     | High-Side Digital Outputs                   |     | 152   |
| 4.13.5.1   | Characteristics of High-Side Output         |     | 152   |
| 4.13.6     | Analog and Digital Inputs                   |     | 153   |
| 4.13.6.1   | Characteristics of Analog Voltage Input     |     | 153   |
| 4.13.6.2   | Characteristics of Digital Input            |     | 153   |
| 4.14       | High-Side Digital/PVG/VOUT Outputs          |     | 155   |
| 4.14.1     | Pinout                                      |     | 155   |
| 4.14.2     | Functional Description                      |     | 156   |
| 4.14.2.1   | Power Stage Pairing                         |     | 156   |
| 4.14.2.2   | Mutual Exclusive Mode                       |     | 156   |
| 4.14.3     | Maximum Ratings                             |     | 156   |
| 4.14.4     | High-Side Digital Outputs                   |     | 157   |
| 4.14.4.1   | Diagnostic Functions                        |     | 158   |

| 4.14.4.2   | Characteristics of High-Side Digital            | 158   |     |
|------------|-------------------------------------------------|-------|-----|
| 4.14.5     | PVG Outputs                                     |       | 159 |
| 4.14.5.1   | Characteristics of PVG                          |       | 160 |
| 4.14.6     | VOUT Outputs                                    |       | 161 |
| 4.14.6.1   | Characteristics of VOUT                         |       | 162 |
| 4.14.7     | Analog and Digital Inputs                       |       | 163 |
| 4.14.7.1   | Characteristics of Analog Voltage Input         |       | 163 |
| 4.14.7.2   | Characteristics of Digital Input                |       | 163 |
| 4.15       | Low-Side Digital Outputs                        |       | 165 |
| 4.15.1     | Pinout                                          |       | 165 |
| 4.15.2     | Functional Description                          |       | 166 |
| 4.15.2.1   | Power Stage Pairing                             |       | 167 |
| 4.15.3     | Diagnostic Functions                            | 167   |     |
| 4.15.4     | Maximum Ratings                                 |       | 167 |
| 4.15.5     | Characteristics of Low-Side Digital Output      |       | 168 |
| 4.15.6     | Analog and Digital Inputs                       |       | 169 |
| 4.15.6.1   | Characteristics of Analog Voltage Input         |       | 169 |
| 4.15.6.2   | Characteristics of Digital Input                |       | 169 |
| 4.16       | LIN                                             |       | 170 |
| 4.16.1     | Pinout                                          |       | 170 |
| 4.16.2     | Functional Description                          |       | 171 |
| 4.16.3     | Maximum Ratings                                 |       | 172 |
| 4.16.4     | Characteristics                                 |       | 172 |
| 4.17       | RS232                                           |       | 173 |
| 4.17.1     | Pinout                                          |       | 173 |
| 4.17.2     | Functional Description                          |       | 174 |
| 4.17.3     | Maximum Ratings                                 |       | 174 |
| 4.17.4     | Characteristics                                 |       | 174 |
| 4.18       | CAN                                             |       | 175 |
| 4.18.1     | Pinout                                          |       | 175 |
| 4.18.2     | Functional Description                          |       | 176 |
| 4.18.2.1   | CAN1 on HY-TTC 590E, HY-TTC 590, and HY-TTC 508 | . . . | 176 |
| 4.18.3     | Maximum Ratings                                 |       | 178 |
| 4.18.4     | Characteristics                                 |       | 178 |
| 4.19       | CAN Termination                                 | 179   |     |
| 4.19.1     | Pinout                                          |       | 179 |
| 4.19.2     | Functional Description                          |       | 180 |
| 4.20       | Ethernet                                        |       | 181 |
| 4.20.1     | Pinout                                          |       | 181 |
| 4.20.2     | Functional Description                          |       | 182 |
| 4.20.3     | Maximum Ratings                                 |       | 182 |
| 4.21       | BroadR-Reach®                                   |       | 183 |
| 4.21.1     | Pinout                                          |       | 183 |
| 4.21.2     | Functional Description                          |       | 183 |

| 4.21.3   | Maximum Ratings                           |     | 184   |
|----------|-------------------------------------------|-----|-------|
| 4.21.4   | Characteristics                           |     | 184   |
| 4.22     | Real-Time Clock (RTC)                     |     | 185   |
| 4.22.1   | Pinout                                    |     | 185   |
| 4.22.2   | Functional Description                    |     | 186   |
| 4.22.3   | Maximum Ratings                           |     | 187   |
| 4.22.4   | Characteristics                           |     | 187   |
| 5        | Internal Structure                        |     | 188   |
| 5.1      | Safety Concept                            |     | 188   |
| 5.1.1    | Overview Safety Concept                   |     | 188   |
| 5.2      | Thermal Management                        |     | 190   |
| 5.2.1    | Board Temperature Sensor                  |     | 190   |
| 5.2.1.1  | Pinout                                    |     | 190   |
| 5.2.1.2  | Functional Description                    |     | 190   |
| 5.2.2    | Characteristics                           |     | 191   |
| 6        | Application Notes                         |     | 192   |
| 6.1      | Cable Harness                             |     | 192   |
| 6.2      | Handling of High-Load Current             |     | 193   |
| 6.2.1    | Load Distribution                         |     | 193   |
| 6.2.2    | Total Load Current                        |     | 193   |
| 6.2.2.1  | Calculation of the battery supply current |     | 194   |
| 6.3      | Inductive Loads                           |     | 195   |
| 6.3.1    | Inductive Loads at PWM Outputs            | 195 |       |
| 6.3.2    | Inductive Loads at Low Side Switches      |     | 195   |
| 6.4      | Ground Connection of Housing              |     | 195   |
| 6.5      | Motor Control                             | 196 |       |
| 6.5.1    | Motor Types supported                     |     | 196   |
| 6.5.2    | Direct Control Options                    |     | 196   |
| 6.5.2.1  | Depending on Direction                    |     | 196   |
| 6.5.2.2  | Depending on Single Motor / Motor Group   | 196 |       |
| 6.5.2.3  | Depending on Control                      |     | 196   |
| 6.5.2.4  | Depending on stalled Motor Current        |     | 196   |
| 6.5.3    | Motor Details                             | 197 |       |
| 6.5.3.1  | Start Current                             |     | 197   |
| 6.5.3.2  | Start Current at low Temperatures         |     | 197   |
| 6.5.3.3  | Battery Voltage Impact                    |     | 197   |
| 6.5.3.4  | Motors with Limit Switch                  |     | 197   |
| 6.5.3.5  | Motors with Electronics Inside            | 198 |       |
| 6.5.3.6  | Unidirectional Motor Drive                |     | 198   |
| 6.5.3.7  | Bidirectional Motor Drive                 |     | 198   |
| 6.5.3.8  | Active Motor Brake                        |     | 198   |
| 6.5.3.9  | Motors Reversing with / without Braking   | 198 |       |
| 6.5.3.10 | PWM Operation / steady State Control      |     | 198   |

| 6.5.3.11         | Maximum Average Current (PWM and Digital Power Stages) 199       |     |     |
|------------------|------------------------------------------------------------------|-----|-----|
| 6.5.3.12         | Peak Current Bidirectional Drive (Digital Power Stages only) 199 |     |     |
| 6.5.3.13         | Peak Current Unidirectional Drive (Digital Power Stages only)    | 199 |     |
| 6.5.4            | Motor Classification                                             |     | 200 |
| 6.5.4.1          | Independent from Speed Class                                     |     | 200 |
| 6.5.4.2          | Fast Accelerating Motors only                                    |     | 203 |
| 6.5.5            | Connection                                                       |     | 208 |
| 6.5.5.1          | Unidirectional Single Power Stage                                |     | 208 |
| 6.5.5.2          | Unidirectional Double Power Stage                                |     | 210 |
| 6.5.5.3          | Bidirectional H-bridge (Single Power Stages)                     |     | 211 |
| 6.5.5.4          | Bidirectional H-bridge (Multiple Low Side Power Stages)          | .   | 212 |
| 6.5.5.5          | Bidirectional H-bridge (Multiple High and Low Side Power Stages) | 213 |     |
| 6.5.5.6          | Motor Cluster                                                    |     | 214 |
| 6.5.6            | Power Stages for Motor Control                                   |     | 215 |
| 6.5.6.1          | High Side Power Stages for PWM Operation                         |     | 215 |
| 6.5.6.2          | High Side Power Stages for Static Operation                      |     | 215 |
| 6.5.6.3          | Low Side Power Stages                                            |     | 215 |
| 6.5.7            | Parallel Operation of Power Stages                               |     | 216 |
| 6.5.8            | Cabling                                                          |     | 216 |
| 6.5.9            | Control Sequence for Bidirectional Drive                         |     | 216 |
| 6.5.9.1          | Motor Running                                                    |     | 217 |
| 6.5.9.2          | Motor Breaking                                                   |     | 217 |
| 6.5.9.3          | Paralleled High Side Power Stage Control                         |     | 217 |
| 6.6              | Power Stage Alternative Functions                                |     | 218 |
| 6.6.1            | High-Side Output Stages                                          |     | 218 |
| 6.6.1.1          | Wiring examples                                                  |     | 218 |
| 7                | Debugging                                                        |     | 224 |
| 7.1              | Functional Description                                           |     | 224 |
| 8                | API Documentation                                                |     | 226 |
| Glossary         | 227                                                              |     |     |
| References       |                                                                  | 229 |     |
| Index            |                                                                  | 231 |     |
| Disposal         |                                                                  | 234 |     |
| Legal Disclaimer |                                                                  | 235 |     |

## List Of Figures

| 1   | HY-TTC 580 Variant                                                           |       | 7   |
|-----|------------------------------------------------------------------------------|-------|-----|
| 2   | HY-TTC 540 Variant                                                           |       | 11  |
| 3   | HY-TTC 520 Variant                                                           |       | 15  |
| 4   | HY-TTC 510 Variant                                                           |       | 19  |
| 5   | HY-TTC 590E Variant                                                          |       | 23  |
| 6   | HY-TTC 590 Variant                                                           |       | 27  |
| 7   | HY-TTC 508 Variant                                                           |       | 31  |
| 8   | ISO 16750-1:2006 [13], Figure 1 - Code allocation                            |       | 35  |
| 9   | ECU label with Version field                                                 |       | 39  |
| 10  | Main connector                                                               |       | 42  |
| 11  | 58 terminal plug housing set                                                 |       | 43  |
| 12  | 96 terminal plug housing set                                                 |       | 43  |
| 13  | Battery Supply - Fuse                                                        |       | 48  |
| 14  | Pinout of BAT+ Power                                                         |       | 96  |
| 15  | Pinout of BAT+ CPU                                                           | 98    |     |
| 16  | Supply pin for the internal ECU logic                                        |       | 99  |
| 17  | ISO 16750-2, Figure 7 - Starting profile                                     | 102   |     |
| 18  | Pinout of BAT-                                                               |       | 104 |
| 19  | Pinout of sensor GND                                                         |       | 106 |
| 20  | Pinout of terminal 15                                                        |       | 108 |
| 21  | Pinout of Wake-Up                                                            |       | 110 |
| 22  | Pinout of sensor supply 5 V                                                  |       | 112 |
| 23  | Sensor supply 5 V                                                            |       | 113 |
| 24  | Pinout of sensor supply variable                                             |       | 114 |
| 25  | Sensor supply variable                                                       |       | 115 |
| 26  | Pinout of analog input 3 mode                                                |       | 116 |
| 27  | Analog voltage input (ratiometric)                                           |       | 117 |
| 28  | Analog voltage input                                                         | 118   |     |
| 29  | Analog current input                                                         |       | 120 |
| 30  | Analog resistance input                                                      |       | 121 |
| 31  | Namur type sensor (only for switches to ground)                              |       | 122 |
| 32  | Switch input (only for switches to ground)                                   |       | 122 |
| 33  | Pinout of analog input 2 mode                                                |       | 124 |
| 34  | Pinout of timer input                                                        |       | 130 |
| 35  | Digital input for frequency/timing measurement with NPN-type 2-pole sensor   |       | 131 |
| 36  | Digital input for frequency/timing measurement with PNP-type 2-pole sensor   |       | 132 |
| 37  | Digital input pair for encoder and direction                                 |       | 132 |
| 38  | Digital input for switch connected to (battery) supply voltage               |       | 133 |
| 39  | Digital input for switch connected to ground                                 | 133   |     |
| 40  | Digital input for frequency measurement with ABS-type 7/14 mA, 2 pole sensor | . . . | 135 |
| 41  | Pinout of high-side PWM outputs                                              |       | 137 |

| 42   | High-side output stage with PWM functionality                    |     | 139   |
|------|------------------------------------------------------------------|-----|-------|
| 43   | Distribution of PWM output stages to shut-off groups/paths       |     | 146   |
| 44   | Tertiary Shut-off Path                                           |     | 148   |
| 45   | Pinout of high-side digital outputs                              |     | 149   |
| 46   | Digital high-side power stage                                    |     | 150   |
| 47   | Pinout of High-side digital/PVG/VOUT outputs                     |     | 155   |
| 48   | Digital high-side power stage                                    |     | 157   |
| 49   | Output stage in PVG mode                                         |     | 159   |
| 50   | Output stage in VOUT mode                                        |     | 161   |
| 51   | Pinout of low-side digital outputs                               |     | 165   |
| 52   | Low-side switch for resistive and inductive loads                |     | 166   |
| 53   | LIN pinout                                                       |     | 170   |
| 54   | LIN interface                                                    |     | 171   |
| 55   | RS232 pinout                                                     |     | 173   |
| 56   | RS232 interface                                                  |     | 174   |
| 57   | CAN pinout                                                       |     | 175   |
| 58   | CAN interface                                                    |     | 177   |
| 59   | Pinout of CAN termination                                        |     | 179   |
| 60   | Optional CAN termination                                         |     | 180   |
| 61   | Ethernet pinout                                                  |     | 181   |
| 62   | Ethernet interface                                               |     | 182   |
| 63   | 100BASE-T1 Ethernet pinout                                       |     | 183   |
| 64   | RTC pinout                                                       |     | 185   |
| 65   | Voltage supply of real-time clock                                |     | 186   |
| 66   | Overview safety concept HY-TTC 500                               |     | 189   |
| 67   | Unidirectional Single Power Stage                                |     | 208   |
| 68   | Unidirectional Single Power Stage                                |     | 209   |
| 69   | Unidirectional Double Power Stage                                |     | 210   |
| 70   | Bidirectional H-bridge (Single Power Stages)                     |     | 211   |
| 71   | Bidirectional H-bridge (Multiple Low Side Power Stages)          |     | 212   |
| 72   | Bidirectional H-bridge (Multiple High and Low Side Power Stages) | 213 |       |
| 73   | Motor Cluster (Example: Outside Mirror Control)                  |     | 214   |
| 74   | Switch connected to GND                                          |     | 219   |
| 75   | Switch connected to GND                                          |     | 219   |
| 76   | Switch connected to GND                                          |     | 220   |
| 77   | Switch connected to PWM high-side output stage                   |     | 220   |
| 78   | Switch connected to PWM high-side output stage                   |     | 221   |
| 79   | Switch connected to PWM high-side output stage                   |     | 221   |
| 80   | Switch connected to digital high-side output stage               |     | 222   |
| 81   | Switch connected to battery supply                               |     | 223   |
| 82   | Switch connected to battery supply                               |     | 223   |
| 83   | Pinning of JTAG Connector on the TTC JTAG-Adapter Board          | 224 |       |

## List Of Tables

| 1   | Variants overview for the Spartan-6 XA6SLX16 FPGA          |     | 4   |
|-----|------------------------------------------------------------|-----|-----|
| 2   | Variants overview for the Spartan-6 XA6SLX9 FPGA           |     | 5   |
| 3   | Variants overview for the Spartan-6 XA6SLX25 FPGA          |     | 6   |
| 4   | List of chemical agents                                    |     | 37  |
| 5   | KOSTAL / HERTH+BUSS part numbers                           | 44  |     |
| 6   | KOSTAL / HERTH+BUSS part numbers                           | 44  |     |
| 7   | KOSTAL / HERTH+BUSS part numbers                           | 45  |     |
| 8   | KOSTAL / HERTH+BUSS part numbers                           | 45  |     |
| 9   | BOSCH part numbers                                         |     | 46  |
| 10  | BOSCH part numbers                                         |     | 46  |
| 11  | BOSCH crimp contacts part numbers                          |     | 47  |
| 12  | BOSCH Tools part numbers                                   |     | 47  |
| 13  | Pinning of HY-TTC 580                                      |     | 56  |
| 14  | Pinning of HY-TTC 540                                      |     | 63  |
| 15  | Pinning of HY-TTC 520                                      |     | 69  |
| 16  | Pinning of HY-TTC 510                                      |     | 75  |
| 17  | Pinning of HY-TTC 590E                                     |     | 82  |
| 18  | Pinning of HY-TTC 590                                      |     | 89  |
| 19  | Pinning of HY-TTC 508                                      |     | 95  |
| 20  | ISO 16750 functional status for 12 V systems               |     | 103 |
| 21  | ISO 16750 functional status for 24 V systems               |     | 103 |
| 23  | Total Load Current Iin-total                               |     | 193 |
| 32  | Order code of JTAG connector on the TTC JTAG-Adapter Board |     | 224 |

Hardware Description

## 1 Introduction

The HY-TTC 500 is a family of programmable electronic control units for sensor/actuator management. Lots of configurable I/Os allow the use of HY-TTC 500 with different sensor and actuator types.

Being part of a complete and compatible product family, the control unit is specifically designed for vehicles and machines that operate in rough environments and at extreme operating temperatures. The robust die-cast aluminum housing of HY-TTC 500 provides **protection against electromagnetic** disturbances and mechanical stress. A 180 MHz TI TMS570-integrated microprocessor provides the necessary processing power. To provide individual features that are scalable to system integrator needs, the HY-TTC 500 family is available in several variants, with different assembly options. See Section 1.5 **on the facing page for variants overview.**

## 1.1 Inputs And Outputs

All inputs and outputs of each HY-TTC 500 variant are protected against electrical surges and short circuits. In addition, internal safety measures allow the detection of open load, overload and short circuit conditions at the outputs. Proportional hydraulic **components can be directly connected to**
the current-controlled PWM outputs. The HY-TTC 500 family is designed to support a variety of analog and digital sensor types. Many software-configurable input options can be selected to adapt to different sensor types. A group of individually configurable analog inputs with a voltage ranging from 0. . . 5V to 0. . . 32V are provided. Those analog inputs can **be set to different voltage ranges by** software in order to achieve the best analog accuracy and resolution. The analog inputs can also be configured as a current input or for resistive measurements.

## 1.2 Communication Interfaces

On the fully equipped variant HY-TTC 580, 7 x CAN (according to CAN 2.0B), 1x RS-232 and 1x LIN interface are available for serial communication. Additionally a 10/100 Mbit/s Ethernet interface for high speed communication, application download, and debug purpose is provided.

## 1.3 Safety And Certification

The HY-TTC 500 family is designed to comply with the international standards IEC 61508 [8],
ISO 13849 [24], and ISO 25119 [25]. For information regarding ISO 26262 [26] compliance, or for any further queries, please contact TTControl at support@ttcontrol.com.

## 1.4 Programming Options

The unit may be programmed in C or CODESYS. CODESYS is one of the most common IEC 611313 programming systems [10] running under Microsoft Windows. CODESYS supports several editors, including the Instruction List Editor, Sequential Function Chart Editor, and Function Block Diagram Editor**. CODESYS produces native machine code for the main processor of HY-TTC 500.**

## 1.5 Hy-Ttc 500 Variants

The following HY-TTC 500 variants are described in this System Manual:
- **HY-TTC 580**
- **HY-TTC 540**
- **HY-TTC 520 (customer-specific variant only)** - **HY-TTC 510**
- **HY-TTC 590E**
- **HY-TTC 590**

## - **Hy-Ttc 508**

The main difference of the listed HY-TTC 500 variants is the amount of available I/Os, whereas the HY-TTC 580 is the most powerful variant with the maximum number of I/Os. See Chapter 3 on page 42 **which main- and alternative functions are available on which variant.**
Unless other specified in Chapter 4 on page **96, the functionality of the available main- and alternative functions do not differ between each variants.**

## 1.5.1 Hy-Ttc 500 Fpga Variants

The following 3 tables Table 1 on the next page, Table 2 on page 5 and Table 3 on page 6 **define the**
main features and I/Os of three different hardware executions: Spartan-6 XA6SLX9 FPGA, Spartan6 XA6SLX16 FPGA and Spartan-6 XA6SLX25 FPGA based

| Feature                                                    | HY-TTC 580            | HY-TTC 540   | HY-TTC 520   | HY-TTC 510   | HY-TTC 590E   | HY-TTC 590   | HY-TTC 508   |       |
|------------------------------------------------------------|-----------------------|--------------|--------------|--------------|---------------|--------------|--------------|-------|
| CPU                                                        | 32-bit TI TMS570      | x            | x            | x            | x             | x            | x            | x     |
| Int. FLASH                                                 | 3 MB                  | 3 MB         | 3 MB         | 3 MB         | 3 MB          | 3 MB         | 3 MB         |       |
| Int. RAM                                                   | 256 kB                | 256 kB       | 256 kB       | 256 kB       | 256 kB        | 256 kB       | 256 kB       |       |
| Memory                                                     | Ext. FLASH            | 8 MB         | -            | -            | -             | 64 MB        | 32 MB        | 16 MB |
| Ext. RAM                                                   | 2 MB                  | 2 MB         | 2 MB         | 2 MB         | 2 MB          | 2 MB         | 2 MB         |       |
| Ext. EEPROM                                                | 64 kB                 | 64 kB        | 64 kB        | 64 kB        | -             | -            | 64 kB        |       |
| Ext. FRAM                                                  | -                     | -            | -            | -            | 32 kB         | 32 kB        | -            |       |
| Interface                                                  | CAN                   | 7            | 4            | 4            | 3             | 7            | 7            | 3     |
| CAN1 is ISOBUS Compliance                                  | -                     | -            | -            | -            | x             | x            | x            |       |
| CAN bus termination                                        | 4                     | 4            | 4            | 3            | 4             | 4            | 3            |       |
| Ethernet                                                   | 1                     | -            | -            | -            | -             | -            | -            |       |
| 100BASE-T1 Ethernet                                        | -                     | -            | -            | -            | 1             | 1            | 1            |       |
| LIN                                                        | 1                     | -            | -            | 1            | 1             | 1            | -            |       |
| RS232                                                      | 1                     | -            | -            | -            | 1             | 1            | -            |       |
| Real time clock                                            | 1                     | -            | -            | -            | 1             | 1            | 1            |       |
| Outputs                                                    | High-Side PWM with CM | 36           | 28           | 18           | 16            | 36           | 36           | 10    |
| High-Side digital                                          | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| High-Side digital, PVG, VOUT                               | 8                     | -            | -            | 8            | 8             | 8            | 6            |       |
| Low-Side digital                                           | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| Inputs Analog input 3 modes (V)(I)(R)                      | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| Analog input 2 modes (V)(I)                                | 16                    | 16           | 16           | 16           | 16            | 16           | 16           |       |
| Analog input (V)                                           | -                     | 8            | -            | -            | -             | -            | -            |       |
| Timer input                                                | 12                    | 20           | 20           | 20           | 12            | 12           | 20           |       |
| Terminal 15                                                | 1                     | 1            | 1            | 1            | 1             | 1            | 1            |       |
| Wake-Up                                                    | 1                     | 1            | 1            | 1            | 1             | 1            | 1            |       |
| Sensor supply                                              | +5V/500mA             | 2            | 2            | 2            | 2             | 2            | 2            | 1     |
| +5-10V/2.5W                                                | 1                     | 1            | 1            | 1            | 1             | 1            | -            |       |
| Safety Switch Nr. of secondary shut-off path               | 3                     | 2            | 2            | 2            | 3             | 3            | 2            |       |
| Table 1: Variants overview for the Spartan-6 XA6SLX16 FPGA |                       |              |              |              |               |              |              |       |

| Feature                                      | HY-TTC 580            | HY-TTC 540   | HY-TTC 520   | HY-TTC 510   | HY-TTC 590E   | HY-TTC 590   | HY-TTC 508   |       |
|----------------------------------------------|-----------------------|--------------|--------------|--------------|---------------|--------------|--------------|-------|
| CPU                                          | 32-bit TI TMS570      | x            | x            | x            | x             | x            | x            | x     |
| Int. FLASH                                   | 3 MB                  | 3 MB         | 3 MB         | 3 MB         | 3 MB          | 3 MB         | 3 MB         |       |
| Int. RAM                                     | 256 kB                | 256 kB       | 256 kB       | 256 kB       | 256 kB        | 256 kB       | 256 kB       |       |
| Memory                                       | Ext. FLASH            | 8 MB         | -            | -            | -             | 64 MB        | 32 MB        | 16 MB |
| Ext. RAM                                     | 2 MB                  | 2 MB         | 2 MB         | 2 MB         | 2 MB          | 2 MB         | 2 MB         |       |
| Ext. EEPROM                                  | 64 kB                 | 64 kB        | 64 kB        | 64 kB        | -             | -            | 64 kB        |       |
| Ext. FRAM                                    | -                     | -            | -            | -            | 32 kB         | 32 kB        | -            |       |
| Interface                                    | CAN                   | 4            | 4            | 4            | 3             | 4            | 4            | 3     |
| CAN1 is ISOBUS Compliance                    | -                     | -            | -            | -            | x             | x            | x            |       |
| CAN bus termination                          | 4                     | 4            | 4            | 3            | 4             | 4            | 3            |       |
| Ethernet                                     | 1                     | -            | -            | -            | -             | -            | -            |       |
| 100BASE-T1 Ethernet                          | -                     | -            | -            | -            | 1             | 1            | 1            |       |
| LIN                                          | 1                     | -            | -            | 1            | 1             | 1            | -            |       |
| RS232                                        | 1                     | -            | -            | -            | 1             | 1            | -            |       |
| Real time clock                              | 1                     | -            | -            | -            | 1             | 1            | 1            |       |
| Outputs                                      | High-Side PWM with CM | 36           | 28           | 18           | 16            | 36           | 36           | 10    |
| High-Side digital                            | 16                    | 8            | 8            | 8            | 16            | 16           | 8            |       |
| High-Side digital, PVG, VOUT                 | 0                     | -            | -            | 8            | 0             | 0            | 6            |       |
| Low-Side digital                             | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| Inputs Analog input 3 modes (V)(I)(R)        | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| Analog input 2 modes (V)(I)                  | 16                    | 16           | 16           | 16           | 16            | 16           | 16           |       |
| Analog input (V)                             | -                     | 8            | -            | -            | -             | -            | -            |       |
| Timer input                                  | 12                    | 20           | 20           | 20           | 12            | 12           | 20           |       |
| Terminal 15                                  | 1                     | 1            | 1            | 1            | 1             | 1            | 1            |       |
| Wake-Up                                      | 1                     | 1            | 1            | 1            | 1             | 1            | 1            |       |
| Sensor supply                                | +5V/500mA             | 2            | 2            | 2            | 2             | 2            | 2            | 1     |
| +5-10V/2.5W                                  | 1                     | 1            | 1            | 1            | 1             | 1            | -            |       |
| Safety Switch Nr. of secondary shut-off path | 3                     | 2            | 2            | 2            | 3             | 3            | 2            |       |

Table 2: Variants overview for the Spartan-6 XA6SLX9 FPGA

| Feature                                      | HY-TTC 580            | HY-TTC 590E   | HY-TTC 590   |       |
|----------------------------------------------|-----------------------|---------------|--------------|-------|
| CPU                                          | 32-bit TI TMS570      | x             | x            | x     |
| Int. FLASH                                   | 3 MB                  | 3 MB          | 3 MB         |       |
| Int. RAM                                     | 256 kB                | 256 kB        | 256 kB       |       |
| Memory                                       | Ext. FLASH            | 8 MB          | 64 MB        | 32 MB |
| Ext. RAM                                     | 2 MB                  | 2 MB          | 2 MB         |       |
| Ext. EEPROM                                  | 64 kB                 | -             | -            |       |
| Ext. FRAM                                    | -                     | 32 kB         | 32 kB        |       |
| Interface                                    | CAN                   | 7             | 7            | 7     |
| CAN1 is ISOBUS Compliance                    | -                     | x             | x            |       |
| CAN bus termination                          | 7                     | 7             | 7            |       |
| Ethernet                                     | 1                     | -             | -            |       |
| 100BASE-T1 Ethernet                          | -                     | 1             | 1            |       |
| LIN                                          | 1                     | 1             | 1            |       |
| RS232                                        | 1                     | 1             | 1            |       |
| Real time clock                              | 1                     | 1             | 1            |       |
| Outputs                                      | High-Side PWM with CM | 36            | 36           | 36    |
| High-Side digital                            | 8                     | 8             | 8            |       |
| High-Side digital, PVG, VOUT                 | 8                     | 8             | 8            |       |
| Low-Side digital                             | 8                     | 8             | 8            |       |
| Inputs Analog input 3 modes (V)(I)(R)        | 8                     | 8             | 8            |       |
| Analog input 2 modes (V)(I)                  | 16                    | 16            | 16           |       |
| Analog input (V)                             | -                     | -             | -            |       |
| Timer input                                  | 12                    | 12            | 12           |       |
| Terminal 15                                  | 1                     | 1             | 1            |       |
| Wake-Up                                      | 1                     | 1             | 1            |       |
| Sensor supply                                | +5V/500mA             | 2             | 2            | 2     |
| +5-10V/2.5W                                  | 1                     | 1             | 1            |       |
| Safety Switch Nr. of secondary shut-off path | 3                     | 3             | 3            |       |

Table 3: Variants overview for the Spartan-6 XA6SLX25 FPGA

## 1.5.2 Hy-Ttc 580 Variant

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on the facing page.**

![18_image_0.png]( The image displays a diagram with various labels and numbers on it. It appears to be a technical drawing or a flowchart, possibly related to computer hardware or software. There are several arrows pointing towards different sections of the diagram, indicating connections between them.

In addition to the main diagram, there is an image of a cell phone in the top left corner of the page. The presence of this cell phone suggests that the diagram might be related to mobile technology or communication devices.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

| External EEPROM     | 64 kB More than 1,000,000 write cycles. More than 40-year data retention.                |
|---------------------|------------------------------------------------------------------------------------------|
| External Flash      | 8 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.   |
| Internal Flash      | 3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention. |
| Configuration Flash | 64 kB More than 100,000 write/erase cycles. More than 15-year data retention.            |
| External SRAM       | 2 MB                                                                                     |
| Internal SRAM       | 256 kB                                                                                   |

## Communication Interfaces

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

- 7 x CAN (50 to 1000 kbit/s)
- 1 x LIN (up to 20 kBd) - 1 x RS232 (up to 115 kBd) - 1 x Ethernet (10/100 Mbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

| 36 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input 8 PWM-controlled HS outputs can be alternatively used as frequency or pulse width measurement input                                                                                           |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x HS outputs                   | Digital output mode PVG output Voltage output (VOUT)                                      |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C 1                                                                                              |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

## 1.5.3 Hy-Ttc 540 Variant

![22_image_1.png]( The image displays a diagram with various settings and options for an electronic device. There are multiple arrows pointing to different sections of the diagram, indicating the connections between them. Some of these sections include "Digital Input," "Digital Output," "Analog Input," and "Analog Output."

In addition to the arrows, there are labels on the diagram that provide information about each section. The labels can be seen in various parts of the image, such as near the top left corner, bottom right corner, and other areas throughout the diagram. This detailed illustration helps users understand the workings and connections within the electronic device.)

![22_image_0.png]( The image displays a long list of numbers and letters on a computer screen. There are several rows of text displayed vertically, with each row containing multiple characters. The text appears to be organized into categories or sections, making it easier for the user to navigate through the content.) 

8 0–32 V

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage

## Memory

External EEPROM 64 kB

More than 1,000,000 write cycles. More than 40-year data retention.

Internal Flash 3 MB

Program Flash. More than 1000 write/erase cycles.

More than 15-year data retention.

Configuration Flash 64 kB

More than 100,000 write/erase cycles. More than 15-year data retention.

External SRAM 2 MB Internal SRAM 256 kB

Communication Interfaces
- 4 x CAN (50 to 1000 kbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection
- Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |
| 8 x timer input            | Frequency and pulse width measurement                                                                                                 |
| 8 x analog input           | 0 to 32 V                                                                                                                             |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

Outputs

| 28 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input                                                                             |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C                                                                                                |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

![26_image_0.png]( The image is a diagram that shows different settings and options for an ARM Cortex processor. There are several icons displayed on the chart, each representing various features of the processor. These icons are arranged in rows, with some placed vertically while others are horizontally aligned.

The diagram provides information about the processor's capabilities, such as its memory size and other technical specifications. The different settings can be used to optimize performance or customize the device according to user preferences.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage

## Memory

External EEPROM 64 kB

More than 1,000,000 write cycles. More than 40-year data retention.

Internal Flash 3 MB

Program Flash. More than 1000 write/erase cycles.

More than 15-year data retention.

Configuration Flash 64 kB

More than 100,000 write/erase cycles. More than 15-year data retention.

External SRAM 2 MB Internal SRAM 256 kB

Communication Interfaces
- 4 x CAN (50 to 1000 kbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection
- Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes                                                                                                                                                   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes                                                                                                                                                  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 8 x timer input                                                                                                                                                            | Frequency and pulse width measurement                                                                                                 |
| 6 x timer input                                                                                                                                                            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input                                                                                                                                                            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |
| All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold. |                                                                                                                                       |

## Outputs

| 18 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input                                                                             |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C                                                                                                |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

![30_image_1.png]( The image is a diagram or flowchart that provides information on how to use an ARM Cortex processor. It consists of several steps and options labeled with blue text, making it easy for users to understand the process.

There are multiple sections in the diagram, each with different labels and instructions. Some of these sections include "Digital In," "Digital Out," "Analog In," "Analog Out," "Sensor Supply," "LED Output," and "Can." The diagram also has a section labeled "Terminal 1" and another one labeled "Terminal 2."

The flowchart is organized in such a way that it guides users through the steps of using the ARM Cortex processor, making it a helpful resource for those who want to learn more about its operation.) 

![30_image_0.png]( The image displays a computer screen with various icons and text displayed on it. There are two main sections of icons, one located towards the left side of the screen and another towards the right side. A row of numbers can be seen at the bottom of the screen, possibly representing some sort of data or information.

In addition to these elements, there is a clock visible in the upper-right corner of the screen, which may indicate the current time. The overall layout suggests that this could be a computer program or application with multiple functionalities and features.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage

## Memory

| External EEPROM     | 64 kB More than 1,000,000 write cycles. More than 40-year data retention.                |
|---------------------|------------------------------------------------------------------------------------------|
| Internal Flash      | 3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention. |
| Configuration Flash | 64 kB More than 100,000 write/erase cycles. More than 15-year data retention.            |
| External SRAM       | 2 MB                                                                                     |
| Internal SRAM       | 256 kB                                                                                   |

## Communication Interfaces

- 3 x CAN (50 to 1000 kbit/s) - 1 x LIN (up to 20 kBd)

## Power Supply

- Supply voltage: 8 to 32 V - Separate supply pins for CPU subsystem and I/O subsystem
- Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software - Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 8 x timer input            | Frequency and pulse width measurement                                                                                                 |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

| 16 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input                                                                             |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x HS outputs                   | Digital output mode PVG output Voltage output (VOUT)                                      |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C                                                                                                |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

## 1.5.6 Hy-Ttc 590E Variant

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

![34_image_1.png]( The image is a close-up of a computer screen displaying various settings and options for an ARM processor. There are several blue buttons on the screen with different functions or instructions, including "Digital Input" and "Digital Output." Additionally, there are two rows of numbers visible in the image, likely representing data or settings related to the ARM processor. The overall layout suggests that this is a technical interface for managing and configuring an electronic device or system.) 

![34_image_0.png]( The image displays a diagram with several options and settings for a computer or electronic device. There are multiple icons arranged on the screen, each representing different functions or features. Some of these icons include "Can," "HSM," "HSM Out," "HSM In," and others.

The arrangement of the icons is organized in rows, with some placed vertically while others are horizontally aligned. The various options and settings make it clear that this diagram serves as a guide or reference for users to understand and utilize the device's functions effectively.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

| External FRAM       | 32 kB More than 10 trillion (1013) write cycles. More than 121-year data retention.      |
|---------------------|------------------------------------------------------------------------------------------|
| External Flash      | 64 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.  |
| Internal Flash      | 3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention. |
| Configuration Flash | 64 kB More than 100,000 write/erase cycles. More than 15-year data retention.            |
| External SRAM       | 2 MB                                                                                     |
| Internal SRAM       | 256 kB                                                                                   |

Communication Interfaces Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

- 7 x CAN (50 to 1000 kbit/s) (CAN1 is ISOBUS compliant)
- 1 x LIN (up to 20 kBd) - 1 x RS232 (up to 115 kBd)
- 1 x 100BASE-T1 BroadR-Reach® **(100 Mbit/s)**

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

| 36 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input 8 PWM-controlled HS outputs can be alternatively used as frequency or pulse width measurement input                                                                                           |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x HS outputs                   | Digital output mode PVG output Voltage output (VOUT)                                      |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C 1                                                                                              |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

## 1.5.7 Hy-Ttc 590 Variant

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

![38_image_0.png]( The image displays a diagram with multiple sections labeled and organized into categories. Each section contains information related to digital cameras, including details on memory cards, settings, and various other aspects of photography. There are several icons or images within each section that provide visual cues for the content being discussed.

The diagram is divided into different areas, such as "Memory Card," which includes options like "RAW" and "JPEG." Other sections include "Settings," where users can find information on camera settings, and "Digital Camera," which offers details about the device itself. The layout of the image allows for easy navigation and understanding of the content being presented.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

| External FRAM       | 32 kB More than 10 trillion (1013) write cycles. More than 121-year data retention.      |
|---------------------|------------------------------------------------------------------------------------------|
| External Flash      | 32 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.  |
| Internal Flash      | 3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention. |
| Configuration Flash | 64 kB More than 100,000 write/erase cycles. More than 15-year data retention.            |
| External SRAM       | 2 MB                                                                                     |
| Internal SRAM       | 256 kB                                                                                   |

Communication Interfaces Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

- 7 x CAN (50 to 1000 kbit/s) (CAN1 is ISOBUS compliant)
- 1 x LIN (up to 20 kBd) - 1 x RS232 (up to 115 kBd)
- 1 x 100BASE-T1 BroadR-Reach® **(100 Mbit/s)**

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

| 36 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input 8 PWM-controlled HS outputs can be alternatively used as frequency or pulse width measurement input                                                                                           |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x HS outputs                   | Digital output mode PVG output Voltage output (VOUT)                                      |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C 1                                                                                              |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

## 1.5.8 Hy-Ttc 508 Variant

![42_image_0.png]( The image displays a diagram with multiple rows of information, including details on digital audio and ARM Cortex. There are several options to choose from, such as digital input, digital output, and digital I/O. Additionally, there is an option for digital-to-analog conversion (DAC).

The diagram also features a section dedicated to the ARM Cortex, which includes information on its architecture and various components. There are several options within this section, such as memory, cache, and safety features. The diagram provides a clear visual representation of these concepts, making it easy for users to understand and navigate through the different options available.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

| External EEPROM     | 64 kB More than 1,000,000 write cycles. More than 40-year data retention.                |
|---------------------|------------------------------------------------------------------------------------------|
| External Flash      | 16 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.  |
| Internal Flash      | 3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention. |
| Configuration Flash | 64 kB More than 100,000 write/erase cycles. More than 15-year data retention.            |
| External SRAM       | 2 MB                                                                                     |
| Internal SRAM       | 256 kB                                                                                   |

## Communication Interfaces

- 3 x CAN (50 to 1000 kbit/s) (CAN1 is ISOBUS compliant)
- 1 x 100BASE-T1 BroadR-Reach® **(100 Mbit/s)**

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |
| 8 x timer input            | Frequency and pulse width measurement                                                                                                 |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

| 10 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x HS outputs                   | Digital output mode PVG output Voltage output (VOUT)                                      |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C                                                                                                |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

## 1.6 Standards And Guidelines

The HY-TTC 500 was developed to comply with several international standards and guidelines. This section lists the relevant standards and guidelines and the **applied limits and severity levels.** Environmental Criteria - ISO 16750 Code:
CODE: ISO 16750 (B1 F
2**), L, G, D, Z, (IP6k7; IP6k9k)**

![46_image_0.png]( The image is a diagram that depicts various aspects of a chemical plant, including climate, temperature, and electrical requirements. There are several nodes on this tree-like structure, each representing different elements or processes within the plant.

The diagram includes labels for different categories such as "climate," "temperature," "electrical," "mechanical," "chemical," and "protection." Each category is represented by a node, which connects to other nodes in the network. The image provides an overview of the plant's operations and the interconnected systems that contribute to its functioning.)

Figure 8: ISO 16750-1:2006 [13], Figure 1 - Code allocation 1.6.1 Electrical Capability

| ISO 16750-2:2012 [22] ISO 7637-2:2011 [20]        | Electrical transient conduction along supply lines. Test pluse: 1: -600 V, 1 ms 2a: +50 V, 50 µs 2b: +20 V, 200 ms 3a: -200 V, 0.1 µs 3b: +200 V, 0.1 µs 4: 12 V system, -6V drop (6 V remaining voltage) 24 V system, -18 V drop (6 V remaining voltage) 5a: +174 V, 2 Ω, 350 ms   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISO 7637-3:2007 [14]                              | Electrical transient transmission along signal lines. Tested for 24 V parameters, severity I                                                                                                                                                                                        |
| 1.6.2 Mechanical Capability ISO 16750-3:2012 [23] | Free fall tests, 1 m high, 6 falls per side Random vibration, broad-band 3 axes, 32 h per axis 57.9 m/s2 -10 Hz to 2 kHz, temperature profile superimposed Shock, half-sine 3 axes, 60 shocks 500 m/s2 , 6 ms                                                                                                                                                                                                                                                                                     |
| 1.6.3 Climatic Capability ISO 16750-4:2012 [18]   | Humid Heat Cyclic, DIN EN 60068-2-30:2006-06 [3], DIN EN 60068-2-38:2009 [5] Damp Heat, DIN EN 60068-2-78:2014-02[9]                                                                                                                                                                |

Salt spray, DIN EN 60068-2-11:2000-02 [2], DIN EN 60068-2-38:1996-10 [5]

## 1.6.4 Chemical Capability

The list of applied chemical agents for tests according to IEC 16750-5:2010**[19] is given in Table** 4 on the current page.

| ID   | Chemical Agent                            | Application Method   |
|------|-------------------------------------------|----------------------|
| AA   | Diesel fuel                               | III. Wiping          |
| AB   | "Bio" diesel                              | III. Wiping          |
| AC   | Petrol/gasoline unleaded                  | III. Wiping          |
| AE   | Methanol                                  | III. Wiping          |
| BA   | Engine oil                                | II. Brushing         |
| BB   | Differential oil                          | II. Brushing         |
| BC   | Transmission fluid                        | II. Brushing         |
| BD   | Hydraulic fluid                           | II. Brushing         |
| CA   | Battery fluid                             | III. Wiping          |
| CB   | Brake fluid                               | III. Wiping          |
| CC   | Antifreeze fluid                          | III. Wiping          |
| CE   | Cavity prodection                         | III. Wiping          |
| CF   | Protective lacquer                        | II. Brushing         |
| CG   | Protective lacquer remover                | III. Wiping          |
| DA   | Windscreen washer fluid                   | II. Brushing         |
| DB   | Vehicle washing chemicals                 | II. Brushing         |
| DC   | Interior cleaner                          | III. Wiping          |
| DD   | Glass cleaner                             | III. Wiping          |
| DE   | Wheel cleaner                             | II. Brushing         |
| DF   | Cold cleaning agent                       | II. Brushing         |
| DK   | Denatured alcohol                         | III. Wiping          |
| ED   | Refreshment containing caffeine and sugar | III. Wiping          |
| YYA  | Gasoline with 15% methanol                | III. Wiping          |
| YYB  | FAM test fuel                             | III. Wiping          |

Table 4: List of chemical agents

## 1.6.5 Ingress Protection Capability

ISO 20653:2013 [17] IP6k7 and IP6k9k

## 1.6.6 Esd And Emc Capability For Road Vehicles

| UNECE 10.4                   | Uniform provisions concerning the approval of vehicles with regard to EMC                                                                       |
|------------------------------|-----------------------------------------------------------------------|
| DIN EN 13309:2010-12 (E) [4] | Construction machinery - Electromagnetic compatibility of machines with internal power supply                                                                       |
| ISO 14982:1998 [11]          | Agricultural and forestry machinery - Electromagnetic compatibility - Test methods and acceptance criteria                                                                       |
| ISO 11452-2:2004 [12]        | 100 V/m, 20 MHz to 3 GHz                                              |
| CISPR 25 ED. 3.0 B:2008 [1]  | Conducted emissions, Class 3                                          |
| ISO 10605:2008 [15]          | ESD powered and unpowered ±6 kV contact discharge ±8 kV air discharge |
| 1.6.7 ESD and EMC Capability for Industrial Applications IEC 61000-6-2:2005 [6] Immunity for industrial environments. Conformance to surge immunity is only given if signal line wire length is less than 30 m. IEC 61000-6-4:2007 [7] Radiated emission for industry 1.6.8 Functional Safety ISO 13849:2015 [16] Safety of machinery - Safety-related parts of control systems IEC 61508:2010 [8] Functional safety of electrical/electronic/programmable electronic safety-related systems (E/E/PE, or E/E/PES), Safety Integrity Level 2 (SIL 2) ISO 25119:2018 [25] Tractors and machinery for agriculture and forestry - Safety-related parts of control systems ISO 26262:2018 [26] Road vehicles - Functional safety                              |                                                                       |

## 1.7 Instructions For Safe Operation

For safe operation of the HY-TTC 500 family ECUs, the following rules have to be obeyed:

## 1.7.1 General

- The HY-TTC 500 System Manual is written for a specific product version, for example 02.00.

Make sure this document corresponds with the product version of the ECU. The *Product* Version **on the title page of this document must match the** *Version* **on the label of the ECU.**
The following figure shows an example of an ECU label:

![50_image_0.png]( The image features a close-up of a white paper with black writing on it. It appears to be an instruction manual or a technical document related to TC Control. There are several numbers and letters scattered across the page, indicating that this is likely a detailed guide or reference material for users.

The text is organized in a way that makes it easy to read and understand. The paper seems to provide essential information about the product or service being discussed, which could be helpful for those who need guidance on how to use TC Control effectively.)

Figure 9: ECU label with Version field
- Please check regularly if there are updated documents (System Manual, Release Notes, . . . )
for your specific product version on the https://www.ttcontrol.com/service-area/ website.

- Carefully read the instructions and specifications listed **in this document before operating the**
ECU.

- The ECU has to be operated by using the type of connectors specified in section section 3.2 on page 43.

- It is not allowed to use any other connector or cable harness **than one of the specified ones.** - It is not allowed to operate the ECU in an environment that violates the specified operational range.

- The ECU has to be operated by skilled personnel only.

- When operating the ECU in an environment close to humans, it **has to be considered that the**
ECU contain power electronics and therefore the housing can **have high temperatures.**
- It is not allowed to open a sealed ECU.

- It is not allowed to operate an unsealed ECU outside the laboratory. - It is not allowed to operate a prototype ECU in a production environment (no matter if it is sealed or unsealed).

- Only skilled and trained personnel is allowed to operate a prototype ECU (no matter if it is sealed or unsealed).

- The ECU does not require maintenance activities by the user/system integrator. The only maintenance activity allowed for the user is exchanging the **ECU (for example after it has**
reached its specified lifetime).

## 1.7.2 Checks To Be Done Before Commissioning The Ecu

- Check the supply voltage before connecting the ECU. - Check the ECU connector and the cable harness to be free of defects. - Check the correct dimensioning of the wires in the cable harness. - Be sure that the ECU is mounted in a way that humans are not directly exposed to it and physical contact is avoided.

- Be sure to choose a mounting location for the ECU that eliminates the possibility of operation temperatures greater than the maximum temperature allowed **for the ECU (see MRD [27]).**
- The power supply of the ECU has to be secured with a fuse. The fuse trip current has to match to the maximum specified input current of the ECU and the cable harness. See Section 3.4 on page 48 **for more information.**

## 1.7.3 Intended Use

The HY-TTC 500 is a family of programmable general-purpose control units for safety-related sensor/actuator management to be used in mobile machinery for construction, agricultural, forestry and municipal applications.

Always operate the product within the electrical and environmental specifications and follow the handling and mounting instructions provided by TTControl GmbH. Usage of the product outside the specifications may result in **hazard to persons or property.**

## 1.7.4 Improper Use

Any use of the product other than as described in Section 1.7.3 **on this page (Intended use) is**
considered to be improper. Use in explosive areas is not permissible. TTControl GmbH is not liable for damages resulting from improper use.

## 2 Mounting And Label 2.1 Mounting Requirements

Any requirements for mounting, temperature and air flow conditions are defined in the Mounting Requirements Document (MRD) [27]. Furthermore, product dimensions and tolerances are defined in the Product Drawing [28].

## 2.2 Label Information

Any information about the label and its content is defined in the Product Drawing [28].

## 3 Pinning And Connector 3.1 Connector

Figure 10 **on the current page shows the main connector of HY-TTC 500 ECU, which has 154 pins** and divided into two segments.

![53_image_0.png]( The image features a close-up of two white, rectangular objects with many small holes on their surfaces. These objects could be described as either a pair of sinks or two pieces of machinery with intricate designs. They are placed side by side in the scene, creating an interesting visual contrast between them.) 

Note: **The main connector is numbered from 1 to 96 (left connector) and 1 to 58 (right connector).** This correspond to pins 101 to 196 and 201 to 258, respectively, in this System Manual.

## 3.2 Mating Connector

The listed part numbers can be ordered from HERTH+BUSS, KOSTAL or BOSCH with a minimum quantity of, for example, 100 pieces.

For lower quantities, TTControl GmbH provides complete kits with BOSCH connectors, crimp contacts and sealings.

| TTControl Order Numbers   | Description                                |
|---------------------------|--------------------------------------------|
| 10619                     | Connector kit for HY-TTC 500, 58-positions |
| 10620                     | Connector kit for HY-TTC 500, 96-positions |

![54_image_0.png]( The image displays a white background with various parts of an electronic device laid out on it. There are several pieces of equipment and tools placed around the area, including screws, wires, and other components. A few of these items can be seen in different positions across the scene, while others are more clustered together.

In addition to the main parts, there is a set of instructions or diagrams visible on the white background, likely providing guidance for assembling or disassembling the electronic device. The presence of these components and tools suggests that someone might be working on repairing or constructing an electronic device in this workspace.)

![54_image_1.png]( The image displays a variety of electronic components and parts laid out on a table or countertop. There are several car parts, including an engine and its parts, which appear to be in the process of being assembled or disassembled. In addition to these automotive items, there is also a cell phone present among the assortment of electronics. The components are arranged in different positions on the table, creating a diverse collection of parts for various projects or repairs.)

## 3.2.1 Kostal Mating Connector

Please follow the Process Specification below for the right handling of the KOSTAL mating connector:
Process Specification DOC00105005, Receptacle Housing 58-way and 96-way for control units

## 3.2.1.1 Mating Connector 96-Positions

| KOSTAL         | HERTH+BUSS   | Description                                    | Note   | Quantity   |
|----------------|--------------|------------------------------------------------|--------|------------|
| Part Number    | Part Number  |                                                |        |            |
| 9409601        | 50390395     | Plug housing                                   | 1      |            |
| 10400794061    | 50390397     | Holder                                         | 1      |            |
| 10400794071    | 50390398     | Secondary lock                                 | 1      |            |
| 22400794081    | 50390399     | Cover cap (cable exit on the left side)        | 1      |            |
| 22400172011    | 50390567     | Cover cap (cable exit on the upper right side) | 1      |            |
| 10800794051    | 50282066     | Sealing-/protection plug                       | 1      | 1          |
| (discontinued) |              |                                                |        |            |
| 10204225       | 50282099     | Sealing-/protection plug                       | 1      | 1          |

Table 5: KOSTAL / HERTH+BUSS part numbers Note **1 In order to achieve the specified IP rating each single wire must be populated**
either with a single-, blind- or a total protection-plug.

## 3.2.1.2 Mating Connector 58-Positions

| KOSTAL      | HERTH+BUSS   | Description                                     | Note   | Quantity   |
|-------------|--------------|-------------------------------------------------|--------|------------|
| Part Number | Part Number  |                                                 |        |            |
| 9405801     | 50390396     | Plug housing                                    | 1      |            |
| 10400758951 | 50390400     | Holder                                          | 1      |            |
| 10400758991 | 50390401     | Secondary lock                                  | 1      |            |
| 22400794001 | 50390402     | Cover cap (cable exit on the right side)        | 1      |            |
| 22400172001 | 50390449     | Cover cap (cable exit on the upper left side)   | 1      |            |
| 10800758941 | 50282065     | Sealing-/protection plug                        | 1      | 1          |
| -           | 50282062     | High power pin single sealing-/protection plug  | 1      | 6          |
| 10800472631 | 50282030     | High power pin single blind-sealing-/protection | 1      | -          |
| plug        |              |                                                 |        |            |

Table 6: KOSTAL / HERTH+BUSS part numbers Note **1 In order to achieve the specified IP rating each single wire must be populated**
either with a single-, blind- or a total protection-plug.

## 3.2.1.3 Crimp Contacts

| For I/O pins (148) KOSTAL Part Number      | HERTH+BUSS   | Note   | Description                                                         |
|--------------------------------------------|--------------|--------|---------------------------------------------------------------------|
| Part Number                                |              |        |                                                                     |
| 22140734080                                | 50253445     | 1      | KKS MLK 1.2 m, crimp contact tinned, wire size 0.75 mm2 to 1 mm2    |
| 32140734080                                | 50253445088  | 2      |                                                                     |
| 22140734070                                | 50253443     | 1      | KKS MLK 1.2 m, crimp contact tinned, wire size 0.5 mm2 to 0.75 mm2  |
| 32140734070                                | 50253443088  | 2      |                                                                     |
| 22140734060                                | 50253441     | 1      | KKS MLK 1.2 m, crimp contact tinned, wire size 0.35 mm2 to 0.5 mm2  |
| 32140734060                                | 50253441088  | 2      |                                                                     |
| 22140734050                                | 50253439     | 1      | KKS MLK 1.2 m, crimp contact tinned, wire size 0.1 mm2 to 0.25 mm2  |
| 32140734050                                | 50253439088  | 2      |                                                                     |
| For High Power pins (6) KOSTAL Part Number | HERTH+BUSS   | Note   | Description                                                         |
| Part Number                                |              |        |                                                                     |
| 22140499580                                | 50253230     | 1      | KKS SLK 2.8 ELA, crimp contact tinned, wire size 1mm2 to 2.5mm2     |
| 32140499580                                | 50253230088  | 2      |                                                                     |
| 22140499570                                | 50253229     | 1      | KKS SLK 2.8 ELA, crimp contact tinned, wire size 0.5mm2 to 0.75 mm2 |
| 32140499570                                | 50253229088  | 2      |                                                                     |
| Table 7: KOSTAL / HERTH+BUSS part numbers  |              |        |                                                                     |

Note **1 Loose crimp contact order code, minimum 50 pieces per packing unit.** Note 2 Strip (reel) crimp contact order code, minimum 4000 pieces **per packing unit.**

## 3.2.1.4 Tools

| KOSTAL      | HERTH+BUSS   | Description                            |
|-------------|--------------|----------------------------------------|
| Part Number | Part Number  |                                        |
| 80411002    | 95942166     | Crimping pliers without inserts        |
| 80411504    | 95942167     | Crimping pliers insert set for MLK 1,2 |
| 80411631    | 95942169     | Crimping pliers insert set for SLK 2,8 |
| 80495003    | 95945400     | Unlocking tool for MLK 1,2             |
| -           | 95945402     | Unlocking tool for SLK 2,8             |

Table 8: KOSTAL / HERTH+BUSS part numbers

## 3.2.2 Bosch Mating Connector

Please follow the assembly instruction and technical customer information below for the right handling of the BOSCH mating connector:
Assembly Instruction 1 928 A00 48M Technical Customer Information 1 928 A00 45T

## 3.2.2.1 Mating Connector 96-Positions

| BOSCH                     | Description                           | Quantity   |
|---------------------------|---------------------------------------|------------|
| Part Number 1 928 404 781 | Plug housing                          | 1          |
| 1 928 404 927             | Plug housing, 90-degree angled (alt.) | -          |
| 1 928 404 773             | Cover cap                             | 1          |
| 1 928 404 762             | Secondary lock                        | 1          |

Table 9: BOSCH part numbers

## 3.2.2.2 Mating Connector 58-Positions

| BOSCH                     | Description                                          | Note   | Quantity   |
|---------------------------|------------------------------------------------------|--------|------------|
| Part Number 1 928 404 916 | Plug housing                                         | 1      |            |
| 1 928 404 780             | Plug housing, 90-degree angled (alt.)                | -      |            |
| 1 928 404 917             | Cover cap                                            | 1      |            |
| 1 928 404 760             | Secondary lock                                       | 1      |            |
| 1 928 404 761             | Secondary lock                                       | 1      |            |
| 1 928 300 600             | High power pin single sealing-/protection plug       | 1      | 6          |
| 1 928 300 601             | High power pin single blind-sealing-/protection plug | 1      | -          |

Table 10: BOSCH part numbers Note **1 In order to achieve the specified IP rating each single wire must be populated**
either with a single protection-, blind protection-, or a total protection-plug.

## 3.2.2.3 Crimp Contacts

| For I/O pins (148) BOSCH Part Number                           | Description                                                       |
|----------------------------------------------------------------|-------------------------------------------------------------------|
| 1 928 498 679                                                  | Matrix 1.2 m, crimp contact tinned, wire size 0.35 mm2 to 0.5 mm2 |
| 1 928 498 137 (alt.) 1 928 498 680                             | Matrix 1.2 m, crimp contact tinned, wire size 0.75 mm2 to 1.0 mm2 |
| 1 928 498 138 (alt.) For High Power pins (6) BOSCH Part Number | Description                                                       |
| 1 928 498 057                                                  | BDK 2.8, crimp contact tinned, wire size 1.5mm2 to 2.5mm2         |
| Table 11: BOSCH crimp contacts part numbers                    |                                                                   |

3.2.2.4 Tools

| BOSCH                     | Description                                     |
|---------------------------|-------------------------------------------------|
| Part Number 1 928 498 161 | Crimping pliers / BDK / BSK 2,8 / 0,5 - 1 mm2   |
| 1 928 498 162             | Crimping pliers / BDK / BSK 2,8 / 1,5 - 2,5 mm2 |
| 1 928 498 212             | Crimping pliers / Matrix 1,2 / 0,35 - 0,5 mm2   |
| 1 928 498 213             | Crimping pliers / Matrix 1,2 / 0,75 - 1,0 mm2   |
| 1 928 498 167             | Unlocking tool for BDK / BSK 2,8                |
| 1 928 498 168             | Unlocking tool spare pin for BDK / BSK 2,8      |
| 1 928 498 218             | Unlocking tool for Matrix 1,2                   |
| 1 928 498 219             | Unlocking tool spare pin for Matrix 1,2         |

Table 12: BOSCH Tools part numbers

## 3.3 Cable Harness

| Description                                                                           | Variants                                       |
|---------------------------------------------------------------------------------------|------------------------------------------------|
| Cable Harness for HY-TTC 500, 3 m, open end                                           | HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510 |
| Cable Harness for HY-TTC 500 family, 1.5 m Cable Harness for HY-TTC 500, BRR, 3 m, OE | HY-TTC 590E, HY-TTC 590, HY-TTC 508            |
| Cable Harness for HY-TTC 500, BRR, 1.5 m                                              |                                                |

Note**: Make sure you use a cable harness fitting to the variant as listed in the table above. Usage of** improper cable harness may damage the device.

## 3.4 Fuse

For cable harness protection, it is recommended to protect each power supply path by a dedicated fuse. Please take note that the selected fuse type has to match to the current capability of the cable harness.

| Symbol   | Parameter                                           | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------------------------------|--------|--------|--------|--------|
| BAT+     | Fuse trip current of Positive Power Supply of Internal Electronics                                                     | 2      | A      |        |        |
| CPU BAT+ | Fuse trip current of Positive Power Supply of Power | 1      | 60     | A      |        |
| Power    | Stages                                              |        |        |        |        |

Note 1 The maximum fuse trip current is dependent on the specific customer application. The maximum total load current must be considered, see Section **4.1.3** on page 97

![59_image_0.png]( The image displays a diagram of an electronic system with various components and their connections. There are multiple power supplies and batteries visible within the system, along with other electrical components like a CPU, memory, and storage devices.

The diagram is organized in a way that highlights the relationships between different parts of the system. The main components are labeled, making it easier to understand their functions and connections. This type of diagram can be helpful for engineers or technicians when designing, troubleshooting, or maintaining electronic systems.)

![60_image_0.png]( The image features a blue and white logo for TC Control International. It is displayed prominently on a grey background, making it stand out. The design of the logo includes a combination of letters and numbers, creating an eye-catching visual representation of the company's name.)

## 3.5 Hy-Ttc 500 Family Pinning

The following subsections describe the HY-TTC 500 family variant dependent main- and the respective alternative functions on connector pin-level.

Each hardware function in the table, e.g. Pin 101 - **HS PWM Output, is referenced to its main-** (*IO_PWM_28***) and alternative (***IO_DO_44, IO_PWD_12, IO_DI_28***) function.** *IO_xx_yy* **represents** the software define for each function. For more information about API documentation, please refer to Chapter 8 on page **226.**
Please take note that the main function shall be used preferably and the technical specifications must particularly be regarded when alternative functions are to be used. See Chapter 4 **on page** 96 for limits and restrictions.

3.5.1 HY-TTC 580 **Variant**

![61_image_0.png]( The image displays a large blue table with various rows of data. There are multiple columns on the table, each containing different types of information. Some of these columns include "Sales," "Expenses," and "Profit."

In addition to the main table, there is another smaller table located towards the right side of the image. This second table also contains rows of data with columns such as "Costs" and "Revenue." The tables are filled with numerical data that provide insights into financial aspects of a business or organization.)

| HS Digital Output   | Timer Input                    | PVG Output   | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|--------------------------------|--------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function                  |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P101                | HS PWM Output                  | IO_DO_44     | IO_PWD_12     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_28           | IO_DI_28                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P102                | HS PWM Output                  | IO_DO_48     | IO_PWD_16     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_32           | IO_DI_32                       | IO_ADC_00    | IO_ADC_00     | IO_DI_48                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P103                | Analog Voltage Input IO_ADC_00 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P104                | Analog Voltage Input           | IO_ADC_02    | IO_ADC_02     | IO_DI_50                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_02           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P105                | Analog Voltage Input           | IO_ADC_04    | IO_ADC_04     | IO_DI_52                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_04           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P106                | Analog Voltage Input           | IO_ADC_06    | IO_ADC_06     | IO_DI_54                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_06           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P107                | Analog Voltage Input           | IO_ADC_08    | IO_DI_56      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_08           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P108                | Analog Voltage Input           | IO_ADC_10    | IO_DI_58      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_10           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P109                | Analog Voltage Input           | IO_ADC_12    | IO_DI_60      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_12           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P110                | Analog Voltage Input           | IO_ADC_14    | IO_DI_62      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_14           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P111                | Analog Voltage Input           | IO_ADC_16    | IO_DI_64      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_16           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P112                | Analog Voltage Input           | IO_ADC_18    | IO_DI_66      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_18           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P113                | Analog Voltage Input           | IO_ADC_20    | IO_DI_68      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_20           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P114                | Analog Voltage Input           | IO_ADC_22    | IO_DI_70      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_22           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P115                | Timer Input                    | IO_PWD_00    | IO_ADC_24     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_00           | IO_DI_36                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P116                | Timer Input                    | IO_PWD_02    | IO_ADC_26     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_02           | IO_DI_38                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P117                | Timer Input                    | IO_PWD_04    | IO_ADC_28     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_04           | IO_DI_40                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P118                | BAT                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P119                | BAT                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P120                | BAT                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P121                | BAT                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P122                | Timer Input                    | IO_ADC_30    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_06           | IO_DI_42                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P123                | Timer Input                    | IO_ADC_32    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_08           | IO_DI_44                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

| HS Digital Output   | Timer Input          | PVG Output   | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|----------------------|--------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function        |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P124                | Timer Input          | IO_ADC_34    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_10           | IO_DI_46             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P125                | HS PWM Output        | IO_DO_45     | IO_DI_29      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_29           | IO_PWD_13            |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P126                | HS PWM Output        | IO_DO_49     | IO_PWD_17     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_33           | IO_DI_33             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P127                | Analog Voltage Input | IO_ADC_01    | IO_ADC_01     | IO_DI_49                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_01           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P128                | Analog Voltage Input | IO_ADC_03    | IO_ADC_03     | IO_DI_51                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_03           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P129                | Analog Voltage Input | IO_ADC_05    | IO_ADC_05     | IO_DI_53                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_05           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P130                | Analog Voltage Input | IO_ADC_07    | IO_ADC_07     | IO_DI_55                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_07           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P131                | Analog Voltage Input | IO_ADC_09    | IO_DI_57      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_09           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P132                | Analog Voltage Input | IO_ADC_11    | IO_DI_59      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_11           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P133                | Analog Voltage Input | IO_ADC_13    | IO_DI_61      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_13           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P134                | Analog Voltage Input | IO_ADC_15    | IO_DI_63      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_15           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P135                | Analog Voltage Input | IO_ADC_17    | IO_DI_65      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_17           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P136                | Analog Voltage Input | IO_ADC_19    | IO_DI_67      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_19           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P137                | Analog Voltage Input | IO_ADC_21    | IO_DI_69      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_21           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P138                | Analog Voltage Input | IO_ADC_23    | IO_DI_71      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_23           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P139                | Timer Input          | IO_PWD_01    | IO_ADC_25     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_01           | IO_DI_37             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P140                | Timer Input          | IO_PWD_03    | IO_ADC_27     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_03           | IO_DI_39             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P141                | Timer Input          | IO_PWD_05    | IO_ADC_29     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_05           | IO_DI_41             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P142                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P143                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P144                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P145                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P146                | Timer Input          | IO_ADC_31    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_07           | IO_DI_43             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P147                | Timer Input          | IO_ADC_33    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_09           | IO_DI_45             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

Alternative *Function*

| Timer Input   | IO_ADC_35         |           |                      |
|---------------|-------------------|-----------|----------------------|
| IO_PWD_11     | IO_DI_47          |           |                      |
| P149          | HS Digital Output | IO_ADC_36 |                      |
| IO_DO_00      | IO_DI_72          |           |                      |
| P150          | HS PWM Output     | IO_DO_46  | IO_PWD_14            |
| IO_PWM_30     | IO_DI_30          |           |                      |
| P151          | HS PWM Output     | IO_DO_50  | IO_PWD_18            |
| IO_PWM_34     | IO_DI_34          |           |                      |
| P152          | HS Digital Output | IO_ADC_38 |                      |
| IO_DO_02      | IO_DI_74          |           |                      |
| P153          | HS PWM Output     | IO_DO_16  | IO_DI_00             |
| IO_PWM_00     |                   |           |                      |
| P154          | HS PWM Output     | IO_DO_30  | IO_DI_14             |
| IO_PWM_14     |                   |           |                      |
| P155          | HS Digital Output | IO_ADC_40 |                      |
| IO_DO_04      | IO_DI_76          |           |                      |
| P156          | HS PWM Output     | IO_DO_18  | IO_DI_02             |
| IO_PWM_02     |                   |           |                      |
| P157          | HS PWM Output     | IO_DO_32  | IO_DI_16             |
| IO_PWM_16     |                   |           |                      |
| P158          | HS Digital Output | IO_ADC_42 |                      |
| IO_DO_06      | IO_DI_78          |           |                      |
| P159          | HS PWM Output     | IO_DO_20  | IO_DI_04             |
| IO_PWM_04     |                   |           |                      |
| P160          | HS PWM Output     | IO_DO_34  | IO_DI_18             |
| IO_PWM_18     |                   |           |                      |
| P161          | HS Digital Output | IO_PVG_00 | IO_VOUT_00 IO_ADC_52 |
| IO_DO_52      | IO_DI_88          |           |                      |
| P162          | HS PWM Output     | IO_DO_23  | IO_DI_07             |
| IO_PWM_07     |                   |           |                      |
| P163          | HS PWM Output     | IO_DO_37  | IO_DI_21             |
| IO_PWM_21     |                   |           |                      |
| P164          | HS Digital Output | IO_PVG_03 | IO_VOUT_03 IO_ADC_55 |
| IO_DO_55      | IO_DI_91          |           |                      |
| P165          | HS PWM Output     | IO_DO_25  | IO_DI_09             |
| IO_PWM_09     |                   |           |                      |
| P166          | HS PWM Output     | IO_DO_39  | IO_DI_23             |
| IO_PWM_23     |                   |           |                      |
| P167          | HS Digital Output | IO_PVG_05 | IO_VOUT_05 IO_ADC_57 |
| IO_DO_57      | IO_DI_93          |           |                      |
| P168          | HS PWM Output     | IO_DO_27  | IO_DI_11             |
| IO_PWM_11     |                   |           |                      |
| P169          | HS PWM Output     | IO_DO_41  | IO_DI_25             |
| IO_PWM_25     |                   |           |                      |
| P170          | HS Digital Output | IO_PVG_07 | IO_VOUT_07 IO_ADC_59 |
| IO_DO_59      | IO_DI_95          |           |                      |

| Alternative       | Function          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
|-------------------|-------------------|------------|----------------------|--------------------------------|--------------------|-------------------------|-------------------------------|-------------------------------|-------------------------|------------------|-------------------------|----------------------------|------------------|
| HS Digital Output | Timer Input       | PVG Output | VOUT Output          | A/D Input (HS Output/PVG/VOUT) | Current Loop Input | A/D Input (Timer Input) | A/D Input (HS Digital Output) | A/D Input (LS Digital Output) | Analog Current Input 2M | Digital Input 2M | Analog Current Input 3M | Analog Resistance Input 3M | Digital Input 3M |
| Pin No.           | Main Function     |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P171              | HS PWM Output     | IO_DO_29   | IO_DI_13             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_13         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P172              | HS PWM Output     | IO_DO_43   | IO_DI_27             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_27         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P173              | HS Digital Output | IO_ADC_37  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_01          | IO_DI_73          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P174              | HS PWM Output     | IO_DO_47   | IO_PWD_15            |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_31         | IO_DI_31          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P175              | HS PWM Output     | IO_DO_51   | IO_PWD_19            |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_35         | IO_DI_35          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P176              | HS Digital Output | IO_ADC_39  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_03          | IO_DI_75          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P177              | HS PWM Output     | IO_DO_17   | IO_DI_01             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_01         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P178              | HS PWM Output     | IO_DO_31   | IO_DI_15             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_15         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P179              | HS Digital Output | IO_ADC_41  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_05          | IO_DI_77          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P180              | HS PWM Output     | IO_DO_19   | IO_DI_03             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_03         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P181              | HS PWM Output     | IO_DO_33   | IO_DI_17             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_17         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P182              | HS Digital Output | IO_ADC_43  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_07          | IO_DI_79          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P183              | HS PWM Output     | IO_DO_21   | IO_DI_05             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_05         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P184              | HS PWM Output     | IO_DO_35   | IO_DI_19             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_19         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P185              | HS Digital Output | IO_PVG_01  | IO_VOUT_01 IO_ADC_53 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_53          | IO_DI_89          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P186              | HS PWM Output     | IO_DO_22   | IO_DI_06             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_06         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P187              | HS PWM Output     | IO_DO_36   | IO_DI_20             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_20         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P188              | HS Digital Output | IO_PVG_02  | IO_VOUT_02 IO_ADC_54 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_54          | IO_DI_90          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P189              | HS PWM Output     | IO_DO_24   | IO_DI_08             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_08         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P190              | HS PWM Output     | IO_DO_38   | IO_DI_22             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_22         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P191              | HS Digital Output | IO_PVG_04  | IO_VOUT_04 IO_ADC_56 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_56          | IO_DI_92          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P192              | HS PWM Output     | IO_DO_26   | IO_DI_10             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_10         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P193              | HS PWM Output     | IO_DO_40   | IO_DI_24             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_24         |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |

| P197 P198 P199 P200 P201   | BAT+ Power                                |
|----------------------------|-------------------------------------------|
| P202                       | BAT+ Power                                |
| P203                       | BAT+ Power                                |
| P204                       | BAT+ Power                                |
| P205                       | BAT+ Power                                |
| P206                       | BAT+ Power                                |
| P207                       | Terminal 15 IO_ADC_K15                    |
| P208                       | LIN IO_LIN                                |
| P209                       | CAN 0 Low IO_CAN_CHANNEL_0                |
| P210                       | CAN 1 Low IO_CAN_CHANNEL_1                |
| P211                       | CAN 2 Low IO_CAN_CHANNEL_2                |
| P212                       | CAN 3 Low IO_CAN_CHANNEL_3                |
| P213                       | CAN 4 Low IO_CAN_CHANNEL_4                |
| P214                       | CAN 5 Low IO_CAN_CHANNEL_5                |
| P215                       | CAN 6 Low IO_CAN_CHANNEL_6                |
| P216                       | CAN Termination 3L                        |
| P217                       | Sensor GND                                |
| P218                       | Ethernet TD+ IO_DOWNLOAD, IO_UDP          |
| P219                       | Ethernet TDIO_DOWNLOAD, IO_UDP                                           |
| P220                       | Wake-Up IO_ADC_WAKE_UP                    |
| P221                       | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |

| P224     | CAN 2 High IO_CAN_CHANNEL_2              |           |
|----------|------------------------------------------|-----------|
| P225     | CAN 3 High IO_CAN_CHANNEL_3              |           |
| P226     | CAN 4 High IO_CAN_CHANNEL_4              |           |
| P227     | CAN 5 High IO_CAN_CHANNEL_5              |           |
| P228     | CAN 6 High IO_CAN_CHANNEL_6              |           |
| P229     | CAN Termination 3H                       |           |
| P230     | Sensor GND                               |           |
| P231     | Ethernet RDIO_DOWNLOAD                                          |           |
| P232     | Ethernet RD+ IO_DOWNLOAD                 |           |
| P233     | RTC_BACKUP_BAT                           |           |
| P234     | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 |           |
| P235     | CAN Termination 0L                       |           |
| P236     | CAN Termination 1L                       |           |
| P237     | CAN Termination 2L                       |           |
| P238     | LS Digital Output                        | IO_ADC_45 |
| IO_DO_09 | IO_DI_81                                 |           |
| P239     | LS Digital Output                        | IO_ADC_47 |
| IO_DO_11 | IO_DI_83                                 |           |
| P240     | LS Digital Output                        | IO_ADC_49 |
| IO_DO_13 | IO_DI_85                                 |           |
| P241     | LS Digital Output                        | IO_ADC_51 |
| IO_DO_15 | IO_DI_87                                 |           |
| P242     | RS232 TXD IO_UART                        |           |
| P243     | Sensor GND                               |           |
| P244     | Sensor GND                               |           |
| P245     | Sensor GND                               |           |
| P246     | BAT+ CPU IO_ADC_UBAT                     |           |
| P247     | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |           |
| P248     | CAN Termination 0H                       |           |
| P249     | CAN Termination 1H                       |           |

![66_image_2.png](1. A table with a row of numbers labeled "can high" and another row labeled "can low."
2. The number "3" is written on both rows, indicating that there are three sets of data to be compared.)

Alternative *Function*

![66_image_0.png]( The image is a white background with several text boxes placed on it. These text boxes contain different words and phrases, possibly related to technology or computer-related topics. Some of these phrases include "long time," "log file," "large file," "log in," and "login." There are also some numbers visible within the text boxes, which might be used for reference or data analysis purposes. The arrangement of the text boxes creates a visually interesting pattern on the white background.)

![66_image_1.png]( The image is a close-up of a gray background with a blue watermark on it. There are no visible objects or people in the scene.)

| CAN Termination 2H   |                   |           |
|----------------------|-------------------|-----------|
| P251                 | LS Digital Output | IO_ADC_44 |
| IO_DO_08             | IO_DI_80          |           |
| P252                 | LS Digital Output | IO_ADC_46 |
| IO_DO_10             | IO_DI_82          |           |
| P253                 | LS Digital Output | IO_ADC_48 |
| IO_DO_12             | IO_DI_84          |           |
| P254                 | LS Digital Output | IO_ADC_50 |
| IO_DO_14             | IO_DI_86          |           |
| P255                 | RS232 RXD IO_UART |           |
| P256                 | Sensor GND        |           |
| P257                 | Sensor GND        |           |
| P258                 | Sensor GND        |           |

![68_image_0.png]( The image displays a large graph with multiple sets of numbers arranged vertically and horizontally. There are several rows of numbers on both sides of the graph, creating an organized and visually appealing presentation. The graph appears to be a combination of a bar chart and a line graph, providing a clear representation of data or information.)

| HS Digital Output   | Timer Input          | PVG Output         | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|----------------------|--------------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function        |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P101                | HS PWM Output        | IO_PWD_12 IO_DI_28 |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P102                | HS PWM Output        | IO_PWD_16 IO_DI_32 |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P103                | Analog Voltage Input | IO_ADC_00          | IO_ADC_00     | IO_DI_48                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_00           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P104                | Analog Voltage Input | IO_ADC_02          | IO_ADC_02     | IO_DI_50                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_02           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P105                | Analog Voltage Input | IO_ADC_04          | IO_ADC_04     | IO_DI_52                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_04           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P106                | Analog Voltage Input | IO_ADC_06          | IO_ADC_06     | IO_DI_54                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_06           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P107                | Analog Voltage Input | IO_ADC_08          | IO_DI_56      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_08           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P108                | Analog Voltage Input | IO_ADC_10          | IO_DI_58      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_10           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P109                | Analog Voltage Input | IO_ADC_12          | IO_DI_60      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_12           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P110                | Analog Voltage Input | IO_ADC_14          | IO_DI_62      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_14           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P111                | Analog Voltage Input | IO_ADC_16          | IO_DI_64      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_16           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P112                | Analog Voltage Input | IO_ADC_18          | IO_DI_66      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_18           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P113                | Analog Voltage Input | IO_ADC_20          | IO_DI_68      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_20           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P114                | Analog Voltage Input | IO_ADC_22          | IO_DI_70      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_22           |                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P115                | Timer Input          | IO_PWD_00          | IO_ADC_24     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_00           | IO_DI_36             |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P116                | Timer Input          | IO_PWD_02          | IO_ADC_26     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_02           | IO_DI_38             |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P117                | Timer Input          | IO_PWD_04          | IO_ADC_28     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_04           | IO_DI_40             |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P118                | BAT                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P119                | BAT                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P120                | BAT                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P121                | BAT                      |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P122                | Timer Input          | IO_ADC_30          |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_06           | IO_DI_42             |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P123                | Timer Input          | IO_ADC_32          |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_08           | IO_DI_44             |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

| Timer Input   | IO_ADC_34             |                    |           |          |
|---------------|-----------------------|--------------------|-----------|----------|
| IO_PWD_10     | IO_DI_46              |                    |           |          |
| P125          | HS PWM Output         | IO_DI_29 IO_PWD_13 |           |          |
| P126          | HS PWM Output         | IO_PWD_17 IO_DI_33 |           |          |
| P127          | Analog Voltage Input  | IO_ADC_01          | IO_ADC_01 | IO_DI_49 |
| IO_ADC_01     |                       |                    |           |          |
| P128          | Analog Voltage Input  | IO_ADC_03          | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03     |                       |                    |           |          |
| P129          | Analog Voltage Input  | IO_ADC_05          | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05     |                       |                    |           |          |
| P130          | Analog Voltage Input  | IO_ADC_07          | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07     |                       |                    |           |          |
| P131          | Analog Voltage Input  | IO_ADC_09          | IO_DI_57  |          |
| IO_ADC_09     |                       |                    |           |          |
| P132          | Analog Voltage Input  | IO_ADC_11          | IO_DI_59  |          |
| IO_ADC_11     |                       |                    |           |          |
| P133          | Analog Voltage Input  | IO_ADC_13          | IO_DI_61  |          |
| IO_ADC_13     |                       |                    |           |          |
| P134          | Analog Voltage Input  | IO_ADC_15          | IO_DI_63  |          |
| IO_ADC_15     |                       |                    |           |          |
| P135          | Analog Voltage Input  | IO_ADC_17          | IO_DI_65  |          |
| IO_ADC_17     |                       |                    |           |          |
| P136          | Analog Voltage Input  | IO_ADC_19          | IO_DI_67  |          |
| IO_ADC_19     |                       |                    |           |          |
| P137          | Analog Voltage Input  | IO_ADC_21          | IO_DI_69  |          |
| IO_ADC_21     |                       |                    |           |          |
| P138          | Analog Voltage Input  | IO_ADC_23          | IO_DI_71  |          |
| IO_ADC_23     |                       |                    |           |          |
| P139          | Timer Input           | IO_PWD_01          | IO_ADC_25 |          |
| IO_PWD_01     | IO_DI_37              |                    |           |          |
| P140          | Timer Input           | IO_PWD_03          | IO_ADC_27 |          |
| IO_PWD_03     | IO_DI_39              |                    |           |          |
| IO_PWD_05     | IO_ADC_29             |                    |           |          |
| P141          | Timer Input IO_PWD_05 | IO_DI_41           |           |          |
| P142          | BAT                       |                    |           |          |
| P143          | BAT                       |                    |           |          |
| P144          | BAT                       |                    |           |          |
| P145          | BAT                       |                    |           |          |
| P146          | Timer Input           | IO_ADC_31          |           |          |
| IO_PWD_07     | IO_DI_43              |                    |           |          |
| P147          | Timer Input           | IO_ADC_33          |           |          |
| IO_PWD_09     | IO_DI_45              |                    |           |          |

| Timer Input        | IO_ADC_35         |                    |          |
|--------------------|-------------------|--------------------|----------|
| IO_PWD_11          | IO_DI_47          |                    |          |
| HS Digital Output  | IO_ADC_36         |                    |          |
| IO_DO_00           | IO_DI_72          |                    |          |
| IO_PWD_14 IO_DI_30 |                   |                    |          |
| P151               | HS PWM Output     | IO_PWD_18 IO_DI_34 |          |
| P152               | HS Digital Output | IO_ADC_38          |          |
| IO_DO_02           | IO_DI_74          |                    |          |
| P153               | HS PWM Output     | IO_DO_16           | IO_DI_00 |
| IO_PWM_00          |                   |                    |          |
| P154               | HS PWM Output     | IO_DO_30           | IO_DI_14 |
| IO_PWM_14          |                   |                    |          |
| P155               | HS Digital Output | IO_ADC_40          |          |
| IO_DO_04           | IO_DI_76          |                    |          |
| P156               | HS PWM Output     | IO_DO_18           | IO_DI_02 |
| IO_PWM_02          |                   |                    |          |
| P157               | HS PWM Output     | IO_DO_32           | IO_DI_16 |
| IO_PWM_16          |                   |                    |          |
| P158               | HS Digital Output | IO_ADC_42          |          |
| IO_DO_06           | IO_DI_78          |                    |          |
| P159               | HS PWM Output     | IO_DO_20           | IO_DI_04 |
| IO_PWM_04          |                   |                    |          |
| P160               | HS PWM Output     | IO_DO_34           | IO_DI_18 |
| IO_PWM_18          |                   |                    |          |
| P161               | HS Digital Output | IO_ADC_52 IO_DI_88 |          |
| P162               | HS PWM Output     | IO_DO_23           | IO_DI_07 |
| IO_PWM_07          |                   |                    |          |
| P163               | HS PWM Output     | IO_DO_37           | IO_DI_21 |
| IO_PWM_21          |                   |                    |          |
| P164               | HS Digital Output | IO_ADC_55 IO_DI_91 |          |
| P165               | HS PWM Output     | IO_DO_25           | IO_DI_09 |
| IO_PWM_09          |                   |                    |          |
| P166               | HS PWM Output     | IO_DO_39           | IO_DI_23 |
| IO_PWM_23          |                   |                    |          |
| P167               | HS Digital Output | IO_ADC_57 IO_DI_93 |          |
| P168               | HS PWM Output     | IO_DO_27           | IO_DI_11 |
| IO_PWM_11          |                   |                    |          |
| P169               | HS PWM Output     | IO_DO_41           | IO_DI_25 |
| IO_PWM_25          |                   |                    |          |
| P170               | HS Digital Output | IO_ADC_59 IO_DI_95 |          |

| P171      | HS PWM Output     | IO_DO_29           | IO_DI_13   |
|-----------|-------------------|--------------------|------------|
| IO_PWM_13 |                   |                    |            |
| P172      | HS PWM Output     | IO_DO_43           | IO_DI_27   |
| IO_PWM_27 |                   |                    |            |
| P173      | HS Digital Output | IO_ADC_37          |            |
| IO_DO_01  | IO_DI_73          |                    |            |
| P174      | HS PWM Output     | IO_PWD_15 IO_DI_31 |            |
| P175      | HS PWM Output     | IO_PWD_19 IO_DI_35 |            |
| P176      | HS Digital Output | IO_ADC_39          |            |
| IO_DO_03  | IO_DI_75          |                    |            |
| P177      | HS PWM Output     | IO_DO_17           | IO_DI_01   |
| IO_PWM_01 |                   |                    |            |
| P178      | HS PWM Output     | IO_DO_31           | IO_DI_15   |
| IO_PWM_15 |                   |                    |            |
| P179      | HS Digital Output | IO_ADC_41          |            |
| IO_DO_05  | IO_DI_77          |                    |            |
| P180      | HS PWM Output     | IO_DO_19           | IO_DI_03   |
| IO_PWM_03 |                   |                    |            |
| P181      | HS PWM Output     | IO_DO_33           | IO_DI_17   |
| IO_PWM_17 |                   |                    |            |
| P182      | HS Digital Output | IO_ADC_43          |            |
| IO_DO_07  | IO_DI_79          |                    |            |
| P183      | HS PWM Output     | IO_DO_21           | IO_DI_05   |
| IO_PWM_05 |                   |                    |            |
| P184      | HS PWM Output     | IO_DO_35           | IO_DI_19   |
| IO_PWM_19 |                   |                    |            |
| P185      | HS Digital Output | IO_ADC_53 IO_DI_89 |            |
| P186      | HS PWM Output     | IO_DO_22           | IO_DI_06   |
| IO_PWM_06 |                   |                    |            |
| P187      | HS PWM Output     | IO_DO_36           | IO_DI_20   |
| IO_PWM_20 |                   |                    |            |
| P188      | HS Digital Output | IO_ADC_54 IO_DI_90 |            |
| P189      | HS PWM Output     | IO_DO_24           | IO_DI_08   |
| IO_PWM_08 |                   |                    |            |
| P190      | HS PWM Output     | IO_DO_38           | IO_DI_22   |
| IO_PWM_22 |                   |                    |            |
| P191      | HS Digital Output | IO_ADC_56 IO_DI_92 |            |
| P192      | HS PWM Output     | IO_DO_26           | IO_DI_10   |
| IO_PWM_10 |                   |                    |            |
| P193      | HS PWM Output     | IO_DO_40           | IO_DI_24   |
| IO_PWM_24 |                   |                    |            |

HS Digital Output **IO_ADC_58**

IO_DI_94

HS PWM **Output**

IO_PWM_12

IO_DO_28 **IO_DI_12**

| IO_DO_42                 | IO_DI_26                                  |
|--------------------------|-------------------------------------------|
| IO_PWM_26                |                                           |
| P197 P198 P199 P200 P201 | BAT+ Power                                |
| P202                     | BAT+ Power                                |
| P203                     | BAT+ Power                                |
| P204                     | BAT+ Power                                |
| P205                     | BAT+ Power                                |
| P206                     | BAT+ Power                                |
| P207                     | Terminal 15 IO_ADC_K15                    |
| P208 P209                | CAN 0 Low IO_CAN_CHANNEL_0                |
| P210                     | CAN 1 Low IO_CAN_CHANNEL_1                |
| P211                     | CAN 2 Low IO_CAN_CHANNEL_2                |
| P212                     | CAN 3 Low IO_CAN_CHANNEL_3                |
| P213 P214 P215 P216      | CAN Termination 3L                        |
| P217                     | Sensor GND                                |
| P218 P219 P220           | Wake-Up IO_ADC_WAKE_UP                    |
| P221                     | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |
| P222                     | CAN 0 High IO_CAN_CHANNEL_0               |
| P223                     | CAN 1 High IO_CAN_CHANNEL_1               |
| P224                     | CAN 2 High IO_CAN_CHANNEL_2               |

| P226 P227 P228 P229   | CAN Termination 3H                       |           |
|-----------------------|------------------------------------------|-----------|
| P230                  | Sensor GND                               |           |
| P231 P232 P233 P234   | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 |           |
| P235                  | CAN Termination 0L                       |           |
| P236                  | CAN Termination 1L                       |           |
| P237                  | CAN Termination 2L                       |           |
| P238                  | LS Digital Output                        | IO_ADC_45 |
| IO_DO_09              | IO_DI_81                                 |           |
| P239                  | LS Digital Output                        | IO_ADC_47 |
| IO_DO_11              | IO_DI_83                                 |           |
| P240                  | LS Digital Output                        | IO_ADC_49 |
| IO_DO_13              | IO_DI_85                                 |           |
| P241                  | LS Digital Output                        | IO_ADC_51 |
| IO_DO_15              | IO_DI_87                                 |           |
| P242 P243             | Sensor GND                               |           |
| P244                  | Sensor GND                               |           |
| P245                  | Sensor GND                               |           |
| P246                  | BAT+ CPU IO_ADC_UBAT                     |           |
| P247                  | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |           |
| P248                  | CAN Termination 0H                       |           |
| P249                  | CAN Termination 1H                       |           |
| P250                  | CAN Termination 2H                       |           |
| P251                  | LS Digital Output                        | IO_ADC_44 |
| IO_DO_08              | IO_DI_80                                 |           |
| P252                  | LS Digital Output                        | IO_ADC_46 |
| IO_DO_10              | IO_DI_82                                 |           |
| P253                  | LS Digital Output                        | IO_ADC_48 |
| IO_DO_12              | IO_DI_84                                 |           |
| P254                  | LS Digital Output                        | IO_ADC_50 |
| IO_DO_14              | IO_DI_86                                 |           |
| P255 P256             | Sensor GND                               |           |

Sensor GND

P258 Sensor GND

Table 14: Pinning of HY-TTC 540

| Alternative       | Function             |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
|-------------------|----------------------|--------------------|-------------|--------------------------------|--------------------|-------------------------|-------------------------------|-------------------------------|-------------------------|------------------|-------------------------|----------------------------|------------------|
| HS Digital Output | Timer Input          | PVG Output         | VOUT Output | A/D Input (HS Output/PVG/VOUT) | Current Loop Input | A/D Input (Timer Input) | A/D Input (HS Digital Output) | A/D Input (LS Digital Output) | Analog Current Input 2M | Digital Input 2M | Analog Current Input 3M | Analog Resistance Input 3M | Digital Input 3M |
| Pin No.           | Main Function        |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P101              | HS PWM Output        | IO_PWD_12 IO_DI_28 |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P102              | HS PWM Output        | IO_PWD_16 IO_DI_32 |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P103              | Analog Voltage Input | IO_ADC_00          | IO_ADC_00   | IO_DI_48                       |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_00         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P104              | Analog Voltage Input | IO_ADC_02          | IO_ADC_02   | IO_DI_50                       |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_02         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P105              | Analog Voltage Input | IO_ADC_04          | IO_ADC_04   | IO_DI_52                       |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_04         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P106              | Analog Voltage Input | IO_ADC_06          | IO_ADC_06   | IO_DI_54                       |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_06         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P107              | Analog Voltage Input | IO_ADC_08          | IO_DI_56    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_08         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P108              | Analog Voltage Input | IO_ADC_10          | IO_DI_58    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_10         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P109              | Analog Voltage Input | IO_ADC_12          | IO_DI_60    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_12         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P110              | Analog Voltage Input | IO_ADC_14          | IO_DI_62    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_14         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P111              | Analog Voltage Input | IO_ADC_16          | IO_DI_64    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_16         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P112              | Analog Voltage Input | IO_ADC_18          | IO_DI_66    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_18         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P113              | Analog Voltage Input | IO_ADC_20          | IO_DI_68    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_20         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P114              | Analog Voltage Input | IO_ADC_22          | IO_DI_70    |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_ADC_22         |                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P115              | Timer Input          | IO_PWD_00          | IO_ADC_24   |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_00         | IO_DI_36             |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P116              | Timer Input          | IO_PWD_02          | IO_ADC_26   |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_02         | IO_DI_38             |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P117              | Timer Input          | IO_PWD_04          | IO_ADC_28   |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_04         | IO_DI_40             |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P118              | BAT                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P119              | BAT                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P120              | BAT                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P121              | BAT                      |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P122              | Timer Input          | IO_ADC_30          |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_06         | IO_DI_42             |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P123              | Timer Input          | IO_ADC_32          |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_08         | IO_DI_44             |                    |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |

3.5.3 HY-TTC 520 Variant (Customer-specific variant **only)**

| Timer Input   | IO_ADC_34                             |           |           |          |
|---------------|---------------------------------------|-----------|-----------|----------|
| IO_PWD_10     | IO_DI_46                              |           |           |          |
| HS PWM Output | IO_DI_29 IO_PWD_13 IO_PWD_17 IO_DI_33 |           |           |          |
| P127          | Analog Voltage Input                  | IO_ADC_01 | IO_ADC_01 | IO_DI_49 |
| IO_ADC_01     |                                       |           |           |          |
| P128          | Analog Voltage Input                  | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03     |                                       |           |           |          |
| P129          | Analog Voltage Input                  | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05     |                                       |           |           |          |
| P130          | Analog Voltage Input                  | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07     |                                       |           |           |          |
| P131          | Analog Voltage Input                  | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09     |                                       |           |           |          |
| P132          | Analog Voltage Input                  | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11     |                                       |           |           |          |
| P133          | Analog Voltage Input                  | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13     |                                       |           |           |          |
| P134          | Analog Voltage Input                  | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15     |                                       |           |           |          |
| P135          | Analog Voltage Input                  | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17     |                                       |           |           |          |
| P136          | Analog Voltage Input                  | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19     |                                       |           |           |          |
| P137          | Analog Voltage Input                  | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21     |                                       |           |           |          |
| P138          | Analog Voltage Input                  | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23     |                                       |           |           |          |
| P139          | Timer Input                           | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01     | IO_DI_37                              |           |           |          |
| P140          | Timer Input                           | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03     | IO_DI_39                              |           |           |          |
| P141          | Timer Input                           | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05     | IO_DI_41                              |           |           |          |
| P142          | BAT                                       |           |           |          |
| P143          | BAT                                       |           |           |          |
| P144          | BAT                                       |           |           |          |
| P145          | BAT                                       |           |           |          |
| P146          | Timer Input                           | IO_ADC_31 |           |          |
| IO_PWD_07     | IO_DI_43                              |           |           |          |
| P147          | Timer Input                           | IO_ADC_33 |           |          |
| IO_PWD_09     | IO_DI_45                              |           |           |          |

| P148                                    | Timer Input       | IO_ADC_35          |          |
|-----------------------------------------|-------------------|--------------------|----------|
| IO_PWD_11                               | IO_DI_47          |                    |          |
| P149                                    | HS Digital Output | IO_ADC_36          |          |
| IO_DO_00                                | IO_DI_72          |                    |          |
| P150                                    | HS PWM Output     | IO_PWD_14 IO_DI_30 |          |
| P151                                    | HS PWM Output     | IO_PWD_18 IO_DI_34 |          |
| P152                                    | HS Digital Output | IO_ADC_38          |          |
| IO_DO_02                                | IO_DI_74          |                    |          |
| P153                                    | HS PWM Output     | IO_DO_16           | IO_DI_00 |
| IO_PWM_00                               |                   |                    |          |
| P154                                    | HS PWM Output     | IO_DO_30           | IO_DI_14 |
| IO_PWM_14                               |                   |                    |          |
| P155                                    | HS Digital Output | IO_ADC_40          |          |
| IO_DO_04                                | IO_DI_76          |                    |          |
| P156                                    | HS PWM Output     | IO_DO_18           | IO_DI_02 |
| IO_PWM_02                               |                   |                    |          |
| P157                                    | HS PWM Output     | IO_DO_32           | IO_DI_16 |
| IO_PWM_16                               |                   |                    |          |
| P158                                    | HS Digital Output | IO_ADC_42          |          |
| IO_DO_06                                | IO_DI_78          |                    |          |
| P159                                    | HS PWM Output     | IO_DO_20           | IO_DI_04 |
| IO_PWM_04                               |                   |                    |          |
| P160                                    | HS PWM Output     | IO_DO_34           | IO_DI_18 |
| IO_PWM_18                               |                   |                    |          |
| P161 P162                               | HS PWM Output     | IO_DO_23           | IO_DI_07 |
| IO_PWM_07                               |                   |                    |          |
| P163                                    | HS PWM Output     | IO_DO_37           | IO_DI_21 |
| IO_PWM_21                               |                   |                    |          |
| P164 P165                               | HS PWM Output     | IO_DO_25           | IO_DI_09 |
| IO_PWM_09                               |                   |                    |          |
| P166 P167 P168 P169 P170 P171 P172 P173 | HS Digital Output | IO_ADC_37          |          |
| IO_DO_01                                | IO_DI_73          |                    |          |
| P174                                    | HS PWM Output     | IO_PWD_15 IO_DI_31 |          |

| HS PWM Output                                               | IO_PWD_19 IO_DI_35   |           |          |
|-------------------------------------------------------------|----------------------|-----------|----------|
| HS Digital Output                                           | IO_ADC_39            |           |          |
| IO_DO_03                                                    | IO_DI_75             |           |          |
| IO_DO_17                                                    | IO_DI_01             |           |          |
| IO_PWM_01                                                   |                      |           |          |
| P178                                                        | HS PWM Output        | IO_DO_31  | IO_DI_15 |
| IO_PWM_15                                                   |                      |           |          |
| P179                                                        | HS Digital Output    | IO_ADC_41 |          |
| IO_DO_05                                                    | IO_DI_77             |           |          |
| P180                                                        | HS PWM Output        | IO_DO_19  | IO_DI_03 |
| IO_PWM_03                                                   |                      |           |          |
| P181                                                        | HS PWM Output        | IO_DO_33  | IO_DI_17 |
| IO_PWM_17                                                   |                      |           |          |
| P182                                                        | HS Digital Output    | IO_ADC_43 |          |
| IO_DO_07                                                    | IO_DI_79             |           |          |
| P183                                                        | HS PWM Output        | IO_DO_21  | IO_DI_05 |
| IO_PWM_05                                                   |                      |           |          |
| P184                                                        | HS PWM Output        | IO_DO_35  | IO_DI_19 |
| IO_PWM_19                                                   |                      |           |          |
| P185 P186                                                   | HS PWM Output        | IO_DO_22  | IO_DI_06 |
| IO_PWM_06                                                   |                      |           |          |
| P187                                                        | HS PWM Output        | IO_DO_36  | IO_DI_20 |
| IO_PWM_20                                                   |                      |           |          |
| P188 P189                                                   | HS PWM Output        | IO_DO_24  | IO_DI_08 |
| IO_PWM_08                                                   |                      |           |          |
| P190 P191 P192 P193 P194 P195 P196 P197 P198 P199 P200 P201 | BAT+ Power           |           |          |
| P202                                                        | BAT+ Power           |           |          |
| P203                                                        | BAT+ Power           |           |          |
| P204                                                        | BAT+ Power           |           |          |
| P205                                                        | BAT+ Power           |           |          |

| P207                | Terminal 15 IO_ADC_K15                    |
|---------------------|-------------------------------------------|
| P208 P209           | CAN 0 Low IO_CAN_CHANNEL_0                |
| P210                | CAN 1 Low IO_CAN_CHANNEL_1                |
| P211                | CAN 2 Low IO_CAN_CHANNEL_2                |
| P212                | CAN 3 Low IO_CAN_CHANNEL_3                |
| P213 P214 P215 P216 | CAN Termination 3L                        |
| P217                | Sensor GND                                |
| P218 P219 P220      | Wake-Up IO_ADC_WAKE_UP                    |
| P221                | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |
| P222                | CAN 0 High IO_CAN_CHANNEL_0               |
| P223                | CAN 1 High IO_CAN_CHANNEL_1               |
| P224                | CAN 2 High IO_CAN_CHANNEL_2               |
| P225                | CAN 3 High IO_CAN_CHANNEL_3               |
| P226 P227 P228 P229 | CAN Termination 3H                        |
| P230                | Sensor GND                                |
| P231 P232 P233 P234 | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1  |
| P235                | CAN Termination 0L                        |
| P236                | CAN Termination 1L                        |
| P237                | CAN Termination 2L                        |

| LS Digital Output   | IO_ADC_45                                |                                 |
|---------------------|------------------------------------------|---------------------------------|
| IO_DO_09            | IO_DI_81                                 |                                 |
| LS Digital Output   | IO_ADC_47                                |                                 |
| IO_DO_11            | IO_DI_83                                 |                                 |
| LS Digital Output   | IO_ADC_49                                |                                 |
| IO_DO_13            | IO_DI_85                                 |                                 |
| LS Digital Output   | IO_ADC_51                                |                                 |
| IO_DO_15            | IO_DI_87                                 |                                 |
| P243                | Sensor GND                               |                                 |
| P244                | Sensor GND                               |                                 |
| P245                | Sensor GND                               |                                 |
| P246                | BAT+ CPU IO_ADC_UBAT                     |                                 |
| P247                | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |                                 |
| P248                | CAN Termination 0H                       |                                 |
| P249                | CAN Termination 1H                       |                                 |
| P250                | CAN Termination 2H LS Digital Output     | IO_ADC_44                       |
| IO_DO_08            | IO_DI_80                                 |                                 |
| LS Digital Output   | IO_ADC_46                                |                                 |
| IO_DO_10            | IO_DI_82                                 |                                 |
| P253                | LS Digital Output                        | IO_ADC_48                       |
| IO_DO_12            | IO_DI_84                                 |                                 |
| P254                | LS Digital Output                        | IO_ADC_50                       |
| IO_DO_14            | IO_DI_86                                 |                                 |
| P255 P256           | Sensor GND                               |                                 |
| P257                | Sensor GND                               |                                 |
| P258                | Sensor GND                               | Table 15: Pinning of HY-TTC 520 |

## 3.5.4 Hy-Ttc 510 **Variant**

Alternative *Function*

![81_image_0.png]( The image is a close-up of a blue and white label with text on it. The label appears to be a watermark or logo for an organization. It seems to be a part of a larger background that includes some gray tones.)

![81_image_1.png]( The image is a close-up of a blue and white sign with text that reads "Blog Radar." The background features a grayscale color scheme, giving it an old or vintage appearance.)

![81_image_3.png]( The image is a close-up of a blue and white sign that reads "Input." It appears to be blurred or slightly distorted, giving it an artistic appearance. The word "input" stands out prominently on the sign, making it easy to read despite its slightly fuzzy nature.)

![81_image_4.png]( The image is a close-up of a textured surface with various words and phrases written on it. Some of these phrases include "a", "and", "the", "of", and "in". The writing appears to be in a foreign language or an unconventional script, making the content difficult to decipher without further context. The close-up view highlights the intricate details of the text on this unique surface.)

![81_image_5.png]( The image is a close-up of a blue and white text that reads "Blogging." The word "Blogging" appears to be written on a computer screen or some other digital display.)

![81_image_6.png]( The image features a blue circle with an arrow pointing towards it. This blue circle appears to be a logo or symbol that is prominently displayed on the screen. It seems like a unique and eye-catching design element within the scene.)

| IO_DI_32   | IO_ADC_00                      | IO_ADC_00   | IO_DI_48   |          |
|------------|--------------------------------|-------------|------------|----------|
| P103       | Analog Voltage Input IO_ADC_00 |             |            |          |
| P104       | Analog Voltage Input           | IO_ADC_02   | IO_ADC_02  | IO_DI_50 |
| IO_ADC_02  |                                |             |            |          |
| P105       | Analog Voltage Input           | IO_ADC_04   | IO_ADC_04  | IO_DI_52 |
| IO_ADC_04  |                                |             |            |          |
| P106       | Analog Voltage Input           | IO_ADC_06   | IO_ADC_06  | IO_DI_54 |
| IO_ADC_06  |                                |             |            |          |
| P107       | Analog Voltage Input           | IO_ADC_08   | IO_DI_56   |          |
| IO_ADC_08  |                                |             |            |          |
| P108       | Analog Voltage Input           | IO_ADC_10   | IO_DI_58   |          |
| IO_ADC_10  |                                |             |            |          |
| P109       | Analog Voltage Input           | IO_ADC_12   | IO_DI_60   |          |
| IO_ADC_12  |                                |             |            |          |
| P110       | Analog Voltage Input           | IO_ADC_14   | IO_DI_62   |          |
| IO_ADC_14  |                                |             |            |          |
| P111       | Analog Voltage Input           | IO_ADC_16   | IO_DI_64   |          |
| IO_ADC_16  |                                |             |            |          |
| P112       | Analog Voltage Input           | IO_ADC_18   | IO_DI_66   |          |
| IO_ADC_18  |                                |             |            |          |
| P113       | Analog Voltage Input           | IO_ADC_20   | IO_DI_68   |          |
| IO_ADC_20  |                                |             |            |          |
| P114       | Analog Voltage Input           | IO_ADC_22   | IO_DI_70   |          |
| IO_ADC_22  | IO_PWD_00                      | IO_ADC_24   |            |          |
| IO_PWD_00  | IO_DI_36                       |             |            |          |
| IO_PWD_02  | IO_ADC_26                      |             |            |          |
| IO_PWD_02  | IO_DI_38                       |             |            |          |
| IO_PWD_04  | IO_ADC_28                      |             |            |          |
| IO_PWD_04  | IO_DI_40 IO_ADC_30             |             |            |          |
| IO_PWD_06  | IO_DI_42 IO_ADC_32             |             |            |          |
| IO_PWD_08  | IO_DI_44                       |             |            |          |

![81_image_2.png]( The image displays a series of four graphs with different labels and data points. Each graph is arranged horizontally across the entire width of the image. The first graph has the label "Pgd12" on it, while the second one features "Pgd13". The third graph shows "Pgd14", and the fourth one displays "Pgd15". Each graph is accompanied by a bar chart that represents the data points.

The graphs are organized in such a way that they appear to be part of a larger dataset, possibly related to scientific research or data analysis. The presence of these graphs suggests that the image might have been taken from a presentation, report, or academic paper.)

| Timer Input                    | IO_ADC_34            |           |           |          |
|--------------------------------|----------------------|-----------|-----------|----------|
| IO_PWD_10                      | IO_DI_46             |           |           |          |
| HS PWM Output                  | IO_DI_29 IO_PWD_13   |           |           |          |
| HS PWM Output                  | IO_PWD_17 IO_DI_33   |           |           |          |
| Analog Voltage Input           | IO_ADC_01            | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01 Analog Voltage Input | IO_ADC_03            | IO_ADC_03 | IO_DI_51  |          |
| IO_ADC_03                      |                      |           |           |          |
| P129                           | Analog Voltage Input | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05                      |                      |           |           |          |
| P130                           | Analog Voltage Input | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07                      |                      |           |           |          |
| P131                           | Analog Voltage Input | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09                      |                      |           |           |          |
| P132                           | Analog Voltage Input | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11                      |                      |           |           |          |
| P133                           | Analog Voltage Input | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13                      |                      |           |           |          |
| P134                           | Analog Voltage Input | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15                      |                      |           |           |          |
| P135                           | Analog Voltage Input | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17                      |                      |           |           |          |
| P136                           | Analog Voltage Input | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19                      |                      |           |           |          |
| P137                           | Analog Voltage Input | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21                      |                      |           |           |          |
| P138                           | Analog Voltage Input | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23                      |                      |           |           |          |
| P139                           | Timer Input          | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01                      | IO_DI_37             |           |           |          |
| P140                           | Timer Input          | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03                      | IO_DI_39             |           |           |          |
| P141                           | Timer Input          | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05                      | IO_DI_41             |           |           |          |
| P142                           | BAT                      |           |           |          |
| P143                           | BAT                      |           |           |          |
| P144                           | BAT                      |           |           |          |
| P145                           | BAT                      |           |           |          |
| P146                           | Timer Input          | IO_ADC_31 |           |          |
| IO_PWD_07                      | IO_DI_43             |           |           |          |
| P147                           | Timer Input          | IO_ADC_33 |           |          |
| IO_PWD_09                      | IO_DI_45             |           |           |          |

| Alternative                 | Function          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
|-----------------------------|-------------------|--------------------|----------------------|--------------------------------|--------------------|-------------------------|-------------------------------|-------------------------------|-------------------------|------------------|-------------------------|----------------------------|------------------|
| HS Digital Output           | Timer Input       | PVG Output         | VOUT Output          | A/D Input (HS Output/PVG/VOUT) | Current Loop Input | A/D Input (Timer Input) | A/D Input (HS Digital Output) | A/D Input (LS Digital Output) | Analog Current Input 2M | Digital Input 2M | Analog Current Input 3M | Analog Resistance Input 3M | Digital Input 3M |
| Pin No.                     | Main Function     |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P148                        | Timer Input       | IO_ADC_35          |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_11                   | IO_DI_47          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P149                        | HS Digital Output | IO_ADC_36          |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_00                    | IO_DI_72          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P150                        | HS PWM Output     | IO_PWD_14 IO_DI_30 |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P151                        | HS PWM Output     | IO_PWD_18 IO_DI_34 |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P152                        | HS Digital Output | IO_ADC_38          |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_02                    | IO_DI_74          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P153                        | HS PWM Output     | IO_DO_16           | IO_DI_00             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_00                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P154                        | HS PWM Output     | IO_DO_30           | IO_DI_14             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_14                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P155                        | HS Digital Output | IO_ADC_40          |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_04                    | IO_DI_76          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P156                        | HS PWM Output     | IO_DO_18           | IO_DI_02             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_02 HS PWM Output     | IO_DO_32          | IO_DI_16           |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_16 HS Digital Output | IO_ADC_42         |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_06                    | IO_DI_78          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P159                        | HS PWM Output     | IO_DO_20           | IO_DI_04             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_04                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P160                        | HS PWM Output     | IO_DO_34           | IO_DI_18             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_18                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P161                        | HS Digital Output | IO_PVG_00          | IO_VOUT_00 IO_ADC_52 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_52                    | IO_DI_88          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P162                        | HS PWM Output     | IO_DO_23           | IO_DI_07             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_07                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P163                        | HS PWM Output     | IO_DO_37           | IO_DI_21             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_21                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P164                        | HS Digital Output | IO_PVG_03          | IO_VOUT_03 IO_ADC_55 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_55                    | IO_DI_91          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P165 P166 P167              | HS Digital Output | IO_PVG_05          | IO_VOUT_05 IO_ADC_57 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_57                    | IO_DI_93          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P168 P169 P170              | HS Digital Output | IO_PVG_07          | IO_VOUT_07 IO_ADC_59 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_59                    | IO_DI_95          |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P171 P172                   |                   |                    |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |

| HS Digital Output        | IO_ADC_37          |           |                      |
|--------------------------|--------------------|-----------|----------------------|
| IO_DO_01                 | IO_DI_73           |           |                      |
| HS PWM Output            | IO_PWD_15 IO_DI_31 |           |                      |
| HS PWM Output            | IO_PWD_19 IO_DI_35 |           |                      |
| HS Digital Output        | IO_ADC_39          |           |                      |
| IO_DO_03                 | IO_DI_75           |           |                      |
| HS PWM Output            | IO_DO_17           | IO_DI_01  |                      |
| IO_PWM_01                |                    |           |                      |
| P178                     | HS PWM Output      | IO_DO_31  | IO_DI_15             |
| IO_PWM_15                |                    |           |                      |
| P179                     | HS Digital Output  | IO_ADC_41 |                      |
| IO_DO_05                 | IO_DI_77           |           |                      |
| P180                     | HS PWM Output      | IO_DO_19  | IO_DI_03             |
| IO_PWM_03                |                    |           |                      |
| P181                     | HS PWM Output      | IO_DO_33  | IO_DI_17             |
| IO_PWM_17                |                    |           |                      |
| P182                     | HS Digital Output  | IO_ADC_43 |                      |
| IO_DO_07                 | IO_DI_79           |           |                      |
| P183                     | HS PWM Output      | IO_DO_21  | IO_DI_05             |
| IO_PWM_05                |                    |           |                      |
| P184                     | HS PWM Output      | IO_DO_35  | IO_DI_19             |
| IO_PWM_19                |                    |           |                      |
| P185                     | HS Digital Output  | IO_PVG_01 | IO_VOUT_01 IO_ADC_53 |
| IO_DO_53                 | IO_DI_89           |           |                      |
| P186                     | HS PWM Output      | IO_DO_22  | IO_DI_06             |
| IO_PWM_06                |                    |           |                      |
| P187                     | HS PWM Output      | IO_DO_36  | IO_DI_20             |
| IO_PWM_20                |                    |           |                      |
| P188                     | HS Digital Output  | IO_PVG_02 | IO_VOUT_02 IO_ADC_54 |
| IO_DO_54                 | IO_DI_90           |           |                      |
| P189 P190 P191           | HS Digital Output  | IO_PVG_04 | IO_VOUT_04 IO_ADC_56 |
| IO_DO_56                 | IO_DI_92           |           |                      |
| P192 P193 P194           | HS Digital Output  | IO_PVG_06 | IO_VOUT_06 IO_ADC_58 |
| IO_DO_58                 | IO_DI_94           |           |                      |
| P195 P196 P197 P198 P199 |                    |           |                      |

Alternative *Function*

Pin No. Main **Function**

![85_image_0.png]( The image displays a large number of blue dots arranged in rows and columns on a white background. There are at least twelve distinct groups of dots visible, each varying in size and position. Some dots are larger and more prominent than others, while the smaller ones can be found scattered throughout the scene. Overall, it appears to be an intricate pattern or design created by these blue dots.)

P200

P201 BAT+ **Power**

P202 BAT+ **Power**

P203 BAT+ **Power**

P204 BAT+ **Power**

P205 BAT+ **Power**

BAT+ **Power**

P207 **Terminal** 15

IO_ADC_K15

P208 LIN

IO_LIN

P209 CAN 0 Low

IO_CAN_CHANNEL_0

P210 CAN 1 Low

IO_CAN_CHANNEL_1

P211 CAN 2 Low

IO_CAN_CHANNEL_2

P212

P213

P214

P215

P216

P217 Sensor GND

P218

P219

P220 **Wake-Up**

IO_ADC_WAKE_UP

P221 Sensor Supply **Var.**

IO_ADC_SENSOR_SUPPLY_2

P222 CAN 0 **High**

IO_CAN_CHANNEL_0

P223 CAN 1 **High**

IO_CAN_CHANNEL_1

P224 CAN 2 **High**

IO_CAN_CHANNEL_2

P225

P226

P227

P228

P229

P230 Sensor GND

P231

P232

P233

| Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 CAN Termination 0L   |                                                                                  |                                 |
|---------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------|
| P236                                                          | CAN Termination 1L                                                               |                                 |
| P237                                                          | CAN Termination 2L                                                               |                                 |
| P238                                                          | LS Digital Output                                                                | IO_ADC_45                       |
| IO_DO_09                                                      | IO_DI_81                                                                         |                                 |
| P239                                                          | LS Digital Output                                                                | IO_ADC_47                       |
| IO_DO_11                                                      | IO_DI_83                                                                         |                                 |
| P240                                                          | LS Digital Output                                                                | IO_ADC_49                       |
| IO_DO_13                                                      | IO_DI_85                                                                         |                                 |
| P241                                                          | LS Digital Output                                                                | IO_ADC_51                       |
| IO_DO_15                                                      | IO_DI_87                                                                         |                                 |
| P242 P243                                                     | Sensor GND                                                                       |                                 |
| P244                                                          | Sensor GND                                                                       |                                 |
| P245                                                          | Sensor GND                                                                       |                                 |
| P246                                                          | BAT+ CPU IO_ADC_UBAT Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 CAN Termination 0H |                                 |
| P249                                                          | CAN Termination 1H                                                               |                                 |
| P250                                                          | CAN Termination 2H                                                               |                                 |
| P251                                                          | LS Digital Output                                                                | IO_ADC_44                       |
| IO_DO_08                                                      | IO_DI_80                                                                         |                                 |
| P252                                                          | LS Digital Output                                                                | IO_ADC_46                       |
| IO_DO_10                                                      | IO_DI_82                                                                         |                                 |
| P253                                                          | LS Digital Output                                                                | IO_ADC_48                       |
| IO_DO_12                                                      | IO_DI_84                                                                         |                                 |
| P254                                                          | LS Digital Output                                                                | IO_ADC_50                       |
| IO_DO_14                                                      | IO_DI_86                                                                         |                                 |
| P255 P256                                                     | Sensor GND                                                                       |                                 |
| P257                                                          | Sensor GND                                                                       |                                 |
| P258                                                          | Sensor GND                                                                       | Table 16: Pinning of HY-TTC 510 |

## 3.5.5 Hy-Ttc 590E **Variant**

Alternative *Function*

| HS Digital Output   | Timer Input                    | PVG Output   | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|--------------------------------|--------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| P101                | HS PWM Output                  | IO_DO_44     | IO_PWD_12     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_28           | IO_DI_28                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P102                | HS PWM Output                  | IO_DO_48     | IO_PWD_16     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_32           | IO_DI_32                       | IO_ADC_00    | IO_ADC_00     | IO_DI_48                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P103                | Analog Voltage Input IO_ADC_00 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P104                | Analog Voltage Input           | IO_ADC_02    | IO_ADC_02     | IO_DI_50                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_02           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P105                | Analog Voltage Input           | IO_ADC_04    | IO_ADC_04     | IO_DI_52                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_04           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P106                | Analog Voltage Input           | IO_ADC_06    | IO_ADC_06     | IO_DI_54                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_06           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P107                | Analog Voltage Input           | IO_ADC_08    | IO_DI_56      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_08           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P108                | Analog Voltage Input           | IO_ADC_10    | IO_DI_58      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_10           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P109                | Analog Voltage Input           | IO_ADC_12    | IO_DI_60      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_12           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P110                | Analog Voltage Input           | IO_ADC_14    | IO_DI_62      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_14           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P111                | Analog Voltage Input           | IO_ADC_16    | IO_DI_64      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_16           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P112                | Analog Voltage Input           | IO_ADC_18    | IO_DI_66      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_18           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P113                | Analog Voltage Input           | IO_ADC_20    | IO_DI_68      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_20           |                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P114                | Analog Voltage Input           | IO_ADC_22    | IO_DI_70      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_22           | IO_PWD_00                      | IO_ADC_24    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_00           | IO_DI_36                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_02           | IO_ADC_26                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_02           | IO_DI_38                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_04           | IO_ADC_28                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_04           | IO_DI_40 IO_ADC_30             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_06           | IO_DI_42 IO_ADC_32             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_08           | IO_DI_44                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

| Timer Input                    | IO_ADC_34            |           |           |          |
|--------------------------------|----------------------|-----------|-----------|----------|
| IO_PWD_10                      | IO_DI_46             |           |           |          |
| HS PWM Output                  | IO_DO_45             | IO_DI_29  |           |          |
| IO_PWM_29                      | IO_PWD_13            |           |           |          |
| HS PWM Output                  | IO_DO_49             | IO_PWD_17 |           |          |
| IO_PWM_33                      | IO_DI_33             |           |           |          |
| Analog Voltage Input           | IO_ADC_01            | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01 Analog Voltage Input | IO_ADC_03            | IO_ADC_03 | IO_DI_51  |          |
| IO_ADC_03                      |                      |           |           |          |
| P129                           | Analog Voltage Input | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05                      |                      |           |           |          |
| P130                           | Analog Voltage Input | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07                      |                      |           |           |          |
| P131                           | Analog Voltage Input | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09                      |                      |           |           |          |
| P132                           | Analog Voltage Input | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11                      |                      |           |           |          |
| P133                           | Analog Voltage Input | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13                      |                      |           |           |          |
| P134                           | Analog Voltage Input | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15                      |                      |           |           |          |
| P135                           | Analog Voltage Input | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17                      |                      |           |           |          |
| P136                           | Analog Voltage Input | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19                      |                      |           |           |          |
| P137                           | Analog Voltage Input | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21                      |                      |           |           |          |
| P138                           | Analog Voltage Input | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23                      |                      |           |           |          |
| P139                           | Timer Input          | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01                      | IO_DI_37             |           |           |          |
| P140                           | Timer Input          | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03                      | IO_DI_39             |           |           |          |
| P141                           | Timer Input          | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05                      | IO_DI_41             |           |           |          |
| P142                           | BAT                      |           |           |          |
| P143                           | BAT                      |           |           |          |
| P144                           | BAT                      |           |           |          |
| P145                           | BAT                      |           |           |          |
| P146                           | Timer Input          | IO_ADC_31 |           |          |
| IO_PWD_07                      | IO_DI_43             |           |           |          |
| P147                           | Timer Input          | IO_ADC_33 |           |          |
| IO_PWD_09                      | IO_DI_45             |           |           |          |

| Alternative                 | Function          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
|-----------------------------|-------------------|------------|----------------------|--------------------------------|--------------------|-------------------------|-------------------------------|-------------------------------|-------------------------|------------------|-------------------------|----------------------------|------------------|
| HS Digital Output           | Timer Input       | PVG Output | VOUT Output          | A/D Input (HS Output/PVG/VOUT) | Current Loop Input | A/D Input (Timer Input) | A/D Input (HS Digital Output) | A/D Input (LS Digital Output) | Analog Current Input 2M | Digital Input 2M | Analog Current Input 3M | Analog Resistance Input 3M | Digital Input 3M |
| Pin No.                     | Main Function     |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P148                        | Timer Input       | IO_ADC_35  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWD_11                   | IO_DI_47          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P149                        | HS Digital Output | IO_ADC_36  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_00                    | IO_DI_72          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P150                        | HS PWM Output     | IO_DO_46   | IO_PWD_14            |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_30                   | IO_DI_30          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P151                        | HS PWM Output     | IO_DO_50   | IO_PWD_18            |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_34                   | IO_DI_34          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P152                        | HS Digital Output | IO_ADC_38  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_02                    | IO_DI_74          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P153                        | HS PWM Output     | IO_DO_16   | IO_DI_00             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_00                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P154                        | HS PWM Output     | IO_DO_30   | IO_DI_14             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_14                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P155                        | HS Digital Output | IO_ADC_40  |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_04                    | IO_DI_76          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P156                        | HS PWM Output     | IO_DO_18   | IO_DI_02             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_02 HS PWM Output     | IO_DO_32          | IO_DI_16   |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_16 HS Digital Output | IO_ADC_42         |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_06                    | IO_DI_78          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P159                        | HS PWM Output     | IO_DO_20   | IO_DI_04             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_04                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P160                        | HS PWM Output     | IO_DO_34   | IO_DI_18             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_18                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P161                        | HS Digital Output | IO_PVG_00  | IO_VOUT_00 IO_ADC_52 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_52                    | IO_DI_88          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P162                        | HS PWM Output     | IO_DO_23   | IO_DI_07             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_07                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P163                        | HS PWM Output     | IO_DO_37   | IO_DI_21             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_21                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P164                        | HS Digital Output | IO_PVG_03  | IO_VOUT_03 IO_ADC_55 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_55                    | IO_DI_91          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P165                        | HS PWM Output     | IO_DO_25   | IO_DI_09             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_09                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P166                        | HS PWM Output     | IO_DO_39   | IO_DI_23             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_23                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P167                        | HS Digital Output | IO_PVG_05  | IO_VOUT_05 IO_ADC_57 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_57                    | IO_DI_93          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P168                        | HS PWM Output     | IO_DO_27   | IO_DI_11             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_11                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P169                        | HS PWM Output     | IO_DO_41   | IO_DI_25             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_PWM_25                   |                   |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P170                        | HS Digital Output | IO_PVG_07  | IO_VOUT_07 IO_ADC_59 |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| IO_DO_59                    | IO_DI_95          |            |                      |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |

| P171      | HS PWM Output     | IO_DO_29   | IO_DI_13             |
|-----------|-------------------|------------|----------------------|
| IO_PWM_13 |                   |            |                      |
| P172      | HS PWM Output     | IO_DO_43   | IO_DI_27             |
| IO_PWM_27 |                   |            |                      |
| P173      | HS Digital Output | IO_ADC_37  |                      |
| IO_DO_01  | IO_DI_73          |            |                      |
| P174      | HS PWM Output     | IO_DO_47   | IO_PWD_15            |
| IO_PWM_31 | IO_DI_31          |            |                      |
| P175      | HS PWM Output     | IO_DO_51   | IO_PWD_19            |
| IO_PWM_35 | IO_DI_35          |            |                      |
| P176      | HS Digital Output | IO_ADC_39  |                      |
| IO_DO_03  | IO_DI_75          |            |                      |
| P177      | HS PWM Output     | IO_DO_17   | IO_DI_01             |
| IO_PWM_01 |                   |            |                      |
| P178      | HS PWM Output     | IO_DO_31   | IO_DI_15             |
| IO_PWM_15 |                   |            |                      |
| P179      | HS Digital Output | IO_ADC_41  |                      |
| IO_DO_05  | IO_DI_77          |            |                      |
| P180      | HS PWM Output     | IO_DO_19   | IO_DI_03             |
| IO_PWM_03 |                   |            |                      |
| P181      | HS PWM Output     | IO_DO_33   | IO_DI_17             |
| IO_PWM_17 |                   |            |                      |
| P182      | HS Digital Output | IO_ADC_43  |                      |
| IO_DO_07  | IO_DI_79          |            |                      |
| P183      | HS PWM Output     | IO_DO_21   | IO_DI_05             |
| IO_PWM_05 |                   |            |                      |
| P184      | HS PWM Output     | IO_DO_35   | IO_DI_19             |
| IO_PWM_19 |                   |            |                      |
| P185      | HS Digital Output | IO_PVG_01  | IO_VOUT_01 IO_ADC_53 |
| IO_DO_53  | IO_DI_89          |            |                      |
| P186      | HS PWM Output     | IO_DO_22   | IO_DI_06             |
| IO_PWM_06 |                   |            |                      |
| P187      | HS PWM Output     | IO_DO_36   | IO_DI_20             |
| IO_PWM_20 |                   |            |                      |
| P188      | HS Digital Output | IO_PVG_02  | IO_VOUT_02 IO_ADC_54 |
| IO_DO_54  | IO_DI_90          |            |                      |
| P189      | HS PWM Output     | IO_DO_24   | IO_DI_08             |
| IO_PWM_08 |                   |            |                      |
| P190      | HS PWM Output     | IO_DO_38   | IO_DI_22             |
| IO_PWM_22 |                   |            |                      |
| P191      | HS Digital Output | IO_PVG_04  | IO_VOUT_04 IO_ADC_56 |
| IO_DO_56  | IO_DI_92          |            |                      |
| P192      | HS PWM Output     | IO_DO_26   | IO_DI_10             |
| IO_PWM_10 |                   |            |                      |
| P193      | HS PWM Output     | IO_DO_40   | IO_DI_24             |
| IO_PWM_24 |                   |            |                      |

HS Digital **Output**

IO_DO_58

IO_PVG_06 IO_VOUT_06 **IO_ADC_58**

IO_DI_94

HS PWM **Output**

IO_PWM_12

IO_DO_28 **IO_DI_12**

HS PWM **Output**

IO_PWM_26

IO_DO_42 **IO_DI_26**

| HS PWM Output       | IO_DO_42                                  | IO_DI_26   |
|---------------------|-------------------------------------------|------------|
| IO_PWM_26           |                                           |            |
| P198 P199 P200 P201 | BAT+ Power                                |            |
| P202                | BAT+ Power                                |            |
| P203                | BAT+ Power                                |            |
| P204                | BAT+ Power                                |            |
| P205                | BAT+ Power                                |            |
| P206                | BAT+ Power                                |            |
| P207                | Terminal 15 IO_ADC_K15                    |            |
| P208                | LIN IO_LIN                                |            |
| P209                | CAN 0 Low IO_CAN_CHANNEL_0                |            |
| P210                | CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN     |            |
| P211                | CAN 2 Low IO_CAN_CHANNEL_2                |            |
| P212                | CAN 3 Low IO_CAN_CHANNEL_3                |            |
| P213                | CAN 4 Low IO_CAN_CHANNEL_4                |            |
| P214                | CAN 5 Low IO_CAN_CHANNEL_5                |            |
| P215                | CAN 6 Low IO_CAN_CHANNEL_6                |            |
| P216                | Sensor GND                                |            |
| P217                | do not connect                            |            |
| P218                | CAN Termination 3H                        |            |
| P219                | CAN Termination 3L                        |            |
| P220                | Wake-Up IO_ADC_WAKE_UP                    |            |
| P221                | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |            |
| P222                | CAN 0 High IO_CAN_CHANNEL_0               |            |

| P223      | CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN   |           |
|-----------|------------------------------------------|-----------|
| P224      | CAN 2 High IO_CAN_CHANNEL_2              |           |
| P225      | CAN 3 High IO_CAN_CHANNEL_3              |           |
| P226      | CAN 4 High IO_CAN_CHANNEL_4              |           |
| P227      | CAN 5 High IO_CAN_CHANNEL_5              |           |
| P228      | CAN 6 High IO_CAN_CHANNEL_6              |           |
| P229 P230 | do not connect                           |           |
| P231      | BRR/100BASE-T1 TRXIO_DOWNLOAD, IO_UDP                                          |           |
| P232      | BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP  |           |
| P233      | RTC_BACKUP_BAT                           |           |
| P234      | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 |           |
| P235      | CAN Termination 0L                       |           |
| P236      | CAN Termination 1L                       |           |
| P237      | CAN Termination 2L                       |           |
| P238      | LS Digital Output                        | IO_ADC_45 |
| IO_DO_09  | IO_DI_81                                 |           |
| P239      | LS Digital Output                        | IO_ADC_47 |
| IO_DO_11  | IO_DI_83                                 |           |
| P240      | LS Digital Output                        | IO_ADC_49 |
| IO_DO_13  | IO_DI_85                                 |           |
| P241      | LS Digital Output                        | IO_ADC_51 |
| IO_DO_15  | IO_DI_87                                 |           |
| P242      | RS232 TXD IO_UART                        |           |
| P243      | Sensor GND                               |           |
| P244      | Sensor GND                               |           |
| P245      | Sensor GND                               |           |
| P246      | BAT+ CPU IO_ADC_UBAT                     |           |
| P247      | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |           |
| P248      | CAN Termination 0H                       |           |
| P249      | CAN Termination 1H                       |           |
| P250      | CAN Termination 2H                       |           |

| LS Digital Output   | IO_ADC_44         |                                  |
|---------------------|-------------------|----------------------------------|
| IO_DO_08            | IO_DI_80          |                                  |
| LS Digital Output   | IO_ADC_46         |                                  |
| IO_DO_10            | IO_DI_82          |                                  |
| LS Digital Output   | IO_ADC_48         |                                  |
| IO_DO_12            | IO_DI_84          |                                  |
| LS Digital Output   | IO_ADC_50         |                                  |
| IO_DO_14            | IO_DI_86          |                                  |
| P255                | RS232 RXD IO_UART |                                  |
| P256                | Sensor GND        |                                  |
| P257                | Sensor GND        |                                  |
| P258                | Sensor GND        | Table 17: Pinning of HY-TTC 590E |

| HS Digital Output   | Timer Input          | PVG Output   | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|----------------------|--------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function        |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P101                | HS PWM Output        | IO_DO_44     | IO_PWD_12     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_28           | IO_DI_28             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P102                | HS PWM Output        | IO_DO_48     | IO_PWD_16     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_32           | IO_DI_32             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P103                | Analog Voltage Input | IO_ADC_00    | IO_ADC_00     | IO_DI_48                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_00           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P104                | Analog Voltage Input | IO_ADC_02    | IO_ADC_02     | IO_DI_50                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_02           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P105                | Analog Voltage Input | IO_ADC_04    | IO_ADC_04     | IO_DI_52                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_04           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P106                | Analog Voltage Input | IO_ADC_06    | IO_ADC_06     | IO_DI_54                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_06           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P107                | Analog Voltage Input | IO_ADC_08    | IO_DI_56      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_08           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P108                | Analog Voltage Input | IO_ADC_10    | IO_DI_58      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_10           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P109                | Analog Voltage Input | IO_ADC_12    | IO_DI_60      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_12           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P110                | Analog Voltage Input | IO_ADC_14    | IO_DI_62      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_14           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P111                | Analog Voltage Input | IO_ADC_16    | IO_DI_64      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_16           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P112                | Analog Voltage Input | IO_ADC_18    | IO_DI_66      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_18           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P113                | Analog Voltage Input | IO_ADC_20    | IO_DI_68      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_20           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P114                | Analog Voltage Input | IO_ADC_22    | IO_DI_70      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_22           |                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P115                | Timer Input          | IO_PWD_00    | IO_ADC_24     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_00           | IO_DI_36             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P116                | Timer Input          | IO_PWD_02    | IO_ADC_26     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_02           | IO_DI_38             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P117                | Timer Input          | IO_PWD_04    | IO_ADC_28     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_04           | IO_DI_40             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P118                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P119                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P120                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P121                | BAT                      |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P122                | Timer Input          | IO_ADC_30    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_06           | IO_DI_42             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P123                | Timer Input          | IO_ADC_32    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_08           | IO_DI_44             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![94_image_0.png]( The image displays a large table with several columns of data arranged vertically. Each column represents different categories or subjects, and there are numerous rows that contain information for each category. The table appears to be organized in a way that allows easy comparison and analysis of the data.

The table is filled with various numbers and text, indicating that it contains quantitative and qualitative information about the topics being studied. This type of data presentation can be useful for researchers or professionals who need to analyze large amounts of information quickly and efficiently.)

| Timer Input          | IO_ADC_34             |           |           |          |
|----------------------|-----------------------|-----------|-----------|----------|
| IO_PWD_10            | IO_DI_46              |           |           |          |
| HS PWM Output        | IO_DO_45              | IO_DI_29  |           |          |
| IO_PWM_29            | IO_PWD_13             |           |           |          |
| HS PWM Output        | IO_DO_49              | IO_PWD_17 |           |          |
| IO_PWM_33            | IO_DI_33              |           |           |          |
| Analog Voltage Input | IO_ADC_01             | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01            |                       |           |           |          |
| P128                 | Analog Voltage Input  | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03            |                       |           |           |          |
| P129                 | Analog Voltage Input  | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05            |                       |           |           |          |
| P130                 | Analog Voltage Input  | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07            |                       |           |           |          |
| P131                 | Analog Voltage Input  | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09            |                       |           |           |          |
| P132                 | Analog Voltage Input  | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11            |                       |           |           |          |
| P133                 | Analog Voltage Input  | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13            |                       |           |           |          |
| P134                 | Analog Voltage Input  | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15            |                       |           |           |          |
| P135                 | Analog Voltage Input  | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17            |                       |           |           |          |
| P136                 | Analog Voltage Input  | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19            |                       |           |           |          |
| P137                 | Analog Voltage Input  | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21            |                       |           |           |          |
| P138                 | Analog Voltage Input  | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23            |                       |           |           |          |
| P139                 | Timer Input           | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01            | IO_DI_37              |           |           |          |
| P140                 | Timer Input           | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03            | IO_DI_39              |           |           |          |
| IO_PWD_05            | IO_ADC_29             |           |           |          |
| P141                 | Timer Input IO_PWD_05 | IO_DI_41  |           |          |
| P142                 | BAT                       |           |           |          |
| P143                 | BAT                       |           |           |          |
| P144                 | BAT                       |           |           |          |
| P145                 | BAT                       |           |           |          |
| P146                 | Timer Input           | IO_ADC_31 |           |          |
| IO_PWD_07            | IO_DI_43              |           |           |          |
| P147                 | Timer Input           | IO_ADC_33 |           |          |
| IO_PWD_09            | IO_DI_45              |           |           |          |

| P148      | Timer Input       | IO_ADC_35   |                      |
|-----------|-------------------|-------------|----------------------|
| IO_PWD_11 | IO_DI_47          |             |                      |
| P149      | HS Digital Output | IO_ADC_36   |                      |
| IO_DO_00  | IO_DI_72          |             |                      |
| P150      | HS PWM Output     | IO_DO_46    | IO_PWD_14            |
| IO_PWM_30 | IO_DI_30          |             |                      |
| P151      | HS PWM Output     | IO_DO_50    | IO_PWD_18            |
| IO_PWM_34 | IO_DI_34          |             |                      |
| P152      | HS Digital Output | IO_ADC_38   |                      |
| IO_DO_02  | IO_DI_74          |             |                      |
| P153      | HS PWM Output     | IO_DO_16    | IO_DI_00             |
| IO_PWM_00 |                   |             |                      |
| P154      | HS PWM Output     | IO_DO_30    | IO_DI_14             |
| IO_PWM_14 |                   |             |                      |
| P155      | HS Digital Output | IO_ADC_40   |                      |
| IO_DO_04  | IO_DI_76          |             |                      |
| P156      | HS PWM Output     | IO_DO_18    | IO_DI_02             |
| IO_PWM_02 |                   |             |                      |
| P157      | HS PWM Output     | IO_DO_32    | IO_DI_16             |
| IO_PWM_16 |                   |             |                      |
| P158      | HS Digital Output | IO_ADC_42   |                      |
| IO_DO_06  | IO_DI_78          |             |                      |
| P159      | HS PWM Output     | IO_DO_20    | IO_DI_04             |
| IO_PWM_04 |                   |             |                      |
| P160      | HS PWM Output     | IO_DO_34    | IO_DI_18             |
| IO_PWM_18 |                   |             |                      |
| P161      | HS Digital Output | IO_PVG_00   | IO_VOUT_00 IO_ADC_52 |
| IO_DO_52  | IO_DI_88          |             |                      |
| P162      | HS PWM Output     | IO_DO_23    | IO_DI_07             |
| IO_PWM_07 |                   |             |                      |
| P163      | HS PWM Output     | IO_DO_37    | IO_DI_21             |
| IO_PWM_21 |                   |             |                      |
| P164      | HS Digital Output | IO_PVG_03   | IO_VOUT_03 IO_ADC_55 |
| IO_DO_55  | IO_DI_91          |             |                      |
| P165      | HS PWM Output     | IO_DO_25    | IO_DI_09             |
| IO_PWM_09 |                   |             |                      |
| P166      | HS PWM Output     | IO_DO_39    | IO_DI_23             |
| IO_PWM_23 |                   |             |                      |
| P167      | HS Digital Output | IO_PVG_05   | IO_VOUT_05 IO_ADC_57 |
| IO_DO_57  | IO_DI_93          |             |                      |
| P168      | HS PWM Output     | IO_DO_27    | IO_DI_11             |
| IO_PWM_11 |                   |             |                      |
| P169      | HS PWM Output     | IO_DO_41    | IO_DI_25             |
| IO_PWM_25 |                   |             |                      |
| P170      | HS Digital Output | IO_PVG_07   | IO_VOUT_07 IO_ADC_59 |
| IO_DO_59  | IO_DI_95          |             |                      |

| HS PWM Output               | IO_DO_29          | IO_DI_13   |                      |
|-----------------------------|-------------------|------------|----------------------|
| IO_PWM_13 HS PWM Output     | IO_DO_43          | IO_DI_27   |                      |
| IO_PWM_27 HS Digital Output | IO_ADC_37         |            |                      |
| IO_DO_01                    | IO_DI_73          |            |                      |
| HS PWM Output               | IO_DO_47          | IO_PWD_15  |                      |
| IO_PWM_31                   | IO_DI_31          |            |                      |
| P175                        | HS PWM Output     | IO_DO_51   | IO_PWD_19            |
| IO_PWM_35                   | IO_DI_35          |            |                      |
| P176                        | HS Digital Output | IO_ADC_39  |                      |
| IO_DO_03                    | IO_DI_75          |            |                      |
| P177                        | HS PWM Output     | IO_DO_17   | IO_DI_01             |
| IO_PWM_01                   |                   |            |                      |
| P178                        | HS PWM Output     | IO_DO_31   | IO_DI_15             |
| IO_PWM_15                   |                   |            |                      |
| P179                        | HS Digital Output | IO_ADC_41  |                      |
| IO_DO_05                    | IO_DI_77          |            |                      |
| P180                        | HS PWM Output     | IO_DO_19   | IO_DI_03             |
| IO_PWM_03                   |                   |            |                      |
| P181                        | HS PWM Output     | IO_DO_33   | IO_DI_17             |
| IO_PWM_17                   |                   |            |                      |
| P182                        | HS Digital Output | IO_ADC_43  |                      |
| IO_DO_07                    | IO_DI_79          |            |                      |
| P183                        | HS PWM Output     | IO_DO_21   | IO_DI_05             |
| IO_PWM_05                   |                   |            |                      |
| P184                        | HS PWM Output     | IO_DO_35   | IO_DI_19             |
| IO_PWM_19                   |                   |            |                      |
| P185                        | HS Digital Output | IO_PVG_01  | IO_VOUT_01 IO_ADC_53 |
| IO_DO_53                    | IO_DI_89          |            |                      |
| P186                        | HS PWM Output     | IO_DO_22   | IO_DI_06             |
| IO_PWM_06                   |                   |            |                      |
| P187                        | HS PWM Output     | IO_DO_36   | IO_DI_20             |
| IO_PWM_20                   |                   |            |                      |
| P188                        | HS Digital Output | IO_PVG_02  | IO_VOUT_02 IO_ADC_54 |
| IO_DO_54                    | IO_DI_90          |            |                      |
| P189                        | HS PWM Output     | IO_DO_24   | IO_DI_08             |
| IO_PWM_08                   |                   |            |                      |
| P190                        | HS PWM Output     | IO_DO_38   | IO_DI_22             |
| IO_PWM_22                   |                   |            |                      |
| P191                        | HS Digital Output | IO_PVG_04  | IO_VOUT_04 IO_ADC_56 |
| IO_DO_56                    | IO_DI_92          |            |                      |
| P192                        | HS PWM Output     | IO_DO_26   | IO_DI_10             |
| IO_PWM_10                   |                   |            |                      |
| P193                        | HS PWM Output     | IO_DO_40   | IO_DI_24             |
| IO_PWM_24                   |                   |            |                      |

| IO_PWM_26                |                                           |
|--------------------------|-------------------------------------------|
| P197 P198 P199 P200 P201 | BAT+ Power                                |
| P202                     | BAT+ Power                                |
| P203                     | BAT+ Power                                |
| P204                     | BAT+ Power                                |
| P205                     | BAT+ Power                                |
| P206                     | BAT+ Power                                |
| P207                     | Terminal 15 IO_ADC_K15                    |
| P208                     | LIN IO_LIN                                |
| P209                     | CAN 0 Low IO_CAN_CHANNEL_0                |
| P210                     | CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN     |
| P211                     | CAN 2 Low IO_CAN_CHANNEL_2                |
| P212                     | CAN 3 Low IO_CAN_CHANNEL_3                |
| P213                     | CAN 4 Low IO_CAN_CHANNEL_4                |
| P214                     | CAN 5 Low IO_CAN_CHANNEL_5                |
| P215                     | CAN 6 Low IO_CAN_CHANNEL_6                |
| P216                     | Sensor GND                                |
| P217                     | do not connect                            |
| P218                     | CAN Termination 3H                        |
| P219                     | CAN Termination 3L                        |
| P220                     | Wake-Up IO_ADC_WAKE_UP                    |
| P221                     | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |
| P222                     | CAN 0 High IO_CAN_CHANNEL_0               |

| P223      | CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN   |           |
|-----------|------------------------------------------|-----------|
| P224      | CAN 2 High IO_CAN_CHANNEL_2              |           |
| P225      | CAN 3 High IO_CAN_CHANNEL_3              |           |
| P226      | CAN 4 High IO_CAN_CHANNEL_4              |           |
| P227      | CAN 5 High IO_CAN_CHANNEL_5              |           |
| P228      | CAN 6 High IO_CAN_CHANNEL_6              |           |
| P229 P230 | do not connect                           |           |
| P231      | BRR/100BASE-T1 TRXIO_DOWNLOAD, IO_UDP                                          |           |
| P232      | BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP  |           |
| P233      | RTC_BACKUP_BAT                           |           |
| P234      | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 |           |
| P235      | CAN Termination 0L                       |           |
| P236      | CAN Termination 1L                       |           |
| P237      | CAN Termination 2L                       |           |
| P238      | LS Digital Output                        | IO_ADC_45 |
| IO_DO_09  | IO_DI_81                                 |           |
| P239      | LS Digital Output                        | IO_ADC_47 |
| IO_DO_11  | IO_DI_83                                 |           |
| P240      | LS Digital Output                        | IO_ADC_49 |
| IO_DO_13  | IO_DI_85                                 |           |
| P241      | LS Digital Output                        | IO_ADC_51 |
| IO_DO_15  | IO_DI_87                                 |           |
| P242      | RS232 TXD IO_UART                        |           |
| P243      | Sensor GND                               |           |
| P244      | Sensor GND                               |           |
| P245      | Sensor GND                               |           |
| P246      | BAT+ CPU IO_ADC_UBAT                     |           |
| P247      | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |           |
| P248      | CAN Termination 0H                       |           |
| P249      | CAN Termination 1H                       |           |
| P250      | CAN Termination 2H                       |           |

| LS Digital Output   | IO_ADC_44   |                                 |
|---------------------|-------------|---------------------------------|
| IO_DO_08            | IO_DI_80    |                                 |
| LS Digital Output   | IO_ADC_46   |                                 |
| IO_DO_10            | IO_DI_82    |                                 |
| LS Digital Output   | IO_ADC_48   |                                 |
| IO_DO_12            | IO_DI_84    |                                 |
| LS Digital Output   | IO_ADC_50   |                                 |
| IO_DO_14            | IO_DI_86    |                                 |
| RS232 RXD IO_UART   |             |                                 |
| P256                | Sensor GND  |                                 |
| P257                | Sensor GND  |                                 |
| P258                | Sensor GND  | Table 18: Pinning of HY-TTC 590 |

Document Number: D-TTC5F-G-20-002

| Pin No.                 | Main Function                  |                                  |           |           |          |
|-------------------------|--------------------------------|----------------------------------|-----------|-----------|----------|
| P101                    | HS PWM Output                  | IO_PWD_12 IO_DI_28               |           |           |          |
| P102                    | HS PWM Output                  | IO_PWD_16 IO_DI_32               | IO_ADC_00 | IO_ADC_00 | IO_DI_48 |
| P103                    | Analog Voltage Input IO_ADC_00 |                                  |           |           |          |
| P104                    | Analog Voltage Input           | IO_ADC_02                        | IO_ADC_02 | IO_DI_50  |          |
| IO_ADC_02               |                                |                                  |           |           |          |
| P105                    | Analog Voltage Input           | IO_ADC_04                        | IO_ADC_04 | IO_DI_52  |          |
| IO_ADC_04               |                                |                                  |           |           |          |
| P106                    | Analog Voltage Input           | IO_ADC_06                        | IO_ADC_06 | IO_DI_54  |          |
| IO_ADC_06               |                                |                                  |           |           |          |
| P107                    | Analog Voltage Input           | IO_ADC_08                        | IO_DI_56  |           |          |
| IO_ADC_08               |                                |                                  |           |           |          |
| P108                    | Analog Voltage Input           | IO_ADC_10                        | IO_DI_58  |           |          |
| IO_ADC_10               |                                |                                  |           |           |          |
| P109                    | Analog Voltage Input           | IO_ADC_12                        | IO_DI_60  |           |          |
| IO_ADC_12               |                                |                                  |           |           |          |
| P110                    | Analog Voltage Input           | IO_ADC_14                        | IO_DI_62  |           |          |
| IO_ADC_14               |                                |                                  |           |           |          |
| P111                    | Analog Voltage Input           | IO_ADC_16                        | IO_DI_64  |           |          |
| IO_ADC_16               |                                |                                  |           |           |          |
| P112                    | Analog Voltage Input           | IO_ADC_18                        | IO_DI_66  |           |          |
| IO_ADC_18               |                                |                                  |           |           |          |
| P113                    | Analog Voltage Input           | IO_ADC_20                        | IO_DI_68  |           |          |
| IO_ADC_20               |                                |                                  |           |           |          |
| P114                    | Analog Voltage Input           | IO_ADC_22                        | IO_DI_70  |           |          |
| IO_ADC_22               |                                |                                  |           |           |          |
| P115                    | Timer Input                    | IO_PWD_00                        | IO_ADC_24 |           |          |
| IO_PWD_00               | IO_DI_36                       |                                  |           |           |          |
| P116                    | Timer Input                    | IO_PWD_02                        | IO_ADC_26 |           |          |
| IO_PWD_02               | IO_DI_38                       |                                  |           |           |          |
| P117                    | Timer Input                    | IO_PWD_04                        | IO_ADC_28 |           |          |
| IO_PWD_04               | IO_DI_40                       |                                  |           |           |          |
| P118                    | BAT                                |                                  |           |           |          |
| P119                    | BAT                                |                                  |           |           |          |
| P120                    | BAT                                |                                  |           |           |          |
| P121                    | BAT                                |                                  |           |           |          |
| P122                    | Timer Input                    | IO_ADC_30                        |           |           |          |
| IO_PWD_06               | IO_DI_42                       |                                  |           |           |          |
| P123                    | Timer Input                    | IO_ADC_32                        |           |           |          |
| IO_PWD_08               | IO_DI_44                       | HY-TTC 500 System Manual V 1.6.0 |           |           |          |
| 3 Pinning and Connector |                                |                                  |           |           |          |

![101_image_1.png]( The image displays a long row of numbers on a gray background, possibly representing a series of measurements or data points. There are several sets of numbers visible, with some appearing to be grouped together and others separated by intervals. The arrangement of the numbers suggests that they might be part of a graphic representation or chart.)

![101_image_0.png]( The image displays a table with several columns of data, including numbers and text. There are multiple rows of information, each containing different types of data. The table is organized neatly, making it easy to read and understand the content. It appears to be a spreadsheet or a similar type of document that contains numerical data and possibly other relevant information.)

3.5.7 HY-TTC 508 **Variant** 
90 

![101_image_2.png]( The image features a blue and white logo for TT Communications International. The logo is displayed prominently on a gray background, making it stand out. The design of the logo consists of two interconnected letters, "TT," which are positioned close to each other. This logo represents the company's focus on communication and international connections.)

| Timer Input                    | IO_ADC_34            |           |           |          |
|--------------------------------|----------------------|-----------|-----------|----------|
| IO_PWD_10                      | IO_DI_46             |           |           |          |
| HS PWM Output                  | IO_DI_29 IO_PWD_13   |           |           |          |
| HS PWM Output                  | IO_PWD_17 IO_DI_33   |           |           |          |
| Analog Voltage Input           | IO_ADC_01            | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01 Analog Voltage Input | IO_ADC_03            | IO_ADC_03 | IO_DI_51  |          |
| IO_ADC_03                      |                      |           |           |          |
| P129                           | Analog Voltage Input | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05                      |                      |           |           |          |
| P130                           | Analog Voltage Input | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07                      |                      |           |           |          |
| P131                           | Analog Voltage Input | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09                      |                      |           |           |          |
| P132                           | Analog Voltage Input | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11                      |                      |           |           |          |
| P133                           | Analog Voltage Input | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13                      |                      |           |           |          |
| P134                           | Analog Voltage Input | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15                      |                      |           |           |          |
| P135                           | Analog Voltage Input | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17                      |                      |           |           |          |
| P136                           | Analog Voltage Input | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19                      |                      |           |           |          |
| P137                           | Analog Voltage Input | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21                      |                      |           |           |          |
| P138                           | Analog Voltage Input | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23                      |                      |           |           |          |
| P139                           | Timer Input          | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01                      | IO_DI_37             |           |           |          |
| P140                           | Timer Input          | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03                      | IO_DI_39             |           |           |          |
| P141                           | Timer Input          | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05                      | IO_DI_41             |           |           |          |
| P142                           | BAT                      |           |           |          |
| P143                           | BAT                      |           |           |          |
| P144                           | BAT                      |           |           |          |
| P145                           | BAT                      |           |           |          |
| P146                           | Timer Input          | IO_ADC_31 |           |          |
| IO_PWD_07                      | IO_DI_43             |           |           |          |
| P147                           | Timer Input          | IO_ADC_33 |           |          |
| IO_PWD_09                      | IO_DI_45             |           |           |          |

![103_image_0.png]( The image displays a table with various columns and rows of data. There are several numbers and dates visible on the table, indicating that it is likely related to financial or business information. The table appears to be organized into different sections, each containing unique data points.

In addition to the main table, there are two smaller tables located towards the right side of the image. These additional tables may provide more context or details about the main subject matter. Overall, the image conveys a sense of organization and structure, with the main focus on the central table containing various data points.)

| P148                          | Timer Input       | IO_ADC_35          |                                  |
|-------------------------------|-------------------|--------------------|----------------------------------|
| IO_PWD_11                     | IO_DI_47          |                    |                                  |
| P149                          | HS Digital Output | IO_ADC_36          |                                  |
| IO_DO_00                      | IO_DI_72          |                    |                                  |
| P150                          | HS PWM Output     | IO_PWD_14 IO_DI_30 |                                  |
| P151                          | HS PWM Output     | IO_PWD_18 IO_DI_34 |                                  |
| P152                          | HS Digital Output | IO_ADC_38          |                                  |
| IO_DO_02                      | IO_DI_74          |                    |                                  |
| P153                          | HS PWM Output     | IO_DO_16           | IO_DI_00                         |
| IO_PWM_00                     |                   |                    |                                  |
| P154                          | HS PWM Output     | IO_DO_30           | IO_DI_14                         |
| IO_PWM_14                     |                   |                    |                                  |
| P155                          | HS Digital Output | IO_ADC_40          |                                  |
| IO_DO_04                      | IO_DI_76          |                    |                                  |
| P156                          | HS PWM Output     | IO_DO_18           | IO_DI_02                         |
| IO_PWM_02                     |                   |                    |                                  |
| P157                          | HS PWM Output     | IO_DO_32           | IO_DI_16                         |
| IO_PWM_16                     |                   |                    |                                  |
| P158                          | HS Digital Output | IO_ADC_42          |                                  |
| IO_DO_06                      | IO_DI_78          |                    |                                  |
| P159                          | HS PWM Output     | IO_DO_20           | IO_DI_04                         |
| IO_PWM_04                     |                   |                    |                                  |
| P160 P161                     | HS Digital Output | IO_PVG_00          | IO_VOUT_00 IO_ADC_52 IO_DI_88    |
| P162 P163 P164                | HS Digital Output | IO_PVG_03          | IO_VOUT_03 IO_ADC_55 IO_DI_91    |
| P165 P166 P167                | HS Digital Output | IO_PVG_05          | IO_VOUT_05 IO_ADC_57 IO_DI_93    |
| P168 P169 P170 P171 P172 P173 | HS Digital Output | IO_ADC_37          |                                  |
| IO_DO_01                      | IO_DI_73          |                    |                                  |
| P174                          | HS PWM Output     | IO_PWD_15 IO_DI_31 | HY-TTC 500 System Manual V 1.6.0 |
| 3 Pinning and Connector       |                   |                    |                                  |

![103_image_1.png]( The image is a close-up of a computer screen displaying text and images. There are two main sections on the screen, one towards the left side and another towards the right side. The content appears to be related to a discussion or presentation involving information about property rights.

In addition to the main sections, there are several smaller elements visible in the image. A bar can be seen near the top-left corner of the screen, while two other bars are located at the bottom-right corner. There is also an arrow pointing towards the right side of the screen.)

Document Number: D-TTC5F-G-20-002

| HS PWM Output                                     | IO_PWD_19 IO_DI_35   |           |                               |
|---------------------------------------------------|----------------------|-----------|-------------------------------|
| HS Digital Output                                 | IO_ADC_39            |           |                               |
| IO_DO_03                                          | IO_DI_75             |           |                               |
| HS PWM Output                                     | IO_DO_17             | IO_DI_01  |                               |
| IO_PWM_01 HS PWM Output                           | IO_DO_31             | IO_DI_15  |                               |
| IO_PWM_15 HS Digital Output                       | IO_ADC_41            |           |                               |
| IO_DO_05                                          | IO_DI_77             |           |                               |
| P180                                              | HS PWM Output        | IO_DO_19  | IO_DI_03                      |
| IO_PWM_03                                         |                      |           |                               |
| P181                                              | HS PWM Output        | IO_DO_33  | IO_DI_17                      |
| IO_PWM_17                                         |                      |           |                               |
| P182                                              | HS Digital Output    | IO_ADC_43 |                               |
| IO_DO_07                                          | IO_DI_79             |           |                               |
| P183                                              | HS PWM Output        | IO_DO_21  | IO_DI_05                      |
| IO_PWM_05                                         |                      |           |                               |
| P184 P185                                         | HS Digital Output    | IO_PVG_01 | IO_VOUT_01 IO_ADC_53 IO_DI_89 |
| P186 P187 P188                                    | HS Digital Output    | IO_PVG_02 | IO_VOUT_02 IO_ADC_54 IO_DI_90 |
| P189 P190 P191                                    | HS Digital Output    | IO_PVG_04 | IO_VOUT_04 IO_ADC_56 IO_DI_92 |
| P192 P193 P194 P195 P196 P197 P198 P199 P200 P201 | BAT+ Power           |           |                               |
| P202                                              | BAT+ Power           |           |                               |
| P203                                              | BAT+ Power           |           |                               |
| P204                                              | BAT+ Power           |           |                               |
| P205                                              | BAT+ Power           |           |                               |
| P206                                              | BAT+ Power           |           |                               |

![105_image_0.png]( The image features a large blue and white graph that spans from left to right across most of the frame. The graph is filled with various data points, making it appear quite detailed. There are also several smaller graphs embedded within the main one, each displaying different sets of information. These smaller graphs can be found in the upper half of the image, as well as scattered throughout the larger blue and white graph.)

| P208 P209                         | CAN 0 Low IO_CAN_CHANNEL_0              |
|-----------------------------------|-----------------------------------------|
| P210                              | CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN   |
| P211                              | CAN 2 Low IO_CAN_CHANNEL_2              |
| P212 P213 P214 P215 P216          | Sensor GND                              |
| P217                              | do not connect                          |
| P218 P219 P220                    | Wake-Up IO_ADC_WAKE_UP                  |
| P221 P222                         | CAN 0 High IO_CAN_CHANNEL_0             |
| P223                              | CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN  |
| P224                              | CAN 2 High IO_CAN_CHANNEL_2             |
| P225 P226 P227 P228 P229 P230     | do not connect                          |
| P231                              | BRR/100BASE-T1 TRXIO_DOWNLOAD, IO_UDP                                         |
| P232                              | BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP |
| P233                              | RTC_BACKUP_BAT                          |
| P234 P235                         | CAN Termination 0L                      |
| P236                              | CAN Termination 1L                      |
| P237                              | CAN Termination 2L                      |
| Document Number: D-TTC5F-G-20-002 | HY-TTC 500 System Manual V 1.6.0        |
| 3 Pinning and Connector           |                                         |

| LS Digital Output   | IO_ADC_45                                |                                 |
|---------------------|------------------------------------------|---------------------------------|
| IO_DO_09            | IO_DI_81                                 |                                 |
| LS Digital Output   | IO_ADC_47                                |                                 |
| IO_DO_11            | IO_DI_83                                 |                                 |
| LS Digital Output   | IO_ADC_49                                |                                 |
| IO_DO_13            | IO_DI_85                                 |                                 |
| LS Digital Output   | IO_ADC_51                                |                                 |
| IO_DO_15            | IO_DI_87                                 |                                 |
| P243                | Sensor GND                               |                                 |
| P244                | Sensor GND                               |                                 |
| P245                | Sensor GND                               |                                 |
| P246                | BAT+ CPU IO_ADC_UBAT                     |                                 |
| P247                | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |                                 |
| P248                | CAN Termination 0H                       |                                 |
| P249                | CAN Termination 1H                       |                                 |
| P250                | CAN Termination 2H                       |                                 |
| P251                | LS Digital Output                        | IO_ADC_44                       |
| IO_DO_08            | IO_DI_80                                 |                                 |
| P252                | LS Digital Output                        | IO_ADC_46                       |
| IO_DO_10            | IO_DI_82                                 |                                 |
| P253                | LS Digital Output                        | IO_ADC_48                       |
| IO_DO_12            | IO_DI_84                                 |                                 |
| P254                | LS Digital Output                        | IO_ADC_50                       |
| IO_DO_14            | IO_DI_86                                 |                                 |
| P255 P256           | Sensor GND                               |                                 |
| P257                | Sensor GND                               |                                 |
| P258                | Sensor GND                               | Table 19: Pinning of HY-TTC 508 |

HY-TTC 500 System Manual V 1.6.0

![107_image_0.png]( The image showcases a blue and white sign that reads "TC Control HyDAC International." This sign is likely associated with an organization or company related to control systems or technology. The design of the sign features a combination of blue and white colors, making it visually appealing and easy to read.)

96 **4 Specification of Inputs and Outputs**

## 4 Specification Of Inputs And Outputs

4.1 Positive Power Supply of Power Stages (BAT+ Power)
4.1.1 Pinout

![107_image_1.png]( The image features a white drawing of an electronic device with multiple rows of green and blue buttons arranged neatly. Each row consists of several buttons, creating a visually appealing pattern on the device's surface. The buttons are spread out across the entire width of the drawing, showcasing their organization and design.) 

| P201   | Battery (+) Supply of Power Stages / BAT+ Power   |
|--------|---------------------------------------------------|
| P202   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P203   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P204   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P205   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P206   | Battery (+) Supply of Power Stages / BAT+ Power   |

Supply pins for power stage supply.

The nominal supply voltage for full operation is between 6 and 32 V, including supply voltage ranges for 12 and 24 V battery operation. In this voltage range, all the I/Os work, as described in the system manual. BAT+ Power pins are equipped with inverse polarity protection.

![108_image_0.png]( The image features a blue and white logo for TTC Control, an international company. The logo is displayed prominently on a gray background, making it stand out against the lighter color of the background.)

TTControl GmbH recommends to use these pins in parallel and the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage **drop and prevent overheating of the** crimp contact.

## 4.1.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol                                           | Parameter                                                                                                 | Note            | Min.   | Max.     | Unit    |      |     |      |    |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------|--------|----------|---------|------|-----|------|----|
| BAT+max Permanent non-destructive supply voltage | 1                                                                                                         | -32             | 32     | V        |         |      |     |      |    |
| BAT+lim                                          | Peak                                                                                                      | non-destructive | supply | clamping | voltage | 1, 2 | -40 | 45   | V  |
| <1 ms                                            |                                                                                                           |                 |        |          |         |      |     |      |    |
| I in-lim                                         | Peak                                                                                                      | non-destructive | supply | clamping | current | 1, 2 | -10 | +100 | A  |
| <1 ms                                            |                                                                                                           |                 |        |          |         |      |     |      |    |
| Td                                               | Load dump protection time according to ISO 7637- 2 [20], Pulse 5, Level IV (superimposed 174 V, Ri = 2 Ω) | 1               | 350    | ms       |         |      |     |      |    |
| I in-max                                         | Permanent battery supply current (all 6 pins in parallel with symmetrical wire connection))                                                                                                           | 3               | 60     | A        |         |      |     |      |    |
| I in-max                                         | Permanent battery supply current per pin                                                                  | 3               | 10     | A        |         |      |     |      |    |
| I in-total                                       | Total load current, 12 V and 24 V battery operation                                                       | 4               | 45     | A        |         |      |     |      |    |
| I in-total                                       | Total load current, 12 V and 24 V battery operation                                                       | 4,5             | 60     | A        |         |      |     |      |    |

Note **1 The control unit is protected by a transient suppressor, specified by clamp voltage, current and duration of voltage transient**
Note 2 1 ms pulse width, non-repetitive. The pulse width is defined **as the point at which**
the peak current decreases to 50 % of the maximum value.

Note **3 This battery supply current is related to the total load current of all high-side**
power-stages. In worst case, all outputs are in non-PWM mode **or with maximum duty cycle operated, the battery current equals the total load current. With**
typical PWM-operation the battery supply current is significant lower than the total load current. For more details please see Section 6.2.2 on page **193.**
Note 4 HY-TTC 500 variant-dependent, see Section 6.2.2 on page 193 Note 5 TECU **= -40. . . +85** °C

## 4.1.4 Characteristics

TECU **= -40. . . +125** °C

| Symbol   | Parameter                         | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance             | 250    | µF     |        |        |
| BAT+     | Supply voltage for full operation | 6      | 32     | V      |        |

![109_image_0.png]( The image features a blue and white logo for Hyundai TC Control International. It is likely that this company specializes in automotive electronics or control systems. The logo appears to be a combination of letters and numbers, possibly representing the brand's name or product offerings.)

98 **4 Specification of Inputs and Outputs**
4.2 Positive Power Supply of Internal Electronics (BAT+ CPU)
4.2.1 Pinout

![109_image_1.png]( The image is a white drawing of an electronic device with many buttons and switches arranged on its surface. The buttons are spread out across various sections of the device, creating a complex pattern. Some of these buttons are located near the top left corner, while others can be found in the middle and bottom areas of the device.

In addition to the buttons, there is also a row of switches situated along the right side of the drawing. This electronic device appears to be an intricate piece of equipment with numerous controls for various functions.) 

Figure 15: Pinout of BAT+ CPU
Pin No. Function **SW-define**
P246 Battery supply of internal electronics IO_ADC_UBAT
Supply pin for positive power supply of internal electronics, sensor supply and PVG/Vout **output**
stages.

As the output voltage of the PVG/Vout **outputs is defined as a percentage value in relation to the**
battery voltage, the voltage drop on the wire to this pin has a **direct influence on the accuracy of the** PVG output voltage. BAT+ CPU pin is equipped with inverse polarity protection.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

![110_image_0.png]( The image displays a diagram of an electronic system with various components and labels. There are multiple layers within this system, including a CPU, power supply, and input/output devices. A large number of cables can be seen connecting these components, indicating the complex interplay between them.

In addition to the main components, there is also a bar graph present in the image, which could represent data or performance metrics related to the electronic system. The presence of this graph suggests that the diagram may have been created for educational purposes or to illustrate the functionality and structure of the electronic device.)

## 4.2.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol   | Parameter                                                                                                 | Note                                                                                                                                        | Min.   | Max.     | Unit    |     |     |      |    |
|----------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------|----------|---------|-----|-----|------|----|
| Uin-max  | Permanent non-destructive supply voltage                                                                  | 1                                                                                                                                           | -32    | 32       | V       |     |     |      |    |
| Uin-lim  | Peak                                                                                                      | non-destructive                                                                                                                             | supply | clamping | voltage | 1,2 | -40 | 45   | V  |
| <1 ms    |                                                                                                           |                                                                                                                                             |        |          |         |     |     |      |    |
| I in-lim | Peak                                                                                                      | non-destructive                                                                                                                             | supply | clamping | current | 1,2 | -10 | +100 | A  |
| <1 ms    |                                                                                                           |                                                                                                                                             |        |          |         |     |     |      |    |
| Td       | Load dump protection time according to ISO 7637- 2 [20], Pulse 5, Level IV (superimposed 174 V, Ri = 2 Ω) | 1                                                                                                                                           | 350    | ms       |         |     |     |      |    |
| I in-max | Permanent input current                                                                                   | 3                                                                                                                                           | 3      | A        |         |     |     |      |    |
| Note     | 1                                                                                                         | The control unit is protected by a transient suppressor, specified by clamp voltage, current and duration of voltage transient.                                                                                                                                             |        |          |         |     |     |      |    |
| Note     | 2                                                                                                         | 1 ms pulse width, non-repetitive. The pulse width is defined as the point at which the peak current decreases to 50 % of the maximum value. |        |          |         |     |     |      |    |

## 4.2.4 Characteristics

TECU **= -40. . . +125** °C

| Symbol    | Parameter                                       | Note                                                                        | Min.   | Max.   | Unit   |
|-----------|-------------------------------------------------|-----------------------------------------------------------------------------|--------|--------|--------|
| Cin       | Pin input capacitance                           | 250                                                                         | µF     |        |        |
| BAT+      | Supply voltage for start-up                     | 1                                                                           | 8      | 32     | V      |
| BAT+      | Supply voltage for full operation               | 2                                                                           | 6      | 32     | V      |
| I in-idle | Supply current of unit without load (8 V)       | 600                                                                         | mA     |        |        |
| I in-idle | Supply current of unit without load (12 V)      | 400                                                                         | mA     |        |        |
| I in-idle | Supply current of unit without load (24 V)      | 200                                                                         | mA     |        |        |
| I in-STBY | Standby supply current (Terminal 15 and Wake-Up | 1                                                                           | mA     |        |        |
| off)      |                                                 |                                                                             |        |        |        |
| I in-STBY | Standby supply current (Terminal 15 and Wake-Up | 3                                                                           | <0.5   | mA     |        |
| off)      |                                                 |                                                                             |        |        |        |
| Note      | 1                                               | 8 V is the initial voltage for start-up at the beginning of the drive cycle |        |        |        |
| Note      | 2                                               | See Section 4.2.5 on the next page                                          |        |        |        |
| Note      | 3                                               | TECU = -40. . . +85 °C                                                      |        |        |        |

The HY-TTC 500 core system is designed for full operation after start-up between 6 V and 32 V, including supply voltage ranges for 12 V and 24 V battery operation and cold-start cranking according to ISO 16750-2 [22]. The initial minimum supply voltage at the beginning of the **drive cycle is 8 V.** After start-up, the CPU will remain operational down to 6 V, e.g. during cold-start cranking. The minimum supply voltage during cold-start cranking is defined by ISO 16750-2:2012 (see Table 3, Starting profile values for systems with 12 V nominal voltage, UN
, and Table 4, *Values for systems* with 24 V nominal voltage, UN
). The HY-TTC 500 core system complies with ISO 16750-2:2012, level I, II (functional status C), III and IV for 12-V systems **and level I, II (functional status A) and III**
(functional status B) for 24-V systems, see Table 20 on page 103 and Table 21 on page **103.**
Restrictions during cold-start cranking apply also for sensor supplies. For more information, see Section 4.7 on page 112 and Section 4.8 on page **114.**
HY-TTC 500 ISO 16750 code specification see Section 1.6 on page 35.

![113_image_0.png]( The image is a white drawing of an electrical circuit with multiple measurements and calculations displayed on it. There are several numbers and letters scattered throughout the drawing, indicating various data points or equations related to the circuit.

In addition to these textual elements, there are two graphs present in the drawing. One graph is located towards the left side of the image, while the other is positioned more centrally. These graphs likely represent different aspects of the electrical circuit's performance or behavior.)

Key t **time**
U **test voltage**
tf**falling slope** tr**rising slope**
t6
, t7
, t8**duration parameters (in accordance with Table 3 and Table 4 of ISO 16750-2)**
UB**supply voltage for generator not in operation (see ISO 16750-1 [13])**
US**supply voltage** US6 **supply voltage at** t6 a f = 2 Hz

## 4.2.5.1 Hy-Ttc 500 Iso 16750 Functional Status

ISO 16750-2:2012 starting profile - functional status for 12 V system nominal voltage

| Functional Status   |    |    |
|---------------------|----|----|
| A                   | B  | C  |
| Level I             | X  |    |
| Level II            | X  |    |
| Level III           | X  |    |
| Level IV            | X  |    |

Table 20: ISO 16750 functional status for 12 V systems ISO 16750-2:2012 starting profile - functional status for 24 V system nominal voltage

| Functional Status   |                    |    |
|---------------------|--------------------|----|
| A                   | B                  | C  |
| Level I             | X                  |    |
| Level II            | X                  |    |
| Level III           | X (after start-up) |    |

Table 21: ISO 16750 functional status for 24 V systems

## 4.2.6 Voltage Monitoring

| Symbol   | Parameter                    | Note   | Min.   | Max.   | Unit   |
|----------|------------------------------|--------|--------|--------|--------|
| τin      | First order low pass filter  | 1.5    | 2.5    | ms     |        |
| Vnom     | Nominal battery supply range | 1      | 0      | 33     | V      |
| Vtol-0   | Zero reading error           | -80    | +80    | mV     |        |
| Vtol-0   | Zero reading error           | 2      | -67    | +67    | mV     |
| Vtol-p   | Proportional error           | -1.2   | +1.2   | %      |        |
| Vtol-p   | Proportional error           | 2      | -1     | +1     | %      |
| LSB      | Nominal value of 1 LSB       | -      | 13.4   | mV     |        |

Note **1 The nominal battery supply range is only a value to calculate the actual voltage.**
Note 2 TECU = -40. . . +85 °C

## 4.3 Negative Power Supply (Bat-)

4.3.1 Pinout

![115_image_1.png]( The image is a close-up of a computer circuit board with multiple electronic components on it. There are several chips and other parts arranged across the board, creating an intricate pattern. The arrangement of these components suggests that they are part of a larger device or system.

The components are spread out in various positions, with some closer to the edges and others more centrally located. Overall, the circuit board appears to be well-organized and functional, showcasing the intricate workings of electronic devices.)

![115_image_0.png]( The image is a white drawing of an empty train car with multiple rows of seats. There are at least twelve rows of seats visible, each row consisting of several chairs. The seats are arranged in various positions within the train car, some closer to the front and others towards the back.

The arrangement of the seats creates a sense of depth and organization within the train car, making it appear like an actual transportation vehicle.) 
Figure 18: Pinout of BAT-

| Pin No.   | Function                     |
|-----------|------------------------------|
| P118      | Negative Power Supply (BAT-) |
| P119      | Negative Power Supply (BAT-) |
| P120      | Negative Power Supply (BAT-) |
| P121      | Negative Power Supply (BAT-) |
| P142      | Negative Power Supply (BAT-) |
| P143      | Negative Power Supply (BAT-) |
| P144      | Negative Power Supply (BAT-) |
| P145      | Negative Power Supply (BAT-) |

Supply pins for BAT- connection. The HY-TTC 500 housing is not directly connected to BAT-, for more information see Section 6.4 on page **195.** TTControl GmbH recommends to use these pins in parallel and the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage **drop and prevent overheating of the** crimp contact.

## 4.3.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                  | Note   | Min.   | Max.   | Unit   |
|----------|----------------------------|--------|--------|--------|--------|
| Iout-max | Permanent current per pin  | 4      | A      |        |        |
| Iout-max | Permanent current all pins | 28     | A      |        |        |

4.4 Sensor GND
4.4.1 Pinout

![117_image_0.png]( The image is a black and white drawing of an electronic device with multiple rows of buttons or switches. There are at least twelve buttons visible on the device, arranged in various positions across the image. Some of these buttons are located towards the top left corner, while others can be found near the center and bottom right areas of the drawing. The design suggests that this could be a control panel for an electronic system or a complex piece of equipment.) 

| Pin No.   | Function   | Applicable to variants                         |
|-----------|------------|------------------------------------------------|
| P216      | Sensor GND | HY-TTC 590E, HY-TTC 590, HY-TTC 508            |
| P217      | Sensor GND | HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510 |
| P230      | Sensor GND | HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510 |
| P243      | Sensor GND | all                                            |
| P244      | Sensor GND | all                                            |
| P245      | Sensor GND | all                                            |
| P256      | Sensor GND | all                                            |
| P257      | Sensor GND | all                                            |
| P258      | Sensor GND | all                                            |

Supply pins for analog sensor GND connection. These pins can also be used as GND connection for digital sensors.

## 4.4.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                 | Note   | Min.   | Max.   | Unit   |
|----------|---------------------------|--------|--------|--------|--------|
| Iout-max | Permanent current per pin | 1      | 1      | A      |        |

Note **1 It is recommended to use all sensor ground pins simultaneously to ensure load**
distribution and minimize voltage drop on the external wiring.

4.5 Terminal 15 4.5.1 Pinout

![119_image_0.png]( The image is a white drawing of an electronic device with multiple ports and connections. There are several cables connected to these ports, indicating that it might be a router or a similar type of equipment. The cables are arranged in various directions, creating a complex network within the device.

In addition to the cables, there are two small icons visible on the drawing. One is located towards the left side of the image and the other one is closer to the right side. These icons might represent different functions or features of the electronic device.) 

Pin No. Function **SW-define**
P207 Terminal 15 Input IO_ADC_K15

This is the power control input for permanently supplied systems. When switched to positive supply, this input gives the command to power up the ECU, regardless of the Wake-Up **pin status. When** switched off, the ECU can activate its keep-alive functionality (if keep-alive functionality is enabled by SW) and is finally switched off by software after a user-defined period of time. This input is monitored by the CPU via an ADC input.

For correct pin wiring, see Section 6.6.1.1 **with wiring examples. See also Section** POWER - Driver for ECU power functions **of the API documentation [30].**

## 4.5.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                           | Note   | Min.   | Max.   | Unit   |
|----------|-------------------------------------|--------|--------|--------|--------|
| Vin      | Permanent (DC) input voltage        | -33    | +33    | V      |        |
| Vin      | Transient peak input voltage 500 ms | -50    | +50    | V      |        |
| Vin      | Transient peak input voltage 1ms    | -100   | +100   | V      |        |

## 4.5.4 Characteristics

TECU **= -40. . . +125** °C

| Symbol   | Parameter                    | Note                                                                        | Min.   | Max.   | Unit   |
|----------|------------------------------|-----------------------------------------------------------------------------|--------|--------|--------|
| Cin      | Pin input capacitance        | 8                                                                           | 12     | nF     |        |
| Rpd      | Pull-down resistor           | 6.5                                                                         | 11.5   | kΩ     |        |
| I in     | Input current                | 1                                                                           | 2      | 2.5    | mA     |
| I in     | Input current                | 2                                                                           | 4      | 4.5    | mA     |
| Vil      | Input voltage for low level  | 0                                                                           | 6      | V      |        |
| Vih      | Input voltage for high level | 3                                                                           | 8      | 32     | V      |
| τin      | Input low pass filter        | 180                                                                         | 280    | µs     |        |
| Note     | 1                            | at 16 V input voltage                                                       |        |        |        |
| Note     | 2                            | at 32 V input voltage                                                       |        |        |        |
| Note     | 3                            | 8 V is the initial voltage for start-up at the beginning of the drive cycle |        |        |        |

4.6 Wake-Up

![121_image_0.png]( The image displays a computer screen with a text-based program or application. There is a long line of text on the screen, possibly representing a musical score or some other form of data. The text appears to be written in a foreign language, which suggests that it could be related to a specific culture or region.)

![121_image_1.png](121. Pinout of a Wake-Up is displayed on this page. The image shows the pinout diagram for a wake-up circuit, which is essential for ensuring proper functioning and interconnectivity within electronic devices. The diagram provides a clear visual representation of the connections between various components in the wake-up circuit, making it easier to understand and troubleshoot any issues that may arise during the design or assembly process.)

![121_image_2.png]( The image displays a computer screen with a blue background and white text. There are two main sections on the screen: one is a description of the function, while the other is a diagram or graph that illustrates the function. The graph appears to be related to a sleep-wake cycle, possibly showing the relationship between sleep and wakefulness.

The text on the screen provides information about the function, which seems to be related to the sleep-wake cycle. There are also two numbers visible in the image: one is "20," while the other is "1." These numbers might represent specific values or measurements associated with the function being described.)

This is the Wake-Up **input for permanently supplied systems. When switched to positive supply**
(rising edge triggered), this input gives the command to power up the ECU, regardless of the Terminal 15 **pin status. When switched off, the ECU can activate its keep-alive functionality (provided that keep-alive functionality is enabled by SW) and finally switches off by software after a**
user-defined period of time. The application software can command the ECU to switch off even if the Wake-Up **pin is high, but only if** Terminal 15 **is off. This input is monitored by the CPU via an**
ADC input.

## Use Case Pre-Boot Sequence

For example, it is possible to start the boot sequence of the ECU by opening the vehicle door by connecting the Wake-Up pin with the vehicle door contact. When the driver enters the **vehicle and**
turns the ignition key on (Terminal 15 **to high), the ECU boot process is already finished. With this**
feature the ECU is ready for operation without any delay.

If the Wake-Up **pin is in a continuous high state (e.g. vehicle door is left open) and** Terminal 15 pin is not switched on, the application software shall power **down the ECU after an application** dependent timeout. After forcing the ECU shutdown via application software, it **is necessary to externally toggle the**
Wake-Up **pin or activate** Terminal 15 **pin to restart the ECU.**
See also section *POWER - Driver for ECU power functions* **of the API documentation [30].**

## 4.6.3 Maximum Ratings

| Symbol   | Parameter                           | Note   | Min.   | Max.   | Unit   |
|----------|-------------------------------------|--------|--------|--------|--------|
| Vin      | Permanent (DC) input voltage        | -33    | 33     | V      |        |
| Vin      | Transient peak input voltage 500 ms | -50    | 50     | V      |        |
| Vin      | Transient peak input voltage 1 ms   | -100   | 100    | V      |        |

4.6.4 Characteristics TECU **= -40. . . +125** °C

| Symbol   | Parameter                    | Note                                                                        | Min.   | Max.   | Unit   |
|----------|------------------------------|-----------------------------------------------------------------------------|--------|--------|--------|
| Cin      | Pin input capacitance        | 8                                                                           | 12     | nF     |        |
| Rpd      | Pull-down resistor           | 6.5                                                                         | 11.5   | kΩ     |        |
| I in     | Input current                | 1                                                                           | 2      | 2.5    | mA     |
| I in     | Input current                | 2                                                                           | 4      | 4.5    | mA     |
| Vil      | Input voltage for low level  | 0                                                                           | 6      | V      |        |
| Vih      | Input voltage for high level | 8                                                                           | 32     | V      |        |
| τin      | Input low pass filter        | 180                                                                         | 280    | µs     |        |
| Note     | 1                            | at 16 V input voltage                                                       |        |        |        |
| Note     | 2                            | at 32 V input voltage                                                       |        |        |        |
| Note     | 3                            | 8 V is the initial voltage for start-up at the beginning of the drive cycle |        |        |        |

## 4.7 Sensor Supplies 5 V

![123_Image_0.Png](123_Image_0.Png)

![123_Image_1.Png](123_Image_1.Png)

![123_Image_2.Png](123_Image_2.Png)

Figure 22: Pinout of sensor supply 5 V

| P247   | Sensor Supply 0   | IO_ADC_SENSOR_SUPPLY_0   |
|--------|-------------------|--------------------------|
| P234   | Sensor Supply 1   | IO_ADC_SENSOR_SUPPLY_1   |

![123_image_3.png]( The image displays a table with two columns of numbers. In one column, there are four sets of numbers labeled P2341, P2345, and P2347. These numbers appear to be related to the other column, which contains three sets of numbers labeled P2348, P2350, and P2352. The table seems to be a comparison between these two sets of numbers or possibly an examination of their differences.)

Two independent sensor supplies 5 V for 3-wire sensors (e.g. **potentiometers, pressure sensors** etc.).

For fully redundant sensors with 2 sensor-supply connections, both supplies must be connected to different sensor supplies.

If the input voltage on the BAT+ CPU pin is lower than typically 6 V (at 5 mA sensor supply load current), the sensor supply output voltage will be out of specification. One example of such low input voltage situations may be cold-start cranking in 12/24 V systems where the supply voltage can drop below 6 V. If the sensor supply output voltage drops below 4.7 **V, the application software will be** informed about this error situation after glitch filtering.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *POWER - Driver for ECU power functions* of the API documentation [30].

![124_image_0.png]( The image is a diagram of an electronic device with various components labeled and connected to each other. There are several batteries placed throughout the device, some closer to the center while others are positioned towards the edges. A large number of wires can be seen connecting these batteries to different parts of the circuit, creating a complex network of connections.

In addition to the batteries and wires, there is a clock visible in the middle-left part of the image, indicating that this device may have a timekeeping function or be used for precise timing purposes. The overall design suggests that this electronic device could be used for various applications, such as power management, data storage, or communication systems.)

Figure 23: Sensor supply 5 V

## 4.7.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol   | Parameter                                                                       | Note   | Min.   | Max.   | Unit   |
|----------|---------------------------------------------------------------------------------|--------|--------|--------|--------|
| Vin      | Output voltage under overload conditions (e.g. short circuit to supply voltage) |        |        |        |        |

4.7.4 Characteristics TECU **= -40. . . +125** °C

| Symbol   | Parameter                | Note   | Min.   | Max.   | Unit   |
|----------|--------------------------|--------|--------|--------|--------|
| Cout     | Pin output capacitance   | 0.8    | 1.2    | µF     |        |
| Vout     | Output voltage, at Iload | 4.85   | 5.15   | V      |        |
| I load   | Load current             | 0      | 500    | mA     |        |

4.8 Sensor Supply Variable

![125_image_0.png]( The image features a white background with a single black line on it, which appears to be a graph or a drawing of some sort. There are no other visible elements in the scene, making it a simple and minimalistic representation.)

![125_image_1.png]( The image is a close-up of a gray background with several black dots arranged vertically and horizontally. There are at least five sets of black dots, each varying in size and position. Some of these dots are closer to the top left corner while others are spread out across the middle and right side of the image. The overall appearance gives an impression of a pattern or design, but it is not clear what specific object or subject this pattern represents.)

Figure 24: Pinout of sensor supply variable

![125_image_2.png]( The image displays a row of white dots arranged vertically on a gray background. There are several rows of dots, with some overlapping and others distinctly separated. A green dot can be seen among these dots, standing out from the rest. The arrangement creates an interesting visual effect that draws attention to the green dot amidst the white dots.)

Pin No. Function **SW-define**
P221 Sensor Supply 2 IO_ADC_SENSOR_SUPPLY_2

One independent sensor supply with variable output voltage, configurable in 1 V steps, is provided for 3-wire sensors (e.g. potentiometers, pressure sensors **etc.).**
As already described in Section 4.7 on page 112, 5 V sensor supply, **Functional Description, the**
BAT+ CPU pin voltage must be at least 1 V higher than the required sensor supply output voltage VSSUP. If the BAT+ CPU pin voltage is lower than VSSUP -1 V, the **sensor supply output voltage** will be out of specification.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *POWER - Driver for ECU power functions* of the API documentation [30].

![126_image_0.png]( The image depicts a diagram of an electronic circuit with various components and labels. There are several green boxes scattered throughout the circuit, which might represent different parts or functions within the system. A few of these green boxes have numbers written on them, possibly indicating specific locations or measurements in the circuit.

The circuit appears to be complex, with multiple connections between different components. The presence of various labels and numbers suggests that this is a well-designed electronic system, likely used for a specific purpose or function.)

## 4.8.3 Maximum Ratings Tecu **= -40. . . +125** °C

Symbol Parameter Note Min. Max. **Unit**
Vin **Output voltage under overload conditions (e.g.**
short circuit to supply voltages)
-1 33 V

## 4.8.4 Characteristics

TECU **= -40. . . +125** °C

| Symbol   | Parameter                                   | Note   | Min.   | Max.   | Unit   |
|----------|---------------------------------------------|--------|--------|--------|--------|
| Cout     | Pin output capacitance                      | 0.8    | 1.2    | µF     |        |
| Vout     | Output voltage, 5-V setting                 | 4.85   | 5.15   | V      |        |
| Vout     | Output voltage, 6-V setting                 | 5.80   | 6.20   | V      |        |
| Vout     | Output voltage, 7-V setting                 | 6.75   | 7.25   | V      |        |
| Vout     | Output voltage, 8-V setting                 | 7.70   | 8.30   | V      |        |
| Vout     | Output voltage, 9-V setting                 | 8.65   | 9.35   | V      |        |
| Vout     | Output voltage, 10-V setting                | 9.60   | 10.40  | V      |        |
| Pload    | Maximum output power, 5-V. . . 10-V setting | 2.5    | W      |        |        |

## 4.9 Analog Input 3 Modes

![127_image_0.png]( The image is a white drawing of an electronic device with multiple rows of blue and green lights arranged vertically. There are several sets of blue lights lined up next to each other, while some green lights can be seen interspersed among them. The arrangement creates the appearance of a futuristic or high-tech device.) 

| Pin No.   | Function 1              | Function 2                | Function 3                 | SW-define   |
|-----------|-------------------------|---------------------------|----------------------------|-------------|
| P103      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_00   |
| P127      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_01   |
| P104      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_02   |
| P128      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_03   |
| P105      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_04   |
| P129      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_05   |
| P106      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_06   |
| P130      | Analog 0. . . 5 V Input | Analog 0. . . 25 mA Input | Analog 0. . . 100 kΩ Input | IO_ADC_07   |

8 multipurpose analog inputs with 12-bit resolution.

The inputs can be configured to 3 different operation modes individually by software:
- **Analog Voltage Input: 8 x 0 to 5 V, ratiometric or with absolute reference** - **Analog Current Input: 8 x 0 to 25 mA, analog current loop sensors**
- **Analog Resistance Input: 8 x 0 to 100 k**Ω
All inputs are short-circuit protected, independent of application software (included in low-level driver software). Each input is provided with a first-order low pass **filter with 3 ms time constant, allowing** 2 ms sample rate.

See also section *ADC - Analog to Digital Converter driver* of the API documentation [30].

## 4.9.3 Maximum Ratings

TECU **= -40. . . +125** °C

![128_image_0.png]( The image displays a blue screen with various data and information displayed on it. There is a graph showing voltage under load conditions, which appears to be a bar plot. In addition to this, there are two other graphs visible on the screen, one located towards the left side of the image and another towards the right side.

The main focus of the image seems to be on the first graph, which is a bar plot showing voltage under load conditions. The data points within the graph are labeled with numbers, providing clear information about the values being displayed.)

Note 1 Due to thermal reasons only one of the 8 inputs may be shorted **to 33 V at the**
same time. A connection to any supply voltage higher than 5 V is not allowed for normal operation.

## 4.9.4 Analog Voltage Input

![128_image_1.png]( The image is a diagram of an analog voltage input circuit with various components and connections. There are multiple wires connecting different parts of the circuit, including a CPU, a sensor supply, and a voltage supply. A green box can be seen in the middle of the circuit, possibly containing a processor or other electronic component.

In addition to these main components, there is also an analog input device present within the circuit. The diagram provides a clear visual representation of the connections between different parts of the system, allowing for easy understanding and analysis of the circuit's functionality.)

## Absolute Vs. Ratiometric Voltage Measurement:

Many sensor types are available in absolute or ratiometric measurement variant.

- Absolute**: The sensor output voltage is a fixed value and directly corresponds to a physical**
value. For example, 2.5 V corresponds to 1 bar. Any tolerance **in the reference voltage of the** sensor and the ECU generates additional measurement inaccuracy.

- Ratiometric: The sensor output voltage is a fixed percentage of the sensor **supply, the ratio**
corresponds to a physical value. For example, 50 % corresponds to 1 bar (or 2.5 V if the sensor supply is exactly 5.00 V). Any tolerance in the reference voltage of the sensor and the ECU is completely compensated and will not generate additional measurement inaccuracy.

![129_image_0.png]( The image displays a diagram of an electronic circuit board with various components and labels. There are multiple wires connecting different parts of the circuit, including a processor, memory, and other electronic devices.

In addition to these components, there is a large green box that appears to be a computer or server unit. It seems to be integrated into the overall design of the circuit board, indicating its importance in the functioning of the system.)

Due to the described behavior, it is generally recommended to use ratiometric sensors. Absolute or ratiometric function selection is done by software for each input individually.

## 4.9.4.1 Characteristics Of 5 V Input (Ratiometric)

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor          | 98     | 107    | kΩ     |        |
| τin      | Input low pass filter       | 2.2    | 3.8    | ms     |        |
| Vnom     | Nominal input voltage range | 0      | 5      | V      |        |
| VIn      | Input voltage range         | 1      | 0.2    | 4.8    | V      |
| Vtol-0   | Zero reading error          | 4,5    | -15    | +15    | mV     |
| Vtol-0   | Zero reading error          | 2,4,5  | -10    | +10    | mV     |
| Vtol-p   | Proportional error          | 4,5    | -0.2   | +0.2   | %      |
| Vtol-p   | Proportional error          | 2,4,5  | -0.2   | +0.2   | %      |
| LSB      | Nominal value of 1 LSB      | -      | 1.2207 | mV     |        |

## 4.9.4.2 Characteristics Of 5 V Input (Absolute) Tecu **= -40. . . +125** °C 4.9.4.3 Characteristics Of 5 V Digital Input

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor          | 98     | 107    | kΩ     |        |
| τin      | Input low pass filter       | 2.2    | 3.8    | ms     |        |
| Vnom     | Nominal input voltage range | 0      | 5      | V      |        |
| Vin      | Input voltage range         | 1      | 0.2    | 4.8    | V      |
| Vtol-0   | Zero reading error          | 3,5    | -15    | +15    | mV     |
| Vtol-0   | Zero reading error          | 2,3,5  | -10    | +10    | mV     |
| Vtol-p   | Proportional error          | 3,5    | -0.8   | +0.8   | %      |
| Vtol-p   | Proportional error          | 2,3,5  | -0.6   | +0.6   | %      |
| LSB      | Nominal value of 1 LSB      | -      | 1.2207 | mV     |        |

Note **1 For full accuracy**
Note 2 TECU **= -40. . . +85** °C
Note 3 Absolute measurement. This includes the conversion error **of the HY-TTC 500**
only. For the calculation of the total measurement error, it **is necessary to sum** the error of HY-TTC 500 and the absolute sensor error (measurement tolerance plus tolerance of external sensor reference).

Note **4 Ratiometric mode. This includes the conversion error of the HY-TTC 500 and the**
sensor supply error. For the calculation of the total measurement error, the error of HY-TTC 500 and the error of the ratiometric sensor (measurement tolerance) must be added.

Note **Configuration by application software**
Note 5 The total measurement error is the sum of zero reading error and the proportional error.

| Symbol   | Parameter                    | Note                                                                       | Min.   | Max.   | Unit   |
|----------|------------------------------|----------------------------------------------------------------------------|--------|--------|--------|
| Cin      | Pin input capacitance        | 8                                                                          | 12     | nF     |        |
| Rpu      | Pull-up resistor             | 4.8                                                                        | 5      | kΩ     |        |
| Vpu      | Pull-up voltage              | 4.9                                                                        | 5.1    | V      |        |
| τin      | Input low pass filter        | 2.2                                                                        | 3.8    | ms     |        |
| Vil      | Input voltage for low level  | 0                                                                          | V      |        |        |
| Vih      | Input voltage for high level | 5                                                                          | V      |        |        |
| LSB      | Nominal value of 1 LSB       | -                                                                          | 1.2207 | mV     |        |
| Note     | 1                            | For full accuracy                                                          |        |        |        |
| Note     | 2                            | TECU = -40. . . +85 °C                                                     |        |        |        |
| Note     | 3                            | Absolute measurement. This includes the conversion error of the HY-TTC 500 |        |        |        |

TECU **= -40. . . +125** °C

## 4.9.5 Analog Current Input

Analog input for 0. . . 25mA sensor measurement. Due to the wider measurement range of the input compared to the output range of popular sensors with 4. . . 20 mA, short to GND, short to BAT+ and cable defects can be easily detected. In case of an overload situation, the pin is switched to a high **impedance state. The protection** mechanism tries re-enabling the output 10 times per drive cycle.

During power down (Terminal 15 **off), the ECU does not disconnect the current sensor input. It is**
not recommended to supply the sensors permanently in order to prevent battery discharge. TTControl GmbH recommends one of the following 2 options:
1. Option 1**: Use a digital output for supplying the sensor. When the device is switched off, the**
ECU can perform an application-controlled shutdown, e. g., **in order to operate a cooling fan** to cool down an engine until the temperature is low enough or to store data in the non-volatile memory of the ECU. If the application controlled shut-down is finished, the ECU switches off and consumes less than 1 mA of battery current (including sensors).

2. **Option 2**: Terminal 15 **is used to supply the current loop sensor directly.**
Note that Terminal 15 **is often used to switch relays or other inductive loads directly. This**
may cause transients in excess of ±**50 V, for which the sensor must be specified.**

![131_image_0.png]( The image is a diagram of an electronic circuit board with various components labeled and connected to each other. There are several wires running through the circuit, connecting different parts of the board.

The main components visible on the circuit board include a CPU (central processing unit), a TMS5708 microcontroller, and a sensor supply. The diagram also shows an analog input, indicating that the circuit is designed for both digital and analog functions. There are multiple capacitors placed throughout the circuit to store electrical energy in the form of electric charge.

Overall, the image provides a clear representation of the electronic components and their connections within the circuit board.)

## 4.9.5.1 Characteristics Of Analog Current Input

| Symbol   | Parameter              | Note   | Min.   | Max.   | Unit   |
|----------|------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance  | 8      | 12     | nF     |        |
| RCS      | Current sense resistor | 1      | 177    | 185    | Ω      |
| τin      | Input low pass filter  | 2.2    | 3.8    | ms     |        |
| I in     | Input current range    | 0      | 25     | mA     |        |
| LSB      | Nominal value of 1 LSB | -      | 6.78   | µA     |        |
| I tol-0  | Zero reading error     | 3      | -70    | +70    | µA     |
| I tol-0  | Zero reading error     | 2,3    | -40    | +40    | µA     |
| I tol-p  | Proportional error     | 3      | -2.5   | +2.5   | %      |
| I tol-p  | Proportional error     | 2,3    | -2.0   | +2.0   | %      |

Note **1 This is the load resistor value for the current loop sensor.**
Note 2 TECU **= -40. . . +85** °C
Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**

## 4.9.6 Analog Resistance Input

Input for 0. . . 100kΩ **resistance sensor measurement.**
Resistive sensors are for example NTC or PTC resistors for temperature measurement. The actual resistor value of the sensor is computed from the measured input voltage together with the known reference resistor value. Be aware that this measurement setup has the highest accuracy and resolution if the sensors resistance is in the magnitude **of the reference resistors value.**

![132_image_0.png]( The image displays a diagram of an electronic circuit with various components and labels. There are several wires connecting different parts of the circuit, including two large wires that appear to be the main power source for the system.

In addition to these wires, there is a computer chip located in the middle of the circuit, which could be responsible for processing information or controlling the overall functioning of the device. The diagram also features several smaller components such as resistors and capacitors that contribute to the proper functioning of the electronic circuit.

Overall, the image provides an overview of a complex electronic system with multiple interconnected parts.)

The resistance mode may also be used as digital input with switches connected to ground, see Figure 32 **on the current page. The use of switches to BAT+ is not allowed.** To enhance the diagnostic coverage, use switches of type Namur. With a Namur-type switch sensor, short to ground, short to BAT+ and cable defects can be easily **detected.**

![133_image_0.png]( The image is a diagram of an electronic circuit with various components and labels. There are several wires connecting different parts of the circuit, including a green wire that goes from one part to another. A few buttons can be seen within the circuit, likely for controlling or interacting with the device.

In addition to the wires and buttons, there is an analog input switch on the left side of the image, which might be used for adjusting settings or inputs in the electronic circuit. The diagram also features a CPU (Central Processing Unit) towards the top right corner, indicating that this part of the circuit may perform complex calculations or control other components within the device.)

![133_image_1.png]( The image is a diagram showing an electronic circuit with various components and labels. There are two main sections of the circuit: one on the left side and another on the right side. The left section includes a switch that can be used to control the flow of electricity in the circuit.

In the right section, there's a green box labeled "ADC." Above this box, there are two labels: "EUC" and "CPU." Additionally, there is an analog input signal displayed on the left side of the diagram. The image also features a bar graph that shows the relationship between the switch and the analog input signal.)

## 4.9.6.1 Characteristics Of Analog Resistance Input

Resistance sensors are, e. g., PTC resistors for temperature measurement.

TECU **= -40. . . +125** °C

Symbol Parameter Note Min. Max. **Unit**

Cin Pin input capacitance **8 12 nF**

Rref Reference resistor 4831 4929 Ω

| Symbol                                  | Parameter             | Note   | Min.   | Max.   | Unit   |
|-----------------------------------------|-----------------------|--------|--------|--------|--------|
| τin                                     | Input low pass filter | 2.2    | 3.8    | ms     |        |
| Rext_range Resistance measurement range | 0                     | 100    | kΩ     |        |        |

The resistance measurement tolerance is given at specific sensor resistance value. Any value in between needs to be linear interpolated.

TECU **= -40. . . +85** °C

| Symbol   | Parameter                                | Note   | Min.   | Max.   | Unit   |
|----------|------------------------------------------|--------|--------|--------|--------|
| Rtol-m   | Measurement tolerance for 0. . . 99 Ω    | -5     | +5     | Ω      |        |
| Rtol-m   | Measurement tolerance for 100 Ω          | -5     | +5     | %      |        |
| Rtol-m   | Measurement tolerance for 200 Ω          | -4     | +4     | %      |        |
| Rtol-m   | Measurement tolerance for 500 Ω          | -2.5   | +2.5   | %      |        |
| Rtol-m   | Measurement tolerance for 1 k. . . 20 kΩ | -2     | +2     | %      |        |
| Rtol-m   | Measurement tolerance for 50 kΩ          | -3     | +3     | %      |        |
| Rtol-m   | Measurement tolerance for 100 kΩ         | -4     | +4     | %      |        |

| Symbol   | Parameter                                  | Note   | Min.   | Max.   | Unit   |
|----------|--------------------------------------------|--------|--------|--------|--------|
| Rtol-m   | Measurement tolerance for 0. . . 99 Ω      | -10    | +10    | Ω      |        |
| Rtol-m   | Measurement tolerance for 100 Ω            | -10    | +10    | %      |        |
| Rtol-m   | Measurement tolerance for 200 Ω            | -6     | +6     | %      |        |
| Rtol-m   | Measurement tolerance for 500 Ω. . . 20 kΩ | -3     | +3     | %      |        |
| Rtol-m   | Measurement tolerance for 50 kΩ            | -4     | +4     | %      |        |
| Rtol-m   | Measurement tolerance for 100 kΩ           | -5     | +5     | %      |        |

TECU **= +85. . . +125** °C

## 4.10 Analog Input 2 Modes

4.10.1 Pinout

![135_image_1.png]( The image is a black and white drawing of an empty stadium with a large seating area. There are multiple rows of seats visible throughout the scene, including some close to the center of the image and others towards the edges. The overall atmosphere suggests that the stadium is currently unoccupied or waiting for spectators to arrive.)

![135_image_0.png]( The image is a white drawing of an empty train with rows of seats and windows. There are several chairs visible throughout the train, some closer to the front and others nearer to the back. The arrangement of these chairs creates a sense of depth in the drawing, giving it a three-dimensional appearance.) 
Figure 33: Pinout of analog input 2 mode

| Pin No.   | Function 1                           | Function 2                | SW-define   |
|-----------|--------------------------------------|---------------------------|-------------|
| P107      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_08   |
| P131      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_09   |
| P108      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_10   |
| P132      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_11   |
| P109      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_12   |
| P133      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_13   |
| P110      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_14   |
| P134      | Analog 0. . . 5 V, 0. . . 10 V Input | Analog 0. . . 25 mA Input | IO_ADC_15   |
| P111      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_16   |
| P135      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_17   |
| P112      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_18   |
| P136      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_19   |
| P113      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_20   |
| P137      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_21   |
| P114      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_22   |
| P138      | Analog 0. . . 5 V, 0. . . 32 V Input | Analog 0. . . 25 mA Input | IO_ADC_23   |

16 multipurpose analog inputs with 12-bit resolution. The inputs can be configured to 3 different operation modes individually by software:
- Analog Voltage Input: 8 x 0 to 5 V/ 0 to 10 V, ratiometric or with **absolute reference.** - Analog Voltage Input: 8 x 0 to 5 V/ 0 to 32 V, ratiometric or with **absolute reference.** - **Analog Current Input: 16 x 0 to 25 mA, analog current loop sensors.**
All inputs are short-circuit protected, independent of application software (included in low-level driver software). Each input is provided with a first-order low pass **filter with 3 ms time constant, and** converted with 2 ms sample rate. See also section *ADC - Analog to Digital Converter driver* **of the API documentation [30].**

## 4.10.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol   | Parameter     | Note   | Min.   | Max.   | Unit   |
|----------|---------------|--------|--------|--------|--------|
| Vin      | Input voltage | 1      | -1     | +33    | V      |

Note **1 Due to thermal reasons only one of 8 inputs (except 32 V setting) may be**
shorted to 33 V at the same time. A connection to any supply voltage higher than the configured voltage setting (5 V, 10 V or 32 V) is not allowed for normal operation.

## 4.10.4 Analog Voltage Input

See Section 4.9.4 on page 117 **for more information.**

## 4.10.4.1 Characteristics Of 5 V Input (Ratiometric)

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor          | 98     | 107    | kΩ     |        |
| τin      | Input low pass filter       | 2.2    | 3.8    | ms     |        |
| Vnom     | Nominal input voltage range | 0      | 5      | V      |        |
| Vin      | Input voltage range         | 1      | 0.2    | 4.8    | V      |
| Vtol-0   | Zero reading error          | 4,5    | -15    | +15    | mV     |
| Vtol-0   | Zero reading error          | 2,4,5  | -10    | +10    | mV     |
| Vtol-p   | Proportional error          | 4,5    | -0.2   | +0.2   | %      |
| Vtol-p   | Proportional error          | 2,4,5  | -0.2   | +0.2   | %      |
| LSB      | Nominal value of 1 LSB      | -      | 1.2207 | mV     |        |

## 4.10.4.2 Characteristics Of 5 V Input (Absolute)

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor          | 98     | 107    | kΩ     |        |
| τin      | Input low pass filter       | 2.2    | 3.8    | ms     |        |
| Vnom     | Nominal input voltage range | 0      | 5      | V      |        |
| Vin      | Input voltage range         | 1      | 0.2    | 4.8    | V      |
| Vtol-0   | Zero reading error          | 3,5    | -15    | +15    | mV     |
| Vtol-0   | Zero reading error          | 2,3,5  | -10    | +10    | mV     |
| Vtol-p   | Proportional error          | 3,5    | -0.8   | +0.8   | %      |
| Vtol-p   | Proportional error          | 2,3,5  | -0.6   | +0.6   | %      |
| LSB      | Nominal value of 1 LSB      | -      | 1.2207 | mV     |        |

## 4.10.4.3 Characteristics Of 10 V Input (Absolute) Tecu **= -40. . . +125** °C

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor          | 19     | 22.5   | kΩ     |        |
| τin      | Input low pass filter       | 2.2    | 3.8    | ms     |        |
| Vnom     | Nominal input voltage range | 0      | 10     | V      |        |
| Vin      | Input voltage range         | 1      | 0.2    | 10     | V      |
| Vtol-0   | Zero reading error          | 3,5    | -18    | +18    | mV     |
| Vtol-0   | Zero reading error          | 2,3,5  | -13    | +13    | mV     |
| Vtol-p   | Proportional error          | 3,5    | -1.8   | +1.8   | %      |
| Vtol-p   | Proportional error          | 2,3,5  | -1.6   | +1.6   | %      |
| LSB      | Nominal value of 1 LSB      | -      | 2.57   | mV     |        |

## 4.10.4.4 Characteristics Of 32 V Input (Absolute)

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor          | 14.7   | 15.3   | kΩ     |        |
| τin      | Input low pass filter       | 2.2    | 3.8    | ms     |        |
| Vnom     | Nominal input voltage range | 0      | 32     | V      |        |
| Vin      | Input voltage range         | 1      | 0.2    | 32     | V      |
| Vtol-0   | Zero reading error          | 5      | -50    | +50    | mV     |
| Vtol-0   | Zero reading error          | 2,5    | -45    | +45    | mV     |
| Vtol-p   | Proportional error          | 3,5    | -4     | +4     | %      |
| Vtol-p   | Proportional error          | 2,5    | -3     | +3     | %      |
| LSB      | Nominal value of 1 LSB      | -      | 8.59   | mV     |        |

TECU **= -40. . . +125** °C

## 4.10.4.5 Characteristics Of 32 V Digital Input

| Symbol    | Parameter                             | Note                                                                                                                                                                                                                                                                                   | Min.   | Max.   | Unit   |
|-----------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|--------|
| Cin       | Pin input capacitance                 | 8                                                                                                                                                                                                                                                                                      | 12     | nF     |        |
| Rpd       | Pull-down resistor                    | 14.7                                                                                                                                                                                                                                                                                   | 15.3   | kΩ     |        |
| τin       | Input low pass filter                 | 2.2                                                                                                                                                                                                                                                                                    | 3.8    | ms     |        |
| Vil       | Input voltage for low level           | 0                                                                                                                                                                                                                                                                                      | V      |        |        |
| Vih       | Input voltage for high level          | 32                                                                                                                                                                                                                                                                                     | V      |        |        |
| LSB       | Nominal value of 1 LSB                | -                                                                                                                                                                                                                                                                                      | 8.59   | mV     |        |
| Note      | 1                                     | For full accuracy                                                                                                                                                                                                                                                                      |        |        |        |
| 2         | TECU = -40. . . +85 °C                |                                                                                                                                                                                                                                                                                        |        |        |        |
| Note Note | 3                                     | Absolute measurement. This includes the conversion error of the HY-TTC 500 only. For the calculation of the total measurement error, it is necessary to sum the error of HY-TTC 500 and the absolute sensor error (measurement tolerance plus tolerance of external sensor reference). |        |        |        |
| Note      | 4                                     | Ratiometric mode. This includes the conversion error of the HY-TTC 500 and the sensor supply error. For the calculation of the total measurement error, the error of HY-TTC 500 and the error of the ratiometric sensor (measurement tolerance) must be added.                         |        |        |        |
| Note      | 5                                     | The total measurement error is the sum of zero reading error and the proportional error.                                                                                                                                                                                                                                                                                        |        |        |        |
| Note      | Configuration by application software |                                                                                                                                                                                                                                                                                        |        |        |        |

## 4.10.5 Analog Current Input

See Section 4.9.5 on page 120 **for more information.**

## 4.10.5.1 Characteristics Of Analog Current Input Tecu **= -40. . . +125** °C

| Symbol   | Parameter              | Note                                                         | Min.   | Max.   | Unit   |
|----------|------------------------|--------------------------------------------------------------|--------|--------|--------|
| Cin      | Pin input capacitance  | 8                                                            | 12     | nF     |        |
| RCS      | Current sense resistor | 1                                                            | 177    | 185    | Ω      |
| τin      | Input low pass filter  | 2.2                                                          | 3.8    | ms     |        |
| I in     | Input current range    | 0                                                            | 25     | mA     |        |
| LSB      | Nominal value of 1 LSB | -                                                            | 6.78   | µA     |        |
| I tol-0  | Zero reading error     | 3                                                            | -70    | +70    | µA     |
| I tol-0  | Zero reading error     | 2,3                                                          | -40    | +40    | µA     |
| I tol-p  | Proportional error     | 3                                                            | -2.5   | +2.5   | %      |
| I tol-p  | Proportional error     | 2,3                                                          | -2.0   | +2.0   | %      |
| Note     | 1                      | This is the load resistor value for the current loop sensor. |        |        |        |
| Note     | 2                      | TECU = -40. . . +85 °C                                       |        |        |        |

Note **1 This is the load resistor value for the current loop sensor.**
Note 2 TECU **= -40. . . +85** °C
Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.11 Timer Inputs

![141_image_1.png]( The image is a black and white drawing of an electronic device with a lot of buttons on it. It appears to be a computer or a control panel for some sort of equipment. The buttons are arranged in rows, covering almost the entire width of the drawing.

In addition to the buttons, there is a clock visible at the top left corner of the image. This clock may indicate that the device has time-related functions or serves as a timer for various tasks.)

![141_image_0.png]( The image is a white drawing of an electronic device with multiple rows of buttons and slots. There are several rows of buttons arranged vertically, each row containing numerous buttons. Some of these buttons have green and orange lights shining through them, creating a visually appealing design.

The arrangement of the buttons and slots is organized in a way that makes it easy to understand the structure of the electronic device. The combination of colors and the clear presentation of the components make this drawing an effective representation of the device's layout.) 
Figure 34: Pinout of timer input

| Pin No.   | Function    | SW-define   |
|-----------|-------------|-------------|
| P115      | Timer Input | IO_PWD_00   |
| P139      | Timer Input | IO_PWD_01   |
| P116      | Timer Input | IO_PWD_02   |
| P140      | Timer Input | IO_PWD_03   |
| P117      | Timer Input | IO_PWD_04   |
| P141      | Timer Input | IO_PWD_05   |
| P122      | Timer Input | IO_PWD_06   |
| P146      | Timer Input | IO_PWD_07   |
| P123      | Timer Input | IO_PWD_08   |
| P147      | Timer Input | IO_PWD_09   |
| P124      | Timer Input | IO_PWD_10   |
| P148      | Timer Input | IO_PWD_11   |

12 digital inputs with timer function to process input signals such as frequency (rotational speed), pulse count and quadrature decoding (incremental length measurement), PWM etc. 6 out of 12 inputs can be alternatively used as digital (7/14 mA) current loop speed sensors. The inputs can be individually configured by software with a pull-up/pull-down resistor to adapt them to different sensor types, The timer input can be used as an analog voltage input as well. **For diagnosis, it is possible to** measure the analog voltage and frequency at the same channel **at the same time.** See also sections *PWD - Pulse Width Decode and digital timer input driver* and *DIO - Driver for* digital inputs and outputs **of the API documentation [30].**

![142_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled and described. There are two main sections within the circuit: one for digital electronics and another for analog electronics. The digital section includes a CPU (central processing unit), while the analog section features a sensor, a power supply, and other electronic components.

In addition to these primary components, there is also a bar graph present in the image, which provides more detailed information about the circuit's structure and functioning. This diagram offers an overview of the electrical system, making it easier for readers to understand its purpose and operation.)

## 4.11.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                               | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------------------|--------|--------|--------|--------|
| Vin      | Input voltage under overload conditions | -1     | +33    | V      |        |

![143_image_0.png]( The image displays a diagram of an electronic circuit with various components and connections. There are multiple wires running throughout the circuit, connecting different parts together. Some of these components include resistors, capacitors, and transistors.

In addition to the main circuitry, there is also a computer mouse on the right side of the image, which might be used for controlling or monitoring the electronic system. The diagram provides an overview of the intricate network of connections within this electronic device.)

![143_image_1.png]( The image is a diagram that illustrates a computer system's components and their relationships. There are several labels on this diagram, including "ECCU," which appears to be an essential part of the system. The diagram also features a clock, with its position in the middle of the image, indicating time management within the system.

In addition to these main elements, there is a bar graph present in the lower-left section of the image. This graph might represent data or performance metrics related to the computer system.)

![144_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled on it. There are multiple wires and connections between these components, creating a complex network. Some of the key labels include "Ecu," "Digital Input," "Analog Input," "Pulse Width Modulation (PWM)," and "ADC." The diagram also shows a series of numbers, possibly representing measurements or data related to the electrical circuit. Overall, it appears to be an intricate representation of an electronic system with multiple functions and connections.)

![144_image_1.png]( The image is a white drawing of an electrical circuit board with various components labeled on it. There are several wires and connections between these components, indicating the intricate workings of the electronic device. The labels include "cpu," "ecu," and other technical terms that help to understand the functioning of the circuit.

In addition to the main components, there is a small green box located towards the right side of the drawing, which may represent another part of the electrical system or serve as a reference point for the overall design.)

## 4.11.4 Timer And Current Loop Inputs 4.11.4.1 Characteristics Of Timer Input Tecu **= -40. . . +125** °C

| Symbol   | Parameter                                        | Note                                                                          | Min.   | Max.   | Unit   |
|----------|--------------------------------------------------|-------------------------------------------------------------------------------|--------|--------|--------|
| Rpud     | Pull-up/pull-down resistor                       | 7.5                                                                           | 10     | kΩ     |        |
| Vpu      | Pull-up voltage (open load)                      | 1                                                                             | 4.25   | 4.8    | V      |
| τin      | Input low pass filter                            | 1.4                                                                           | 3.4    | µs     |        |
| Fmax     | Maximum input frequency range                    | 20                                                                            | kHz    |        |        |
| Fmin     | Minimum input frequency                          | 0.1                                                                           | Hz     |        |        |
| τmin     | Minimum on/off time to be measured by timer unit | 20                                                                            | µs     |        |        |
| Vil      | Input voltage for low level                      | 0                                                                             | 2      | V      |        |
| Vih      | Input voltage for high level                     | 3                                                                             | 32     | V      |        |
| t res    | Timer resolution                                 | 2                                                                             | 2      | 2      | µs     |
| t res    | Timer resolution                                 | 3                                                                             | 0.5    | 0.5    | µs     |
| Note     | 1                                                | This is the input voltage with pull-up setting, without the sensor connected. |        |        |        |
| Note     | 2                                                | IO_PWD_00 - IO_PWD_05                                                         |        |        |        |
| Note     | 3                                                | IO_PWD_06 - IO_PWD_11                                                         |        |        |        |

## 4.11.4.2 Characteristics Of Current Loop Input

The timer input IO_PWD_00 to IO_PWD_05 can be alternatively **also used as digital (7/14 mA)** current loop sensor inputs. See Figure 40 **on the facing page.**
During power down (Terminal 15 **off), the ECU does not disconnect the timer and current loop**
sensor inputs. It is not recommended to supply the sensors permanently in order to prevent battery discharge. TTControl GmbH recommends one of the following 2 options:
1. Option 1**: Use a digital output for supplying the sensor. When the device is switched off, the**
ECU can perform an application-controlled shutdown, e. g., **in order to operate a cooling fan** to cool down an engine until the temperature is low enough or to store data in the non-volatile memory of the ECU. If the application controlled shut-down is finished, the ECU switches off and consumes less than 1 mA of battery current (including sensors).

2. **Option 2**: Terminal 15 **is used to supply the current loop sensor directly.**
Note that Terminal 15 **is often used to switch relays or other inductive loads directly. This** may cause transients in excess of ±50 V, for which the sensor must be specified.

| TECU = -40. . . +125 °C Symbol Parameter   | Note                                                | Min.   | Max.   | Unit   |    |
|--------------------------------------------|-----------------------------------------------------|--------|--------|--------|----|
| Rpdc                                       | Pull-down resistor (current loop config.)           | 1      | 88     | 93     | Ω  |
| Rpud                                       | Pull-up/pull-down resistor                          | 7.5    | 10     | kΩ     |    |
| Vpu                                        | Pull-up voltage (open load)                         | 4.25   | 4.8    | V      |    |
| τin                                        | Input low pass filter                               | 1.4    | 1.6    | µs     |    |
| Fmax                                       | Maximum input frequency range                       | 20     | kHz    |        |    |
| Fmin                                       | Minimum input frequency                             | 0.1    | Hz     |        |    |
| τmin                                       | Minimum on/off time to be measured by timer unit    | 20     | µs     |        |    |
| I il                                       | Input current for low level(current loop config.)   | 4      | 8.5    | mA     |    |
| I ih                                       | Input current for high level (current loop config.) | 11     | 20     | mA     |    |
| I il SRC                                   | Input current (7/14 mA) sensor SRC too low          | 2      | 0      | 4      | mA |
| I ih SRC                                   | Input current (7/14 mA) sensor SRC too high         | 3      | 20     | mA     |    |
| t res                                      | Timer resolution                                    | 2      | 2      | µs     |    |

Note **1 With software setting for digital (7/14 mA) current loop sensor inputs (ABS-type**
sensors).

Note **2 Fault detection window for defect digital (7/14 mA) current loop sensor inputs**
with too low current.

Note **3 Fault detection window for defect digital (7/14 mA) current loop sensor inputs**
with too high current. If the current exceeds the maximum input current, then overload protection gets active.

![146_image_0.png]( The image displays a diagram of an electronic circuit with various components labeled and connected to each other. There are multiple wires connecting different parts of the circuit, indicating its intricate structure.

The main components visible on the diagram include a CPU (Central Processing Unit) located near the top left corner, a memory unit situated in the middle-left area, and an ECC (Error Correcting Code) unit towards the right side of the image. Additionally, there are two transistors placed within the circuit, one at the bottom-right corner and another slightly above it.

The diagram provides a clear representation of the electronic device's internal workings, showcasing its complex design and interconnected components.)

## 4.11.5 Analog And Digital Inputs 4.11.5.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C

| Symbol     | Parameter                           | Note   | Min.   | Max.   | Unit   |
|------------|-------------------------------------|--------|--------|--------|--------|
| Resolution | 12                                  | 12     | bit    |        |        |
| Rpud       | Pull-up/pull-down resistor          | 7.5    | 10     | kΩ     |        |
| Vpu        | Pull-up voltage (open load)         | 2      | 4.25   | 4.8    | V      |
| Vin        | Input voltage range                 | 0      | 32     | V      |        |
| τin        | Input low pass filter (analog path) | 8      | 12     | ms     |        |
| Vtol-0     | Zero reading error                  | 3      | -55    | +55    | mV     |
| Vtol-0     | Zero reading error                  | 1,3    | -50    | +50    | mV     |
| Vtol-p     | Proportional error                  | 3      | -4     | +4     | %      |
| Vtol-p     | Proportional error                  | 1,3    | -3     | +3     | %      |
| LSB        | Nominal value of 1 LSB              | -      | 8.00   | mV     |        |

## 4.11.5.2 Characteristics Of Digital Input

| Symbol   | Parameter                    | Note                                                                          | Min.   | Max.   | Unit   |
|----------|------------------------------|-------------------------------------------------------------------------------|--------|--------|--------|
| Rpud     | Pull-up/pull-down resistor   | 7.5                                                                           | 10     | kΩ     |        |
| Vpu      | Pull-up voltage (open load)  | 2                                                                             | 4.25   | 4.8    | V      |
| Vin      | Input voltage range          | 0                                                                             | 32     | V      |        |
| τin      | Input low pass filter        | 2.8                                                                           | 3.2    | µs     |        |
| Vil      | Input voltage for low level  | 0                                                                             | 2      | V      |        |
| Vih      | Input voltage for high level | 3                                                                             | 32     | V      |        |
| Note     | 1                            | TECU = -40. . . +85 °C                                                        |        |        |        |
| Note     | 2                            | This is the input voltage with pull-up setting, without the sensor connected. |        |        |        |

TECU **= -40. . . +125** °C

## 4.12 High-Side Pwm Outputs 4.12.1 Pinout

![148_image_0.png]( The image is a white drawing of a large room with multiple rows of seats. There are several chairs arranged throughout the room, some placed closer to the front and others near the back. In total, there are at least 14 chairs visible in the scene.

The seating arrangement appears to be organized for an event or gathering, as it is a large space with multiple rows of seats. The chairs vary in size and position, creating a diverse and inviting atmosphere for guests attending the event.) 
Figure 41: Pinout of high-side PWM outputs The following table depicts the high-side PWM outputs together with their corresponding external and secondary shut-off group/paths and power stages.

| Pin No.   | Function             | SW-define   | Ext./Second. Shut-off   | Power stage   |
|-----------|----------------------|-------------|-------------------------|---------------|
| P153      | High-Side PWM Output | IO_PWM_00   | A                       | a             |
| P177      | High-Side PWM Output | IO_PWM_01   | A                       | a             |
| P156      | High-Side PWM Output | IO_PWM_02   | A                       | b             |
| P180      | High-Side PWM Output | IO_PWM_03   | A                       | b             |
| P159      | High-Side PWM Output | IO_PWM_04   | A                       | c             |
| P183      | High-Side PWM Output | IO_PWM_05   | A                       | c             |
| P186      | High-Side PWM Output | IO_PWM_06   | A                       | d             |
| P162      | High-Side PWM Output | IO_PWM_07   | A                       | d             |
| P189      | High-Side PWM Output | IO_PWM_08   | A                       | e             |
| P165      | High-Side PWM Output | IO_PWM_09   | A                       | e             |
| P192      | High-Side PWM Output | IO_PWM_10   | A                       | f             |
| P168      | High-Side PWM Output | IO_PWM_11   | A                       | f             |
| P195      | High-Side PWM Output | IO_PWM_12   | A                       | g             |
| P171      | High-Side PWM Output | IO_PWM_13   | A                       | g             |
| P154      | High-Side PWM Output | IO_PWM_14   | B                       | h             |
| P178      | High-Side PWM Output | IO_PWM_15   | B                       | h             |
| P157      | High-Side PWM Output | IO_PWM_16   | B                       | i             |

| Pin No.   | Function             | SW-define   | Ext./Second. Shut-off   | Power stage   |
|-----------|----------------------|-------------|-------------------------|---------------|
| P181      | High-Side PWM Output | IO_PWM_17   | B                       | i             |
| P160      | High-Side PWM Output | IO_PWM_18   | B                       | j             |
| P184      | High-Side PWM Output | IO_PWM_19   | B                       | j             |
| P187      | High-Side PWM Output | IO_PWM_20   | B                       | k             |
| P163      | High-Side PWM Output | IO_PWM_21   | B                       | k             |
| P190      | High-Side PWM Output | IO_PWM_22   | B                       | l             |
| P166      | High-Side PWM Output | IO_PWM_23   | B                       | l             |
| P193      | High-Side PWM Output | IO_PWM_24   | B                       | m             |
| P169      | High-Side PWM Output | IO_PWM_25   | B                       | m             |
| P196      | High-Side PWM Output | IO_PWM_26   | B                       | n             |
| P172      | High-Side PWM Output | IO_PWM_27   | B                       | n             |
| P101      | High-Side PWM Output | IO_PWM_28   | C                       | o             |
| P125      | High-Side PWM Output | IO_PWM_29   | C                       | o             |
| P150      | High-Side PWM Output | IO_PWM_30   | C                       | p             |
| P174      | High-Side PWM Output | IO_PWM_31   | C                       | p             |
| P102      | High-Side PWM Output | IO_PWM_32   | C                       | q             |
| P126      | High-Side PWM Output | IO_PWM_33   | C                       | q             |
| P151      | High-Side PWM Output | IO_PWM_34   | C                       | r             |
| P175      | High-Side PWM Output | IO_PWM_35   | C                       | r             |

Power output stages with freewheeling diodes for inductive **loads with low-side connection.**
The load current is controlled with PWM. For better accuracy **and diagnostics, a current measurement/feedback loop is provided.**
If an error is detected in a safety-critical system, the watchdog or the main CPU can disable the output stage (off state), triggered by the application software. For diagnostic and safety reasons, the actual PWM output signal is looped back to a timer input, and the measured value is compared to the set value. For safety-critical applications, fast error detection is necessary. For this reason, a permanent PWM output is available, setting a minimum on/off time to 100/200 µ**s instead of 0 or 100 % duty cycle. This means, there is a reliable periodical state**
change of the output allowing permanent load monitoring that is independent of the operation point.

So, even when the load is switched off, a short on the load can be detected.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *PWM - Pulse Width Modulation driver* of the API documentation [30].

![150_image_0.png]( The image displays a diagram of an electrical circuit with various components and connections. There are multiple wires running through the circuit, connecting different parts to one another. A few power supplies can be seen within the circuit, along with some switches that control the flow of electricity.

In addition to these components, there is a clock visible in the middle of the circuit, likely used for timekeeping or synchronization purposes. The diagram also includes labels and text describing the different parts and their functions, making it easier to understand the overall structure of the electrical system.)

## 4.12.2.1 Power Stage Pairing

If outputs shall be used in parallel, always combine two channels from the same double-channel power stage and use the digital output mode. See Section 4.12.1 on page 137 **for using the right** power stage outputs in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip.

For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.12.2.2 Mutual Exclusive Mode

The HY-TTC 500 uses double-channel high-side power stages. **For load leveling it is a benefit if** loads, which are switched on mutually exclusive (which means either load A, or load B is on, but not A and B at the same time), are connected to the same double-channel power stage. This reduces the thermal stress of the components. The power stage pairing is given in Section 4.12.1 on page **137.** For HS PWM output stage operating in 444–1000 Hz mode, the current limit is increased to 1 A if used in mutual exclusive mode, see Section 4.12.4.1 **on the next page.**

## 4.12.3 Maximum Ratings

| Symbol   | Parameter                               | Note   | Min.   | Max.            | Unit   |
|----------|-----------------------------------------|--------|--------|-----------------|--------|
| Vin      | Input voltage under overload conditions | 1      | -0.5   | 32              | V      |
| Vin      | Input voltage under overload conditions | 1      | -0.5   | BAT+ Power +0.5 | V      |

Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.12.4 High-Side Pwm Outputs 4.12.4.1 Characteristics Of High-Side Pwm Output Tecu **= -40. . . +125** °C

| Symbol                                   | Parameter                                   | Note   | Min.   | Max.   | Unit   |
|------------------------------------------|---------------------------------------------|--------|--------|--------|--------|
| Cout                                     | Pin input capacitance                       | 15     | 25     | nF     |        |
| Rpu                                      | Pull-up resistor                            | 4      | 5      | kΩ     |        |
| Vpu                                      | Pull-up voltage (open load)                 | 4.2    | 4.8    | V      |        |
| fPWM                                     | PWM frequency                               | 1      | 50     | 1000   | Hz     |
| Tmin-on                                  | Minimum on time                             | 2      | 100    | µs     |        |
| Tmin-off                                 | Minimum off time                            | 2      | 200    | µs     |        |
| Ron                                      | On-resistance                               | 150    | mΩ     |        |        |
| Imax                                     | Maximum load current (f = 50. . . 200 Hz)   | 3      | A      |        |        |
| Imax                                     | Maximum load current (f = 50. . . 200 Hz)   | 3      | 4      | A      |        |
| Imax                                     | Maximum load current (f = 210. . . 400 Hz)  | 1.2    | A      |        |        |
| Imax                                     | Maximum load current (f = 444. . . 1000 Hz) | 0.1    | A      |        |        |
| Imax                                     | Maximum load current (f = 444. . . 1000 Hz) | 4      | 1      | A      |        |
| Ipeak                                    | Peak load current limit                     | 5      | 5.5    | A      |        |
| Rload_min Minimum coil resistance (12 V) | 6                                           | 2      | Ω      |        |        |
| Rload_min Minimum coil resistance (24 V) | 6                                           | 4      | Ω      |        |        |
| Rload_max Maximum load resistance        | 7                                           | 1      | kΩ     |        |        |

Note **1 Not all values for PWM frequency are possible, see section** PWM - Pulse Width Modulation driver **of the API documentation [30] for supported frequency values**
Note **2 Instead of 0 % or 100 % output, minimum on/off time is inserted automatically**
when the output is configured to be safety critical. This is necessary for optimal load diagnostics.

Note 3 TECU **= -40. . . +85** °C
Note **4 HS power stage used in mutual exclusive mode**
Note 5 For t < **5 ms**
Note 6 Additionally to observing the maximum load current limit, **there is also a minimum load resistance limit, depending on the battery supply voltage.**
Note **7 Exceeding this value will trigger open load detection.**

## 4.12.4.2 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

The diagnostic functions are different between PWM and digital operation:

## - Pwm-Operated High-Side Output (Duty Cycle 0 % < X < **100 %)**:

Under normal load conditions, the feedback signals to the timer unit and the ADC follow the corresponding PWM output. In case of a disconnected load (open load), the output is pulled to 5 V by an internal resistor. If there is a short circuit to ground, the feedback signals are constantly low. A short circuit to BAT+ implicates that the feedback signals are pulled to 5 V, which also results in a constantly high level. By merging the **measurement results from the** timer and the ADC unit, it is possible to differentiate the diagnostic functions, as shown in the table below.

Output Signal Status Signal Normal Open Load Short to GND Short to UBAT
0 % < X < **100 %**

## = Detected - Digitally Operated High-Side Output (True Duty Cycle Of 0 Or **100 %, Without Min. And** Max. Pulses):

When the power stage is switched off, the monitoring interface will read back low level if the load is properly connected or if there is a short circuit to ground. In case of open load or short circuit to BAT+ the monitoring interface will read back high **level.**
When the power stage is switched on, a high level will be read back in case of normal operation. In case of excessive overload or short circuit to ground, the output switches off in order to protect the output stage. In this case, the monitoring interface will read back a low level. The possible diagnostic functions of the digital operation **are shown in the table below.**

| Output Signal   | Status Signal   |              |               |
|-----------------|-----------------|--------------|---------------|
| Normal          | Open Load       | Short to GND | Short to UBAT |
| On              | ×               | ×            |               |
| Off             | ×               |              |               |

= detected
× **= not detected**

## 4.12.4.3 Characteristics Of Current Measurement Tecu **= -40. . . +125** °C

| Symbol   | Parameter                                      | Note                                                                          | Min.   | Max.   | Unit   |
|----------|------------------------------------------------|-------------------------------------------------------------------------------|--------|--------|--------|
| I tol-p  | Proportional error                             | 1,2                                                                           | -2.5   | +2.5   | %      |
| I tol-p  | Proportional error                             | 4,2                                                                           | -2.0   | +2.0   | %      |
| I tol-0  | Zero reading error                             | 1,2                                                                           | -40    | +40    | mA     |
| I tol-0  | Zero reading error                             | 1,2,4                                                                         | -35    | +35    | mA     |
| LSB      | Nominal value of 1 LSB                         | -                                                                             | 1      | mA     |        |
| fg_LP    | Cut off frequency of 3rd order low pass filter | 3                                                                             | 30     | 50     | Hz     |
| Note     | 1                                              | The measured value is clipped in software if below zero. So at some devices a |        |        |        |

Note **1 The measured value is clipped in software if below zero. So at some devices a**
small output current is necessary to get ADC-values greater **than zero.**
Note 2 The total error (Itol**) is the sum of proportional error and zero reading error:**
Itol = ±(Itol − p
⋅Iload +Itol −0)
Note **3 An active low pass filter (3rd order) is provided to reduce current ripple from**
the ADC input. Further digital filtering is applied to eliminate the current ripple completely and provide a stable measurement value for the application.

Note 4 TECU = -40. . . +85 °C

## 4.12.5 High-Side Digital Outputs

When pulse width modulation is not necessary, the output can **be configured as a simple digital** output. This output mode is only allowed for non-safety critical applications, otherwise the high-side PWM mode needs to be used.

## 4.12.5.1 Characteristics Of High-Side Digital Output

| Symbol                                   | Parameter                   | Note                                                   | Min.   | Max.   | Unit   |
|------------------------------------------|-----------------------------|--------------------------------------------------------|--------|--------|--------|
| Cout                                     | Pin input capacitance       | 15                                                     | 25     | nF     |        |
| Rpu                                      | Pull-up resistor            | 4                                                      | 5      | kΩ     |        |
| Vpu                                      | Pull-up voltage (open load) | 4.2                                                    | 4.7    | V      |        |
| Ron                                      | On-resistance               | 150                                                    | mΩ     |        |        |
| Imax                                     | Maximum load current        | 3                                                      | A      |        |        |
| Imax                                     | Maximum load current        | 1                                                      | 4      | A      |        |
| Ipeak                                    | Peak load current limit     | 2                                                      | 5.5    | A      |        |
| Rload_min Minimum coil resistance (12 V) | 3                           | 2                                                      | Ω      |        |        |
| Rload_min Minimum coil resistance (24 V) | 3                           | 4                                                      | Ω      |        |        |
| Rload_max Maximum load resistance        | 4                           | 1                                                      | kΩ     |        |        |
| Note                                     | 1                           | TECU = -40. . . +85 °C                                 |        |        |        |
| Note                                     | 2                           | For t < 5 ms                                           |        |        |        |
| Note                                     | 3                           | Additionally to observing the maximum load current limit, there is also a minimum load resistance limit, depending on the battery supply voltage.                                                        |        |        |        |
| Note                                     | 4                           | Exceeding this value will trigger open load detection. |        |        |        |

## Tecu **= -40. . . +125** °C

See Section 4.12.4.3 on page 142 **for characteristics of current measurement.**

## 4.12.6 Digital And Frequency Inputs

If a high-side output is not needed on IO_PWM_00 - IO_PWM_35, **the loop-back path of these** output stages can be alternatively used as a digital or frequency input. External switches which are directly switching to battery voltage must not be used with alternative inputs. See Section 6.6 on page 218 **for more information on using the alternative digital and frequency** input function of the High-Side PWM Outputs.

## 4.12.6.1 Characteristics Of Digital Input

| Symbol   | Parameter                    | Note   | Min.   | Max.            | Unit   |
|----------|------------------------------|--------|--------|-----------------|--------|
| Cin      | Pin input capacitance        | 15     | 25     | nF              |        |
| τin      | Input low pass filter        | 1.4    | 3.4    | µs              |        |
| Rpu      | Pull-up resistor             | 4      | 5      | kΩ              |        |
| Vpu      | Pull-up voltage              | 4.2    | 4.8    | V               |        |
| Vil      | Input voltage for low level  | 0      | 2      | V               |        |
| Vih      | Input voltage for high level | 1      | 3      | 32              | V      |
| Vin      | Input voltage range          | 1      | -0.5   | BAT+ Power +0.5 | V      |

Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.12.6.2 Characteristics Of Timer Input

| TECU = -40. . . +125 °C Symbol Parameter   | Note                                              | Min.   | Max.   | Unit            |    |
|--------------------------------------------|---------------------------------------------------|--------|--------|-----------------|----|
| Cin                                        | Pin input capacitance                             | 15     | 25     | nF              |    |
| τin                                        | Input low pass filter                             | 1.4    | 3.4    | µs              |    |
| Rpu                                        | Pull-up resistor                                  | 4      | 5      | kΩ              |    |
| Vpu                                        | Pull-up voltage                                   | 4.25   | 4.8    | V               |    |
| fmax                                       | Maximum input frequency                           | 1      | 2      | kHz             |    |
| fmax                                       | Maximum input frequency                           | 2      | 10     | kHz             |    |
| fmin                                       | Minimum input frequency                           | 3      | 0.1    | Hz              |    |
| t res                                      | Timer resolution                                  | 1      | 1      | µs              |    |
| tmin                                       | Minimum on/off time to be measured by timer input | 20     | µs     |                 |    |
| Vil                                        | Input voltage for low level                       | 0      | 2      | V               |    |
| Vih                                        | Input voltage for high level                      | 4      | 3      | 32              | V  |
| Vin                                        | Input voltage range                               | 4      | -0.5   | BAT+ Power +0.5 | V  |

Note **1 With open collector sensor output.** Note **2 With push-pull sensor output stage.** Note **3 Due to the dynamic range of the timer, there is a minimum frequency when a**
timer overflow occurs. Even at a lower frequency the output value will be read as 0 Hz.

Note **4 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.12.7 Secondary Shut-Off Paths

The available PWM output stages are allocated to three independent secondary shut-off paths (=Safety switches). See Section 4.12.1 on page **137, column** *Ext./Second. Shut-Off* **of pinout table.** For safety-critical applications, these paths allow to selectively activate/deactivate a set of specific PWM outputs in case of a detected actuator failure. Thus, the **ECU can be operated in a reduced** (limp home) mode that allows the vehicle to be safely driven to the repair shop. Figure 43 **on the current page shows the detailed distribution of the PWM output stages to the**
shut-off paths.

See Section 5.1.1 on page 188 **for safety concept overview.**

![157_image_0.png]( The image displays a diagram of an electrical system with multiple power sources and connections. There are several wires and cables running through the scene, indicating various components within the system.

In addition to the main power source, there is a smaller one located towards the right side of the image. A number of other smaller power sources can be seen throughout the diagram, with some placed closer to the center and others near the edges. The arrangement of these power sources suggests that they are part of an intricate electrical network or system.)

## 4.12.8 External Shut-Off Groups

6 analog inputs can be configured acting as external activating or deactivating switch input for shutoff groups A, B and C, see Figure 43 **on the preceding page.**
The external analog input pins can deactivate the shut-off groups independently of the watchdog functionality and the application software as well. List of analog input pins to shut-off group mapping:

Pin No. Function SW-define **Shut-Off Group**

P112 0. . . 32 V Input IO_ADC_18 A P136 0. . . 32 V Input IO_ADC_19 A P113 0. . . 32 V Input IO_ADC_20 B P137 0. . . 32 V Input IO_ADC_21 B P114 0. . . 32 V Input IO_ADC_22 C

P138 0. . . 32 V Input IO_ADC_23 C

Depending on the voltage level on the external pin(s), the software driver switches the corresponding shut-off group ON or OFF within the previously configured failure reaction time. 2 Analog Inputs have to be used in parallel for each shut-off group to guarantee SIL 2 Level.

## 4.12.8.1 Characteristics Of External Shut-Off

TECU **= -40. . . +125** °C
Note 1 TECU **= -40. . . +85** °C
Note 2 The total measurement error is the sum of zero reading error and the proportional error.

| Symbol   | Parameter                                        | Note   | Min.   | Max.   | Unit   |
|----------|--------------------------------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance                            | 8      | 12     | nF     |        |
| Rpd      | Pull-down resistor                               | 14.7   | 15.3   | kΩ     |        |
| Vin      | Input voltage range                              | 0      | 32     | V      |        |
| Vil      | Input voltage level to signal a low level input  | 0      | 4      | V      |        |
| Vih      | Input voltage level to signal a high level input | 6      | 32     | V      |        |
| Vtol-0   | Zero reading error                               | 2      | -50    | +50    | mV     |
| Vtol-0   | Zero reading error                               | 1,2    | -45    | +45    | mV     |
| Vtol-p   | Proportional error                               | 2      | -4     | +4     | %      |
| Vtol-p   | Proportional error                               | 1,2    | -3     | +3     | %      |
| LSB      | Nominal value of 1 LSB                           | -      | 8.59   | mV     |        |

## 4.12.9 Tertiary Shut-Off Path 4.12.9.1 Functional Description

Loads on safety-critical high-side PWM channels can be connected to the ground as shown in Figure 42 on page 139 or to a low-side digital output as shown in Figure 44 **on the current page.**

![159_image_0.png]( The image displays a diagram of an electronic circuit with various components and connections. There are multiple wires and cables that connect different parts of the circuit, indicating its intricate design. Some key components include resistors, capacitors, and transistors.

The diagram is labeled with numbers, likely representing specific positions or functions within the circuit. The presence of these labels helps in understanding the structure and functioning of the electronic device.)

With the tertiary shut-off configuration shown in 44 **the HY-TTC 500 is able to switch off the high-side** PWM channels even if the load has a short circuit to the positive battery supply.

Please refer to section *PWM - Pulse Width Modulation driver* **of the API documentation [30] for more** information how to configure such an output.

4.13 High-Side Digital Outputs 4.13.1 Pinout Figure 45: Pinout of high-side digital outputs

| Pin No.   | Function                 | SW-define   | Power stage   |
|-----------|--------------------------|-------------|---------------|
| P149      | High-Side Digital Output | IO_DO_00    | a             |
| P173      | High-Side Digital Output | IO_DO_01    | a             |
| P152      | High-Side Digital Output | IO_DO_02    | b             |
| P176      | High-Side Digital Output | IO_DO_03    | b             |
| P155      | High-Side Digital Output | IO_DO_04    | c             |
| P179      | High-Side Digital Output | IO_DO_05    | c             |
| P158      | High-Side Digital Output | IO_DO_06    | d             |
| P182      | High-Side Digital Output | IO_DO_07    | d             |

Eight power output stages with freewheeling diodes for inductive and resistive loads with low-side connection. Suitable loads are lamps, valves, relays etc. If an error is detected in a safety-critical resource, the watchdog CPU or the main CPU will disable the output stage (off state). For diagnostic reasons, the output signal is looped back to the CPU, and the value measured is compared with the value set. When the output is not used, the loop-back signal can be used as an analog input or as a digital input.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

![161_image_0.png]( The image displays a diagram of an electronic circuit with various components connected to each other. There are multiple wires and connections throughout the circuit, indicating that it is a complex system.

In addition to the wiring, there are several labels on the circuit, providing information about the different parts. Some of these labels include "CPU," "ECC," "Salt Power," "Watchdog," "Digital Input," "Digital Output," and "ACC." The presence of these labels suggests that this is a well-designed electronic system with specific functions and purposes.)

## 4.13.2.1 Power Stage Pairing

If outputs shall be used in parallel, always combine two channels from the same double-channel power stage and use the digital output mode. See Section 4.13.1 on page 149 **for using the right** power stage outputs in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip.

For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.13.2.2 Mutual Exclusive Mode

The HY-TTC 500 uses double-channel high-side power stages. **For load leveling it is a benefit if** loads, which are switched on mutually exclusive (which means either load A, or load B is on, but not A and B at the same time), are connected to the same double-channel power stage. This reduces the thermal stress of the components. The power stage pairing is given in Section 4.13.1 on page **149.**

## 4.13.3 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

![162_image_0.png]( The image displays a graph with multiple lines and buttons, likely representing various types of signals or settings. There are two main sets of lines, one on the left side and another on the right side of the graph. Each set consists of several lines, which could be related to different signal types or levels.

In addition to the lines, there are multiple buttons scattered around the graph, possibly for adjusting settings or controlling the signals displayed. The buttons can be found in various positions, such as at the top, bottom, and sides of the graph. Overall, the image presents a complex visual representation of different signal types and their corresponding settings.)

![162_image_1.png]( The image displays a computer screen with several lines of text written on it. The text appears to be related to a conversation or discussion involving multiple people. There are at least five distinct sets of text visible within the image, each possibly representing different participants in the conversation.

The text is organized across various rows and columns, creating an organized appearance. Some of the lines of text are positioned closer together, while others are spaced further apart, indicating a dynamic and engaging discussion taking place on the screen.)

## 4.13.4 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                                      | Note   | Min.            | Max.   | Unit   |
|----------|------------------------------------------------|--------|-----------------|--------|--------|
| Vin      | Input/output voltage under overload conditions | -0.5   | BAT+ Power +0.5 | V      |        |

## 4.13.5 High-Side Digital Outputs 4.13.5.1 Characteristics Of High-Side Output Tecu **= -40. . . +125** °C

| Symbol   | Parameter                   | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8      | 12     | nF     |        |
| Rpud     | Pull-up/pull-down resistor  | 7.5    | 10     | kΩ     |        |
| Vpu      | Pull-up voltage (open load) | 4      | 4.5    | V      |        |
| Ron      | On-resistance               | 100    | mΩ     |        |        |
| I load   | Nominal load current        | 0      | 3      | A      |        |
| I load   | Nominal load current        | 1      | 0      | 4      | A      |
| Ipeak    | Peak load current           | 2      | 0      | 6      | A      |
| I tol-p  | Proportional error          | 3      | -14    | +14    | %      |
| I tol-p  | Proportional error          | 1,3    | -10    | +10    | %      |
| I tol-0  | Zero reading error          | 3      | -150   | +150   | mA     |
| I tol-0  | Zero reading error          | 1,3    | -150   | +150   | mA     |

Note 1 TECU **= -40. . . +85** °C
Note **2 Peak current for not more than 100 ms. Exceeding this value will trigger the**
overload protection and switch off the power stage. Steady state operation goes only up to 3 A/4 A depending on temperature.

Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.13.6 Analog And Digital Inputs

External switches which are directly switching to battery voltage must not be used with alternative inputs. See Section 6.6 on page 218 **for more information.**

## 4.13.6.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C

| Symbol     | Parameter                           | Note   | Min.   | Max.            | Unit   |
|------------|-------------------------------------|--------|--------|-----------------|--------|
| Cin        | Pin input capacitance               | 8      | 12     | nF              |        |
| τin        | Input low pass filter (analog path) | 1.5    | 2.5    | ms              |        |
| Rpud       | Pull-up/pull-down                   | 1      | 7.5    | 10              | kΩ     |
| Vpu        | Pull-up voltage (open load)         | 4      | 4.5    | V               |        |
| Resolution | 12                                  | 12     | bit    |                 |        |
| Vtol-0     | Zero reading error                  | 3      | -55    | +55             | mV     |
| Vtol-0     | Zero reading error                  | 1,3    | -50    | +50             | mV     |
| Vtol-p     | Proportional error                  | 3      | -4     | +4              | %      |
| Vtol-p     | Proportional error                  | 1,3    | -3     | +3              | %      |
| LSB        | Nominal value of 1 LSB              | -      | 13.4   | mV              |        |
| Vin        | Input voltage measurement range     | 2      | 0      | 32              | V      |
| Vin        | Input voltage range                 | 2      | -0.5   | BAT+ Power +0.5 | V      |

Note 1 TECU **= -40. . . +85** °C
Note **2 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**

## 4.13.6.2 Characteristics Of Digital Input Tecu **= -40. . . +125** °C

| Symbol     | Parameter                    | Note   | Min.   | Max.            | Unit   |
|------------|------------------------------|--------|--------|-----------------|--------|
| Cin        | Pin input capacitance        | 8      | 12     | nF              |        |
| τin        | Input low pass filter        | 1.5    | 2.5    | ms              |        |
| Rpud       | Pull-up/pull-down resistor   | 7.5    | 10     | kΩ              |        |
| Vpu        | Pull-up voltage (open load)  | 4      | 4.5    | V               |        |
| Resolution | 12                           | 12     | bit    |                 |        |
| Vil        | Input voltage for low level  | 0      | V      |                 |        |
| Vih        | Input voltage for high level | 1      | 32     | V               |        |
| Vin        | Input voltage range          | 1      | -0.5   | BAT+ Power +0.5 | V      |

Note **Configuration by application software**
Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

4.14 High-Side Digital/PVG/VOUT Outputs 4.14.1 Pinout Figure 47: Pinout of High-side digital/PVG/VOUT outputs

| Pin No.   | Function                          | SW-define   | Power stage   |
|-----------|-----------------------------------|-------------|---------------|
| P161      | High-Side Digital Output/PVG/VOUT | IO_PVG_00   | a             |
| P185      | High-Side Digital Output/PVG/VOUT | IO_PVG_01   | a             |
| P188      | High-Side Digital Output/PVG/VOUT | IO_PVG_02   | b             |
| P164      | High-Side Digital Output/PVG/VOUT | IO_PVG_03   | b             |
| P191      | High-Side Digital Output/PVG/VOUT | IO_PVG_04   | c             |
| P167      | High-Side Digital Output/PVG/VOUT | IO_PVG_05   | c             |
| P194      | High-Side Digital Output/PVG/VOUT | IO_PVG_06   | d             |
| P170      | High-Side Digital Output/PVG/VOUT | IO_PVG_07   | d             |

Output stages for interfacing to PVG type hydraulic valve groups (PVG mode), for low power analog voltage loads (VOUT **mode) or for high power inductive/resistive loads (HS mode).**
All eight outputs can be configured independently of each other.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *PVG - Proportional Valve output driver* **of the API documentation [30].**

## 4.14.2.1 Power Stage Pairing

If outputs shall be used in parallel, always combine two channels from the same double-channel power stage and use the digital output mode. See Section 4.14.1 **on the previous page for using** the right power stage outputs in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip. For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.14.2.2 Mutual Exclusive Mode

The HY-TTC 500 uses double-channel high-side power stages. **For load leveling it is a benefit if** loads, which are switched on mutually exclusive (which means either load A, or load B is on, but not A and B at the same time), are connected to the same double-channel power stage. This reduces the thermal stress of the components. The power stage pairing is given in Section 4.14.1 **on the**
preceding page.

## 4.14.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                                      | Note   | Min.            | Max.   | Unit   |
|----------|------------------------------------------------|--------|-----------------|--------|--------|
| Vin      | Input/output voltage under overload conditions | -0.5   | BAT+ Power +0.5 | V      |        |

## 4.14.4 High-Side Digital Outputs

Eight power output stages with freewheeling diodes for inductive and resistive loads with low-side connection. Suitable loads are lamps, valves, relays etc. If an error is detected in a safety-critical resource, the watchdog CPU or the main CPU can disable the output stage (off state). For diagnostic reasons the output signal is looped back to the CPU, and the value measured is compared with the value set. When the output is not used, the loop-back signal can be used as an analog input or as a digital input.

![168_image_0.png]( The image features a diagram depicting an electronic circuit with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts of the system. Some key components include a CPU (central processing unit), a digital output, a watchdog timer, and a power supply.

In addition to these main components, there is also an A/D converter present in the circuit. The diagram provides a clear visual representation of how these electronic components work together within the system.)

## 4.14.4.1 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and detection of load loss.

| Output Signal   | Status Signal   |              |               |
|-----------------|-----------------|--------------|---------------|
| Normal          | Open Load       | Short to GND | Short to UBAT |
| On              | ×               | ×            |               |
| Off             | ×               |              |               |

= detected
× **= not detected**

## 4.14.4.2 Characteristics Of High-Side Digital

TECU **= -40. . . +125** °C

| Symbol   | Parameter                   | Note                                                                        | Min.   | Max.   | Unit   |
|----------|-----------------------------|-----------------------------------------------------------------------------|--------|--------|--------|
| Cin      | Pin input capacitance       | 8                                                                           | 12     | nF     |        |
| Rpud     | Pull-up/pull-down resistor  | 2.5                                                                         | 2.6    | kΩ     |        |
| Vpu      | Pull-up voltage (open load) | 2.15                                                                        | 2.45   | V      |        |
| Ron      | On-resistance               | 100                                                                         | mΩ     |        |        |
| I load   | Nominal load current        | 0                                                                           | 3      | A      |        |
| Imax     | Maximum load current        | 1                                                                           | 4      | A      |        |
| Ipeak    | Peak load current           | 2                                                                           | 0      | 6      | A      |
| I tol-p  | Proportional error          | 3                                                                           | -14    | +14    | %      |
| I tol-p  | Proportional error          | 1,3                                                                         | -10    | +10    | %      |
| I tol-0  | Zero reading error          | 3                                                                           | -150   | +150   | mA     |
| I tol-0  | Zero reading error          | 1,3                                                                         | -150   | +150   | mA     |
| Note     | 1                           | TECU = -40. . . +85 °C                                                      |        |        |        |
| Note     | 2                           | Peak current for maximal 100 ms. Exceeding this value will trigger overload |        |        |        |

Note 1 TECU **= -40. . . +85** °C
Note **2 Peak current for maximal 100 ms. Exceeding this value will trigger overload**
protection and switch off the power stage.Steady state operation goes only up to 3 A/4 A depending on temperature.

Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.14.5 Pvg Outputs

Proportional Valve Groups (PVG) are a group of hydraulic load-sensing valves with integrated electronics allowing advanced flow controllability, e.g., for load-independent flow control.

![170_image_0.png]( The image is a diagram that shows an electrical circuit with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts of the system.

In addition to the wires, there are several labels on the diagram, indicating the names or functions of the individual components. These include "PVC," "EUC," "VPG," "VPC," and "CPU." The diagram also features a green box with an AC/DC symbol, suggesting that it may be related to power supply or conversion.

Overall, the image provides a clear visual representation of the electrical circuit's structure and its various components.) For diagnostic reasons in output mode, the output signal is looped back to the CPU, and the measured value is compared to the set value. If the difference between these two values is above a fixed limit, an overload is detected, and the output is disabled. The protection mechanism tries re-enabling the output 10 times per drive cycle. It is not allowed to use two outputs in parallel to increase driving strength.

The PVG output can be used to control PVG valves of the types PVEA, PVEH and PVES. These types of valves apply a low pass filter to the input signal and use the resulting DC voltage in relation to the valves supply voltage (BAT+) as a parameter for flow control. The HY-TTC 500 uses the BAT+ CPU pin as a reference voltage input. The principle schematic is shown in Figure 49 **on the current page. The output is open loop controlled. The ADC input is for** diagnostic purposes only and can be evaluated by the application software.

## 4.14.5.1 Characteristics Of Pvg

| TECU = -40. . . +125 °C Symbol Parameter   | Note                                                 | Min.   | Max.       | Unit       |    |
|--------------------------------------------|------------------------------------------------------|--------|------------|------------|----|
| Cout                                       | Pin capacitance                                      | 430    | 530        | nF         |    |
| Rout                                       | Output resistance                                    | 2.5    | 2.6        | kΩ         |    |
| Vnom                                       | Nominal voltage range (BAT+ = 8. . . 32 V, nominal   | 1,2    | 0.1 ⋅ BAT+ | 0.9 ⋅ BAT+ | V  |
| load resistance)                           |                                                      |        |            |            |    |
| Vtol-p                                     | Proportional error (BAT+ = 8. . . 32 V, nominal load | 1,3    | -2         | +2         | %  |
| resistance)                                |                                                      |        |            |            |    |
| Vtol-0                                     | Zero reading error (BAT+ = 8. . . 32 V, nominal load | 1,3    | -100       | +100       | mV |
| resistance)                                |                                                      |        |            |            |    |

Note 1 The PVG valves use a voltage divider with 2 ⋅ 24 k Ω **between ground and**
BAT+. This is equivalent to 1 ⋅ 12 k Ω **against 50 % of BAT+.**
Note 2 The standard PVG valves are controllable between 25 % and 75 **% of BAT+.**
This specification parameter is to show the HW-related control limits only.

Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.14.6 Vout Outputs

In VOUT **mode, the outputs generate a DC voltage that can be used to connect to any high-impedance**
analog input. The load resistance of the receiving device defines the maximum possible output voltage.

![172_image_0.png]( The image displays a diagram of an electronic circuit with various components and connections. There are two main parts to the circuit: a power supply and a control system. The power supply consists of multiple batteries, while the control system features a CPU and a green box.

The circuit is made up of numerous wires that connect different components together. Some of these wires can be seen in the middle section of the diagram, while others are located closer to the top or bottom edges. The overall layout of the circuit appears complex, with multiple connections between various parts.)

In PVG mode, PVG valves have a well-defined input resistance, **and the output signal settings can** be calculated in advance by considering the characteristics of the output stage. In voltage mode, however, a PID controller must be applied to generate the desired output voltage. This results in a certain settling time, which depends on the parameter set of **the PID controllers.**
The VOUT **mode output can be used to control PVG valves of the type PVEU or other generic resistive**
loads.

For diagnostic reasons, the output signal is looped back to the CPU in output mode, and the measured value is compared to the set value. If the difference between these two values is above a fixed limit, an overload is detected and the output is disabled. The protection mechanism tries to reenable the output 10 times per drive cycle. It is not allowed to use two outputs in parallel to increase driving strength.

## 4.14.6.1 Characteristics Of Vout

| TECU = -40. . . +125 °C Symbol Parameter   | Note                                    | Min.        | Max.   | Unit   |        |
|--------------------------------------------|-----------------------------------------|-------------|--------|--------|--------|
| Cout                                       | Pin capacitance                         | 430         | 530    | nF     |        |
| Rout                                       | Output resistance                       | 2.5         | 2.6    | kΩ     |        |
| I load                                     | Nominal load current                    | 0           | 5      | mA     |        |
| 1                                          | 0.0 ⋅ BAT+                              | 0.99 ⋅ BAT+ |        |        |        |
| Vnom                                       | Nominal                                 | voltage     | range  | (open  | load), |
| BAT+ = 8. . . 32 V                         |                                         |             |        |        |        |
| Vtol-p                                     | Proportional error (BAT+ = 8. . . 32 V) | 3           | -2     | +2     | %      |
| Vtol-p                                     | Proportional error (BAT+ = 8. . . 32 V) | 2,3         | -1.5   | +1.5   | %      |
| Vtol-0                                     | Zero error (BAT+ = 8. . . 32 V)         | 3           | -300   | +300   | mV     |
| Vtol-0                                     | Zero error (BAT+ = 8. . . 32 V)         | 2,3         | -200   | +200   | mV     |

Note **1 In the VOUT setting, the open load voltage is only open loop controlled. The**
load creates a voltage divider with the well-defined output resistance (Rout) of the VOUT stage. This effect must be considered in the application SW. To get a desired (loaded) output voltage the proper open load voltage must be calculated and set to a (higher) open load voltage level. For **example, with a**
load RL = 10 kΩ **to ground the open load voltage (Vset) must be set to 12.55 V**
(Vset = *Vout* RL+2.55 *kohm* RL **) to get an output voltage of 10 V.**
Note 2 TECU **= -40. . . +85** °C
Note 3 The total error is the sum of zero error and the proportional error.

## 4.14.7 Analog And Digital Inputs

This input type is suitable for low impedance switches and sensors only. For standard analog senors please use Analog Input 2 Modes (Section 4.10 on page **124) and Analog Input 3 Modes (Section** 4.9 on page **116).** External switches which are directly switching to battery voltage must not be used with alternative inputs. See Section 6.6 on page 218 **for more information.**

## 4.14.7.1 Characteristics Of Analog Voltage Input

| TECU = -40. . . +125 °C Symbol Parameter   | Note                            | Min.   | Max.   | Unit            |    |
|--------------------------------------------|---------------------------------|--------|--------|-----------------|----|
| Cin                                        | Pin input capacitance           | 384    | 576    | nF              |    |
| τin                                        | Input low pass filter           | 8      | 12     | ms              |    |
| Rpud                                       | Pull-up/pull-down resistor      | 2.5    | 2.6    | kΩ              |    |
| Vpu                                        | Pull-up voltage (open load)     | 4.7    | 5.1    | V               |    |
| Resolution                                 | 12                              | 12     | bit    |                 |    |
| Vtol-0                                     | Zero reading error              | 3      | -55    | +55             | mV |
| Vtol-0                                     | Zero reading error              | 1,3    | -50    | +50             | mV |
| Vtol-p                                     | Proportional error              | 3      | -4     | +4              | %  |
| Vtol-p                                     | Proportional error              | 1,3    | -3     | +3              | %  |
| LSB                                        | Nominal value of 1 LSB          | -      | 8      | mV              |    |
| Vin                                        | Input voltage measurement range | 2      | 0      | 32              | V  |
| Vin                                        | Input voltage range             | 2      | -0.5   | BAT+ Power +0.5 | V  |

Note 1 TECU **= -40. . . +85** °C
Note **2 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**

## 4.14.7.2 Characteristics Of Digital Input Tecu **= -40. . . +125** °C

Symbol Parameter Note Min. Max. **Unit**

Cin Pin input capacitance **384 576 nF**

τin Input low pass filter **8 12 ms** Rpud **Pull-up/pull-down resistor 2.5 2.6 k**Ω

Vpu **Pull-up voltage (open load) 4.7 5.1 V**

Resolution **12 12 bit**

Vil Input voltage for low level 0 V

| Symbol   | Parameter                             | Note   | Min.   | Max.            | Unit   |
|----------|---------------------------------------|--------|--------|-----------------|--------|
| Vih      | Input voltage for high level          | 1      | 32     | V               |        |
| Vin      | Input voltage range                   | 1      | -0.5   | BAT+ Power +0.5 | V      |
| Note     | Configuration by application software |        |        |                 |        |

Note **Configuration by application software**
Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

4.15 Low-Side Digital Outputs 4.15.1 Pinout

![176_image_1.png]( The image features a large white circle with several small circles inside it. These smaller circles are arranged around the edges of the larger circle and appear to be connected by lines. There is also a row of numbers displayed on the outer edge of the larger circle, which may represent data or measurements related to the smaller circles. Overall, the image seems to depict an intricate design or pattern that combines both geometric shapes and numerical information.)

![176_image_0.png]( The image is a white drawing of an empty room with a large number of chairs arranged throughout the space. There are at least twelve chairs visible, each positioned in various locations within the room. Some chairs are placed closer to the walls, while others are situated more centrally. The arrangement of these chairs creates a sense of organization and orderliness within the room.) 

| Pin No.   | Function                | SW-define   |
|-----------|-------------------------|-------------|
| P251      | Low-Side Digital Output | IO_DO_08    |
| P238      | Low-Side Digital Output | IO_DO_09    |
| P252      | Low-Side Digital Output | IO_DO_10    |
| P239      | Low-Side Digital Output | IO_DO_11    |
| P253      | Low-Side Digital Output | IO_DO_12    |
| P240      | Low-Side Digital Output | IO_DO_13    |
| P254      | Low-Side Digital Output | IO_DO_14    |
| P241      | Low-Side Digital Output | IO_DO_15    |

Eight low-side switches with freewheeling diodes to a clamping structure for inductive and resistive

![177_image_0.png]( The image displays a diagram of an electrical circuit with various components and connections. There are multiple wires running through the circuit, connecting different parts of the system. A power supply is visible at one end of the circuit, while other components like capacitors and resistors can be found throughout the network.

In addition to these components, there are several labels on the diagram indicating their functions or designations. The overall arrangement of the wires and components suggests a well-organized electrical system that may be used for various purposes such as powering electronic devices or controlling specific functions within a larger device.) loads.

The current through the low-side switch is monitored and triggers the opening in case of overcurrent. Short-circuit and overload protection is included in low-level driver software. Before a tripped channel can be re-enabled, the overload situation has to be removed.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *DIO - Driver for digital inputs and outputs* **of the API documentation [30].**

## 4.15.2.1 Power Stage Pairing

If higher load current is needed, the output stages can be used in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip. For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.15.3 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

![178_image_0.png]( The image displays a graph with several different colored lines on it, possibly representing various types of data or information. There are multiple green dots scattered throughout the graph, which could represent individual data points or markers for specific events.

In addition to the main graph, there is a smaller graph located towards the top right corner of the image. The presence of these graphs suggests that they may be used for analyzing and visualizing different aspects of a particular subject or process.)

![178_image_1.png]( The image is a close-up of a white background with text that reads "United." This word appears to be part of a larger phrase or sentence.)

× **= not detected**

## 4.15.4 Maximum Ratings

| Symbol   | Parameter                                      | Note   | Min.            | Max.   | Unit   |
|----------|------------------------------------------------|--------|-----------------|--------|--------|
| Vin      | Input/output voltage under overload conditions | -0.5   | BAT+ Power +0.5 | V      |        |
| Vout     | Output voltage under overload conditions       | 1      | -1              | 33     | V      |
| Wmax     | Inductive clamping Energy ( LI2 )              | 2      | 450             | mJ     |        |
| 2        |                                                |        |                 |        |        |
| fmax     | Maximum combined switching rate                | 3      | 11              | Hz     |        |
| Pmax     | Maximum combined clamping power                | 3      | 5               | W      |        |

Note **1 Inductive load transients will be clamped internally to <33 V referred to GND.** Note **2 With 3 A load current in a system with 32 V supply voltage, this corresponds to**
a maximum inductivity of 100 mH. For higher inductivities see Section 6.3 on page **195.**
Note **3 This is the sum of all inductive switch-off events on all eight low side outputs.**
With lower energy, faster switching is possible as the limit is the average power.

## 4.15.5 Characteristics Of Low-Side Digital Output Tecu **= -40. . . +125** °C

| Symbol   | Parameter             | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance | 8      | 12     | nF     |        |
| Rpu      | Pull-up resistor      | 8      | 12     | kΩ     |        |
| Vpu      | Pull-up voltage       | 4      | 4.5    | V      |        |
| Ron      | On-resistance         | 50     | mΩ     |        |        |
| I load   | Nominal load current  | 0      | 3      | A      |        |
| Imax     | Maximum load current  | 1      | 4      | A      |        |
| Ipeak    | Peak load current     | 2      | 0      | 6      | A      |
| I tol-0  | Zero reading error    | 3      | -400   | +400   | mA     |
| I tol-0  | Zero reading error    | 1,3    | -300   | +300   | mA     |
| I tol-p  | Proportional error    | 3      | -14    | +14    | %      |
| I tol-p  | Proportional error    | 1,3    | -10    | +10    | %      |

Note 1 TECU **= -40. . . +85** °C.

Note **2 Peak current for not more than 100 ms. Exceeding this value will trigger overload**
protection and switch off the power stage. Steady state operation goes only up to 3 A/4 A depending on temperature Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.15.6 Analog And Digital Inputs 4.15.6.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C 4.15.6.2 Characteristics Of Digital Input Tecu **= -40. . . +125** °C

| TECU = -40. . . +125 °C Symbol Parameter   | Note                            | Min.   | Max.   | Unit            |    |
|--------------------------------------------|---------------------------------|--------|--------|-----------------|----|
| Cin                                        | Pin input capacitance           | 8      | 12     | nF              |    |
| τin                                        | Input low pass filter           | 1.5    | 2.5    | ms              |    |
| Rpu                                        | Pull-up resistor                | 8      | 12     | kΩ              |    |
| Vpu                                        | Pull-up voltage                 | 4      | 4.5    | V               |    |
| Resolution                                 | 12                              | 12     | bit    |                 |    |
| Vtol-0                                     | Zero reading error              | 3      | -55    | +55             | mV |
| Vtol-0                                     | Zero reading error              | 1,3    | -50    | +50             | mV |
| Vtol-p                                     | Proportional error              | 3      | -4     | +4              | %  |
| Vtol-p                                     | Proportional error              | 1,3    | -3     | +3              | %  |
| LSB                                        | Nominal value of 1 LSB          | -      | 13.4   | mV              |    |
| Vin                                        | Input voltage measurement range | 2      | 0      | 32              | V  |
| Vin                                        | Input voltage range             | 2      | -0.5   | BAT+ Power +0.5 | V  |

| Symbol     | Parameter                    | Note   | Min.   | Max.   | Unit   |
|------------|------------------------------|--------|--------|--------|--------|
| Cin        | Pin input capacitance        | 8      | 12     | nF     |        |
| τin        | Input low pass filter        | 1.5    | 2.5    | ms     |        |
| Rpu        | Pull-up resistor             | 8      | 12     | kΩ     |        |
| Vpu        | Pull-up voltage              | 4      | 4.5    | V      |        |
| Resolution | 12                           | 12     | bit    |        |        |
| Vil        | Input voltage for low level  | 0      | V      |        |        |
| Vih        | Input voltage for high level | 32     | V      |        |        |

Note 1 TECU **= -40. . . +85** °C
Note **2 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**
Note Configuration by application software

![181_image_1.png]( The image is a white drawing of an electrical circuit board with several components labeled on it. There are multiple switches and buttons arranged across the board, some placed closer to the center while others are positioned towards the edges.

In addition to the switches and buttons, there are two green lights visible in the middle section of the drawing. The overall design suggests a complex electronic system with various functionalities.) 

![181_image_0.png]( The image is a white drawing of a seat arrangement inside an airplane or train car. There are several rows of seats lined up, with each row consisting of multiple chairs. The chairs are arranged in a way that allows passengers to face forward while seated.

The drawing also includes a green arrow pointing towards the left side of the image, possibly indicating the direction of travel or the entrance/exit point for passengers. Overall, it is an artistic representation of a typical seat arrangement found in various modes of transportation.) 

Figure 53: LIN pinout Pin No. Function **SW-define**
P208 LIN IO_LIN

LIN is configured in master mode. LIN is a bidirectional half duplex serial bus for up to 10 nodes. Note: **A common ground (chassis) or a proper ground connection is necessary for LIN operation. If** you connect to an external device (e.g., to a PC with a LIN interface), make sure not to violate the maximum voltage ratings when connecting to the LIN connection.

See also section *LIN - Local Interconnect Network driver* **of the API documentation [30].**

![182_image_0.png]( The image displays a diagram of an electronic system with multiple layers and components labeled. There are two main sections within the diagram - one on the left side and another on the right side.

The left section features a large blue box that spans almost the entire width of the image, while the right section consists of several smaller boxes arranged vertically. The various labels indicate different parts of the electronic system, making it easier to understand its structure and functioning.)

## 4.16.3 Maximum Ratings

| TECU = -40. . . +125 °C Symbol Parameter   | Note                                  | Min.   | Max.   | Unit   |
|--------------------------------------------|---------------------------------------|--------|--------|--------|
| VLIN                                       | Bus voltage under overload conditions | -1     | +33    | V      |

## 4.16.4 Characteristics

TECU **= -40. . . +125** °C

| Symbol                          | Parameter                | Note           | Min.   | Max.   | Unit   |
|---------------------------------|--------------------------|----------------|--------|--------|--------|
| Cout                            | Pin output capacitance   | 0.8            | 1.2    | nF     |        |
| VBUSdom Receiver dominant state | 0.4 ⋅ VBat_LIN           | V              |        |        |        |
| VBUSrec                         | Receiver recessive state | 0.6 ⋅ VBat_LIN | -      | V      |        |
| VOL                             | Output low voltage       | 2.0            | V      |        |        |
| VBat_LIN                        | LIN supply voltage       | 1              | 13     | 15     | V      |
| Rpu                             | Pull-up resistor         | 0.95           | 1.05   | kΩ     |        |
| STr                             | Baud rate                | 20             | kBd    |        |        |

Note 1 For battery voltages higher than V_Bat_LIN +0.5 V
4.17 RS232 4.17.1  Pinout
,
i

![184_image_0.png]( The image consists of a white background with two black lines on it. One line is located towards the left side of the image and appears to be slightly shorter than the other line. The second line is positioned more towards the right side of the image and is longer. The contrast between these two lines creates an interesting visual effect, as they appear to be floating in space.)

![184_image_1.png]( The image displays a series of horizontal lines arranged in a row. Each line is slightly different from one another, creating an interesting visual effect. There are at least twelve distinct lines visible in the scene, with varying lengths and positions. This arrangement might be used to represent data or simply for artistic purposes, depending on the context in which it was created.)

Figure 55: RS232 pinout

  \begin{tabular}{l l} P242 & RS232 Serial Interface Output(TX) \\ P255 & RS232 Serial Interface Output(RX) \\ \end{tabular}  
$$10\_{\mathrm{UART}}$$
RS232 is used as a full duplex serial interface. Note: **Handshake lines (RTS, CTS) are not available. A common ground (chassis) or a proper** ground connection is necessary for RS232 operation. If you connect to an external device (e.g., to a PC with an RS232 interface), make sure not to violate the maximum ratings.

See also section *UART - Universal Asynchronous Receiver Transmitter driver* **of the API documentation [30].**

![185_image_0.png]( The image displays a diagram that illustrates the functioning of a computer system. There are two main sections within this diagram - one on the left side and another on the right side. The left section consists of multiple layers, including the CPU (Central Processing Unit), memory, and other components.

The right side of the image features a block diagram that shows the relationship between various elements in the computer system. It includes labels such as "CPU," "Memory," "I/O," and "System." The diagram provides an overview of how these components work together to perform tasks within the computer system.)

## 4.17.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                                                                     | Note   | Min.   | Max.   | Unit   |
|----------|-------------------------------------------------------------------------------|--------|--------|--------|--------|
| VRS232x  | Bus voltage under overload conditions (e.g. short circuit to supply voltages) |        |        |        |        |

## 4.17.4 Characteristics

TECU **= -40. . . +125** °C

| Symbol   | Parameter                     | Note   | Min.   | Max.   | Unit   |
|----------|-------------------------------|--------|--------|--------|--------|
| Cout     | Pin output capacitance        | 100    | 150    | pF     |        |
| Vil      | Input voltage for low level   | -22    | 0.8    | V      |        |
| Vih      | Input voltage for high level  | 2.4    | 22     | V      |        |
| Vol      | Output voltage for low level  | -5     | V      |        |        |
| Voh      | Output voltage for high level | +5     | V      |        |        |
| STr      | Baud rate                     | 115    | kBd    |        |        |

4.18 CAN
4.18.1 Pinout

![186_image_0.png]( The image is a grayscale picture of a white background with black and white lines on it. There are several black and white horizontal lines running across the scene, creating an interesting pattern. The lines vary in length and position, adding visual interest to the overall composition.)

![186_image_1.png]( The image displays a gray background with a single white line running horizontally across it. This white line is located towards the left side of the image and extends all the way to the right edge. There are no other lines or objects visible in the scene.)

![186_image_2.png]( The image is a close-up of a computer screen displaying several lines of text or numbers. The lines are organized in rows and appear to be part of a spreadsheet or data analysis tool. There are multiple rows with varying lengths, creating an organized yet complex visual representation.)

Figure 57: CAN pinout

| Pin No.   | Function                    | SW-define        |
|-----------|-----------------------------|------------------|
| P209      | CAN Interface 0 - Low Line  | IO_CAN_CHANNEL_0 |
| P222      | CAN Interface 0 - High Line |                  |
| P210      | CAN Interface 1 - Low Line  | IO_CAN_CHANNEL_1 |
| P223      | CAN Interface 1 - High Line |                  |
| P211      | CAN Interface 2 - Low Line  | IO_CAN_CHANNEL_2 |
| P224      | CAN Interface 2 - High Line |                  |
| P212      | CAN Interface 3 - Low Line  | IO_CAN_CHANNEL_3 |
| P225      | CAN Interface 3 - High Line |                  |
| P213      | CAN Interface 4 - Low Line  | IO_CAN_CHANNEL_4 |
| P226      | CAN Interface 4 - High Line |                  |
| P214      | CAN Interface 5 - Low Line  | IO_CAN_CHANNEL_5 |
| P227      | CAN Interface 5 - High Line |                  |
| P215      | CAN Interface 6 - Low Line  | IO_CAN_CHANNEL_6 |
| P228      | CAN Interface 6 - High Line |                  |

CAN is a bidirectional twisted pair bus. Needs termination with 120 Ω **in 2-control units, whereas**
the others remain unterminated.

Termination must be fit at the ends of the bus line to prevent wave reflection. Termination is necessary to enter the recessive state. See Figure 58 **on the facing page for details.**
Note: **A common ground (chassis) or a proper ground connection is necessary for CAN operation.**
In case of connecting with an external device (e.g. PC with CAN-interface for downloading software) please make sure that the maximum voltage ratings are not violated when connecting to or disconnecting from the CAN bus. The CAN interface is ISO 11898-2/-5 compliant except for the **input resistance. This input resistance** is lower due to an RF termination, which drastically improves EMC immunity and is used, required and proven for it's performance in the automotive industry for many years. The differential internal resistance is given in table **4.18.4.**
See also section *CAN - Controller Area Network driver* **of the API documentation [30].**

## 4.18.2.1 Can1 On Hy-Ttc 590E, Hy-Ttc 590, And Hy-Ttc 508

Due to the requirements of the ISOBUS standard [21], CAN1 has a lower EMC protection than the other CAN interfaces. The high impedance RF termination is removed. To achieve equivalent RF immunity it is recommended to use CAN1 with a termination. That is, CAN1 should be connected at the terminated end of the CAN bus line. It is recommended to use either an internal CAN termination or an equivalent circuit according to Figure 60 on page 180.

![188_image_0.png]( The image displays a diagram with multiple layers of information, including a high-resolution image and a low-resolution image. There are two main diagrams visible, each showing different levels of detail. The first one is located on the left side of the image, while the second one can be seen in the middle section.

In addition to these diagrams, there are several other elements present in the image. A cell phone is positioned towards the right side of the image, and a TV is visible at the top-right corner. Two clocks can also be spotted within the scene, one near the center and another slightly lower on the left side.)

## 4.18.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol   | Parameter                               | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------------------|--------|--------|--------|--------|
| VCAN_H , | Bus voltage under overload conditions   |        |        |        |        |
| VCAN_L   | (e.g. short circuit to supply voltages) |        |        |        |        |

## 4.18.4 Characteristics Tecu **= -40. . . +125** °C

Note **1 Due to high current in the cable harness, the individual ground potential of the**
control units can differ up to several V. This difference will also appear as common mode voltage between a transmitting and a receiving control unit and not influence the differential bus signal, as long as it is within **the common mode** limits.

Note **2 Pay attention to the limitations of CAN. The arbitration process allows 1 Mbit/s**
operation only in small networks and reduced wire length. By **way of example,** a so-called "private CAN", which is a short point-to-point connection (less than 10 m) between two nodes only, can be operated at 1 MBit/s.

Note **3 For typical network sizes and topologies (networks with stub wires) and more**
than two nodes, the practical limit is 500 kbit/s.

Note 4 Any value that conforms to CAN protocol standard definition **is valid.** Note 5 ISOBUS CAN variant.

| Symbol                               | Parameter                                   | Note   | Min.   | Max.   | Unit   |
|--------------------------------------|---------------------------------------------|--------|--------|--------|--------|
| Cin                                  | Pin output capacitance                      | 100    | pF     |        |        |
| Vin-CMM                              | Input common mode range                     | 1      | -12    | 12     | V      |
| Vin-dif                              | Differential input threshold voltage        | 0.5    | 0.9    | V      |        |
| (VCAN_H - VCAN_L )                   |                                             |        |        |        |        |
| Vout-dif                             | Differential output voltage dominant state  | 1.5    | 3      | V      |        |
| (VCAN_H - VCAN_L )                   |                                             |        |        |        |        |
| Vout-dif                             | Differential output voltage recessive state | -0.1   | +0.1   | V      |        |
| (VCAN_H - VCAN_L )                   |                                             |        |        |        |        |
| VCAN_L ,                             | Common mode idle voltage (recessive state)  | 2      | 3      | V      |        |
| VCAN_H ICAN_CNL Output current limit | -40                                         | -200   | mA     |        |        |
| ICAN_CNH Output current limit        | 40                                          | 200    | mA     |        |        |
| STr                                  | Bit rate                                    | 2,3,4  | 20     | 1000   | kbit/s |
| Rdiff                                | Differential internal resistance            | 5      | 27     | 29     | kΩ     |
| Rdiff                                | Differential internal resistance            | 3.7    | 3.9    | kΩ     |        |

Figure 59: Pinout of CAN termination

| Pin No.   | Function                     | Applicable to variants                         |
|-----------|------------------------------|------------------------------------------------|
| P235      | 120 Ω CAN Termination 0 Low  | all                                            |
| P248      | 120 Ω CAN Termination 0 High | all                                            |
| P236      | 120 Ω CAN Termination 1 Low  | all                                            |
| P249      | 120 Ω CAN Termination 1 High | all                                            |
| P237      | 120 Ω CAN Termination 2 Low  | all                                            |
| P250      | 120 Ω CAN Termination 2 High | all                                            |
| P216      | 120 Ω CAN Termination 3 Low  | HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510 |
| P229      | 120 Ω CAN Termination 3 High | HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510 |
| P218      | 120 Ω CAN Termination 3 High | HY-TTC 590E, HY-TTC 590, HY-TTC 508            |
| P219      | 120 Ω CAN Termination 3 Low  | HY-TTC 590E, HY-TTC 590, HY-TTC 508            |

For easy termination of the CAN bus, there are four built in 120 Ω **termination resistors on the**
HY-TTC 500 which are accessible via 2 connector pins each. They can be used for any CAN port.

The 120 Ω termination of a control unit is realized with two serial 60 Ω **resistors (split termination).** To get an impedance of 60 Ω on the whole bus, a termination resistor of 120 Ω **is required in two**
control units.

![191_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled throughout. There are several wires and connections that make up the circuit, including a line labeled "EUC." The diagram also features a reference to CAN termination H, which is likely related to the overall functioning of the electrical system.

The image is in black and white, giving it an old-fashioned appearance. It seems to be a detailed representation of how the circuit works or is designed, with labels indicating specific components and their functions within the system.) 

4.20 Ethernet Figure 61: Ethernet pinout

| Pin No.   | Function                             | SW-define           | Applicable to variants   |
|-----------|--------------------------------------|---------------------|--------------------------|
| P218      | Ethernet Differential Transmit - TD+ | IO_DOWNLOAD, IO_UDP | HY-TTC 580               |
| P219      | Ethernet Differential Transmit - TD- | HY-TTC 580          |                          |
| P231      | Ethernet Differential Receive - RD-  | HY-TTC 580          |                          |
| P232      | Ethernet Differential Receive - RD+  | HY-TTC 580          |                          |

The Ethernet interface supports application download and the UDP communication protocol. The 10/100 Mbit/s full duplex Ethernet port is designed for IEEE 802.3 compliance. However, there is no standard Ethernet connector provided, the Ethernet signals are located on the main connector. Make sure to use appropriate cabling according to the Ethernet standard. Use at least an Ethernet CAT3 cable for a transmission speed of 10 Mbit/s and an Ethernet CAT5 cable for a transmission speed of 100 Mbit/s. In a noisy environment, it is recommended to use shielded cables. See also sections *IO_UDP* and *IO_DOWNLOAD* **in the API documentation [30].**

![193_image_0.png]( The image displays a diagram that illustrates a computer system's architecture, including its various components and their interactions. There are multiple layers within this diagram, with each layer representing different functionalities of the computer system.

The diagram features several labels, indicating key elements like "CPU," "Memory," "Input/Output," and "Magnetics." The CPU is located in the lower-left part of the image, while memory can be found towards the top-right corner. Input/output is situated in the middle-right area, and magnetics are positioned at the upper-left side of the diagram.

The overall layout provides a clear understanding of how these components work together to form a well-functioning computer system.)

## 4.20.3 Maximum Ratings

TECU = −40. . . +125 °C

| Symbol             | Parameter                                    | Note   | Min.   | Max.   | Unit   |
|--------------------|----------------------------------------------|--------|--------|--------|--------|
| Vin-CMM            | Input common mode voltage range 50/60 HZ AC, | 0      | 750    | VRMS   |        |
| 60 s test duration |                                              |        |        |        |        |

Figure 63: 100BASE-T1 Ethernet pinout

| Pin No.       | Function   | SW-define                           | Applicable to variants              |
|---------------|------------|-------------------------------------|-------------------------------------|
| P231          | 100BASE-T1 Ethernet TRX            | IO_DOWNLOAD, IO_UDP                 | HY-TTC 590, HY-TTC 590E, HY-TTC 508 |
| P232          | 100BASE-T1 | HY-TTC 590, HY-TTC 590E, HY-TTC 508 |                                     |
| Ethernet TRX+ |            |                                     |                                     |

The standardized BroadR-Reach® **(also known as 100BASE-T1 Ethernet) link is an advancement**
of the IEEE 802.3 100Base-TX Fast Ethernet standard and was standardized by OPEN ALLIANCE. It uses a single unshielded twisted pair cable (UTP) and is therefore low in costs. The 100BASE-T1 Ethernet link is capable of 100 MBit/s full-duplex transmission rate. Typical applications are
- **IP-based camera links** - **driver assistance systems**
- **in-vehicle backbone**
- infotainment

## 4.21.3 Maximum Ratings Tecu = −40. . . +125 °C

| Symbol                      | Parameter                                          | Note   | Min.   | Max.   | Unit   |
|-----------------------------|----------------------------------------------------|--------|--------|--------|--------|
| VBRR                        | Bus voltage under overload conditions (i.e., short | -32    | +32    | V      |        |
| circuit to supply voltages) |                                                    |        |        |        |        |

## 4.21.4 Characteristics Tecu **= -40. . . +125** °C

| Symbol                         | Parameter                   | Note   | Min.   | Max.   | Unit   |
|--------------------------------|-----------------------------|--------|--------|--------|--------|
| Vin-CMM                        | Input common mode range     | -32    | +32    | V      |        |
| Vout-dif                       | Differential output voltage | -1     | +1     | V      |        |
| VBRR_P,                        | Common mode idle voltage    | -0.1   | +0.1   | V      |        |
| VVBRR_M STr Bit rate           | 100                         | Mbit/s |        |        |        |
| Rin_AC_dif Input resistance AC | 90                          | 110    | Ω      |        |        |
| Rin_DC_dif Input resistance DC | 1.8                         | 2.2    | kΩ     |        |        |

4.22 Real-Time Clock (RTC)
Figure 64: RTC pinout

| Pin No.   | Function                       | SW-define   |
|-----------|--------------------------------|-------------|
| P233      | Real-Time Clock Backup Battery | IO_RTC      |

The HY-TTC 500 includes a real-time clock with a backup power **system for exact system time- and** date-keeping after every power cycle. The real-time clock module is either supplied by the internal 5 V supply, vehicle battery, or by the external RTC battery pin. When HY-TTC 500 is connected to the vehicle battery via the BAT+ CPU pin, the RTC is supplied by the vehicle battery independent of whether the device is operational or in power-off mode. When both the RTC backup battery and BAT+ CPU are disconnected, the real-time clock is supplied by an internal capacitor. The capacitor provides approximately 10 minutes of backup time when fully charged. Charging an empty capacitor takes at least 5 minutes. See also section *RTC - Real Time Clock driver* **of the API documentation [30].**

![197_image_0.png]( The image displays a diagram of an electronic circuit with various components and connections. There are multiple batteries present, one towards the left side of the image and another on the right side. A CPU is also visible within the circuit, positioned near the center-right area.

Several wires connect different parts of the circuit, including a wire running from the top-left corner to the bottom-right corner, as well as multiple smaller wires connecting various components throughout the image. The diagram provides an overview of the electronic device's structure and functioning.)

## 4.22.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter     | Note   | Min.   | Max.   | Unit   |
|----------|---------------|--------|--------|--------|--------|
| Vin      | Input voltage | -1     | +33    | V      |        |

## 4.22.4 Characteristics Tecu **= -40. . . +125** °C

| Symbol   | Parameter                                       | Note   | Min.   | Max.   | Unit   |
|----------|-------------------------------------------------|--------|--------|--------|--------|
| Cin      | Pin input capacitance                           | 8      | 12     | nF     |        |
| I in     | Steady state input current (after 1 min, 3.6 V) | 10     | µA     |        |        |
| I in     | Steady state input current for high voltage operation (after 1 min, 16 V)                                                 | 260    | µA     |        |        |
| I in     | Steady state input current for high voltage operation (after 1 min, 32 V)                                                 | 600    | µA     |        |        |
| Vin      | Input voltage                                   | 2.5    | 32     | V      |        |
| Vin      | Input voltage                                   | 1      | 1.8    | 32     | V      |
| ∆ t/day  | Time variation per day at +25 °C                | ± 1.5  | s/day  |        |        |
| RTCres   | Real-time clock resolution                      | 1      | s      |        |        |

Note 1 TECU = -40. . . +85 °C

## 5 Internal Structure 5.1 Safety Concept

If HY-TTC 500 is used in safety-critical applications, you must follow the requirements specified in the Safety Manual [29].

## 5.1.1 Overview Safety Concept

The following picture descibes all possible (application-controlled) enable/disable paths for the HYTTC 500 powerstages.

![200_image_0.png]( The image is a diagram that illustrates a complex network of interconnected components and processes. It appears to be a flowchart or a schematic representation of various elements within a system.

There are multiple arrows pointing towards different parts of the diagram, indicating connections between these elements. Some of the key components include "CPU," "Memory," "Power Supply," "Input/Output," and "Hard Drive." The diagram also features labels for each component, making it easier to understand the relationships between them.

Overall, this diagram provides a comprehensive view of the intricate connections within the system, allowing users to better understand its structure and functioning.)

## 5.2 Thermal Management 5.2.1 Board Temperature Sensor

5.2.1.1 Pinout

![201_image_0.png]( The image displays a computer screen with various temperature readings displayed on it. There are several graphs and charts showing different types of data related to the temperatures. Some of these graphs are located towards the top left corner of the screen, while others can be found in the middle and bottom sections.

In addition to the graphs, there is a text box that provides information about the temperature readings. The text appears to be written in another language, possibly Chinese, as it reads "PIN N" at the top left corner of the screen.)

![201_image_1.png]( The image is a close-up of two different shades of gray, with one being lighter and the other darker. They are placed next to each other on a white background, creating an interesting contrast between the colors. The grays appear to be blending together, giving the impression that they might be a single color in varying degrees of lightness.)

To measure the temperature TECU within the housing, there is a temperature sensor located on the printed circuit board. This sensor allows monitoring of the **internal board temperature for diagnostic**
purposes and monitoring of safety features.

Dependent on the TECU **board temperature, the maximum current limit for High- and Low-side output**
stages is adjusted, see e.g. Section 4.12.4.1 on page **141. This is a strategy to allow higher current**
consumption at lower temperatures and to bring the ECU immediately to a safe state and switch off loads if over temperature is detected. See Section 5.2.2 **on the next page for temperature limits** triggering the safe state. All input/output tolerance characteristics stated in this **System Manual are worst case tolerances**
and are respected to the internal worst ECU temperature TECU. At lower TECU/Tambient **temperature**
and/or lower loads, the tolerances are better.

The (internal) ECU temperature TECU **is close to ambient temperature, when there is no load driven**
by the power stages at all. The ECU temperature may rise by 40 K **above ambient temperature,**
when there is significant output load (many outputs activated with high load current at the same time) and no airflow supports cooling of the housing. Many applications tend to be somewhere in the middle. Reading out the ECU temperature during system development is a useful feature to analyze the application-specific thermal load and mounting **situation. For more information please** ask your local sales representative.

## 5.2.2 Characteristics

TECU **= -40. . . +125** °C

| Symbol                        | Parameter                       | Note   | Min.   | Max.   | Unit   |
|-------------------------------|---------------------------------|--------|--------|--------|--------|
| Tm                            | Temperature measurement range   | -40    | +125   | °C     |        |
| Ttol-m                        | Temperature tolerance at 120 °C | -3     | +3     | K      |        |
| Tsafe state Temperature limit | 1                               | -40    | +125   | °C     |        |

Note 1 A temperature (including measurement tolerance) below or **above the specified**
limits immediately triggers the safe state

## 6 Application Notes 6.1 Cable Harness

The following general layout rules for the cable harness must be obeyed to enable safe operation of HY-TTC 500.

The ECU is limited to a total load current for the power stages **connected to the BAT+ Power pins.** When all loads are tied toward ground, the load current will be carried by these supply pins as well.

As each contact pin is thermally limited to 10 A, multiple supply pins work in parallel for the power stages supply. So, the system designer must be careful with the cable harness design to ensure an even supply current distribution on all pins. Example: **Do not use a cable with a length of two meters and a large diameter for a connection** between a fuse box and the ECU and do not crimp it to some piggy tails with a small diameter in the connector area. Small differences between the contact pressure can lead to a big imbalance. In the worst case, one contact carries most of the current load and is overloaded at maximum current. It is necessary to use six wires with the same total cross sectional area as one thick cable. All wires must have the same length and diameter. In this case, an even current distribution can be achieved, even with slightly different contact resistances.

## 6.2 Handling Of High-Load Current 6.2.1 Load Distribution

The permanent input current of the HY-TTC 500 Iin-max **is limited due to thermal limits and contact**
current limits. As the power stages do not have negligible power dissipation, each load current leads to a rise in temperature within the device. To ensure proper operation of the HY-TTC 500 in its temperature range (-40 °C to +85 °C) the total current Iin-total **driven by the power stages must**
be limited and the load must be evenly distributed. If two output stages are operated in mutually exclusive states (e.g. output channel 00 is only activated in state 1 and output channel 01 is only activated in state 2; never activated at the same time), then, as a rule of thumb, these outputs should be driven by a double-channel high-side power stage due to only one active channel at a time.

## 6.2.2 Total Load Current

Operating all power stages ON with maximum rated current (4 A) that would result in a load current Iin-total **in excess of 200 A, which is far beyond any allowed limit to ensure no violation of the allowed**
contact current limit as well as overall thermal limits. Therefore, the maximum allowed load current, which can be controlled simultaneously with different power stages, is separately given as the maximum total load current Iin-total**. This value can only be**
applied if an equal load distribution over different power stages is ensured - which implicit a different Iin-total **limit set by the different number of power stages in each HY-TTC 500 variant, e.g. the same**
current distributed over 52 output stages cannot be driven with 38 output stages due to the square rise of the power dissipation of the output stages and the respective thermal limit.

| Variant                | I in-total [A],         | I in-total [A],   |
|------------------------|-------------------------|-------------------|
| TECU = -40. . . +85 °C | TECU = -40. . . +125 °C |                   |
| HY-TTC 580             | 60                      | 45                |
| HY-TTC 540             | 50                      | 40                |
| HY-TTC 520             | 40                      | 30                |
| HY-TTC 510             | 40                      | 30                |
| HY-TTC 590E            | 60                      | 45                |
| HY-TTC 590             | 60                      | 45                |
| HY-TTC 508             | 40                      | 30                |

## Maximum Total Load Current Iin-Total For Each Variant At Different Tecu:

Table 23: Total Load Current Iin-total

## 6.2.2.1 Calculation Of The Battery Supply Current

For the PWM- and digital output stage supply pins BAT+ Power, **up to 6 pins can be used in parallel** to increase the overall current capability.

For the maximum battery supply current of 60 A, all 6 pins must **be used in parallel with the maximum possible wire size (FLRY type) to reduce voltage drop and prevent overheating of the crimp**
contact. To define a proper cabling, it is important to calculate the maximum average battery supply current first. For a single digital output power stage it is simply calculated as:
Ibat = Ipower-stage (1)
If for example one power stage is loaded with 2 A, it will also load the battery supply with 2 A. For PWM output stages with inductive load it is calculated as:

$$I_{\mathrm{{hat}}}={\frac{I_{\mathrm{{power-stage}}}*(d u t y\ c y c l e)}{100}}$$
100

(2)
Example: **A load current of 2 A with a duty cycle of 25 % results in an average battery current of**
0.5 A. More precisely explained: a single power stage with 100 Hz PWM frequency will draw 2.5 s in duration 2 A out of the battery followed by 7.5 ms with 0 A. The average current is 0.5 A, the rms current is higher.

However, with a couple of used PWM power stages, there is no significant difference between average and rms current, due to different phase operation of the individual power stages.

Once, the maximum battery supply current for the individual **application is calculated, the required** minimum number of battery supply wires and/or cabling diameter can be defined.

## 6.3 Inductive Loads 6.3.1 Inductive Loads At Pwm Outputs

Inductive loads in PWM operation generate current through the freewheeling diodes, but these diodes have, at the same current, a power dissipation that is **several times greater than the high-side** switches themselves. Therefore the duty cycle has a great influence on the power dissipation of the output devices. The duty cycle results from the relationship between coil resistance and supply voltage. A low resistance at a high supply voltage is the worst combination, because it **results in a low duty cycle and, thus, in** a long conduction time of the diodes.

## 6.3.2 Inductive Loads At Low Side Switches

For load inductivities >100 mH, either the current has to be lower or an external freewheeling diode or clamping device parallel to the coil has to be used. The clamping device has to clamp below 50 V.

Examples for clamping devices are: varistor, bidirectional Transzorb® **diode, Zener diode with antiserial diode or a suitably sized resistor.**
A resistor can be calculated as 50 V/(maximum possible coil current). It can be a cost-effective solution. But it increases steady state power dissipation, **so it may not be suitable in all cases.**

## 6.4 Ground Connection Of Housing

The HY-TTC 500 housing is not directly connected to ground. In case of chassis mounting this prevents ground loops or excessive current flow through the Negative Power Supply (BAT-) pins and cables in case of partly power connection loss in the negative supply rail of the vehicle. Instead of direct connection, the housing is capacitively connected to BAT-. In order to discharge static electricity, a 1 MΩ **resistor is equipped between housing and BAT-.**
Note: It is allowed to mount the housing without any additional isolation directly to the vehicle chassis.

## 6.5 Motor Control

This application note describes control options for directly driving a DC-motor with outputs of the HY-TTC 500.

## 6.5.1 Motor Types Supported

- Standard brushed DC-motors with defined power rating - Motors with end position switches and diodes for rotation direction dependent automatic stop at full excursion.

- Motors with integrated electronic control (including brushless DC-motors) up to a well-defined current limit and a maximum input capacitance.

Motors running at different speed by using different windings are not supported.

## 6.5.2 Direct Control Options

The following control options are described into details in **the following chapters:**

## 6.5.2.1 Depending On Direction

- Unidirectional drive - Bidirectional drive

## 6.5.2.2 Depending On Single Motor / Motor Group

- Single motor drive - Motor cluster

## 6.5.2.3 Depending On Control

- PWM operation
- Steady state operation

## 6.5.2.4 Depending On Stalled Motor Current

- 0 to 2 A max. motor current
- 2 to 4 A max. motor current - 4 to 16 A max. motor current - 16 A and higher

## 6.5.3 Motor Details 6.5.3.1 Start Current

A typical standard (brushed) DC-motor is driven by a current **through the rotor winding and permanent magnets in the stator. The rotor winding is normally made out of copper wire with a well-defined**
DC-resistance. The DC-resistance defines the maximum possible current, when the motor does not rotate (stalled motor). The same current shows as peak current in the moment when supply voltage is switched on the motor. By taking up speed the motor builds up an electro motoric force (EMF) that works against the voltage applied on the motor terminals thus reducing the virtual voltage on the winding -> the current drops. When the motor stabilizes at nominal speed (depending on motor voltage) and the motor runs idle (no mechanical load) the current drops to a value 10 to 100 times smaller than the start current, depending on motor friction **in the bearings and other constructive** details. This stall current (= max. motor current with blocked motor) **is required to classify the motor power.** This has a main impact on possible motor control options and even number of paralleled power stages, if required.

## 6.5.3.2 Start Current At Low Temperatures

The motor windings are made out of copper. The winding resistance goes down towards lower temperature, by approx. 0.4 % / K. This means that at -40 °**C the winding resistance is lower than**
the nominal value at +25 °C by 26 %. Depending on the lowest operating temperature this **effect**
needs to be considered. In our example that turns a 2 A motor (@+25 °**C) into a 2.7 A motor (@-**
40 °C).

## 6.5.3.3 Battery Voltage Impact

The start current increases proportionally with higher battery voltage. In our assumption the battery voltage of a 12 V system stays below 14 V and for a 24 V system below 28 V. Often the DC
resistance of the motor is not specified but the maximum current at nominal voltage. Any maximum current rating of the motor for a nominal voltage needs to be modified for the maximum voltage that the system actually can have.

## 6.5.3.4 Motors With Limit Switch

Some motor assemblies are fitted with an limit switch turning **off the motor power when a maximum**
position is reached. To allow reversing the motor to move out **of this position a diode is placed in**
parallel to the switch. Operating these kinds of motors is no **problem. Care should be taken that** diagnostics may detect an open load in the end position which **is intended with this kind of operation** and no failure.

## 6.5.3.5 Motors With Electronics Inside

There is no general do or don't with that kind of motors. Essential is only the maximum start current in excess of 50 ms (to be found in chapter Motor classification) and the maximum capacitive load of the motor electronics:
- Max 5 µ**F when used with H-bridge** - Max 200 µ**F when used with a single high side power stage (unidirectional supply)**

## 6.5.3.6 Unidirectional Motor Drive

This uses in the simplest case just one high side power stage.

## 6.5.3.7 Bidirectional Motor Drive

By configuring an H-bridge out of 4 power stages a reverse operation of the motor is possible.

## 6.5.3.8 Active Motor Brake

With bidirectional motor drive active braking by shorting the motor terminals is supported.

## 6.5.3.9 Motors Reversing With / Without Braking

Motor reversing out of full speed can lead to unexpected high **motor current. The cause is that for** example a 24 V motor running at nominal speed has a back EMF of almost 24 V with the same sign as the voltage applied. By sudden revering the EMF-voltage adds to the terminal voltage, which means the motor current is as high as with starting at 48 V battery voltage. In other words, the peak motor current is doubled by sudden reverse. For small motors this is neither a problem to the motor nor to the driving power stages. For bigger motors a braking phase needs to be inserted first followed by the reversing command.

## 6.5.3.10 Pwm Operation / Steady State Control

In general PWM operation is not recommended as the PWM frequency for high efficient motors often require frequencies in excess of 10 kHz. A PWM frequency so high would cause lots of unacceptable electromagnetic noise (EMI) or dramatic switching losses or both. For small motors we can use a 200 Hz PWM instead. This causes a significant torque ripple which might be desirable for slow positioning of the motor with the need to prevent static friction.

As mentioned in section 6.5.3.9 **above, motors produce a back EMF when running. With PWM** controlled motors the motor is essentially free running between the PWM pulses. Depending on operating voltage and motor speed this back EMF can sometimes lead to false diagnostic errors.

## 6.5.3.11 Maximum Average Current (Pwm And Digital Power Stages)

The maximum steady state motor current is 4 A (up to +85 °**C internal ECU temperature) or 3 A** (over +85 °**C). This comes from the limits of the power stage used. Normally the start current limits**
the choice of suitable motors and not the supply current, when the motor is running. The motor current is measured in the ECU and can be used for control / diagnostic purposes.

## 6.5.3.12 Peak Current Bidirectional Drive (Digital Power Stages Only)

The digital (non-PWM) power stages tolerate inrush current **of up to 6 A for 100 ms. Fast accelerating**
motors show first an inrush current peak followed by a reduction in current to less than 50 % of the initial current after 20 ms. In other words, most motors that **start with 6 A drop to less than 4 A in** 100 ms. Motors with that kind of fast acceleration will work properly even with a winding resistance that is lower by a factor of 1.5 (stall current 6 A instead of 4 A).

## 6.5.3.13 Peak Current Unidirectional Drive (Digital Power **Stages Only)**

Single high side power stages tolerate an inrush current that linearly declines from 16 to 6 A in 50 ms. Fast accelerating motors show after an initial current peak a reduction in current to less than 50 % after 20 ms. Motors with that kind of fast acceleration may have a winding resistance that is lower by a factor of 4 (stall current 16 A instead of 4 A).

## 6.5.4 Motor Classification 6.5.4.1 Independent From Speed Class

The most conservative limits apply for slow accelerating motors, found in the following section:
6.5.4.1.1 Tiny Motors (0 to 2 A) **This class gives the widest choice of control options.**

| 12 V System                     | 24 V System                               |          |
|---------------------------------|-------------------------------------------|----------|
| Max. battery voltage 1          | 14 V                                      | 28 V     |
| Motor blocked current           | 0 to 2 A                                  |          |
| DC-resistance                   | >=7.0 Ω                                   | >=14.0 Ω |
| Unidirectional drive            | yes                                       | yes      |
| Bidirectional drive             | yes                                       | yes      |
| Active motor braking            | yes                                       | yes      |
| Reverse without brake           | yes                                       | yes      |
| PWM operation                   | yes                                       | yes      |
| Suitable high side power stages | PWM power stages, digital HS power stages |          |

1 For other max. battery voltage please recalculate winding resistance (R = U / I).

6.5.4.1.2 Small Motors (2 to 4 A) **For this class some restrictions apply.**

| 12 V System                                                                         | 24 V System                               |         |
|-------------------------------------------------------------------------------------|-------------------------------------------|---------|
| Max. battery voltage 1                                                              | 14 V                                      | 28 V    |
| Motor blocked current                                                               | 2 to 4 A                                  |         |
| DC-resistance                                                                       | >=3.5 Ω                                   | >=7.0 Ω |
| Unidirectional drive                                                                | yes                                       | yes     |
| Bidirectional drive                                                                 | yes                                       | yes     |
| Active motor braking                                                                | yes                                       | yes     |
| Reverse without brake                                                               | no                                        | no      |
| PWM operation                                                                       | no                                        | no      |
| Suitable high side power stages                                                     | PWM power stages, digital HS power stages |         |
| Maximum periodic DC peak current 2                                                  | 4 A (TECU < +85 °C)                       |         |
| Maximum periodic DC peak current 2                                                  | 3 A (TECU > +85 °C)                       |         |
| 1 For other max. battery voltage please recalculate winding resistance (R = U / I). |                                           |         |

1 **For other max. battery voltage please recalculate winding resistance (R = U / I).**

2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.1.3 Medium Power Motors (4 to 14 A) **This class needs paralleled power stages. In the example below each switch utilizes 4 power stages in parallel for each switch. This in theory quadruples**
the power rating. In practice depending on close-to-perfect cabling a de-rating of maximum current (14 A instead of 16 A) is foreseen.

| 12 V System                        | 24 V System                  |         |
|------------------------------------|------------------------------|---------|
| Max. battery voltage 1             | 14 V                         | 28 V    |
| Motor blocked current              | 4 to 14 A                    |         |
| DC-resistance                      | >=1.0 Ω                      | >=2.0 Ω |
| Unidirectional drive               | yes                          | yes     |
| Bidirectional drive                | yes                          | yes     |
| Active motor braking               | yes                          | yes     |
| Reverse without brake              | no                           | no      |
| PWM operation                      | no                           | no      |
| Suitable high side power stages    | digital HS power stages only |         |
| Maximum periodic DC peak current 2 | 12 A (TECU < +85 °C)         |         |
| Maximum periodic DC peak current 2 | 10 A (TECU > +85 °C)         |         |

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

## 6.5.4.2 Fast Accelerating Motors Only

Higher inrush current,is allowed for fast accelerating motors. Most actuator motors fall into this category. Depending on operation mode different limits apply:
6.5.4.2.1 Bidirectional (max. 6 A) **For this class some restrictions apply.**

| 12 V System                        | 24 V System                             |         |
|------------------------------------|-----------------------------------------|---------|
| Max. battery voltage 1             | 14 V                                    | 28 V    |
| Motor blocked current              | <6 A                                    |         |
| DC-resistance                      | >=2.35 Ω                                | >=4.7 Ω |
| Unidirectional drive               | yes                                     | yes     |
| Bidirectional drive                | yes                                     | yes     |
| Active motor braking               | yes                                     | yes     |
| Reverse without brake              | no                                      | no      |
| PWM operation                      | no                                      | no      |
| Suitable high side power stages    | digital HS power stages only            |         |
| Maximum periodic DC peak current 2 | 4 A (TECU < +85 °C)                     |         |
| Maximum periodic DC peak current 2 | 3 A (TECU > +85 °C)                     |         |
| Inrush current drops after 50ms to | <6 A                                    |         |
| Inrush current drops after 50ms to | <4 / 3 A (depending on ECU temperature) |         |

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.2.2 Bidirectional (max. 16 A) **For this class each low side switch is built out of 4 switches** working in parallel to increase current handling. The high side switches are still single switches.

| 12 V System                        | 24 V System                             |          |
|------------------------------------|-----------------------------------------|----------|
| Max. battery voltage 1             | 14 V                                    | 28 V     |
| Motor blocked current              | <16 A                                   |          |
| DC-resistance                      | >=0.88 Ω                                | >=1.75 Ω |
| Unidirectional drive               | yes                                     | yes      |
| Bidirectional drive                | yes                                     | yes      |
| Active motor braking               | yes                                     | yes      |
| Reverse without brake              | no                                      | no       |
| PWM operation                      | no                                      | no       |
| Suitable high side power stages    | digital HS power stages only            |          |
| Maximum periodic DC peak current 2 | 4 A (TECU < +85 °C)                     |          |
| Maximum periodic DC peak current 2 | 3 A (TECU > +85 °C)                     |          |
| Inrush current drops after 50ms to | <6 A                                    |          |
| Inrush current drops after 50ms to | <4 / 3 A (depending on ECU temperature) |          |

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.2.3 Bidirectional (max. 20 A) **For this class each high and low side switch is built out of 4** switches working in parallel to increase current handling. **This in theory quadruples the power rating.** In practice depending on close-to-perfect cabling a de-rating of maximum current (20 A instead of 24 A) is foreseen.

| 12 V System                        | 24 V System                               |         |
|------------------------------------|-------------------------------------------|---------|
| Max. battery voltage 1             | 14 V                                      | 28 V    |
| Motor blocked current              | <20 A                                     |         |
| DC-resistance                      | >=0.7 Ω                                   | >=1.4 Ω |
| Unidirectional drive               | yes                                       | yes     |
| Bidirectional drive                | yes                                       | yes     |
| Active motor braking               | yes                                       | yes     |
| Reverse without brake              | no                                        | no      |
| PWM operation                      | no                                        | no      |
| Suitable high side power stages    | digital HS power stages only              |         |
| Maximum periodic DC peak current 2 | 12 A (TECU < +85 °C)                      |         |
| Maximum periodic DC peak current 2 | 10 A (TECU > +85 °C)                      |         |
| Inrush current drops after 50ms to | <12 / 10 A (depending on ECU temperature) |         |

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

| 12 V System                        | 24 V System                             |          |
|------------------------------------|-----------------------------------------|----------|
| Max. battery voltage 1             | 14 V                                    | 28 V     |
| Motor blocked current              | <16 A                                   |          |
| DC-resistance                      | >=0.88 Ω                                | >=1.75 Ω |
| Unidirectional drive               | yes                                     | yes      |
| Bidirectional drive                | no                                      | no       |
| Active motor braking               | no                                      | no       |
| Reverse without brake              | no                                      | no       |
| PWM operation                      | no                                      | no       |
| Suitable high side power stages    | digital HS power stages only            |          |
| Maximum periodic DC peak current 2 | 4 A (TECU < +85 °C)                     |          |
| Maximum periodic DC peak current 2 | 3 A (TECU > +85 °C)                     |          |
| Inrush current drops after 50ms to | <6 A                                    |          |
| Inrush current drops after 50ms to | <4 / 3 A (depending on ECU temperature) |          |

6.5.4.2.4 Unidirectional (max. 16 A) 1 **For other max. battery voltage please recalculate winding**
resistance (R = U/I).

2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.2.5 Unidirectional (max. 32 A) **For this class two digital high side power stages are operated in parallel.**

| 12 V System                        | 24 V System                             |         |
|------------------------------------|-----------------------------------------|---------|
| Max. battery voltage 1             | 14 V                                    | 28 V    |
| Motor blocked current              | <32 A                                   |         |
| DC-resistance                      | >=0.4 Ω                                 | >=0.8 Ω |
| Unidirectional drive               | yes                                     | yes     |
| Bidirectional drive                | no                                      | no      |
| Active motor braking               | no                                      | no      |
| Reverse without brake              | no                                      | no      |
| PWM operation                      | no                                      | no      |
| Suitable high side power stages    | digital HS power stages only            |         |
| Maximum periodic DC peak current 2 | 8 A (TECU < +85 °C)                     |         |
| Maximum periodic DC peak current 2 | 6 A (TECU > +85 °C)                     |         |
| Inrush current drops after 50ms to | <12 A                                   |         |
| Inrush current drops after 50ms to | <8 / 6 A (depending on ECU temperature) |         |

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

## 6.5.5 Connection 6.5.5.1 Unidirectional Single Power Stage

Figure 67 **on this page shows the battery wiring for maximum total load current. This kind of wiring is** used to increase output current capability. It is strongly recommended to support equal distribution of current between the power supply pins. This implies to use **cables of same diameter and same** wire length in parallel. In this example all power supply pins (BAT+ and GND) are connected to cable of maximum diameter supported by the appropriate connector **pin. The cables in parallel are going**
to a distribution point (for example in the fuse box) and from **there with a bigger diameter all the way** to the battery.

The return pin of the motor is connected not direct to the ECU ground but to somewhere else, perhaps to the chassis. In this case significant voltage drops may occur between ECU and motor ground connection. This can lead to unexpected fluctuations **in motor voltage and motor current.**

![219_image_0.png]( The image displays a diagram of an electrical circuit with various components and connections. There are multiple wires running through the circuit, including one that has a green light on it. A few switches can be seen within the circuit, with one located near the center of the image and another towards the right side.

In addition to these elements, there is an array of numbers scattered throughout the diagram, possibly representing voltage levels or other electrical properties. The overall layout suggests that this could be a schematic for a complex electronic device or system.)

A better solution for achieving less voltage drop in the return path shows the Figure 68 **on the current** page.

![220_image_0.png]( The image is a black and white diagram of an electrical system, featuring various components like wires, switches, and batteries. There are multiple batteries placed throughout the diagram, with one located near the center-left side, another in the middle-right area, and two more towards the bottom right corner.

The diagram also includes a number of switches, which can be seen scattered across the image. Some switches are positioned close to each other, while others are spaced further apart. The arrangement of these components suggests that they work together in an interconnected electrical system.)

## 6.5.5.2 Unidirectional Double Power Stage

Higher current can be achieved by paralleling output stages, see Figure 69 **on this page. Please** observe the use of cables of same diameter and same wire length in parallel on the power stages as well.

![221_image_0.png](6x BAT+ is written on this electrical diagram, which shows a complex network of connections and components. The diagram features multiple wires, switches, and other electrical devices, indicating that it represents an intricate system. There are also several knobs in the image, suggesting that these controls might be used to adjust or manipulate various aspects of the system. Overall, this diagram provides a detailed view of the inner workings of an electrical device or network.)

6.5.5.3 Bidirectional H-bridge (Single Power Stages)

![222_image_0.png](16 HS output is displayed on a white background with multiple diagrams and descriptions of the circuitry. The image features a series of blue boxes labeled "U" that are placed throughout the scene. These boxes are likely part of the electrical system being described in the diagram.

There are also several green boxes scattered around the image, which may represent different components or connections within the circuitry. Overall, the image provides an informative and detailed view of the electrical system being discussed.)

6.5.5.4  Bidirectional H-bridge (Multiple Low Side Power Stages)

![223_image_0.png]( The image is a white drawing of an electrical circuit board with multiple components labeled on it. There are several blue boxes scattered throughout the circuit board, likely representing electronic devices or connections. The labels indicate that there are two ECU (Electronic Control Unit) outputs present in the circuit.

The circuit board appears to be a complex network of interconnected parts, with various components arranged across its surface. This drawing provides an overview of the structure and organization of the electronic device being represented.)

![224_image_0.png]( The image is a white drawing of an electrical device with multiple rows and columns of numbers. There are several blue boxes lined up vertically within the drawing, each containing a number or letter. Some of these boxes have green numbers inside them. The arrangement of the boxes creates a complex pattern that resembles a computer circuit board.

In addition to the blue and green boxes, there is a row of red boxes positioned horizontally across the top of the drawing. These boxes are also filled with numbers or letters, adding more depth to the overall design.)

## 6.5.5.6 Motor Cluster

This is a usual configuration to control 2 motors, that are never operated at the same time, with 3 half bridges (3 x high side + 3 x low side power stage). Example: Outside mirror control

![225_image_0.png](1xHS Output is displayed on a white background with multiple diagrams and labels. There are several boxes labeled M2, each containing different types of equipment or connections. The diagrams showcase various configurations of these devices, likely related to the FCLJ circuit.

In addition to the M2 boxes, there are other smaller boxes scattered throughout the image. These may represent different components or aspects of the FCLJ circuit as well. Overall, the image provides a detailed view of the equipment and connections within the FCLJ circuit.)

## 6.5.6 Power Stages For Motor Control 6.5.6.1 High Side Power Stages For Pwm Operation

Depending on the HY-TTC 500 variant, up to 36 high side PWM power stages are provided:
- HY-TTC 580:E **HS channel 00. . . 35**
- HY-TTC 540:E **HS channel 00. . . 27** - HY-TTC 520:E **HS channel 00. . . 09, 14. . . 21** - HY-TTC 510:E **HS channel 00. . . 07, 14. . . 21**
- HY-TTC 590E: HS channel 00. . . 35 - HY-TTC 590:E **HS channel 00. . . 35**
- HY-TTC 508:E **HS channel 00. . . 05, 14. . . 17**

## 6.5.6.2 High Side Power Stages For Static Operation

Depending on the HY-TTC 500 variant, up to 16 digital high side power stages are provided:
- HY-TTC 580:E **HS channel 36. . . 51**
- HY-TTC 540:E **HS channel 36. . . 43**
- HY-TTC 520:E **HS channel 36. . . 43**
- HY-TTC 510:E **HS channel 36. . . 51** - HY-TTC 590E: HS channel 36. . . 51 - HY-TTC 590:E **HS channel 36. . . 51** - HY-TTC 508:E **HS channel 36. . . 49**

## 6.5.6.3 Low Side Power Stages

8 digital low side power stages are provided independent from the HY-TTC 500 variant:
- HY-TTC 580:E **LS channel 00. . . 07**
- HY-TTC 540:E **LS channel 00. . . 07** - HY-TTC 520:E **LS channel 00. . . 07** - HY-TTC 510:E **LS channel 00. . . 07** - HY-TTC 590E: LS channel 00. . . 07 - HY-TTC 590:E **LS channel 00. . . 07** - HY-TTC 508:E LS channel 00. . . 07

## 6.5.7 Parallel Operation Of Power Stages

This kind of wiring is used to increase output current capability. It is strongly recommended to support equal distribution of current between those power stages. This implies to use cables of same diameter and same wire length in parallel as well as to use matched power stages inside the ECU. Matched power stages are always grouped in pairs of even and following odd signal number. For example a good pair is HS-OUT-36 and 37. See Section 4.15.2.1 on page 167 **for more information** about Power Stage Pairing.

## 6.5.8 Cabling

The cable resistance adds to the rotor resistance of the motor. While the impact of a small voltage drop is negligible for normal operation it can be helpful to reduce inrush current when switching on the motor. If there is significant cable length used for motor **cabling, please add the wire resistance** to the motor current classification to relax need of paralleling power stages. For power stages operated in parallel please observe that this cable resistance also helps to equally distribute the load current over the power stages. On the other hand, if there is significant difference in wire length of paralleled output stages this enhances non-symmetric load, which means one power stage might carry significant more load current than the others. This ends up in reduced power capability. 4 power stages of the HY-TTC 500 would theoretically deliver **a total current of 16 A if switched on** concurrently.

So the system designer must be careful with the cable harness **design to guarantee evenly distribution of supply current on all 4 pins. For example, it is not OK to use 1 cable with large diameter to** connect from a fuse box to the ECU for, let's say 2 meters and crimp it to 4 piggy tails with small diameter in the connector area. Small differences in the contact pressure can lead to a big imbalance.

In worst case condition 2 contacts carry almost the full current load and are overloaded at maximum current. It is better to use 4 wires with the same total cross sectional area than this one thick cable.

All wires must have exactly the same length and diameter. In this case an evenly distribution of current will be the case even with slightly different contact resistance.

## 6.5.9 Control Sequence For Bidirectional Drive

The complexity of SW control for bidirectional motor operation depends more or less on the motor type. Up to 2 A peak current a sudden reverse is still limited to 4 A maximum current, which is below the over load threshold of the power stages. Above 2 A an active braking sequence close to speed 0 must be inserted prior to reversing the motor.

## 6.5.9.1 Motor Running

Forward or backward rotation is managed by diagonally switch on a high side and a low side power stage simultaneously. Always switch on low side first followed by high side. Never switch on high side first and then switch on low side.

## 6.5.9.2 Motor Breaking

Motor braking is managed by switching on both high side power **stages simultaneously.**
Always switch off low side first before switching on high side. Never switch on high side while low side is still on. Please observe that the high side power stages can only measure current in positive direction (out of the terminal towards ground) While the high side power stages are actively braking, one power stage (this one that was operated before entering brake mode) shows a high current (close to start current) declining to 0 A, while the other is reverse operated and does not show any current at all. The brake sequence is considered to be finished when the brake **current falls below 1 A. By using** multiple power stages the limit is 1 A per power stage. A reverse motor run now can be started.

## 6.5.9.3 Paralleled High Side Power Stage Control

This configuration can be needed for to increasing inrush current capability. However, in case of a short circuit this also dramatically increases the peak current that might be drawn out of the battery terminals. It is strongly recommended to first switch on only **one single power stage and measure**
the output voltage. If the output voltage is > **0.75xVBAT this indicates that no short circuit is on the**
motor terminals and the other 1 to 3 high side power stages working in parallel can be switched on.

The time that only one single power stage is working shall be limited to <= **20 ms. Important: this**
sequencing applies only on the high side power stages. The low side outputs needs to be switched on first.

## 6.6 Power Stage Alternative Functions

This application note describes the DO and DON'TS when using **the alternative functions of HY-TTC** 500 high- and low-side power stages.

## 6.6.1 High-Side Output Stages

High-side power stages can alternatively used as analog, digital or frequency inputs.

## Bat+Power +0,5 V

In all high-side power stages there is a parasitic diode that **conducts if the output voltage or, in case** of alternative input function, the input voltage is externally driven higher than the voltage on the BAT+Power supply pins. The input voltage on all high-side stages, including the alternative input functions, must never exceed the power stage supply BAT+ Power +0,5 V. This application requirement is valid in active, standby and power-off state of the ECU.

To counteract such fault scenarios, maximum ratings and specified wiring examples must be followed and are essential for safe operation.

## 6.6.1.1 Wiring Examples Attention!

In many applications external switches (open collector, open drain (NPN) or a push-pull type), pushbuttons or analog sensors have to be monitored by an alternative input of the ECU. Switches which are directly switching to battery voltage must not be used with alternative inputs.

For safety critical applicactions, however, additional restrictions apply, see the following sections.

## Workarounds For Safety Critical Applications:

- Usage of external switches connected to GND.

Short circuits to battery supply needs to be excluded in the system architecture.

- Battery supplied switches and sensors need to be supplied via a digital output of the HY-TTC
500.

6.6.1.1.1  Valid Wiring Examples    The following wiring examples for external switches and analog sensors connected to battery supply (PWM/digital high-side output) and to GND are allowed and can help avoiding system fault scenarios:

## Switch Connected To Gnd:

Usage of external switches connected to GND.

Short circuits to battery supply needs to be excluded in the system architecture.

![230_image_0.png]( The image is a diagram of an electrical circuit with various components labeled throughout. There are two main sections within the circuit, one on the left side and another on the right side.

In the left section, there are multiple labels indicating different parts of the circuit, such as "BATPOWER," "BATTERY," "BATT," and "BAT." The right section features a more complex arrangement of components, including labels like "CORE," "KC," "LOOP," and "POWER."

There are also two switches visible in the circuit diagram, one located near the center-left side and another closer to the bottom-right corner. These switches likely control different aspects of the electrical system within the circuit.)

![230_image_1.png]( The image features a diagram of an electrical system with multiple components labeled and connected to each other. There are several batteries placed throughout the circuit, some closer together while others are spaced further apart. A mix of wires can be seen connecting these batteries to various parts of the system, creating a complex network of connections.

In addition to the batteries, there is a clock visible in the middle-left part of the diagram, possibly indicating the time or providing reference for the electrical system's operation. The overall layout and arrangement of components suggest that this could be an illustration of a power supply or an electrical circuit.)

![231_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled and connected to each other. There are multiple batteries present in the circuit, some placed near the top left corner while others can be found closer to the center of the image.

A series of switches are also visible throughout the circuit, with one located at the bottom right side and another towards the middle-right area. The diagram seems to provide a clear representation of how these components work together in an electrical system.)

## Switches Connected To Pwm High-Side Output Stage:

Digital switches and analog sensors are supplied via an HY-TTC 500 PWM high-side output pin, the switch/sensor output is monitored by an alternative (PWM high-side) input.

Caution! - The sourcing PWM high-side output stage (IO_PWM_00 - IO_PWM_35) must be out of the same secondary shut-off path (A, B or C) as the alternative input pin. For example IO_PWM_00 (output/source) supplies the digital sensor and the sensor output is monitored by IO_PWM_13 (input), both IO's are out of secondary shut-off path A. See Table 22 on page 138 for secondary shut-off paths and their relation to the alternative inputs.

![231_image_1.png]( The image displays a diagram of an electrical circuit with various components and labels. There are multiple batteries present in the circuit, including one labeled "battery" at the top left corner and another towards the right side. A series of switches can be seen throughout the circuit, with some located near the center and others closer to the edges.

In addition to the switches, there are several other labels visible in the diagram, indicating different parts of the electrical system. The overall layout of the circuit appears complex, showcasing a detailed understanding of its components and their relationships.)

![232_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled throughout. There are multiple batteries and power sources, including one towards the left side of the image, another near the center, and two more on the right side. A green battery can be seen in the middle-right area of the image.

The circuit also features a number of switches, with one located at the top-left corner, another close to the center, and a third towards the bottom-right part of the diagram. There are two power supplies visible, one on the left side and the other in the middle-right area. A computer is also present within the circuit, situated near the center.

Overall, this image provides an overview of an intricate electrical system with multiple components working together to create a functional circuit.)

![232_image_1.png]( The image displays a detailed diagram of an electrical circuit with various components and connections. There are multiple batteries visible throughout the circuit, some placed closer to the left side while others are positioned more towards the right. A series of wires can be seen connecting these batteries to other parts of the circuit, creating a complex network of interconnected elements.

In addition to the batteries and wires, there is an array of switches and buttons scattered throughout the diagram. These components likely control different aspects of the electrical system or allow for user input in the operation of the circuit. Overall, the image provides a comprehensive view of the intricate workings of an electrical circuit.)

## Switches Connected To Digital High-Side Output Stage:

Digital switches and analog sensors are supplied via an HY-TTC 500 digital high-side output pin, the switch/sensor output is monitored by an alternative (digital high-side) input. IO_DO_00 - IO_DO_07 and IO_PVG_00 - IO_PVG_07 are not equipped with an secondary shut-off

![233_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled throughout the drawing. There are multiple batteries and power sources, including one near the top left corner, another at the bottom right, and two more towards the center-left side. A cell phone is also present in the middle area of the circuit.

The diagram includes a number of wires connecting these components to create an intricate network. Some of the wires are located on the left side of the image, while others can be found near the top right corner and the center-right part of the drawing. The overall layout of the circuit is quite complex, showcasing the interconnectedness of various electrical elements.)

paths. These high-side output stages can by themselves not be used for safety critical applications. If the alternative input function of IO_DO_00 - IO_DO_07 and **IO_PVG_00 - IO_PVG_07 shall be** used, the connected sensor must be supplied by an digital output stage out of these outputs.

6.6.1.1.2  Invalid Wiring Examples    The following wiring examples of external switches or analog sensors connected to battery supply are not allowed and must be avoided for safety critical systems.

Nonconforming wiring can lead to destruction of the HY-TTC 500.

## Stop Switch / Blown Fuse / K15 Wiring

Digital switches and analog sensors are supplied directly from the battery.

If for example the fuse is blown, BAT+Power is disconnected (loose connection) or the stop switch is pressed, digital switches or analog sensors are still supplied. The current flows over the closed switch and the parasitic body diode of the output stage used as input. All the load current of all other outputs now flows via the body diode of this single output stage. This may overload and even destroy this output stage.

![234_image_0.png]( The image displays a diagram of an electrical system with various components and connections. There are multiple batteries visible throughout the scene, some connected to other parts of the circuit while others remain separate. A few cords can be seen running through the system, likely carrying electricity between different components.

In addition to the batteries and cords, there is a computer processor present in the diagram, indicating that this electrical system may also serve as part of a larger electronic device or machine. The intricate arrangement of these elements suggests that it could be an illustration of a complex electrical circuit or a schematic for a specific project.)

![234_image_1.png]( The image displays a diagram of an electrical circuit with various components labeled and connected to each other. There are multiple wires and connections throughout the circuit, indicating that it is a complex system. Some key components include a battery, which can be found on the left side of the image, as well as several switches and connectors scattered around the circuit.

In addition to these elements, there are two clocks visible in the diagram, one located towards the center-left area and another near the top right corner. These clocks may serve as a reference for the timing or synchronization of the electrical system.)

## 7 Debugging 7.1  Functional Description

After connecting the HY-TTC 500 and the Lauterbach Debugging Device with the TTC JTAG-Adapter Board (for the connector pinning, see Figure 83 on the current page), open the Trace32 Software for ARM CPUs. Double-click the batch file flash.cmm , which is located in the corresponding template directory. When prompted by the dialog whether to flash the application or to load only the symbols for debugging, click Yes to start the flashing procedure.

![235_image_0.png]( The image displays a diagram of Texas Instruments Programmer circuitry with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts together.

The diagram is organized into several sections, including a large section in the center that contains many connections. Other smaller sections can be found around the edges of the image, indicating additional components or connections within the overall circuitry. The arrangement and labels on this Texas Instruments Programmer make it easy to understand its structure and function.)

| Manufacturer:              | TE CONNECTIVITY / AMP   |
|----------------------------|-------------------------|
| Manufacturer Article Code: | 2-1634689-0             |
| Farnell Order Number:      | 8396027                 |

Table 32: Order code of JTAG connector on the TTC JTAG-Adapter Board For debugging details, see [ 31 ].

Software Description

## 8 Api Documentation

Please refer to [30] for the API documentation of the HY-TTC 500 I/O driver.

| Entry   | Description                                         |
|---------|-----------------------------------------------------|
| 2M      | 2 Mode                                              |
| 3M      | 3 Mode                                              |
| A/D     | Analog and Digital                                  |
| ADC     | Analog-to-Digital Converter                         |
| API     | Application Programming Interface                   |
| CAN     | Controller Area Network                             |
| CPU     | Central Processing Unit                             |
| CTS     | Clear to Send                                       |
| DC      | Direct Current                                      |
| DI      | Digital Input                                       |
| DOUT    | Digital Output                                      |
| DO      | Digital Output                                      |
| ECU     | Electronic Control Unit                             |
| EEPROM  | Electrically Erasable Programmable Read-Only Memory |
| EMC     | Electromagnetic Compatibility                       |
| Flash   | Nonvolatile computer storage                        |
| GND     | Ground                                              |
| HS      | High Side                                           |
| HW      | Hardware                                            |
| I/O     | Input and Output                                    |
| IN      | Input                                               |
| LIN     | Local Interconnect Network                          |
| LSB     | Least Significant Bit                               |
| LS      | Low Side                                            |

| Entry       | Description                                   |
|-------------|-----------------------------------------------|
| MRD         | Mounting Requirements Document                |
| Max.        | Maximal                                       |
| Min.        | Minimal                                       |
| OUT         | Output                                        |
| PC          | Personal Computer                             |
| PD          | Pull Down                                     |
| PID         | Proportional Integral Differential            |
| PL          | Performance Level                             |
| PU          | Pull Up                                       |
| PVG         | Proportional Valve Group                      |
| PWD         | Pulse Width Demodulation                      |
| PWM         | Pulse With Modulation                         |
| RTC         | Real-Time Clock                               |
| RTS         | Request to Send                               |
| SIL         | Safety Integrity Level                        |
| SRC         | Signal Range Check                            |
| SSUP        | Sensor Supply                                 |
| SW          | Software                                      |
| TBD         | To Be Defined                                 |
| Tambient    | Ambient Temperature                           |
| Terminal 15 | Battery+ from ignition switch                 |
| UNECE       | United Nations Economic Commission for Europe |
| Ubat        | Battery Voltage                               |
| VOUT        | Voltage Output                                |

## References

[1] ANSI. CISPR 25 ED. 3.0 B:2008, vehicles, boats and internal combustion engines - radio disturbance characteristics - limits and methods of measurement for the **protection of on-board receivers. American** National Standard, American National Standards Institute, Inc., 2008.

[2] DIN. DIN EN 60068-2-11:2000-02, Umweltprüfungen - Teil **2: Prüfungen; Prüfung Ka: Salznebel (IEC**
60068-2-11:1981 . European Standard, Deutsches Institut für Normung (DIN), 2000.

[3] DIN. DIN EN 60068-2-30:2006-06, Umgebungseinflüsse - Teil 2-30: Prüfverfahren - Prüfung Db:
Feuchte Wärme, zyklisch (12 + 12 Stunden) (IEC 60068-2-30:2005) . European Standard, Deutsches Institut für Normung (DIN), 2006.

[4] DIN. DIN EN 13309:2010-12 (E), *Construction machinery - Electromagnetic compatibility of machines* with internal power supply . European Standard, Deutsches Institut für Normung (DIN), **2010.**
[5] DIN. DIN EN 60068-2-38:2010-06, Umgebungseinflüsse - Teil 2-38: Prüfverfahren - Prüfung Z/AD:
Zusammengesetzte Prüfung, Temperatur/Feuchte, zyklisch **(IEC 60068-2-38:2009) . European Standard, Deutsches Institut für Normung (DIN), 2010.**
[6] IEC. IEC 61000-6-2:2005, *Electromagnetic compatibility (EMC) - Part 6-2: Generic standards - Immunity for industrial environments (2nd ed.)* **. International Standard, International Electrotechnical Commission (IEC), 2005.**
[7] IEC. IEC 61000-6-4:2007, *Electromagnetic compatibility (EMC) - Part 6-4: Generic standards - Emission standard for industrial environments* **. International Standard, International Electrotechnical Commission (IEC), 2007.**
[8] IEC. IEC 61508:2010, Functional safety of electrical/electronic/programmable electronic safety-related systems**. International Standard, International Electrotechnical Commission (IEC), 2010.**
[9] IEC. IEC 60068-2-78:2012, Environmental testing - Part 2-78: Tests - Tests - Test Cab: Damp heat, steady state **. International Standard, International Electrotechnical Commission (IEC), 2012.**
[10] IEC. IEC 61131-3:2013, *Programming languages (3rd ed.)***. International Standard, International Electrotechnical Commission (IEC), 2013.**
[11] ISO. ISO 14982:1998, *Agricultural and forestry machinery - Electromagnetic compatibility - Test methods and acceptance criteria*. International Standard, International Organization for **Standardization**
(ISO), 1998.

[12] ISO. ISO 11452-2:2004 , Road vehicles - Component test methods for electrical disturbances from narrowband radiated electromagnetic energy - Part 2: Absorber-lined shielded enclosure**. International** Standard, International Organization for Standardization (ISO), 2004.

[13] ISO. ISO 16750-1:2006, *Road vehicles - Environmental conditions and testing for electrical and electronic equipment - Part 1: General (2nd ed.)***. International Standard, International Organization for**
Standardization (ISO), 2006.

[14] ISO. ISO 7637-3:2007, *Road vehicles - Electrical disturbances from conduction and coupling - Part 3:*
Electrical transient transmission by capacitive and inductive coupling via lines other than supply lines. International Standard, International Organization for Standardization (ISO), 2007.

[15] ISO. ISO 10605:2008, *Road vehicles - Test methods for electrical disturbances from electrostatic discharge*. International Standard, International Organization for **Standardization (ISO), 2008.**
[16] ISO. ISO 13849:2008-12, *Safety of machinery - Safety-related parts of control systems***. International**
Standard, International Organization for Standardization (ISO), 2008.

[17] ISO. ISO 20653:2013, Road vehicles - Degrees of protection (IP code) - Protection of electrical equipment against foreign objects, water and access. International Standard, International Organization for Standardization (ISO), 2008.

[18] ISO. ISO 16750-4:2010, *Road vehicles - Environmental conditions and testing for electrical and electronic equipment - Part 4: Climatic loads (3rd ed.)***. International Standard, International Organization**
for Standardization (ISO), 2010.

[19] ISO. ISO 16750-5:2010, *Road vehicles - Environmental conditions and testing for electrical and electronic equipment - Part 5: Chemical loads (2nd ed.)***. International Standard, International Organization**
for Standardization (ISO), 2010.

[20] ISO. ISO 7637-2:2011, Road vehicles - Electrical disturbances from conduction and coupling - Part 2:
Electrical transient conduction along supply lines only (2nd ed.)**. International Standard, International** Organization for Standardization (ISO), 2011.

[21] ISO. ISO 11783-2:2012(E), *Tractors and machinery for agriculture and forestry - Serial control and* communications data network - Part 2: Physical Layer (2nd ed.)**. International Standard, International**
Organization for Standardization (ISO), 2012.

[22] ISO. ISO 16750-2:2012, *Road vehicles - Environmental conditions and testing for electrical and electronic equipment - Part 2: Electrical loads (4th ed.)***. International Standard, International Organization**
for Standardization (ISO), 2012.

[23] ISO. ISO 16750-3:2012, *Road vehicles - Environmental conditions and testing for electrical and electronic equipment - Part 3: Mechanical loads (3rd ed.)***. International Standard, International Organization**
for Standardization (ISO), 2012.

[24] ISO. ISO 13849:2015, *Safety of machinery - Safety-related parts of control systems***. International**
Standard, International Organization for Standardization (ISO), 2015.

[25] ISO. ISO 25119:2018, Tractors and machinery for agriculture and forestry - Safety-related parts of control systems. International Standard, International Organization for **Standardization (ISO), 2018.**
[26] ISO. ISO 26262:2018, Road vehicles - Functional safety. International Standard, International Organization for Standardization (ISO), 2018.

[27] TTControl. HY-TTC 500 Mounting Requirements Document. User Documentation D-TTC5F-M-02-004, TTTech, Off-Highway-Services.

[28] TTControl. HY-TTC 500 Product Drawing. User Documentation D-TTC5F-C-20-007, TTTech, OffHighway-Services.

[29] TTControl. HY-TTC 500 Safety Manual. User Documentation D-TTC5F-M-02-002, TTTech, OffHighway-Services.

[30] TTControl GmbH. HY-TTC 500 I/O Driver Manual. S-TTC5F-G-20-001.

[31] TTControl GmbH. HY-TTC 500 Quick Start Guide - C Programming. User Documentation D-TTC5F-G20-004, TTTech, BU Off-Highway, Services & Operations.

| - A -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Analog input 2 mode 124 analog current input 129 analog voltage input 126 functional description 125 maximum ratings 125 pinout 124 Analog input 3 mode 116 analog current input 120 analog resistance input 121 analog voltage input 117 functional description 116 maximum ratings 117 pinout 116 API Documentation 226 Application notes 192 cable harness 192 ground connection of housing 195 handling of high-load current 193 load distribution 193 total load current 193 i/o alternative functions 218 high-side output stages 218 inductive loads 195 motor control 196 Cabling 216 connection 208 control sequence for bidirectional drive216 direct control options 196 motor classification 200 motor details 197 motor types supported 196 parallel operation of power stages 216 power stages for motor control 215 |

| - B -                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BAT+ CPU 98 characteristics 100 functional description 99 low-voltage Operation 101 maximum ratings 100 pinout 98 voltage monitoring 103 BAT+ Power 96 characteristics 97 |

## Index

- D —
Debugging.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .224 functional description .. . . . . . . . . . . . . . . . . . 224

| functional description 96 maximum ratings 97 pinout 96                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOSCH mating connector 58 positions 46 96 positions 46 crimp contacts 47 tools 47 - C - CAN 175 characteristics 178 functional description 176 maximum ratings 178 pinout 175 CAN termination 179 functional description 180 pinout 179 Communication interfaces 2 Connector 42 Connector pinning HY-TTC 508 90 HY-TTC 510 70 HY-TTC 520 64 HY-TTC 540 57 HY-TTC 580 50 HY-TTC 590 83 HY-TTC 590E 76 |

| - F -                        |
|------------------------------|
| Functional safety 38 Fuse 48 |

| - E -                                                                  |
|------------------------------------------------------------------------|
| Ethernet 181 functional description 182 maximum ratings 182 pinout 181 |

| - H -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hardware description 1 High-side digital outputs 149 analog and digital inputs 153 diagnostic functions 151 functional description 150 mutual exclusive mode 151 power stage pairing 151 high-side digital outputs 152 maximum ratings 151 pinout 149 High-side digital/PVG/VOUT outputs 155 analog voltage inputs 163 digital inputs 163 functional description 156 mutual exclusive mode 156 power stage pairing 156 high-side digital outputs 157 maximum_ratings 156 pinout 155 PVG outputs 159 VOUT outputs 161 High-side PWM outputs 137, 141 diagnostic functions 141 digital and frequency inputs 144 external shut-off groups 147 functional description 138 mutual exclusive mode 140 power stage pairing 140 high-side digital outputs 144 maximum ratings 140 pinout 137 secondary shut-off paths 146 tertiary shut-off path 148 functional description 148 HY-TTC 500 family variant pinning 49 HY-TTC 500 Variants 3 |

| - I -                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs 2, 96 Instructions for safe operation 39 Internal structure 188 overview safety concept 188 safety concept 188 thermal management 190 board temperature sensor 190 Introduction 2 |

- M —
Mating connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 Motor control high side power stages for PWM operation 215 motor control high side power stages for static operation 215 Mounting requirements.. . . . . . . . . . . . . . . . . . . . . . .41

| - K -                                                                              |
|------------------------------------------------------------------------------------|
| KOSTAL mating connector 58 positions 44 96 positions 44 crimp contacts 45 tools 45 |

| - L -                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Label 41 LIN 170 characteristics 172 functional description 171 maximum ratings 172 pinout 170 Low-side digital outputs 165 analog voltage inputs 169 diagnostic functions 167 digital inputs 169 functional description 166 power stage pairing 167 low-side outputs 168 maximum ratings 167 pinout 165 |

- N —
Negative power supply BAT- . . . . . . . . . . . . . . . . . 104 functional description .. . . . . . . . . . . . . . . . . . 105 maximum ratings . . . . . . . . . . . . . . . . . . . . . . . 105 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
- O —
Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2, 96

| - P -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pinning and connector 42 Programming options 3 - R - RS232 173 characteristics 174 functional description 174 maximum ratings 174 pinout 173 RTC backup battery 185 characteristics 187 functional description 186 maximum ratings 187 pinout 185 - S - Safety and certification 2 Safety concept 188 Sensor GND 106 functional description 107 maximum ratings 107 pinout 106 Sensor supplies 5 V 112 characteristics 113 functional description 112 maximum ratings 113 pinout 112 Sensor supply variable 114 characteristics 115 functional description 114 maximum ratings 115 pinout 114 Software description 225 Standards and guidelines 35 chemical capability 37 climatic capability 36 electrical capability 36 industrial applications ESD and EMC capability 38 ingress protection capability 37 mechanical capability 36 road vehicles ESD and EMC capability 38 |

| - W -                                                                                     |
|-------------------------------------------------------------------------------------------|
| Wake-Up 110 characteristics 111 functional description 110 maximum ratings 111 pinout 110 |

| - T -                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terminal 15 108 characteristics 109 functional description 109 maximum ratings 109 pinout 108 Timer inputs 130 analog voltage input 136 current loop input 134 digital input 136 functional description 131 maximum ratings 131 pinout 130 timer input 134 |

## Notice

If disposal has to be undertaken after the life span of the device, the respective applicable country-specific regulations are to be observed.

## Legal Disclaimer

THE INFORMATION GIVEN IN THIS DOCUMENT IS GIVEN AS A SUPPORT FOR THE USAGE OF THE PRODUCT AND SHALL NOT BE REGARDED AS ANY DESCRIPTION OR **WARRANTY**
OF A CERTAIN FUNCTIONALITY, CONDITION OR QUALITY OF THE PRODUCT. THE RECIPIENT OF THIS DOCUMENT MUST VERIFY ANY FUNCTION DESCRIBED HEREIN IN THE REAL
APPLICATION. THIS DOCUMENT WAS MADE TO THE BEST OF KNOWLEDGE **OF TTCONTROL GMBH. NEVERTHELESS AND DESPITE GREATEST CARE, IT CANNOT BE EXCLUDED**
THAT MISTAKES COULD HAVE CREPT IN. TTCONTROL GMBH PROVIDES THE DOCUMENT
FOR THE PRODUCT "AS IS" AND WITH ALL FAULTS AND HEREBY DISCLAIMS ALL WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING **BUT NOT LIMITED**
TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, ACCURACY OR COMPLETENESS, OR OF RESULTS TO THE EXTENT PERMITTED
BY APPLICABLE LAW. THE ENTIRE RISK, AS TO THE QUALITY, USE OR PERFORMANCE OF THE DOCUMENT, REMAINS WITH THE RECIPIENT. TO THE MAXIMUM EXTENT PERMITTED
BY APPLICABLE LAW TTCONTROL GMBH SHALL IN NO EVENT BE LIABLE FOR ANY SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES WHATSOEVER (INCLUDING
BUT NOT LIMITED TO LOSS OF DATA, DATA BEING RENDERED INACCURATE, BUSINESS INTERRUPTION OR ANY OTHER PECUNIARY OR OTHER LOSS WHATSOEVER) **ARISING OUT**
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
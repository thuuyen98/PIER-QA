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

HY-TTC 500 System Manual V 1.6.0 Contents iii

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

HY-TTC 500 System Manual V 1.6.0 Contents v

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

HY-TTC 500 System Manual V 1.6.0 Contents vii

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

| Feature                                                   | HY-TTC 580            | HY-TTC 540   | HY-TTC 520   | HY-TTC 510   | HY-TTC 590E   | HY-TTC 590   | HY-TTC 508   |       |
|-----------------------------------------------------------|-----------------------|--------------|--------------|--------------|---------------|--------------|--------------|-------|
| CPU                                                       | 32-bit TI TMS570      | x            | x            | x            | x             | x            | x            | x     |
| Int. FLASH                                                | 3 MB                  | 3 MB         | 3 MB         | 3 MB         | 3 MB          | 3 MB         | 3 MB         |       |
| Int. RAM                                                  | 256 kB                | 256 kB       | 256 kB       | 256 kB       | 256 kB        | 256 kB       | 256 kB       |       |
| Memory                                                    | Ext. FLASH            | 8 MB         | -            | -            | -             | 64 MB        | 32 MB        | 16 MB |
| Ext. RAM                                                  | 2 MB                  | 2 MB         | 2 MB         | 2 MB         | 2 MB          | 2 MB         | 2 MB         |       |
| Ext. EEPROM                                               | 64 kB                 | 64 kB        | 64 kB        | 64 kB        | -             | -            | 64 kB        |       |
| Ext. FRAM                                                 | -                     | -            | -            | -            | 32 kB         | 32 kB        | -            |       |
| Interface                                                 | CAN                   | 4            | 4            | 4            | 3             | 4            | 4            | 3     |
| CAN1 is ISOBUS Compliance                                 | -                     | -            | -            | -            | x             | x            | x            |       |
| CAN bus termination                                       | 4                     | 4            | 4            | 3            | 4             | 4            | 3            |       |
| Ethernet                                                  | 1                     | -            | -            | -            | -             | -            | -            |       |
| 100BASE-T1 Ethernet                                       | -                     | -            | -            | -            | 1             | 1            | 1            |       |
| LIN                                                       | 1                     | -            | -            | 1            | 1             | 1            | -            |       |
| RS232                                                     | 1                     | -            | -            | -            | 1             | 1            | -            |       |
| Real time clock                                           | 1                     | -            | -            | -            | 1             | 1            | 1            |       |
| Outputs                                                   | High-Side PWM with CM | 36           | 28           | 18           | 16            | 36           | 36           | 10    |
| High-Side digital                                         | 16                    | 8            | 8            | 8            | 16            | 16           | 8            |       |
| High-Side digital, PVG, VOUT                              | 0                     | -            | -            | 8            | 0             | 0            | 6            |       |
| Low-Side digital                                          | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| Inputs Analog input 3 modes (V)(I)(R)                     | 8                     | 8            | 8            | 8            | 8             | 8            | 8            |       |
| Analog input 2 modes (V)(I)                               | 16                    | 16           | 16           | 16           | 16            | 16           | 16           |       |
| Analog input (V)                                          | -                     | 8            | -            | -            | -             | -            | -            |       |
| Timer input                                               | 12                    | 20           | 20           | 20           | 12            | 12           | 20           |       |
| Terminal 15                                               | 1                     | 1            | 1            | 1            | 1             | 1            | 1            |       |
| Wake-Up                                                   | 1                     | 1            | 1            | 1            | 1             | 1            | 1            |       |
| Sensor supply                                             | +5V/500mA             | 2            | 2            | 2            | 2             | 2            | 2            | 1     |
| +5-10V/2.5W                                               | 1                     | 1            | 1            | 1            | 1             | 1            | -            |       |
| Safety Switch Nr. of secondary shut-off path              | 3                     | 2            | 2            | 2            | 3             | 3            | 2            |       |
| Table 2: Variants overview for the Spartan-6 XA6SLX9 FPGA |                       |              |              |              |               |              |              |       |

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

![18_image_0.png]( The image displays a diagram or flowchart with various labels and icons arranged on it. There are several sections of the chart that provide information related to digital audio workstations (DAWs) and their components. Some of these labels include "arm cortex," "32 bit float," "16 bit integer," "8 bit integer," "32 bit float," and "16 bit float."

In addition, there are multiple icons representing different aspects of the digital audio workstation, such as a computer mouse for navigation, a speaker for sound output, and a lightning bolt symbolizing the application's power. The chart is organized in a way that allows users to understand the various components and functionalities of the digital audio workstation.) 

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
- Board temperature, sensor supply and battery monitoring

## Inputs

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

![22_image_1.png]( The image is a diagram with several blue labels on it, likely representing different settings or options for an electronic device. There are at least five distinct labels visible, each providing information about the device's features and functions.

The labels are arranged in various positions across the diagram, indicating that they might be related to different aspects of the device. The overall layout suggests a well-organized presentation of the device's settings or options for users to understand and navigate easily.)

![22_image_0.png](16 different audio files are displayed on a computer screen with their respective file names and sizes. The files vary in size, ranging from small to large, indicating that they may contain various types of audio content. Each file name is accompanied by its corresponding file size, allowing users to easily identify the size of each audio file.) 

8 0–32 V

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

Communication Interfaces
- 4 x CAN (50 to 1000 kbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection
- Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |
| 8 x timer input            | Frequency and pulse width measurement                                                                                                 |
| 8 x analog input           | 0 to 32 V                                                                                                                             |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

| 28 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input                                                                             |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Outputs Specifications

| Dimensions                    | See [28]                                                                                                        |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Weight                        | See [28]                                                                                                        |
| Operating ambient temperature | -40 °C to +85 °C                                                                                                |
| Storage temperature           | -40 °C to +85 °C                                                                                                |
| Housing                       | IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier |
| Operating altitude            | 0 to 4000 m                                                                                                     |

![26_image_0.png]( The image is a diagram that shows various settings and options for an ARM Cortex processor. There are multiple sections within this diagram, each with different settings or information related to the processor. Some of these sections include "Digital In," "Digital Out," "Sensor Supply," and "HSW Out."

In addition to these sections, there is a list of options that includes "Terminal 16," "Wake Up," "Sleep," "Low Power," "DMA," "Interrupt," "Pin Muxing," "Clock," "Reset," and "HSW Out." The diagram also features several arrows pointing to different sections, indicating the connections or relationships between them.) 

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

Communication Interfaces
- 4 x CAN (50 to 1000 kbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection
- Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 8 x timer input            | Frequency and pulse width measurement                                                                                                 |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

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

![30_image_1.png]( The image features a diagram with several blue boxes and labels, likely representing different components of an electronic device or system. There are at least ten distinct labels visible on the diagram, each providing information about the various parts involved.

In addition to the labels, there is a clock in the upper left corner of the diagram, which might be used for timekeeping purposes within the system. The overall layout and content of the diagram suggest that it could be an educational or technical resource related to electronics or computer hardware.) 

![30_image_0.png](16-bit Eprom is displayed on a computer screen with various options and settings. The screen shows a list of numbers, including a row of sixteen numbers arranged vertically. There are also two buttons visible at the top left corner of the screen, possibly for navigating or selecting different options within the program.) 

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
- Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software - Board temperature, sensor supply and battery monitoring

## Inputs

| 8 x analog input 3 modes   | Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 16 x analog input 2 modes  | Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA        |
| 8 x timer input            | Frequency and pulse width measurement                                                                                                 |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V                                             |
| 6 x timer input            | Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V |

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

| 16 x PWM-controlled HS Outputs   | PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback   |
|----------------------------------|-------------------------------------------------------------------------------------------|
| when used as an input            | Digital input                                                                             |
| 8 x digital HS outputs           | Digital output mode Nominal current 4 A with voltage feedback                             |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x digital LS outputs           | Digital output mode Nominal current 4 A                                                   |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |
| 8 x HS outputs                   | Digital output mode PVG output Voltage output (VOUT)                                      |
| when used as an input            | Voltage measurement 0 to 32 V Digital input                                               |

## Outputs

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

![34_image_1.png]( The image is a close-up of a computer screen displaying several lines of text and numbers. These lines are organized into different sections or categories, with some labeled "Digital Numerical" and others containing various other terms. There are multiple instances of the number "10," which could be related to the content displayed on the screen. The overall appearance suggests that this is a technical document or reference material for a specific topic.) 

![34_image_0.png]( The image displays a series of blue and white icons arranged on a grid-like structure. Each icon represents a different function or feature, with some being larger than others. There are at least thirteen distinct icons visible in the image, each one providing information about various aspects related to the subject matter.

The arrangement of these icons creates an organized and visually appealing presentation, making it easy for viewers to understand the different functions available. The use of blue and white colors adds a sense of cohesion and professionalism to the overall design.) 

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

## Communication Interfaces

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

- 7 x CAN (50 to 1000 kbit/s) (CAN1 is ISOBUS compliant)
- 1 x LIN (up to 20 kBd) - 1 x RS232 (up to 115 kBd)
- 1 x 100BASE-T1 BroadR-Reach® **(100 Mbit/s)**

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

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

![38_image_0.png]( The image is a diagram that shows various settings and options for an ARM Cortex processor. There are multiple sections within the diagram, each with different information related to the processor's configuration. Some of these sections include "Digital Input," "Digital Output," "Analog Input," and "Analog Output."

In addition to these main sections, there is a list of options for each section, such as "Sensor Supply," "Digital I/O," and "ADC." The diagram also features a clock that shows the time in different formats. Overall, this image provides an organized view of various settings and options available for the ARM Cortex processor.) 

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

## Communication Interfaces

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

- 7 x CAN (50 to 1000 kbit/s) (CAN1 is ISOBUS compliant)
- 1 x LIN (up to 20 kBd) - 1 x RS232 (up to 115 kBd)
- 1 x 100BASE-T1 BroadR-Reach® **(100 Mbit/s)**

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

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

![42_image_0.png]( The image displays a diagram with several options and settings for an ARM Cortex processor. There are multiple buttons arranged across the diagram, each representing different features or functions of the processor. Some of these buttons include "Digital Input," "Digital Output," "Analog Input," "Analog Output," "Sleep Mode," and others. The diagram appears to be a user guide or reference for understanding and utilizing the ARM Cortex processor effectively.) 

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
- Board temperature, sensor supply and battery monitoring

## Inputs

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

![46_image_0.png]( The image is a diagram that illustrates various aspects of a product or process. It consists of multiple nodes and arrows connecting them, representing different elements involved in the subject matter. Some key points include "Supply voltage," "Mechanical vibration," "Temperature," and "Climatic conditions." There are also references to "Electrical," "Chemical," and "Protection" within the diagram. The nodes and arrows help to visualize the relationships between these elements, making it easier to understand the product or process being discussed.)

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

![50_image_0.png]( The image features a white piece of paper with various information written on it. There are two main sections of text, one occupying most of the left side and another towards the right side. A small part of the paper is highlighted in red, possibly indicating an important detail or section.

In addition to the text, there are several numbers scattered throughout the document, with some appearing more prominently than others. The presence of these numbers suggests that they might be related to specific data points or measurements. Overall, the content on this piece of paper seems to be informative and possibly technical in nature.)

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

![53_image_0.png]( The image features a white background with two black objects placed on it. These objects appear to be a pair of scissors and a knife, both lying horizontally across the background. The scissors are positioned slightly above the knife in terms of height. This arrangement creates an interesting contrast between the black objects and the white background.) 

Note: **The main connector is numbered from 1 to 96 (left connector) and 1 to 58 (right connector).** This correspond to pins 101 to 196 and 201 to 258, respectively, in this System Manual.

## 3.2 Mating Connector

The listed part numbers can be ordered from HERTH+BUSS, KOSTAL or BOSCH with a minimum quantity of, for example, 100 pieces.

For lower quantities, TTControl GmbH provides complete kits with BOSCH connectors, crimp contacts and sealings.

| TTControl Order Numbers   | Description                                |
|---------------------------|--------------------------------------------|
| 10619                     | Connector kit for HY-TTC 500, 58-positions |
| 10620                     | Connector kit for HY-TTC 500, 96-positions |

![54_image_0.png]( The image features a white background with various parts and tools laid out on it. There are two main items in focus - an electronic device and its corresponding parts. The electronic device is placed towards the left side of the image, while the parts are spread across the right side.

In addition to these primary objects, there are several smaller items scattered throughout the scene. These include a cup located near the top-right corner, two screws in the middle area, and three more screws closer to the bottom-left corner of the image. The presence of these parts suggests that they might be used for repairing or assembling the electronic device.)

![54_image_1.png]( The image displays a white background with various parts of an electronic device placed on it. There are three main components visible: a car stereo system, a computer keyboard, and a cell phone. These items are arranged in different positions across the scene, creating an interesting composition.

In addition to these main objects, there is also a smaller cell phone located towards the right side of the image. The arrangement of these electronic devices highlights their diverse functions and showcases the modern technology we use daily.)

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

![59_image_0.png]( The image displays a diagram with multiple layers of information, including a flow chart and several diagrams. There are two main diagrams visible, one on the left side and another on the right side of the image. These diagrams present various components and processes within an electrical system or device.

In addition to these diagrams, there is a bar graph located in the middle of the image, which provides numerical data related to the subject matter. The combination of visual elements and data helps convey complex information about the topic at hand.)

![60_image_0.png]( The image features a blue and white logo for TC Control International. The logo is displayed prominently on the left side of the image with its distinctive design. There are no other elements or distractions visible in the scene, making it a clean and focused representation of the company's branding.)

## 3.5 Hy-Ttc 500 Family Pinning

The following subsections describe the HY-TTC 500 family variant dependent main- and the respective alternative functions on connector pin-level.

Each hardware function in the table, e.g. Pin 101 - **HS PWM Output, is referenced to its main-** (*IO_PWM_28***) and alternative (***IO_DO_44, IO_PWD_12, IO_DI_28***) function.** *IO_xx_yy* **represents** the software define for each function. For more information about API documentation, please refer to Chapter 8 on page **226.**
Please take note that the main function shall be used preferably and the technical specifications must particularly be regarded when alternative functions are to be used. See Chapter 4 **on page** 96 for limits and restrictions.

3.5.1 HY-TTC 580 **Variant**

![61_image_0.png]( The image features a large blue and black graph with numerous numbers on it. It appears to be a financial chart or a data visualization tool that helps analyze and understand information. The chart is filled with various numbers, making it an essential tool for decision-making in the context of finance or other fields that require data analysis.)

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

![62_image_0.png]( The image displays a large blue table with several rows of data arranged neatly. Each row consists of various numbers and text, possibly representing different categories or statistics. There is also a clock visible on the left side of the table, indicating that the time is being tracked alongside the data. The overall layout suggests an organized presentation of information for easy analysis and comparison.)

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

![63_image_0.png]( The image features a black and white table with various columns of text arranged vertically. The first column is titled "Alphabet," while the second column is labeled "Abbreviation." The remaining columns are filled with different words or phrases that appear to be related to the content in the table.

The layout of the table suggests it might be used for organizing information, possibly in a reference book or an educational setting.)

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

![64_image_0.png]( The image displays a large graph with many lines and numbers on it. There are several rows of data points, each representing different categories or measurements. The graph is filled with information, making it an excellent visual representation of the data.)

| HS Digital Output   | Timer Input       | PVG Output   | VOUT Output          | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|-------------------|--------------|----------------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function     |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P171                | HS PWM Output     | IO_DO_29     | IO_DI_13             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_13           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P172                | HS PWM Output     | IO_DO_43     | IO_DI_27             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_27           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P173                | HS Digital Output | IO_ADC_37    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_01            | IO_DI_73          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P174                | HS PWM Output     | IO_DO_47     | IO_PWD_15            |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_31           | IO_DI_31          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P175                | HS PWM Output     | IO_DO_51     | IO_PWD_19            |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_35           | IO_DI_35          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P176                | HS Digital Output | IO_ADC_39    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_03            | IO_DI_75          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P177                | HS PWM Output     | IO_DO_17     | IO_DI_01             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_01           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P178                | HS PWM Output     | IO_DO_31     | IO_DI_15             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_15           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P179                | HS Digital Output | IO_ADC_41    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_05            | IO_DI_77          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P180                | HS PWM Output     | IO_DO_19     | IO_DI_03             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_03           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P181                | HS PWM Output     | IO_DO_33     | IO_DI_17             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_17           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P182                | HS Digital Output | IO_ADC_43    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_07            | IO_DI_79          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P183                | HS PWM Output     | IO_DO_21     | IO_DI_05             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_05           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P184                | HS PWM Output     | IO_DO_35     | IO_DI_19             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_19           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P185                | HS Digital Output | IO_PVG_01    | IO_VOUT_01 IO_ADC_53 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_53            | IO_DI_89          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P186                | HS PWM Output     | IO_DO_22     | IO_DI_06             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_06           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P187                | HS PWM Output     | IO_DO_36     | IO_DI_20             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_20           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P188                | HS Digital Output | IO_PVG_02    | IO_VOUT_02 IO_ADC_54 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_54            | IO_DI_90          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P189                | HS PWM Output     | IO_DO_24     | IO_DI_08             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_08           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P190                | HS PWM Output     | IO_DO_38     | IO_DI_22             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_22           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P191                | HS Digital Output | IO_PVG_04    | IO_VOUT_04 IO_ADC_56 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_56            | IO_DI_92          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P192                | HS PWM Output     | IO_DO_26     | IO_DI_10             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_10           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P193                | HS PWM Output     | IO_DO_40     | IO_DI_24             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_24           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![65_image_0.png]( The image displays a long list of various items, possibly related to automotive or mechanical engineering. It appears to be an inventory or catalogue of products, with each item described in a series of words.

The list is organized into several sections, and the items are arranged vertically down the page. Some of the sections include "Automatische Fahrtücher," "Fahrzeug-Konstruktionen," "Motor-Wagen-Teile," and "Automatische Fahrtücher." The list is quite extensive, covering a wide range of products or services related to automotive engineering.)

| P194                     | HS Digital Output                         | IO_PVG_06   | IO_VOUT_06 IO_ADC_58   |
|--------------------------|-------------------------------------------|-------------|------------------------|
| IO_DO_58                 | IO_DI_94                                  |             |                        |
| P195                     | HS PWM Output                             | IO_DO_28    | IO_DI_12               |
| IO_PWM_12                |                                           |             |                        |
| P196                     | HS PWM Output                             | IO_DO_42    | IO_DI_26               |
| IO_PWM_26                |                                           |             |                        |
| P197 P198 P199 P200 P201 | BAT+ Power                                |             |                        |
| P202                     | BAT+ Power                                |             |                        |
| P203                     | BAT+ Power                                |             |                        |
| P204                     | BAT+ Power                                |             |                        |
| P205                     | BAT+ Power                                |             |                        |
| P206                     | BAT+ Power                                |             |                        |
| P207                     | Terminal 15 IO_ADC_K15                    |             |                        |
| P208                     | LIN IO_LIN                                |             |                        |
| P209                     | CAN 0 Low IO_CAN_CHANNEL_0                |             |                        |
| P210                     | CAN 1 Low IO_CAN_CHANNEL_1                |             |                        |
| P211                     | CAN 2 Low IO_CAN_CHANNEL_2                |             |                        |
| P212                     | CAN 3 Low IO_CAN_CHANNEL_3                |             |                        |
| P213                     | CAN 4 Low IO_CAN_CHANNEL_4                |             |                        |
| P214                     | CAN 5 Low IO_CAN_CHANNEL_5                |             |                        |
| P215                     | CAN 6 Low IO_CAN_CHANNEL_6                |             |                        |
| P216                     | CAN Termination 3L                        |             |                        |
| P217                     | Sensor GND                                |             |                        |
| P218                     | Ethernet TD+ IO_DOWNLOAD, IO_UDP          |             |                        |
| P219                     | Ethernet TDIO_DOWNLOAD, IO_UDP                                           |             |                        |
| P220                     | Wake-Up IO_ADC_WAKE_UP                    |             |                        |
| P221                     | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |             |                        |

![66_image_0.png]( The image displays a large table with multiple rows of data arranged vertically. Each row contains various columns filled with numbers and text, making it appear like a spreadsheet or a chart. There are at least twelve distinct rows visible on the table, each containing different information.

The table is organized in such a way that the data is easily readable and understandable. The presence of multiple rows and columns suggests that this might be a complex dataset or a comprehensive report.)

| HS Digital Output   | Timer Input                              | PVG Output   | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|------------------------------------------|--------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function                            |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P222                | CAN 0 High IO_CAN_CHANNEL_0              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P223                | CAN 1 High IO_CAN_CHANNEL_1              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P224                | CAN 2 High IO_CAN_CHANNEL_2              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P225                | CAN 3 High IO_CAN_CHANNEL_3              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P226                | CAN 4 High IO_CAN_CHANNEL_4              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P227                | CAN 5 High IO_CAN_CHANNEL_5              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P228                | CAN 6 High IO_CAN_CHANNEL_6              |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P229                | CAN Termination 3H                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P230                | Sensor GND                               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P231                | Ethernet RDIO_DOWNLOAD                                          |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P232                | Ethernet RD+ IO_DOWNLOAD                 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P233                | RTC_BACKUP_BAT                           |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P234                | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P235                | CAN Termination 0L                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P236                | CAN Termination 1L                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P237                | CAN Termination 2L                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P238                | LS Digital Output                        | IO_ADC_45    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_09            | IO_DI_81                                 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P239                | LS Digital Output                        | IO_ADC_47    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_11            | IO_DI_83                                 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P240                | LS Digital Output                        | IO_ADC_49    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_13            | IO_DI_85                                 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P241                | LS Digital Output                        | IO_ADC_51    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_15            | IO_DI_87                                 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P242                | RS232 TXD IO_UART                        |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P243                | Sensor GND                               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P244                | Sensor GND                               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P245                | Sensor GND                               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P246                | BAT+ CPU IO_ADC_UBAT                     |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P247                | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P248                | CAN Termination 0H                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P249                | CAN Termination 1H                       |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![67_image_0.png]( The image displays a long row of blue and white text arranged vertically on a black background. It appears to be an organized list or a series of numbers. This arrangement creates a visually appealing contrast between the dark background and the bright colors of the text.)

| P250     | CAN Termination 2H   |           |
|----------|----------------------|-----------|
| P251     | LS Digital Output    | IO_ADC_44 |
| IO_DO_08 | IO_DI_80             |           |
| P252     | LS Digital Output    | IO_ADC_46 |
| IO_DO_10 | IO_DI_82             |           |
| P253     | LS Digital Output    | IO_ADC_48 |
| IO_DO_12 | IO_DI_84             |           |
| P254     | LS Digital Output    | IO_ADC_50 |
| IO_DO_14 | IO_DI_86             |           |
| P255     | RS232 RXD IO_UART    |           |
| P256     | Sensor GND           |           |
| P257     | Sensor GND           |           |
| P258     | Sensor GND           |           |

![68_image_0.png]( The image is a close-up of a computer screen displaying a graph with multiple lines and numbers on it. The graph appears to be showing data or information related to the financial industry. There are several bars visible within the graph, each representing different aspects of the data being analyzed.

The screen also displays a clock in the top right corner, indicating the time while the user is working with the data. Overall, it seems like an informative and detailed visual representation of financial information.)

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

![69_image_0.png]( The image displays a black and white chart with various columns of text. Each column is labeled with different names or descriptions, possibly representing different categories or topics. The chart appears to be organized in a way that allows for easy comparison between the different sections.)

| P124      | Timer Input           | IO_ADC_34          |           |          |
|-----------|-----------------------|--------------------|-----------|----------|
| IO_PWD_10 | IO_DI_46              |                    |           |          |
| P125      | HS PWM Output         | IO_DI_29 IO_PWD_13 |           |          |
| P126      | HS PWM Output         | IO_PWD_17 IO_DI_33 |           |          |
| P127      | Analog Voltage Input  | IO_ADC_01          | IO_ADC_01 | IO_DI_49 |
| IO_ADC_01 |                       |                    |           |          |
| P128      | Analog Voltage Input  | IO_ADC_03          | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03 |                       |                    |           |          |
| P129      | Analog Voltage Input  | IO_ADC_05          | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05 |                       |                    |           |          |
| P130      | Analog Voltage Input  | IO_ADC_07          | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07 |                       |                    |           |          |
| P131      | Analog Voltage Input  | IO_ADC_09          | IO_DI_57  |          |
| IO_ADC_09 |                       |                    |           |          |
| P132      | Analog Voltage Input  | IO_ADC_11          | IO_DI_59  |          |
| IO_ADC_11 |                       |                    |           |          |
| P133      | Analog Voltage Input  | IO_ADC_13          | IO_DI_61  |          |
| IO_ADC_13 |                       |                    |           |          |
| P134      | Analog Voltage Input  | IO_ADC_15          | IO_DI_63  |          |
| IO_ADC_15 |                       |                    |           |          |
| P135      | Analog Voltage Input  | IO_ADC_17          | IO_DI_65  |          |
| IO_ADC_17 |                       |                    |           |          |
| P136      | Analog Voltage Input  | IO_ADC_19          | IO_DI_67  |          |
| IO_ADC_19 |                       |                    |           |          |
| P137      | Analog Voltage Input  | IO_ADC_21          | IO_DI_69  |          |
| IO_ADC_21 |                       |                    |           |          |
| P138      | Analog Voltage Input  | IO_ADC_23          | IO_DI_71  |          |
| IO_ADC_23 |                       |                    |           |          |
| P139      | Timer Input           | IO_PWD_01          | IO_ADC_25 |          |
| IO_PWD_01 | IO_DI_37              |                    |           |          |
| P140      | Timer Input           | IO_PWD_03          | IO_ADC_27 |          |
| IO_PWD_03 | IO_DI_39              |                    |           |          |
| IO_PWD_05 | IO_ADC_29             |                    |           |          |
| P141      | Timer Input IO_PWD_05 | IO_DI_41           |           |          |
| P142      | BAT                       |                    |           |          |
| P143      | BAT                       |                    |           |          |
| P144      | BAT                       |                    |           |          |
| P145      | BAT                       |                    |           |          |
| P146      | Timer Input           | IO_ADC_31          |           |          |
| IO_PWD_07 | IO_DI_43              |                    |           |          |
| P147      | Timer Input           | IO_ADC_33          |           |          |
| IO_PWD_09 | IO_DI_45              |                    |           |          |

![70_image_0.png]( The image displays a large table with several columns of data arranged on it. Each column is labeled and contains different types of information. There are numerous rows within each column, showcasing various data points for each category.

The table appears to be organized in a way that allows easy comparison and analysis of the data. The presence of multiple columns and rows suggests that this could be a spreadsheet or a database used for tracking or analyzing information related to different aspects of a project or organization.)

| HS Digital Output   | IO_ADC_36         |                    |          |
|---------------------|-------------------|--------------------|----------|
| IO_DO_00            | IO_DI_72          |                    |          |
| IO_PWD_14 IO_DI_30  |                   |                    |          |
| P151                | HS PWM Output     | IO_PWD_18 IO_DI_34 |          |
| P152                | HS Digital Output | IO_ADC_38          |          |
| IO_DO_02            | IO_DI_74          |                    |          |
| P153                | HS PWM Output     | IO_DO_16           | IO_DI_00 |
| IO_PWM_00           |                   |                    |          |
| P154                | HS PWM Output     | IO_DO_30           | IO_DI_14 |
| IO_PWM_14           |                   |                    |          |
| P155                | HS Digital Output | IO_ADC_40          |          |
| IO_DO_04            | IO_DI_76          |                    |          |
| P156                | HS PWM Output     | IO_DO_18           | IO_DI_02 |
| IO_PWM_02           |                   |                    |          |
| P157                | HS PWM Output     | IO_DO_32           | IO_DI_16 |
| IO_PWM_16           |                   |                    |          |
| P158                | HS Digital Output | IO_ADC_42          |          |
| IO_DO_06            | IO_DI_78          |                    |          |
| P159                | HS PWM Output     | IO_DO_20           | IO_DI_04 |
| IO_PWM_04           |                   |                    |          |
| P160                | HS PWM Output     | IO_DO_34           | IO_DI_18 |
| IO_PWM_18           |                   |                    |          |
| P161                | HS Digital Output | IO_ADC_52 IO_DI_88 |          |
| P162                | HS PWM Output     | IO_DO_23           | IO_DI_07 |
| IO_PWM_07           |                   |                    |          |
| P163                | HS PWM Output     | IO_DO_37           | IO_DI_21 |
| IO_PWM_21           |                   |                    |          |
| P164                | HS Digital Output | IO_ADC_55 IO_DI_91 |          |
| P165                | HS PWM Output     | IO_DO_25           | IO_DI_09 |
| IO_PWM_09           |                   |                    |          |
| P166                | HS PWM Output     | IO_DO_39           | IO_DI_23 |
| IO_PWM_23           |                   |                    |          |
| P167                | HS Digital Output | IO_ADC_57 IO_DI_93 |          |
| P168                | HS PWM Output     | IO_DO_27           | IO_DI_11 |
| IO_PWM_11           |                   |                    |          |
| P169                | HS PWM Output     | IO_DO_41           | IO_DI_25 |
| IO_PWM_25           |                   |                    |          |
| P170                | HS Digital Output | IO_ADC_59 IO_DI_95 |          |

![71_image_0.png]( The image displays a long list of countries with their respective names and descriptions. There are at least 13 countries visible on this list, each occupying a different position along the length of the page. The countries vary in size and prominence, making it an interesting visual representation of various nations around the world.)

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

![72_image_0.png]( The image displays a table with various columns of data, including dates and numbers. There are multiple rows of information arranged across the table, making it easy to read and understand. The table is filled with different types of data, possibly related to financial or statistical analysis.)

| HS Digital Output        | IO_ADC_58 IO_DI_94                        |          |
|--------------------------|-------------------------------------------|----------|
| HS PWM Output            | IO_DO_28                                  | IO_DI_12 |
| IO_PWM_12                | IO_DO_42                                  | IO_DI_26 |
| IO_PWM_26                |                                           |          |
| P197 P198 P199 P200 P201 | BAT+ Power                                |          |
| P202                     | BAT+ Power                                |          |
| P203                     | BAT+ Power                                |          |
| P204                     | BAT+ Power                                |          |
| P205                     | BAT+ Power                                |          |
| P206                     | BAT+ Power                                |          |
| P207                     | Terminal 15 IO_ADC_K15                    |          |
| P208 P209                | CAN 0 Low IO_CAN_CHANNEL_0                |          |
| P210                     | CAN 1 Low IO_CAN_CHANNEL_1                |          |
| P211                     | CAN 2 Low IO_CAN_CHANNEL_2                |          |
| P212                     | CAN 3 Low IO_CAN_CHANNEL_3                |          |
| P213 P214 P215 P216      | CAN Termination 3L                        |          |
| P217                     | Sensor GND                                |          |
| P218 P219 P220           | Wake-Up IO_ADC_WAKE_UP                    |          |
| P221                     | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |          |
| P222                     | CAN 0 High IO_CAN_CHANNEL_0               |          |
| P223                     | CAN 1 High IO_CAN_CHANNEL_1               |          |
| P224                     | CAN 2 High IO_CAN_CHANNEL_2               |          |

| P225                | CAN 3 High IO_CAN_CHANNEL_3              |           |
|---------------------|------------------------------------------|-----------|
| P226 P227 P228 P229 | CAN Termination 3H                       |           |
| P230                | Sensor GND                               |           |
| P231 P232 P233 P234 | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1 |           |
| P235                | CAN Termination 0L                       |           |
| P236                | CAN Termination 1L                       |           |
| P237                | CAN Termination 2L                       |           |
| P238                | LS Digital Output                        | IO_ADC_45 |
| IO_DO_09            | IO_DI_81                                 |           |
| P239                | LS Digital Output                        | IO_ADC_47 |
| IO_DO_11            | IO_DI_83                                 |           |
| P240                | LS Digital Output                        | IO_ADC_49 |
| IO_DO_13            | IO_DI_85                                 |           |
| P241                | LS Digital Output                        | IO_ADC_51 |
| IO_DO_15            | IO_DI_87                                 |           |
| P242 P243           | Sensor GND                               |           |
| P244                | Sensor GND                               |           |
| P245                | Sensor GND                               |           |
| P246                | BAT+ CPU IO_ADC_UBAT                     |           |
| P247                | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |           |
| P248                | CAN Termination 0H                       |           |
| P249                | CAN Termination 1H                       |           |
| P250                | CAN Termination 2H                       |           |
| P251                | LS Digital Output                        | IO_ADC_44 |
| IO_DO_08            | IO_DI_80                                 |           |
| P252                | LS Digital Output                        | IO_ADC_46 |
| IO_DO_10            | IO_DI_82                                 |           |
| P253                | LS Digital Output                        | IO_ADC_48 |
| IO_DO_12            | IO_DI_84                                 |           |
| P254                | LS Digital Output                        | IO_ADC_50 |
| IO_DO_14            | IO_DI_86                                 |           |
| P255 P256           | Sensor GND                               |           |

![73_image_0.png]( The image features a black and white chart with various categories labeled along its horizontal axis. There are several rows of text that appear to be related to different subjects or topics. The chart is organized into sections, each containing multiple rows of information.

The chart's vertical axis consists of numbers, likely representing data points for the categories displayed on the horizontal axis. This visual representation allows for easy comparison and analysis of the data across the different subjects or topics.)

![74_image_0.png]( The image displays a table with several rows of data arranged vertically. Each row represents a different category or variable, and there are numerous columns that provide additional information. The table is filled with numbers, indicating various statistics related to the categories.

The first row contains the label "table planning," while subsequent rows contain other labels such as "hybrid VTC SAB." There are also several columns labeled with letters A through Z, which may represent different categories or subcategories within the data set. The table appears to be a visual representation of data analysis and provides valuable insights into the subject matter being studied.)

P257 Sensor GND

P258 Sensor GND

3.5.3 HY-TTC 520 Variant (Customer-specific variant **only)**

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

![76_image_0.png]( The image features a white background with multiple blue lines and numbers arranged vertically. These lines are likely representing different types of data or categories, possibly related to finance or other numerical information. There is also a small section of text visible on the left side of the image, but it does not provide any context for the rest of the scene. The overall appearance suggests that this could be an infographic, chart, or visual representation of data.)

| HS PWM Output   | IO_DI_29 IO_PWD_13 IO_PWD_17 IO_DI_33   |           |           |          |
|-----------------|-----------------------------------------|-----------|-----------|----------|
| P127            | Analog Voltage Input                    | IO_ADC_01 | IO_ADC_01 | IO_DI_49 |
| IO_ADC_01       |                                         |           |           |          |
| P128            | Analog Voltage Input                    | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03       |                                         |           |           |          |
| P129            | Analog Voltage Input                    | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05       |                                         |           |           |          |
| P130            | Analog Voltage Input                    | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07       |                                         |           |           |          |
| P131            | Analog Voltage Input                    | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09       |                                         |           |           |          |
| P132            | Analog Voltage Input                    | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11       |                                         |           |           |          |
| P133            | Analog Voltage Input                    | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13       |                                         |           |           |          |
| P134            | Analog Voltage Input                    | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15       |                                         |           |           |          |
| P135            | Analog Voltage Input                    | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17       |                                         |           |           |          |
| P136            | Analog Voltage Input                    | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19       |                                         |           |           |          |
| P137            | Analog Voltage Input                    | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21       |                                         |           |           |          |
| P138            | Analog Voltage Input                    | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23       |                                         |           |           |          |
| P139            | Timer Input                             | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01       | IO_DI_37                                |           |           |          |
| P140            | Timer Input                             | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03       | IO_DI_39                                |           |           |          |
| P141            | Timer Input                             | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05       | IO_DI_41                                |           |           |          |
| P142            | BAT                                         |           |           |          |
| P143            | BAT                                         |           |           |          |
| P144            | BAT                                         |           |           |          |
| P145            | BAT                                         |           |           |          |
| P146            | Timer Input                             | IO_ADC_31 |           |          |
| IO_PWD_07       | IO_DI_43                                |           |           |          |
| P147            | Timer Input                             | IO_ADC_33 |           |          |
| IO_PWD_09       | IO_DI_45                                |           |           |          |

![77_image_0.png]( The image is a black and white photo of a table with a list of countries on it. There are several rows of countries arranged vertically, each row containing multiple names. The countries are lined up in alphabetical order, making the list easy to read. The arrangement showcases a clear distinction between the different nations, providing an organized view of the data.)

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

![78_image_0.png]( The image is a black and white photo of a large table with various columns of data. There are multiple rows of information, including dates and numbers, organized neatly on the table. Some of the rows have different colored text, which might indicate varying categories or types of data.

The table appears to be a spreadsheet or a ledger, possibly used for tracking financial transactions or other important records. The layout and organization of the data suggest that it is being used for a specific purpose or task, such as budgeting, accounting, or record-keeping.)

| HS Digital Output                                           | IO_ADC_39         |           |          |
|-------------------------------------------------------------|-------------------|-----------|----------|
| IO_DO_03                                                    | IO_DI_75          |           |          |
| IO_DO_17                                                    | IO_DI_01          |           |          |
| IO_PWM_01                                                   |                   |           |          |
| P178                                                        | HS PWM Output     | IO_DO_31  | IO_DI_15 |
| IO_PWM_15                                                   |                   |           |          |
| P179                                                        | HS Digital Output | IO_ADC_41 |          |
| IO_DO_05                                                    | IO_DI_77          |           |          |
| P180                                                        | HS PWM Output     | IO_DO_19  | IO_DI_03 |
| IO_PWM_03                                                   |                   |           |          |
| P181                                                        | HS PWM Output     | IO_DO_33  | IO_DI_17 |
| IO_PWM_17                                                   |                   |           |          |
| P182                                                        | HS Digital Output | IO_ADC_43 |          |
| IO_DO_07                                                    | IO_DI_79          |           |          |
| P183                                                        | HS PWM Output     | IO_DO_21  | IO_DI_05 |
| IO_PWM_05                                                   |                   |           |          |
| P184                                                        | HS PWM Output     | IO_DO_35  | IO_DI_19 |
| IO_PWM_19                                                   |                   |           |          |
| P185 P186                                                   | HS PWM Output     | IO_DO_22  | IO_DI_06 |
| IO_PWM_06                                                   |                   |           |          |
| P187                                                        | HS PWM Output     | IO_DO_36  | IO_DI_20 |
| IO_PWM_20                                                   |                   |           |          |
| P188 P189                                                   | HS PWM Output     | IO_DO_24  | IO_DI_08 |
| IO_PWM_08                                                   |                   |           |          |
| P190 P191 P192 P193 P194 P195 P196 P197 P198 P199 P200 P201 | BAT+ Power        |           |          |
| P202                                                        | BAT+ Power        |           |          |
| P203                                                        | BAT+ Power        |           |          |
| P204                                                        | BAT+ Power        |           |          |
| P205                                                        | BAT+ Power        |           |          |

![79_image_0.png]( The image is a black and white photograph of a large table with several rows of text written on it. The text appears to be organized into columns, possibly representing different categories or topics. The table has a total of nine rows, each containing various pieces of information.

The first row contains the word "Abundance" in the leftmost column and "Misery" in the rightmost column. The second row features "Effortlessness" on the left side and "Struggle" on the right side. In the third row, there is "Freedom" on the left and "Oppression" on the right.

The fourth row has "Prosperity" in the leftmost column and "Poverty" in the rightmost column. The fifth row displays "Happiness" on the left side and "Sadness" on the right side. In the sixth row, there is "Love" on the left and "Hate" on the right.

The seventh row has "Success" on the left and "Failure" on the right. The eighth row features "Peace" in the leftmost column and "War" in the rightmost column. Finally, the ninth row contains "Power" on the left side and "Weakness" on the right side.)

| P206                | BAT+ Power                                |
|---------------------|-------------------------------------------|
| P207                | Terminal 15 IO_ADC_K15                    |
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

![80_image_0.png]( The image is a black and white graph displaying various data points along an x-axis. There are several blue dots scattered across the graph, possibly representing different categories or values. The graph appears to be a line chart with multiple lines, each possibly corresponding to a specific category of information. Overall, it seems like a complex visual representation of data, likely used for analysis or comparison purposes.)

P242

P243 Sensor GND

P244 Sensor GND

P245 Sensor GND

P246 BAT+ CPU

IO_ADC_UBAT

P247 Sensor **Supply** 5 V

IO_ADC_SENSOR_SUPPLY_0

P248 CAN **Termination** 0H

P249 CAN **Termination** 1H

P250 CAN **Termination** 2H

P251 LS Digital **Output**

IO_DO_08

IO_ADC_44

IO_DI_80

P252 LS Digital **Output**

IO_DO_10

IO_ADC_46

IO_DI_82

P253 LS Digital **Output**

IO_DO_12

IO_ADC_48

IO_DI_84

P254 LS Digital **Output**

IO_DO_14

IO_ADC_50

IO_DI_86

P255

P256 Sensor GND

P257 Sensor GND

P258 Sensor GND

Table 15: Pinning of HY-TTC 520

3.5.4 HY-TTC 510 **Variant**

![81_image_0.png]( The image displays a large number of lines on a blue background, possibly representing data or information. There are several sets of numbers and letters arranged along these lines, which could be part of a graph or table. The arrangement creates an organized and visually appealing presentation of the data.)

| HS Digital Output   | Timer Input                    | PVG Output         | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|--------------------------------|--------------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function                  |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P101                | HS PWM Output                  | IO_PWD_12 IO_DI_28 |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P102                | HS PWM Output                  | IO_PWD_16 IO_DI_32 | IO_ADC_00     | IO_ADC_00                        | IO_DI_48             |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P103                | Analog Voltage Input IO_ADC_00 |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P104                | Analog Voltage Input           | IO_ADC_02          | IO_ADC_02     | IO_DI_50                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_02           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P105                | Analog Voltage Input           | IO_ADC_04          | IO_ADC_04     | IO_DI_52                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_04           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P106                | Analog Voltage Input           | IO_ADC_06          | IO_ADC_06     | IO_DI_54                         |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_06           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P107                | Analog Voltage Input           | IO_ADC_08          | IO_DI_56      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_08           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P108                | Analog Voltage Input           | IO_ADC_10          | IO_DI_58      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_10           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P109                | Analog Voltage Input           | IO_ADC_12          | IO_DI_60      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_12           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P110                | Analog Voltage Input           | IO_ADC_14          | IO_DI_62      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_14           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P111                | Analog Voltage Input           | IO_ADC_16          | IO_DI_64      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_16           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P112                | Analog Voltage Input           | IO_ADC_18          | IO_DI_66      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_18           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P113                | Analog Voltage Input           | IO_ADC_20          | IO_DI_68      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_20           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P114                | Analog Voltage Input           | IO_ADC_22          | IO_DI_70      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_ADC_22           |                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P115                | Timer Input                    | IO_PWD_00          | IO_ADC_24     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_00           | IO_DI_36                       |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P116                | Timer Input                    | IO_PWD_02          | IO_ADC_26     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_02           | IO_DI_38                       |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P117                | Timer Input                    | IO_PWD_04          | IO_ADC_28     |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_04           | IO_DI_40                       |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P118                | BAT                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P119                | BAT                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P120                | BAT                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P121                | BAT                                |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P122                | Timer Input                    | IO_ADC_30          |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_06           | IO_DI_42                       |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P123                | Timer Input                    | IO_ADC_32          |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_08           | IO_DI_44                       |                    |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

| IO_PWD_10            | IO_DI_46             |           |           |          |
|----------------------|----------------------|-----------|-----------|----------|
| HS PWM Output        | IO_DI_29 IO_PWD_13   |           |           |          |
| HS PWM Output        | IO_PWD_17 IO_DI_33   |           |           |          |
| Analog Voltage Input | IO_ADC_01            | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01            |                      |           |           |          |
| P128                 | Analog Voltage Input | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03            |                      |           |           |          |
| P129                 | Analog Voltage Input | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05            |                      |           |           |          |
| P130                 | Analog Voltage Input | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07            |                      |           |           |          |
| P131                 | Analog Voltage Input | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09            |                      |           |           |          |
| P132                 | Analog Voltage Input | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11            |                      |           |           |          |
| P133                 | Analog Voltage Input | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13            |                      |           |           |          |
| P134                 | Analog Voltage Input | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15            |                      |           |           |          |
| P135                 | Analog Voltage Input | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17            |                      |           |           |          |
| P136                 | Analog Voltage Input | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19            |                      |           |           |          |
| P137                 | Analog Voltage Input | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21            |                      |           |           |          |
| P138                 | Analog Voltage Input | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23            |                      |           |           |          |
| P139                 | Timer Input          | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01            | IO_DI_37             |           |           |          |
| P140                 | Timer Input          | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03            | IO_DI_39             |           |           |          |
| P141                 | Timer Input          | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05            | IO_DI_41             |           |           |          |
| P142                 | BAT                      |           |           |          |
| P143                 | BAT                      |           |           |          |
| P144                 | BAT                      |           |           |          |
| P145                 | BAT                      |           |           |          |
| P146                 | Timer Input          | IO_ADC_31 |           |          |
| IO_PWD_07            | IO_DI_43             |           |           |          |
| P147                 | Timer Input          | IO_ADC_33 |           |          |
| IO_PWD_09            | IO_DI_45             |           |           |          |

![82_image_0.png]( The image is a whiteboard with a timeline displayed on it. The timeline consists of various dates and times, possibly representing different events or milestones. There are several labels along the timeline, which provide additional information or context for each date and time point. Overall, the whiteboard appears to be used for planning, organizing, or visualizing a sequence of events or tasks.)

Alternative *Function*

![83_image_0.png]( The image is a close-up of a large blue and white graph with several columns and rows. There are multiple bars within each column, indicating various data points or categories. The graph appears to be a time line, possibly representing different periods or events.

The overall layout of the graph suggests that it could be used for tracking progress, comparing data over time, or visualizing trends in a particular subject area.)

| HS Digital Output   | Timer Input       | PVG Output         | VOUT Output          | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|-------------------|--------------------|----------------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function     |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P148                | Timer Input       | IO_ADC_35          |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_11           | IO_DI_47          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P149                | HS Digital Output | IO_ADC_36          |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_00            | IO_DI_72          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P150                | HS PWM Output     | IO_PWD_14 IO_DI_30 |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P151                | HS PWM Output     | IO_PWD_18 IO_DI_34 |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P152                | HS Digital Output | IO_ADC_38          |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_02            | IO_DI_74          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P153                | HS PWM Output     | IO_DO_16           | IO_DI_00             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_00           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P154                | HS PWM Output     | IO_DO_30           | IO_DI_14             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_14           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P155                | HS Digital Output | IO_ADC_40          |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_04            | IO_DI_76          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P156                | HS PWM Output     | IO_DO_18           | IO_DI_02             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_02           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P157                | HS PWM Output     | IO_DO_32           | IO_DI_16             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_16           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P158                | HS Digital Output | IO_ADC_42          |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_06            | IO_DI_78          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P159                | HS PWM Output     | IO_DO_20           | IO_DI_04             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_04           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P160                | HS PWM Output     | IO_DO_34           | IO_DI_18             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_18           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P161                | HS Digital Output | IO_PVG_00          | IO_VOUT_00 IO_ADC_52 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_52            | IO_DI_88          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P162                | HS PWM Output     | IO_DO_23           | IO_DI_07             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_07           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P163                | HS PWM Output     | IO_DO_37           | IO_DI_21             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_21           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P164                | HS Digital Output | IO_PVG_03          | IO_VOUT_03 IO_ADC_55 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_55            | IO_DI_91          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P165 P166 P167      | HS Digital Output | IO_PVG_05          | IO_VOUT_05 IO_ADC_57 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_57            | IO_DI_93          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P168 P169 P170      | HS Digital Output | IO_PVG_07          | IO_VOUT_07 IO_ADC_59 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_59            | IO_DI_95          |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P171 P172           |                   |                    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![84_image_0.png]( The image displays a large table with various columns and rows of data. There are several different types of information presented on the table, including text and numbers. Some of the columns have headings that indicate their purpose or content.

In addition to the main table, there is another smaller table located towards the right side of the image. The tables appear to be organized in a way that allows for easy comparison and analysis of the data they contain.)

| HS PWM Output            | IO_PWD_15 IO_DI_31   |           |                      |
|--------------------------|----------------------|-----------|----------------------|
| HS PWM Output            | IO_PWD_19 IO_DI_35   |           |                      |
| HS Digital Output        | IO_ADC_39            |           |                      |
| IO_DO_03                 | IO_DI_75             |           |                      |
| P177                     | HS PWM Output        | IO_DO_17  | IO_DI_01             |
| IO_PWM_01                |                      |           |                      |
| P178                     | HS PWM Output        | IO_DO_31  | IO_DI_15             |
| IO_PWM_15                |                      |           |                      |
| P179                     | HS Digital Output    | IO_ADC_41 |                      |
| IO_DO_05                 | IO_DI_77             |           |                      |
| P180                     | HS PWM Output        | IO_DO_19  | IO_DI_03             |
| IO_PWM_03                |                      |           |                      |
| P181                     | HS PWM Output        | IO_DO_33  | IO_DI_17             |
| IO_PWM_17                |                      |           |                      |
| P182                     | HS Digital Output    | IO_ADC_43 |                      |
| IO_DO_07                 | IO_DI_79             |           |                      |
| P183                     | HS PWM Output        | IO_DO_21  | IO_DI_05             |
| IO_PWM_05                |                      |           |                      |
| P184                     | HS PWM Output        | IO_DO_35  | IO_DI_19             |
| IO_PWM_19                |                      |           |                      |
| P185                     | HS Digital Output    | IO_PVG_01 | IO_VOUT_01 IO_ADC_53 |
| IO_DO_53                 | IO_DI_89             |           |                      |
| P186                     | HS PWM Output        | IO_DO_22  | IO_DI_06             |
| IO_PWM_06                |                      |           |                      |
| P187                     | HS PWM Output        | IO_DO_36  | IO_DI_20             |
| IO_PWM_20                |                      |           |                      |
| P188                     | HS Digital Output    | IO_PVG_02 | IO_VOUT_02 IO_ADC_54 |
| IO_DO_54                 | IO_DI_90             |           |                      |
| P189 P190 P191           | HS Digital Output    | IO_PVG_04 | IO_VOUT_04 IO_ADC_56 |
| IO_DO_56                 | IO_DI_92             |           |                      |
| P192 P193 P194           | HS Digital Output    | IO_PVG_06 | IO_VOUT_06 IO_ADC_58 |
| IO_DO_58                 | IO_DI_94             |           |                      |
| P195 P196 P197 P198 P199 |                      |           |                      |

Alternative *Function*

| HS Digital Output             | Timer Input                               | PVG Output   | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|-------------------------------|-------------------------------------------|--------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.                       | Main Function                             |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P200 P201                     | BAT+ Power                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P202                          | BAT+ Power                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P203                          | BAT+ Power                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P204                          | BAT+ Power                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P205                          | BAT+ Power                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P206                          | BAT+ Power                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P207                          | Terminal 15 IO_ADC_K15                    |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P208                          | LIN IO_LIN                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P209                          | CAN 0 Low IO_CAN_CHANNEL_0                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P210                          | CAN 1 Low IO_CAN_CHANNEL_1                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P211                          | CAN 2 Low IO_CAN_CHANNEL_2                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P212 P213 P214 P215 P216 P217 | Sensor GND                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P218 P219 P220                | Wake-Up IO_ADC_WAKE_UP                    |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P221                          | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P222                          | CAN 0 High IO_CAN_CHANNEL_0               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P223                          | CAN 1 High IO_CAN_CHANNEL_1               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P224                          | CAN 2 High IO_CAN_CHANNEL_2               |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P225 P226 P227 P228 P229 P230 | Sensor GND                                |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P231 P232 P233                |                                           |              |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![85_image_0.png]( The image is a close-up of a blue and white background with a light blue border. It appears to be an artistic representation or a painting rather than a photograph. In this artwork, there are two main elements: a large blue square in the center and a smaller blue square towards the right side. The overall composition creates a visually appealing and harmonious design.)

![85_image_1.png]( The image is a close-up of a ruler with several measurements on it. There are ten distinct measurements marked along the ruler, each varying from one to four units long. The ruler appears to be made of metal and has a blue background. The measurements are evenly spaced apart, providing a clear visual representation of the different lengths.)

![86_image_0.png]( The image displays a long row of blue and white text arranged vertically on a gray background. The text appears to be organized into sections or categories, with each section having its own distinct color combination. The blue text is interspersed between the white text, creating an alternating pattern along the length of the row. This arrangement creates a visually appealing and structured presentation of information.)

| Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1   |                                          |                                 |
|--------------------------------------------|------------------------------------------|---------------------------------|
| P235                                       | CAN Termination 0L                       |                                 |
| P236                                       | CAN Termination 1L                       |                                 |
| P237                                       | CAN Termination 2L                       |                                 |
| P238                                       | LS Digital Output                        | IO_ADC_45                       |
| IO_DO_09                                   | IO_DI_81                                 |                                 |
| P239                                       | LS Digital Output                        | IO_ADC_47                       |
| IO_DO_11                                   | IO_DI_83                                 |                                 |
| P240                                       | LS Digital Output                        | IO_ADC_49                       |
| IO_DO_13                                   | IO_DI_85                                 |                                 |
| P241                                       | LS Digital Output                        | IO_ADC_51                       |
| IO_DO_15                                   | IO_DI_87                                 |                                 |
| P242 P243                                  | Sensor GND                               |                                 |
| P244                                       | Sensor GND                               |                                 |
| P245                                       | Sensor GND                               |                                 |
| P246                                       | BAT+ CPU IO_ADC_UBAT                     |                                 |
| P247                                       | Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0 |                                 |
| P248                                       | CAN Termination 0H                       |                                 |
| P249                                       | CAN Termination 1H                       |                                 |
| P250                                       | CAN Termination 2H                       |                                 |
| P251                                       | LS Digital Output                        | IO_ADC_44                       |
| IO_DO_08                                   | IO_DI_80                                 |                                 |
| P252                                       | LS Digital Output                        | IO_ADC_46                       |
| IO_DO_10                                   | IO_DI_82                                 |                                 |
| P253                                       | LS Digital Output                        | IO_ADC_48                       |
| IO_DO_12                                   | IO_DI_84                                 |                                 |
| P254                                       | LS Digital Output                        | IO_ADC_50                       |
| IO_DO_14                                   | IO_DI_86                                 |                                 |
| P255 P256                                  | Sensor GND                               |                                 |
| P257                                       | Sensor GND                               |                                 |
| P258                                       | Sensor GND                               | Table 16: Pinning of HY-TTC 510 |

3.5.5 HY-TTC 590E **Variant**

![87_image_0.png]( The image features a large blue and white graph with several small black dots scattered throughout it. These dots are likely data points or markers on the graph, indicating various values or measurements. The graph appears to be quite complex, with numerous lines converging at different points. It is difficult to discern specific details about the content of the graph without more information.)

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

![88_image_0.png]( The image displays a large table with several columns and rows of data. Each row represents a different category or topic, while each column contains information related to that particular subject. The table is filled with numbers and text, making it easy for the reader to understand the data presented.

In addition to the main table, there are two smaller tables visible in the image. One table is located on the left side of the main table, while the other is positioned towards the right side. These smaller tables may contain more detailed information or be part of a larger dataset.)

| Timer Input          | IO_ADC_34            |           |           |          |
|----------------------|----------------------|-----------|-----------|----------|
| IO_PWD_10            | IO_DI_46             |           |           |          |
| HS PWM Output        | IO_DO_45             | IO_DI_29  |           |          |
| IO_PWM_29            | IO_PWD_13            |           |           |          |
| HS PWM Output        | IO_DO_49             | IO_PWD_17 |           |          |
| IO_PWM_33            | IO_DI_33             |           |           |          |
| Analog Voltage Input | IO_ADC_01            | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01            |                      |           |           |          |
| P128                 | Analog Voltage Input | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03            |                      |           |           |          |
| P129                 | Analog Voltage Input | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05            |                      |           |           |          |
| P130                 | Analog Voltage Input | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07            |                      |           |           |          |
| P131                 | Analog Voltage Input | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09            |                      |           |           |          |
| P132                 | Analog Voltage Input | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11            |                      |           |           |          |
| P133                 | Analog Voltage Input | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13            |                      |           |           |          |
| P134                 | Analog Voltage Input | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15            |                      |           |           |          |
| P135                 | Analog Voltage Input | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17            |                      |           |           |          |
| P136                 | Analog Voltage Input | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19            |                      |           |           |          |
| P137                 | Analog Voltage Input | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21            |                      |           |           |          |
| P138                 | Analog Voltage Input | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23            |                      |           |           |          |
| P139                 | Timer Input          | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01            | IO_DI_37             |           |           |          |
| P140                 | Timer Input          | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03            | IO_DI_39             |           |           |          |
| P141                 | Timer Input          | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05            | IO_DI_41             |           |           |          |
| P142                 | BAT                      |           |           |          |
| P143                 | BAT                      |           |           |          |
| P144                 | BAT                      |           |           |          |
| P145                 | BAT                      |           |           |          |
| P146                 | Timer Input          | IO_ADC_31 |           |          |
| IO_PWD_07            | IO_DI_43             |           |           |          |
| P147                 | Timer Input          | IO_ADC_33 |           |          |
| IO_PWD_09            | IO_DI_45             |           |           |          |

![89_image_0.png]( The image displays a large table with several rows of data arranged neatly. Each row consists of multiple columns filled with numbers and text. The table appears to be organized for easy reference or analysis. The rows are labeled with the letters A through J, indicating that they may represent different categories or aspects of the data being analyzed. Overall, it is a well-structured and informative display of information.)

| HS Digital Output   | Timer Input       | PVG Output   | VOUT Output          | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|---------------------|-------------------|--------------|----------------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.             | Main Function     |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P148                | Timer Input       | IO_ADC_35    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_11           | IO_DI_47          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P149                | HS Digital Output | IO_ADC_36    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_00            | IO_DI_72          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P150                | HS PWM Output     | IO_DO_46     | IO_PWD_14            |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_30           | IO_DI_30          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P151                | HS PWM Output     | IO_DO_50     | IO_PWD_18            |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_34           | IO_DI_34          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P152                | HS Digital Output | IO_ADC_38    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_02            | IO_DI_74          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P153                | HS PWM Output     | IO_DO_16     | IO_DI_00             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_00           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P154                | HS PWM Output     | IO_DO_30     | IO_DI_14             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_14           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P155                | HS Digital Output | IO_ADC_40    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_04            | IO_DI_76          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P156                | HS PWM Output     | IO_DO_18     | IO_DI_02             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_02           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P157                | HS PWM Output     | IO_DO_32     | IO_DI_16             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_16           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P158                | HS Digital Output | IO_ADC_42    |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_06            | IO_DI_78          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P159                | HS PWM Output     | IO_DO_20     | IO_DI_04             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_04           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P160                | HS PWM Output     | IO_DO_34     | IO_DI_18             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_18           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P161                | HS Digital Output | IO_PVG_00    | IO_VOUT_00 IO_ADC_52 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_52            | IO_DI_88          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P162                | HS PWM Output     | IO_DO_23     | IO_DI_07             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_07           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P163                | HS PWM Output     | IO_DO_37     | IO_DI_21             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_21           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P164                | HS Digital Output | IO_PVG_03    | IO_VOUT_03 IO_ADC_55 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_55            | IO_DI_91          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P165                | HS PWM Output     | IO_DO_25     | IO_DI_09             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_09           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P166                | HS PWM Output     | IO_DO_39     | IO_DI_23             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_23           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P167                | HS Digital Output | IO_PVG_05    | IO_VOUT_05 IO_ADC_57 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_57            | IO_DI_93          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P168                | HS PWM Output     | IO_DO_27     | IO_DI_11             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_11           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P169                | HS PWM Output     | IO_DO_41     | IO_DI_25             |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_25           |                   |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P170                | HS Digital Output | IO_PVG_07    | IO_VOUT_07 IO_ADC_59 |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_59            | IO_DI_95          |              |                      |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![90_image_0.png]( The image displays a black and white table with text on it. There are several columns of text arranged vertically, each containing different types of information. The table appears to be organized into sections or categories, making it easy for the reader to understand the content.)

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

![91_image_0.png]( The image displays a table with various columns of numbers and text. There are multiple rows of data, including some that have the word "million" written on them. The table appears to be organized into different sections or categories, each containing numerical information.

The table is quite large, occupying most of the space in the image. It seems to be a financial report or a spreadsheet with detailed data and calculations.)

| HS PWM Output            | IO_DO_28                                  | IO_DI_12   |
|--------------------------|-------------------------------------------|------------|
| IO_PWM_12 HS PWM Output  | IO_DO_42                                  | IO_DI_26   |
| IO_PWM_26                |                                           |            |
| P197 P198 P199 P200 P201 | BAT+ Power                                |            |
| P202                     | BAT+ Power                                |            |
| P203                     | BAT+ Power                                |            |
| P204                     | BAT+ Power                                |            |
| P205                     | BAT+ Power                                |            |
| P206                     | BAT+ Power                                |            |
| P207                     | Terminal 15 IO_ADC_K15                    |            |
| P208                     | LIN IO_LIN                                |            |
| P209                     | CAN 0 Low IO_CAN_CHANNEL_0                |            |
| P210                     | CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN     |            |
| P211                     | CAN 2 Low IO_CAN_CHANNEL_2                |            |
| P212                     | CAN 3 Low IO_CAN_CHANNEL_3                |            |
| P213                     | CAN 4 Low IO_CAN_CHANNEL_4                |            |
| P214                     | CAN 5 Low IO_CAN_CHANNEL_5                |            |
| P215                     | CAN 6 Low IO_CAN_CHANNEL_6                |            |
| P216                     | Sensor GND                                |            |
| P217                     | do not connect                            |            |
| P218                     | CAN Termination 3H                        |            |
| P219                     | CAN Termination 3L                        |            |
| P220                     | Wake-Up IO_ADC_WAKE_UP                    |            |
| P221                     | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |            |
| P222                     | CAN 0 High IO_CAN_CHANNEL_0               |            |

![92_image_0.png]( The image displays a long list of names and descriptions on a black background. There are at least twelve people visible in the list, each with their own name and possibly some additional information. The names are arranged vertically down the page, making it easy to read through the entire list.)

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

![93_image_0.png]( The image features a large table with various columns of data, including one labeled "Teacher." Each column is filled with different information, possibly related to student performance or teacher evaluations. There are multiple rows within each column, providing more detailed data on the subject matter.

The table appears to be organized in such a way that it can easily be used for analyzing and comparing data across different categories. The presence of so many columns and rows suggests that this could be an important tool for decision-making or research purposes.)

LS Digital **Output**

IO_DO_12

IO_ADC_48

IO_DI_84

P254 LS Digital **Output**

IO_DO_14

IO_ADC_50

IO_DI_86

P255 RS232 RXD

IO_UART

P256 Sensor GND

P257 Sensor GND

P258 Sensor GND

Table 17: Pinning of HY-TTC 590E

![94_image_0.png]( The image is a black and white photo of a large book with many pages. Each page has a line down the middle, dividing it into two sections. There are several words written on each page, indicating that this could be an educational text or reference material.

The book appears to be quite thick, as there are numerous pages visible in the image. The lines on the pages help to organize and structure the content, making it easier for readers to follow along with the information presented.)

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

![95_image_0.png]( The image displays a large table with various columns and rows of data. There are several small boxes within each column, which contain different types of information. Some of these boxes have numbers or other numerical values, while others may be empty or contain textual descriptions.

The table appears to be organized in such a way that it can be used for tracking or analyzing data. The presence of multiple columns and rows suggests that the table is designed to accommodate various types of information, making it suitable for diverse applications.)

| IO_PWD_10     | IO_DI_46              |           |           |          |
|---------------|-----------------------|-----------|-----------|----------|
| HS PWM Output | IO_DO_45              | IO_DI_29  |           |          |
| IO_PWM_29     | IO_PWD_13             |           |           |          |
| HS PWM Output | IO_DO_49              | IO_PWD_17 |           |          |
| IO_PWM_33     | IO_DI_33              |           |           |          |
| P127          | Analog Voltage Input  | IO_ADC_01 | IO_ADC_01 | IO_DI_49 |
| IO_ADC_01     |                       |           |           |          |
| P128          | Analog Voltage Input  | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03     |                       |           |           |          |
| P129          | Analog Voltage Input  | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05     |                       |           |           |          |
| P130          | Analog Voltage Input  | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07     |                       |           |           |          |
| P131          | Analog Voltage Input  | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09     |                       |           |           |          |
| P132          | Analog Voltage Input  | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11     |                       |           |           |          |
| P133          | Analog Voltage Input  | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13     |                       |           |           |          |
| P134          | Analog Voltage Input  | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15     |                       |           |           |          |
| P135          | Analog Voltage Input  | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17     |                       |           |           |          |
| P136          | Analog Voltage Input  | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19     |                       |           |           |          |
| P137          | Analog Voltage Input  | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21     |                       |           |           |          |
| P138          | Analog Voltage Input  | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23     |                       |           |           |          |
| P139          | Timer Input           | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01     | IO_DI_37              |           |           |          |
| P140          | Timer Input           | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03     | IO_DI_39              |           |           |          |
| IO_PWD_05     | IO_ADC_29             |           |           |          |
| P141          | Timer Input IO_PWD_05 | IO_DI_41  |           |          |
| P142          | BAT                       |           |           |          |
| P143          | BAT                       |           |           |          |
| P144          | BAT                       |           |           |          |
| P145          | BAT                       |           |           |          |
| P146          | Timer Input           | IO_ADC_31 |           |          |
| IO_PWD_07     | IO_DI_43              |           |           |          |
| P147          | Timer Input           | IO_ADC_33 |           |          |
| IO_PWD_09     | IO_DI_45              |           |           |          |

![96_image_0.png]( The image displays a long list of names with various descriptions underneath them. The names are arranged vertically and appear to be organized by categories or subjects. Each name is accompanied by a brief description that provides additional information about the person or subject being described. This could be an educational setting, such as a classroom or a school, where students' names and their respective subjects are listed for easy reference.)

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

![97_image_0.png]( The image displays a large table with multiple rows of data organized into columns. Each row represents a different category or topic, and each column contains information related to that category. There are several rows of text on the table, which may be descriptions or details about the categories.

The table appears to be a part of a larger spreadsheet or database, as it is filled with various data points. The organization and presentation of the data suggest that this could be used for analysis, comparison, or visualization purposes.)

| HS PWM Output               | IO_DO_29          | IO_DI_13   |                      |
|-----------------------------|-------------------|------------|----------------------|
| IO_PWM_13 HS PWM Output     | IO_DO_43          | IO_DI_27   |                      |
| IO_PWM_27 HS Digital Output | IO_ADC_37         |            |                      |
| IO_DO_01                    | IO_DI_73          |            |                      |
| P174                        | HS PWM Output     | IO_DO_47   | IO_PWD_15            |
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

![98_image_0.png]( The image features a large white sheet of paper with various columns and rows of text. There are several lines of text arranged vertically down the page, creating a sense of organization. Some of these lines appear to be organized into groups or categories, possibly indicating different types of information or data.

The text is written in blue, which contrasts nicely against the white background, making it easy to read and understand. The layout of the paper suggests that it could be used for a presentation, study guide, or reference material.)

| P194                     | HS Digital Output                         | IO_PVG_06   | IO_VOUT_06 IO_ADC_58   |
|--------------------------|-------------------------------------------|-------------|------------------------|
| IO_DO_58                 | IO_DI_94                                  |             |                        |
| P195                     | HS PWM Output                             | IO_DO_28    | IO_DI_12               |
| IO_PWM_12                |                                           |             |                        |
| P196                     | HS PWM Output                             | IO_DO_42    | IO_DI_26               |
| IO_PWM_26                |                                           |             |                        |
| P197 P198 P199 P200 P201 | BAT+ Power                                |             |                        |
| P202                     | BAT+ Power                                |             |                        |
| P203                     | BAT+ Power                                |             |                        |
| P204                     | BAT+ Power                                |             |                        |
| P205                     | BAT+ Power                                |             |                        |
| P206                     | BAT+ Power                                |             |                        |
| P207                     | Terminal 15 IO_ADC_K15                    |             |                        |
| P208                     | LIN IO_LIN                                |             |                        |
| P209                     | CAN 0 Low IO_CAN_CHANNEL_0                |             |                        |
| P210                     | CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN     |             |                        |
| P211                     | CAN 2 Low IO_CAN_CHANNEL_2                |             |                        |
| P212                     | CAN 3 Low IO_CAN_CHANNEL_3                |             |                        |
| P213                     | CAN 4 Low IO_CAN_CHANNEL_4                |             |                        |
| P214                     | CAN 5 Low IO_CAN_CHANNEL_5                |             |                        |
| P215                     | CAN 6 Low IO_CAN_CHANNEL_6                |             |                        |
| P216                     | Sensor GND                                |             |                        |
| P217                     | do not connect                            |             |                        |
| P218                     | CAN Termination 3H                        |             |                        |
| P219                     | CAN Termination 3L                        |             |                        |
| P220                     | Wake-Up IO_ADC_WAKE_UP                    |             |                        |
| P221                     | Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2 |             |                        |
| P222                     | CAN 0 High IO_CAN_CHANNEL_0               |             |                        |

![99_image_0.png]( The image features a large, detailed graph displaying various types of information. There are several columns on the graph, each representing different categories or data points. The rows of the graph span across the entire width of the image, providing an extensive overview of the data.

In addition to the main graph, there is also a smaller bar chart located towards the right side of the image. This secondary chart likely provides more detailed information about one specific aspect of the larger graph or serves as a comparison tool for the viewer.)

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

![100_image_0.png]( The image features a large table with multiple rows of data displayed on it. Each row consists of various columns filled with numerical information. Some of these columns are labeled, while others remain unidentified. The table appears to be used for analyzing and organizing data in a structured manner.

The layout of the table is quite dense, with numerous rows and columns filling up most of the visible space. This suggests that the data being displayed is extensive and requires careful organization to make it easily understandable.)

IO_DO_12

IO_DI_84

LS Digital **Output**

IO_DO_14

IO_ADC_50

IO_DI_86

P255 RS232 RXD

IO_UART

P256 Sensor GND

P257 Sensor GND

P258 Sensor GND

Table 18: Pinning of HY-TTC 590

![101_image_0.png]( The image features a table with various columns and rows of numbers, possibly representing financial data or statistics. There are several rows of numbers that appear to be related to expenses, with some numbers grouped together in each row.

In addition to the numerical data, there is a line graph present on the right side of the table, which may provide additional context or information about the data displayed. The overall layout and content suggest that this image could be related to financial analysis or reporting.)

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

![101_image_1.png]( The image features a grayscale photograph of a computer screen displaying several numbers and letters. There are multiple instances of the number "10" visible on the screen, with one near the top left corner and another towards the center-left side. Additionally, there is a row of numbers running horizontally across the middle section of the image. The overall appearance suggests that this could be an old computer monitor or a screenshot from a vintage device.)

3.5.7 HY-TTC 508 **Variant** 
90 

![101_image_2.png]( The image features a blue and white logo for Hydaq International, which is an international company that specializes in telecommunications. The logo appears to be a combination of letters and numbers, possibly representing their brand or services. The design of the logo gives it a modern and professional look, making it suitable for various applications such as business cards, websites, or promotional materials.)

Document Number: D-TTC5F-G-20-002

| IO_PWD_10            | IO_DI_46             |           |           |          |
|----------------------|----------------------|-----------|-----------|----------|
| HS PWM Output        | IO_DI_29 IO_PWD_13   |           |           |          |
| HS PWM Output        | IO_PWD_17 IO_DI_33   |           |           |          |
| Analog Voltage Input | IO_ADC_01            | IO_ADC_01 | IO_DI_49  |          |
| IO_ADC_01            |                      |           |           |          |
| P128                 | Analog Voltage Input | IO_ADC_03 | IO_ADC_03 | IO_DI_51 |
| IO_ADC_03            |                      |           |           |          |
| P129                 | Analog Voltage Input | IO_ADC_05 | IO_ADC_05 | IO_DI_53 |
| IO_ADC_05            |                      |           |           |          |
| P130                 | Analog Voltage Input | IO_ADC_07 | IO_ADC_07 | IO_DI_55 |
| IO_ADC_07            |                      |           |           |          |
| P131                 | Analog Voltage Input | IO_ADC_09 | IO_DI_57  |          |
| IO_ADC_09            |                      |           |           |          |
| P132                 | Analog Voltage Input | IO_ADC_11 | IO_DI_59  |          |
| IO_ADC_11            |                      |           |           |          |
| P133                 | Analog Voltage Input | IO_ADC_13 | IO_DI_61  |          |
| IO_ADC_13            |                      |           |           |          |
| P134                 | Analog Voltage Input | IO_ADC_15 | IO_DI_63  |          |
| IO_ADC_15            |                      |           |           |          |
| P135                 | Analog Voltage Input | IO_ADC_17 | IO_DI_65  |          |
| IO_ADC_17            |                      |           |           |          |
| P136                 | Analog Voltage Input | IO_ADC_19 | IO_DI_67  |          |
| IO_ADC_19            |                      |           |           |          |
| P137                 | Analog Voltage Input | IO_ADC_21 | IO_DI_69  |          |
| IO_ADC_21            |                      |           |           |          |
| P138                 | Analog Voltage Input | IO_ADC_23 | IO_DI_71  |          |
| IO_ADC_23            |                      |           |           |          |
| P139                 | Timer Input          | IO_PWD_01 | IO_ADC_25 |          |
| IO_PWD_01            | IO_DI_37             |           |           |          |
| P140                 | Timer Input          | IO_PWD_03 | IO_ADC_27 |          |
| IO_PWD_03            | IO_DI_39             |           |           |          |
| P141                 | Timer Input          | IO_PWD_05 | IO_ADC_29 |          |
| IO_PWD_05            | IO_DI_41             |           |           |          |
| P142                 | BAT                      |           |           |          |
| P143                 | BAT                      |           |           |          |
| P144                 | BAT                      |           |           |          |
| P145                 | BAT                      |           |           |          |
| P146                 | Timer Input          | IO_ADC_31 |           |          |
| IO_PWD_07            | IO_DI_43             |           |           |          |
| P147                 | Timer Input          | IO_ADC_33 |           |          |
| IO_PWD_09            | IO_DI_45             |           |           |          |

![102_image_0.png]( The image is a white background with several blue lines and text. There are two main sets of blue lines, one running horizontally across the top half of the image and another set running vertically down the left side. These lines appear to be part of a graph or chart.

In addition to these blue lines, there is a bar plot towards the bottom right corner of the image. The bar plot consists of three bars, with one being longer than the other two. This visual representation could represent data or information related to the topic at hand.)

Alternative *Function*

![103_image_0.png]( The image is a black and white photo of a large book with many pages. The book appears to be an atlas or a reference guide, possibly for a city or region. There are several columns on each page, providing information and data in a structured manner.

The book is open to a specific page, which has a grid-like pattern across the entire width of the image. This grid might represent different sections within the atlas or reference guide, allowing for easy navigation and organization of the content.)

| TTControl GmbH Confidential and Proprietary Information. Copyright  2022 TTControl GmbH. All rights reserved.   | HS Digital Output                | Timer Input        | PVG Output                    | VOUT Output   | A/D Input (HS Output/PVG/VOUT)   | Current Loop Input   | A/D Input (Timer Input)   | A/D Input (HS Digital Output)   | A/D Input (LS Digital Output)   | Analog Current Input 2M   | Digital Input 2M   | Analog Current Input 3M   | Analog Resistance Input 3M   | Digital Input 3M   |
|------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------|-------------------------------|---------------|----------------------------------|----------------------|---------------------------|---------------------------------|---------------------------------|---------------------------|--------------------|---------------------------|------------------------------|--------------------|
| Pin No.                                                                                                          | Main Function                    |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P148                                                                                                             | Timer Input                      | IO_ADC_35          |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWD_11                                                                                                        | IO_DI_47                         |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P149                                                                                                             | HS Digital Output                | IO_ADC_36          |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_00                                                                                                         | IO_DI_72                         |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P150                                                                                                             | HS PWM Output                    | IO_PWD_14 IO_DI_30 |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P151                                                                                                             | HS PWM Output                    | IO_PWD_18 IO_DI_34 |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P152                                                                                                             | HS Digital Output                | IO_ADC_38          |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_02                                                                                                         | IO_DI_74                         |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P153                                                                                                             | HS PWM Output                    | IO_DO_16           | IO_DI_00                      |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_00                                                                                                        |                                  |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P154                                                                                                             | HS PWM Output                    | IO_DO_30           | IO_DI_14                      |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_14                                                                                                        |                                  |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P155                                                                                                             | HS Digital Output                | IO_ADC_40          |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_04                                                                                                         | IO_DI_76                         |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P156                                                                                                             | HS PWM Output                    | IO_DO_18           | IO_DI_02                      |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_02                                                                                                        |                                  |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P157                                                                                                             | HS PWM Output                    | IO_DO_32           | IO_DI_16                      |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_16                                                                                                        |                                  |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P158                                                                                                             | HS Digital Output                | IO_ADC_42          |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_06                                                                                                         | IO_DI_78                         |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P159                                                                                                             | HS PWM Output                    | IO_DO_20           | IO_DI_04                      |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_PWM_04                                                                                                        |                                  |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P160 P161                                                                                                        | HS Digital Output                | IO_PVG_00          | IO_VOUT_00 IO_ADC_52 IO_DI_88 |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P162 P163 P164                                                                                                   | HS Digital Output                | IO_PVG_03          | IO_VOUT_03 IO_ADC_55 IO_DI_91 |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P165 P166 P167                                                                                                   | HS Digital Output                | IO_PVG_05          | IO_VOUT_05 IO_ADC_57 IO_DI_93 |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P168 P169 P170 P171 P172 P173                                                                                    | HS Digital Output                | IO_ADC_37          |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| IO_DO_01                                                                                                         | IO_DI_73                         |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| P174                                                                                                             | HS PWM Output                    | IO_PWD_15 IO_DI_31 |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| Document Number: D-TTC5F-G-20-002                                                                                | HY-TTC 500 System Manual V 1.6.0 |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |
| 3 Pinning and Connector                                                                                          |                                  |                    |                               |               |                                  |                      |                           |                                 |                                 |                           |                    |                           |                              |                    |

![104_image_0.png]( The image displays a large white sheet of paper with various columns and rows of numbers. There are multiple tables on the paper, each containing different sets of data. Some of these tables have headings like "1000" and "1500," indicating specific categories or sections within the data.

The sheets of paper are organized in a way that makes it easy to read and understand the information presented. The layout allows for efficient comparison and analysis of the data, making it suitable for use in various applications such as business, finance, or research.)

| IO_DI_35                                          |                   |           |                               |
|---------------------------------------------------|-------------------|-----------|-------------------------------|
| HS Digital Output                                 | IO_ADC_39         |           |                               |
| IO_DO_03                                          | IO_DI_75          |           |                               |
| HS PWM Output                                     | IO_DO_17          | IO_DI_01  |                               |
| IO_PWM_01 HS PWM Output                           | IO_DO_31          | IO_DI_15  |                               |
| IO_PWM_15                                         |                   |           |                               |
| P179                                              | HS Digital Output | IO_ADC_41 |                               |
| IO_DO_05                                          | IO_DI_77          |           |                               |
| P180                                              | HS PWM Output     | IO_DO_19  | IO_DI_03                      |
| IO_PWM_03                                         |                   |           |                               |
| P181                                              | HS PWM Output     | IO_DO_33  | IO_DI_17                      |
| IO_PWM_17                                         |                   |           |                               |
| P182                                              | HS Digital Output | IO_ADC_43 |                               |
| IO_DO_07                                          | IO_DI_79          |           |                               |
| P183                                              | HS PWM Output     | IO_DO_21  | IO_DI_05                      |
| IO_PWM_05                                         |                   |           |                               |
| P184 P185                                         | HS Digital Output | IO_PVG_01 | IO_VOUT_01 IO_ADC_53 IO_DI_89 |
| P186 P187 P188                                    | HS Digital Output | IO_PVG_02 | IO_VOUT_02 IO_ADC_54 IO_DI_90 |
| P189 P190 P191                                    | HS Digital Output | IO_PVG_04 | IO_VOUT_04 IO_ADC_56 IO_DI_92 |
| P192 P193 P194 P195 P196 P197 P198 P199 P200 P201 | BAT+ Power        |           |                               |
| P202                                              | BAT+ Power        |           |                               |
| P203                                              | BAT+ Power        |           |                               |
| P204                                              | BAT+ Power        |           |                               |
| P205                                              | BAT+ Power        |           |                               |
| P206                                              | BAT+ Power        |           |                               |

| TTControl GmbH Confidential and Proprietary Information. Copyright  2022 TTControl GmbH. All rights reserved.   | Alternative                             | Function   | 94          |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------|------------|-------------|--------------------------------|--------------------|-------------------------|-------------------------------|-------------------------------|-------------------------|------------------|-------------------------|----------------------------|------------------|
| HS Digital Output                                                                                                | Timer Input                             | PVG Output | VOUT Output | A/D Input (HS Output/PVG/VOUT) | Current Loop Input | A/D Input (Timer Input) | A/D Input (HS Digital Output) | A/D Input (LS Digital Output) | Analog Current Input 2M | Digital Input 2M | Analog Current Input 3M | Analog Resistance Input 3M | Digital Input 3M |
| Pin No.                                                                                                          | Main Function                           |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P207                                                                                                             | Terminal 15 IO_ADC_K15                  |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P208 P209                                                                                                        | CAN 0 Low IO_CAN_CHANNEL_0              |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P210                                                                                                             | CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN   |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P211                                                                                                             | CAN 2 Low IO_CAN_CHANNEL_2              |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P212 P213 P214 P215 P216                                                                                         | Sensor GND                              |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P217                                                                                                             | do not connect                          |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P218 P219 P220                                                                                                   | Wake-Up IO_ADC_WAKE_UP                  |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P221 P222                                                                                                        | CAN 0 High IO_CAN_CHANNEL_0             |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P223                                                                                                             | CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN  |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P224                                                                                                             | CAN 2 High IO_CAN_CHANNEL_2             |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P225 P226 P227 P228 P229 P230                                                                                    | do not connect                          |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P231                                                                                                             | BRR/100BASE-T1 TRXIO_DOWNLOAD, IO_UDP                                         |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P232                                                                                                             | BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P233                                                                                                             | RTC_BACKUP_BAT                          |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P234 P235                                                                                                        | CAN Termination 0L                      |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P236                                                                                                             | CAN Termination 1L                      |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| P237                                                                                                             | CAN Termination 2L                      |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| Document Number: D-TTC5F-G-20-002                                                                                | HY-TTC 500 System Manual V 1.6.0        |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |
| 3 Pinning and Connector                                                                                          |                                         |            |             |                                |                    |                         |                               |                               |                         |                  |                         |                            |                  |

![106_image_0.png]( The image features a white table with several rows of data displayed on it. Each row contains various columns filled with numbers and text, likely representing different types of information or metrics. The table appears to be organized and well-structured, making it easy for someone to analyze the data presented.)

P242

P243 Sensor GND

P244 Sensor GND

P245 Sensor GND

P246 BAT+ CPU

IO_ADC_UBAT

P247 Sensor **Supply** 5 V

IO_ADC_SENSOR_SUPPLY_0

P248 CAN **Termination** 0H

P249 CAN **Termination** 1H

P250 CAN **Termination** 2H

P251 LS Digital **Output**

IO_DO_08

IO_ADC_44

IO_DI_80

P252 LS Digital **Output**

IO_DO_10

IO_ADC_46

IO_DI_82

P253 LS Digital **Output**

IO_DO_12

IO_ADC_48

IO_DI_84

P254 LS Digital **Output**

IO_DO_14

IO_ADC_50

IO_DI_86

P255

P256 Sensor GND

P257 Sensor GND

P258 Sensor GND

Table 19: Pinning of HY-TTC 508

HY-TTC 500 System Manual V 1.6.0

![107_image_0.png]( The image features a blue and white logo for TTC Control HyDAC International. The logo is prominently displayed on the left side of the image with its distinctive colors and design. The company's name can be seen in bold letters below the logo, emphasizing their brand identity.)

96 **4 Specification of Inputs and Outputs**

## 4 Specification Of Inputs And Outputs

4.1 Positive Power Supply of Power Stages (BAT+ Power)
4.1.1 Pinout

![107_image_1.png]( The image displays a white and blue circuit board with numerous electronic components. There are several rows of green and red lights arranged across the board, indicating that it is an electrical device or computer component.

In total, there are 14 green lights and 13 red lights on the board, which are placed at various positions along its length. The arrangement of these lights suggests a well-organized and functional circuitry design.) 

| P201   | Battery (+) Supply of Power Stages / BAT+ Power   |
|--------|---------------------------------------------------|
| P202   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P203   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P204   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P205   | Battery (+) Supply of Power Stages / BAT+ Power   |
| P206   | Battery (+) Supply of Power Stages / BAT+ Power   |

Supply pins for power stage supply.

The nominal supply voltage for full operation is between 6 and 32 V, including supply voltage ranges for 12 and 24 V battery operation. In this voltage range, all the I/Os work, as described in the system manual. BAT+ Power pins are equipped with inverse polarity protection.

![108_image_0.png]( The image features a blue and white logo for TTC Control, an international company. It appears to be a promotional or informational piece showcasing their branding. The logo is displayed on a light blue background, which provides a clean and professional appearance.)

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

![109_image_0.png]( The image displays a blue and white logo for HyTec Control International. The company's name is written in red on top of the logo, making it stand out against the background. The logo appears to be related to a system manual or a computer system, possibly used for controlling various aspects of an operation.)

98 **4 Specification of Inputs and Outputs**
4.2 Positive Power Supply of Internal Electronics (BAT+ CPU)
4.2.1 Pinout

![109_image_1.png]( The image is a white drawing of a computer circuit board with many electronic components on it. There are numerous wires and connections throughout the board, indicating that it's a complex system. In addition to the wires, there are several buttons scattered across the circuit board, which may be used for various functions or controls within the device. The overall design of the circuit board suggests that it is an essential part of a larger electronic device or computer system.) 

Figure 15: Pinout of BAT+ CPU
Pin No. Function **SW-define**
P246 Battery supply of internal electronics IO_ADC_UBAT

Supply pin for positive power supply of internal electronics, sensor supply and PVG/Vout **output**
stages.

As the output voltage of the PVG/Vout **outputs is defined as a percentage value in relation to the**
battery voltage, the voltage drop on the wire to this pin has a **direct influence on the accuracy of the** PVG output voltage. BAT+ CPU pin is equipped with inverse polarity protection.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

![110_image_0.png]( The image is a diagram illustrating various components of an electronic device. There are several layers and sections within this device, including a CPU (Central Processing Unit) at the top left corner, a memory unit towards the center, and other smaller components spread across the rest of the image.

The diagram also features a power supply located in the bottom right section, with a green box labeled "ACDC" indicating its function. The overall layout showcases the intricate connections between these electronic components to create an efficient device.)

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

## 4.2.5 Low-Voltage Operation

The HY-TTC 500 core system is designed for full operation after start-up between 6 V and 32 V, including supply voltage ranges for 12 V and 24 V battery operation and cold-start cranking according to ISO 16750-2 [22]. The initial minimum supply voltage at the beginning of the **drive cycle is 8 V.** After start-up, the CPU will remain operational down to 6 V, e.g. during cold-start cranking. The minimum supply voltage during cold-start cranking is defined by ISO 16750-2:2012 (see Table 3, Starting profile values for systems with 12 V nominal voltage, UN
, and Table 4, *Values for systems* with 24 V nominal voltage, UN
). The HY-TTC 500 core system complies with ISO 16750-2:2012, level I, II (functional status C), III and IV for 12-V systems **and level I, II (functional status A) and III**
(functional status B) for 24-V systems, see Table 20 on page 103 and Table 21 on page **103.**
Restrictions during cold-start cranking apply also for sensor supplies. For more information, see Section 4.7 on page 112 and Section 4.8 on page **114.**
HY-TTC 500 ISO 16750 code specification see Section 1.6 on page 35.

![113_image_0.png]( The image is a white drawing of an electrical circuit with a waveform displayed on it. There are several numbers and letters scattered throughout the drawing, possibly representing measurements or calculations related to the circuit. A ruler can be seen running along the top edge of the drawing, indicating that this could be a technical diagram or schematic for the electrical system.)

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

![115_image_1.png]( The image is a close-up of an electronic device with multiple rows of buttons and switches. There are at least ten buttons visible on the device, arranged in various positions along its length. Some buttons are located towards the front, while others are situated further back.

The arrangement of these buttons creates an organized and functional design for the electronic device, which could be a remote control or another type of electronic gadget.)

![115_image_0.png]( The image depicts a large room with multiple rows of seats arranged neatly. There are several chairs placed throughout the room, some closer to the front and others further back. The chairs vary in size and design, creating an organized and visually appealing space.

In addition to the chairs, there is a TV mounted on the wall towards the right side of the room. This setup suggests that this could be a meeting or conference area where people can gather for presentations or discussions.) 
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

![117_image_0.png]( The image is a white drawing of an electronic device with multiple rows and columns filled with numbers. There are several buttons arranged across the device, each containing different numbers or symbols. Some of these buttons have labels like "P0," "P1," and "P2." The arrangement of buttons and numbers creates a complex pattern that resembles a circuit board.) 

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

![119_image_0.png]( The image is a white drawing of an electronic device with many ports and connections. It appears to be a computer or a similar type of equipment. There are several cords visible throughout the drawing, indicating various connections for input/output devices or power sources.

In addition to the cords, there are multiple buttons scattered across the drawing, possibly representing controls or switches for the device. The overall design suggests that this is an illustration of a complex electronic system with numerous ports and connections.) 

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

![121_image_0.png]( The image is a diagram of a computer system with various components labeled and connected together. There are several switches and cables visible throughout the drawing, indicating a complex network setup.

In addition to the switches, there are multiple keyboards and mice scattered around the image, suggesting that this could be a workspace or an area where people interact with these devices regularly. The combination of computer components, peripherals, and cables creates a detailed representation of a technology-driven environment.) 

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

## 4.6.3 Maximum Ratings Tecu **= -40. . . +125** °C

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

![123_image_0.png]( The image is a detailed diagram of an electronic device with multiple layers and components. There are several switches and ports visible throughout the device, some of which have green lights on them. The switches are arranged in various positions within the device, indicating different functionalities or connections.

In addition to the switches, there are two rows of buttons located towards the bottom of the image. These buttons may be used for controlling or configuring the electronic device. Overall, the diagram provides a clear representation of the internal structure and components of this particular electronic device.) 

![123_image_1.png]( The image displays a table with two columns of data. In one column, there are sensor supplies listed, while in the other column, there is a list of sensor supplies with their corresponding values. The table appears to be organized and well-presented for easy reference.)

Two independent sensor supplies 5 V for 3-wire sensors (e.g. **potentiometers, pressure sensors** etc.).

For fully redundant sensors with 2 sensor-supply connections, both supplies must be connected to different sensor supplies.

If the input voltage on the BAT+ CPU pin is lower than typically 6 V (at 5 mA sensor supply load current), the sensor supply output voltage will be out of specification. One example of such low input voltage situations may be cold-start cranking in 12/24 V systems where the supply voltage can drop below 6 V. If the sensor supply output voltage drops below 4.7 **V, the application software will be** informed about this error situation after glitch filtering.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *POWER - Driver for ECU power functions* of the API documentation [30].

![124_image_0.png]( The image displays a diagram of an electronic circuit with multiple components and labels. There are several boxes labeled with numbers, indicating different parts of the circuit. A processor is also visible within the circuitry.

The diagram appears to be a schematic or blueprint for a computer system, possibly related to a sensor supply. The various components are arranged in an organized manner, making it easy to understand the structure and functioning of the electronic device.)

Figure 23: Sensor supply 5 V

## 4.7.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol                           | Parameter                                      | Note   | Min.   | Max.   | Unit   |
|----------------------------------|------------------------------------------------|--------|--------|--------|--------|
| Vin                              | Output voltage under overload conditions (e.g. | -1     | +33    | V      |        |
| short circuit to supply voltage) |                                                |        |        |        |        |

4.7.4 Characteristics TECU **= -40. . . +125** °C

| Symbol   | Parameter                | Note   | Min.   | Max.   | Unit   |
|----------|--------------------------|--------|--------|--------|--------|
| Cout     | Pin output capacitance   | 0.8    | 1.2    | µF     |        |
| Vout     | Output voltage, at Iload | 4.85   | 5.15   | V      |        |
| I load   | Load current             | 0      | 500    | mA     |        |

## 4.8 Sensor Supply Variable

![125_image_0.png]( The image displays a diagram of an electronic device with multiple rows and columns filled with numbers. These numbers are arranged in a grid-like pattern, creating a visual representation of the device's circuitry or connections. The diagram appears to be a schematic drawing, providing insight into the inner workings of the electronic component.) 

![125_image_1.png]( The image displays a computer screen with a blue background and white text. There is a list of sensor supplies on the screen, including various types of sensors. Some of these sensors are labeled "SW-Define," indicating that they may be related to software or specific functions.

The list includes several rows of information about the different sensor supplies, such as their names and descriptions. The text is organized in a way that makes it easy for users to understand and navigate through the available options.)

One independent sensor supply with variable output voltage, configurable in 1 V steps, is provided for 3-wire sensors (e.g. potentiometers, pressure sensors **etc.).**
As already described in Section 4.7 on page 112, 5 V sensor supply, **Functional Description, the**
BAT+ CPU pin voltage must be at least 1 V higher than the required sensor supply output voltage VSSUP. If the BAT+ CPU pin voltage is lower than VSSUP -1 V, the **sensor supply output voltage** will be out of specification.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *POWER - Driver for ECU power functions* of the API documentation [30].

![126_image_0.png]( The image is a diagram of an electronic circuit with various components and labels. There are two main sections within the circuit: the left side and the right side. On the left side, there are several components including a sensor, an analog input, a voltage source, and a green box labeled "ADC." The right side of the circuit features more components such as a CPU, a memory unit, and another green box labeled "TM570."

The diagram also includes a bar graph that shows the relationship between different components within the electronic circuit. This visual representation helps to understand the connections and interactions between these various parts in the system.)

Figure 25: Sensor supply variable

## 4.8.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol   | Parameter                                                                        | Note   | Min.   | Max.   | Unit   |
|----------|----------------------------------------------------------------------------------|--------|--------|--------|--------|
| Vin      | Output voltage under overload conditions (e.g. short circuit to supply voltages) |        |        |        |        |

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

![127_image_0.png]( The image is a white drawing of an empty seat arrangement with multiple rows and columns. There are several chairs placed throughout the scene, each varying in size and position. Some chairs are located closer to the center while others are situated near the edges or corners of the drawing. Overall, the layout appears organized and well-structured for a seating area.) 

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

![128_image_0.png]( The image displays a graph with various data points and values. There are two main graphs present; one is located on the left side of the image, while the other is situated towards the right side. Both graphs have a blue background, which contrasts well with the white numbers displayed in each graph.

In addition to these graphs, there are three smaller graphs placed at different positions within the larger graphs. One of them can be found on the left side of the main graph, while the other two are located towards the right side. The presence of multiple graphs and data points suggests that this image is a visual representation of numerical information or data analysis.)

Note 1 Due to thermal reasons only one of the 8 inputs may be shorted **to 33 V at the**
same time. A connection to any supply voltage higher than 5 V is not allowed for normal operation.

## 4.9.4 Analog Voltage Input

![128_image_1.png]( The image is a diagram of an electronic circuit with various components and wires. There are two main power supplies present in the circuit, one on the left side and another on the right side. A CPU can be seen towards the right side of the circuit, while a voltage supply is located near the center.

Several other components are also visible within the circuit, such as a sensor supply, an analog output, and several wires connecting these various parts together. The diagram provides a clear representation of the electronic system's structure and functioning.)

## Absolute Vs. Ratiometric Voltage Measurement:

Many sensor types are available in absolute or ratiometric measurement variant.

- Absolute**: The sensor output voltage is a fixed value and directly corresponds to a physical**
value. For example, 2.5 V corresponds to 1 bar. Any tolerance **in the reference voltage of the** sensor and the ECU generates additional measurement inaccuracy.

- Ratiometric: The sensor output voltage is a fixed percentage of the sensor **supply, the ratio**
corresponds to a physical value. For example, 50 % corresponds to 1 bar (or 2.5 V if the sensor supply is exactly 5.00 V). Any tolerance in the reference voltage of the sensor and the ECU is completely compensated and will not generate additional measurement inaccuracy.

![129_image_0.png]( The image displays a diagram of an electronic circuit with various components labeled and arranged on it. There are multiple wires connecting these components, creating a complex network. Some key labels include "ADC," "ECC," and "Sensor Supply."

In addition to the main components, there is also a bar graph present in the image, which provides additional information about the circuit's structure or functioning. The diagram appears to be a detailed representation of an electronic device, likely used for communication or data processing purposes.)

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

![131_image_0.png]( The image features a diagram of an electronic circuit board with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts of the system.

In addition to the wires, there is a large green box on the right side of the circuit board, which might be a power supply or another essential component. The diagram provides a clear representation of the electronic components and their connections within the circuit.)

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

![132_image_0.png]( The image displays a diagram of an electronic circuit with a focus on the CPU and its components. There are several labels visible throughout the circuit, indicating various parts of the system. A green box is located towards the right side of the image, possibly representing a power supply or another essential component.

In addition to the main components, there are two smaller boxes in the middle section of the diagram, which could be related to memory or other functionalities within the CPU. The circuit appears to be well-organized and clearly labeled, providing an overview of its structure and functioning.)

The resistance mode may also be used as digital input with switches connected to ground, see Figure 32 **on the current page. The use of switches to BAT+ is not allowed.** To enhance the diagnostic coverage, use switches of type Namur. With a Namur-type switch sensor, short to ground, short to BAT+ and cable defects can be easily **detected.**

![133_image_0.png]( The image displays a diagram of an electronic circuit with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts together. A green box can be seen on the right side of the circuit, likely containing some essential component or functioning as part of the overall system.

The diagram is accompanied by a list of labels that correspond to specific components in the circuit. These labels are placed above their respective parts, providing an organized and informative visual representation of the electronic device's structure.)

![133_image_1.png]( The image displays a diagram with several components labeled and described. There are two main sections of the diagram: one on the left side and another on the right side.

On the left side, there is an explanation of the Ecu (Electronic Control Unit) with its CPU (Central Processing Unit), which appears to be a part of a car's engine control system. The image also includes a switch that connects to the Gnd (Ground).

On the right side, there is an explanation of the Analog Input and Digital Output sections. These components are essential for monitoring and controlling various aspects of the vehicle's performance. Additionally, there are two buttons labeled as "Switches" on this side of the diagram.)

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

![135_image_1.png]( The image depicts a white background with an empty track or raceway that is designed to hold a race car. The track appears to be a part of a larger structure, possibly a stadium or arena. There are no cars or other objects visible on the track at this time.)

![135_image_0.png]( The image depicts a large room filled with numerous chairs arranged in rows. There are at least twelve chairs visible in the scene, each occupying different positions within the room. The chairs are placed close to one another, creating an organized and neat appearance. The arrangement of these chairs suggests that this space could be used for various purposes such as a classroom or a meeting area.) 
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
Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.11 Timer Inputs

![141_image_1.png]( The image is a white drawing of an electrical device with many small dots and lines on it. These dots are arranged to resemble a circuit board or a computer chip. The drawing appears to be a close-up view of the device, showcasing its intricate details. It seems like a schematic representation of an electronic component or a part of a larger system.)

![141_image_0.png]( The image features a large white room with multiple rows of seats arranged neatly. There are several chairs placed throughout the room, some closer to the front and others further back. Each chair has a green light on it, indicating that they are currently unoccupied.

The arrangement of chairs is organized in two distinct sections: one section occupies the left side of the room, while the other spans across the right side. The chairs vary in size and positioning, creating an inviting atmosphere for guests or attendees to sit and enjoy their time in this large space.) 
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

![142_image_0.png]( The image displays a diagram of an electronic circuit with various components and labels. There is a large green box on the right side of the circuit, which likely contains a power supply. A smaller green box can be seen towards the top left corner of the circuit.

Several other boxes are scattered throughout the circuit, some of them containing different types of electronic components. The diagram also includes labels for various parts such as capacitors and resistors. There is a bar graph located in the middle-left part of the image, which might represent the values or connections between different components within the circuit.)

12 digital inputs with timer function to process input signals such as frequency (rotational speed), pulse count and quadrature decoding (incremental length measurement), PWM etc. 6 out of 12 inputs can be alternatively used as digital (7/14 mA) current loop speed sensors. The inputs can be individually configured by software with a pull-up/pull-down resistor to adapt them to different sensor types, The timer input can be used as an analog voltage input as well. **For diagnosis, it is possible to** measure the analog voltage and frequency at the same channel **at the same time.** See also sections *PWD - Pulse Width Decode and digital timer input driver* and *DIO - Driver for* digital inputs and outputs **of the API documentation [30].**

## 4.11.3 Maximum Ratings

TECU **= -40. . . +125** °C

| Symbol   | Parameter                               | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------------------|--------|--------|--------|--------|
| Vin      | Input voltage under overload conditions | -1     | +33    | V      |        |

![143_image_0.png]( The image is a diagram of an electronic circuit board with various components and connections. There are multiple wires and connectors visible throughout the circuit, indicating that it is a complex system. Some of these components include resistors, capacitors, and transistors.

In addition to the primary components, there are also several labels on the diagram, providing information about each component's function or purpose within the circuit. The overall layout of the circuit board appears to be well-organized and thoughtfully designed for efficient operation.)

![143_image_1.png]( The image depicts a diagram of an electronic circuit with various components and labels. There are two main elements in this circuit: a CPU (central processing unit) and a sensor A. The CPU is positioned towards the top-left side of the image, while the sensor A is located near the center.

In addition to these primary components, there are several other smaller labels scattered throughout the diagram, indicating different parts or functions within the circuit. Overall, this diagram provides an overview of a complex electronic system with multiple interconnected components.)

![144_image_0.png]( The image features a diagram of an electrical circuit with various components labeled and arranged throughout the scene. There are multiple wires connecting different parts of the circuit, including a green box that is part of the system.

In addition to the main components, there are several labels on the diagram, such as "EUC," which might refer to an electronic unit control. The image also includes a bar graph displaying data related to the electrical circuit, providing insight into its function and performance.)

![144_image_1.png]( The image is a diagram of an electrical circuit with various components labeled and connected to each other. There are multiple wires and connections throughout the circuit, indicating that it's a complex system. Some key components include a CPU, a power supply, and several switches.

In addition to these main elements, there is also a bar plot visible in the image, which could be used for visual representation or analysis of data related to the electrical circuit. The diagram provides an overview of the connections between different parts of the system, making it easier to understand its functioning and components.)

## 4.11.4 Timer And Current Loop Inputs 4.11.4.1 Characteristics Of Timer Input

TECU **= -40. . . +125** °C

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

![146_image_0.png]( The image displays a diagram of an electronic circuit with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts together. Some of these connections include a CPU, EMCU, and RPM sensor.

The diagram is quite detailed, showing the intricate connections between the components. The labels on the image provide information about the specific functions of each component within the electronic circuit. Overall, it appears to be an illustration of a well-designed electrical system.)

## 4.11.5 Analog And Digital Inputs 4.11.5.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C 4.11.5.2 Characteristics Of Digital Input

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

| Symbol   | Parameter                    | Note   | Min.   | Max.   | Unit   |
|----------|------------------------------|--------|--------|--------|--------|
| Rpud     | Pull-up/pull-down resistor   | 7.5    | 10     | kΩ     |        |
| Vpu      | Pull-up voltage (open load)  | 2      | 4.25   | 4.8    | V      |
| Vin      | Input voltage range          | 0      | 32     | V      |        |
| τin      | Input low pass filter        | 2.8    | 3.2    | µs     |        |
| Vil      | Input voltage for low level  | 0      | 2      | V      |        |
| Vih      | Input voltage for high level | 3      | 32     | V      |        |

Note 1 TECU **= -40. . . +85** °C
Note 2 This is the input voltage with pull-up setting, without the **sensor connected.**
Note 3 The total measurement error is the sum of zero reading error and the proportional error.

TECU **= -40. . . +125** °C

## 4.12 High-Side Pwm Outputs 4.12.1 Pinout

![148_image_0.png]( The image is a white drawing of an airplane with a long row of seats lined up inside it. There are multiple rows of chairs, each containing several individual seats. The arrangement of the chairs creates a sense of organization and order within the aircraft cabin.) 

## Figure 41: Pinout Of High-Side Pwm Outputs

The following table depicts the high-side PWM outputs together with their corresponding external and secondary shut-off group/paths and power stages.

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

![150_image_0.png]( The image displays a detailed diagram of an electronic circuit board with various components and connections. There are multiple wires running through the circuit, connecting different parts of the system. A large number of switches can be seen throughout the diagram, indicating the complexity of the circuitry.

In addition to the switches, there is a clock placed on the right side of the image, likely providing timekeeping functions for the electronic device. The overall layout and arrangement of components suggest that this is an intricate and well-designed system.)

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

![157_image_0.png]( The image is a diagram showing the internal structure of an ECC (Error Correcting Code) unit. The main components include a CPU (Central Processing Unit), memory, and various other parts that work together to ensure data integrity in the system.

There are several wires connecting different parts within the ECC unit, with some labeled as "GAT" or "SAT." These wires represent the communication between different components of the system. The diagram also includes labels such as "Watchdog," which could be a reference to a specific function or monitoring tool within the ECC unit.

Overall, this image provides an in-depth view of the internal workings and connections within the ECC unit, highlighting its essential components and their relationships.)

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

![159_image_0.png](4-wire circuit diagram showing a power supply with several components connected to it. The circuit includes a transformer and a rectifier, which are essential for converting AC to DC power. There is also an audio amplifier present within the system.

The image features multiple labels and descriptions, providing information about each component in the circuit. The diagram is organized into sections, making it easy to understand the connections between various components.)

With the tertiary shut-off configuration shown in 44 **the HY-TTC 500 is able to switch off the high-side** PWM channels even if the load has a short circuit to the positive battery supply.

Please refer to section *PWM - Pulse Width Modulation driver* **of the API documentation [30] for more** information how to configure such an output.

## 4.13 High-Side Digital Outputs

4.13.1 Pinout

![160_image_1.png]( The image is a close-up of a carousel with several cars on it. There are at least nine cars visible in various positions around the carousel. Some cars are closer to the front, while others are further back, creating an interesting visual effect. The arrangement of these cars creates a sense of depth and movement within the scene.)

![160_image_0.png]( The image is a black and white drawing of an electronic device with many small squares arranged on it. Each square contains a single letter or number, creating a pattern that resembles a keyboard layout. There are multiple rows of these squares, giving the impression of a large number pad.

In addition to the letters and numbers, there is also a row of green and blue squares placed among the other squares. These colors add a touch of contrast to the otherwise monochromatic drawing.) 
Figure 45: Pinout of high-side digital outputs

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

![161_image_0.png]( The image is a diagram of an electronic circuit with various components and labels. There are multiple wires connecting different parts of the circuit, including a CPU, digital output, watchdog timer, and other elements. The diagram displays a detailed view of the system's structure, making it easy to understand its functioning.

In addition to the main components, there is also a clock visible in the image, which likely plays an essential role within the electronic circuit. Overall, the diagram provides a clear representation of the intricate connections and components that make up this particular electronic system.)

## 4.13.2.1 Power Stage Pairing

If outputs shall be used in parallel, always combine two channels from the same double-channel power stage and use the digital output mode. See Section 4.13.1 on page 149 **for using the right** power stage outputs in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip.

For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.13.2.2 Mutual Exclusive Mode

The HY-TTC 500 uses double-channel high-side power stages. **For load leveling it is a benefit if** loads, which are switched on mutually exclusive (which means either load A, or load B is on, but not A and B at the same time), are connected to the same double-channel power stage. This reduces the thermal stress of the components. The power stage pairing is given in Section 4.13.1 on page **149.**

## 4.13.3 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

![162_image_0.png]( The image displays a graph showing different types of output signals and their corresponding statuses. There are several green dots on the graph, indicating that some of these signals are active or functioning properly. The graph is organized into sections with labels for each type of signal, making it easy to identify which section corresponds to which signal.

In addition to the main graph, there are two smaller graphs located at the top left corner and bottom right corner of the image. These graphs may provide additional information or context related to the main subject matter.)

![162_image_1.png]( The image displays a computer screen with various lines of text and numbers. There are two main sections on the screen, one towards the top left corner and another at the bottom right corner. The top section appears to be related to detecting or not detecting something, while the bottom section seems to be a list of data points.

In addition to these sections, there is a smaller text box in the middle-left area of the screen that might provide more context or information about the displayed content. Overall, it appears to be a technical or computer-related document with multiple lines of data and instructions.)

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

## 4.14 High-Side Digital/Pvg/Vout Outputs

4.14.1 Pinout

![166_image_1.png]( The image is a black and white photo of an empty room with a large window. There are no people or objects visible within the frame. The focus of the scene is on the window, which takes up a significant portion of the space in the room.)

![166_image_0.png]( The image features a large white box with numerous rows of small squares inside it. Each square is filled with different colored balls, creating an intricate and visually appealing pattern. There are at least twelve distinct colors visible within the box, showcasing a variety of hues that make the scene interesting to observe.) 
Figure 47: Pinout of High-side digital/PVG/VOUT outputs

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

![168_image_0.png]( The image is a diagram of an electrical system with multiple components labeled and connected to each other. There are several power lines, including one that reads "Ecu," indicating a central control unit for the system. Other labels include "ATT Power," "Watchdog," and "CPU."

The diagram features various electronic devices such as a CPU (central processing unit), an ATT power supply, and a watchdog timer. There are also multiple wires connecting these components to each other, illustrating the intricate network of connections within the system. The image provides a clear visual representation of the electrical system's structure and functioning.)

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

![170_image_0.png]( The image displays a diagram of an electrical circuit with several components labeled and connected to each other. There are two main sections within the circuit - one on the left side and another on the right side.

On the left side, there is a VCV (Voltage Controlled Voltage) component, along with a 27V output. On the right side of the circuit, there is an ECCU (Electronic Control Unit) connected to a CPU (Central Processing Unit).

The diagram also includes multiple wires connecting these components, indicating their interconnectedness within the electrical system.) For diagnostic reasons in output mode, the output signal is looped back to the CPU, and the measured value is compared to the set value. If the difference between these two values is above a fixed limit, an overload is detected, and the output is disabled. The protection mechanism tries re-enabling the output 10 times per drive cycle. It is not allowed to use two outputs in parallel to increase driving strength.

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

![172_image_0.png]( The image displays a diagram of an electronic circuit with various components and labels. There are multiple wires connecting different parts of the circuit, including a CPU, an ADC (analog-to-digital converter), and other electronic devices.

The circuit is described in German, indicating that it might be related to a specific language or region's electronics industry. The diagram provides a clear visual representation of the connections between these components, allowing for better understanding and analysis of the circuit's functionality.)

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

| Symbol     | Parameter                   | Note   | Min.   | Max.   | Unit   |
|------------|-----------------------------|--------|--------|--------|--------|
| Cin        | Pin input capacitance       | 384    | 576    | nF     |        |
| τin        | Input low pass filter       | 8      | 12     | ms     |        |
| Rpud       | Pull-up/pull-down resistor  | 2.5    | 2.6    | kΩ     |        |
| Vpu        | Pull-up voltage (open load) | 4.7    | 5.1    | V      |        |
| Resolution | 12                          | 12     | bit    |        |        |
| Vil        | Input voltage for low level | 0      | V      |        |        |

| Symbol   | Parameter                             | Note   | Min.   | Max.            | Unit   |
|----------|---------------------------------------|--------|--------|-----------------|--------|
| Vih      | Input voltage for high level          | 1      | 32     | V               |        |
| Vin      | Input voltage range                   | 1      | -0.5   | BAT+ Power +0.5 | V      |
| Note     | Configuration by application software |        |        |                 |        |

Note **Configuration by application software**
Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

4.15 Low-Side Digital Outputs 4.15.1 Pinout

![176_image_1.png]( The image features a close-up of an electronic device with several buttons and ports on it. There are five visible buttons arranged around the center of the device, possibly indicating different functions or settings. Additionally, there is a port located near the bottom left corner of the device, which could be used for connecting to other devices or charging purposes. The overall design suggests that this electronic device might be used for various tasks or communication purposes.)

![176_image_0.png]( The image is a white drawing of an airplane with many rows of seats and green numbers indicating where passengers are seated. There are multiple rows of seats throughout the plane, each containing various numbers that correspond to different sections or areas within the aircraft.

The drawing also features a few chairs placed in different locations, likely representing additional seating options for passengers. The overall layout of the airplane is well-organized and clearly depicted through this white drawing.) 

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

![177_image_0.png]( The image is a diagram of an electronic circuit board with various components and connections. There are multiple wires connecting different parts of the circuit, including a green box that appears to be a power supply. A few other boxes can also be seen on the circuit board, possibly indicating additional functionalities or components.

The diagram is labeled with text, providing information about each component and its function within the circuit. The labels are placed at various points throughout the image, allowing for easy identification of the different parts. Overall, it's a detailed representation of an electronic circuit board that showcases its intricate structure and connections.) loads.

The current through the low-side switch is monitored and triggers the opening in case of overcurrent. Short-circuit and overload protection is included in low-level driver software. Before a tripped channel can be re-enabled, the overload situation has to be removed.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *DIO - Driver for digital inputs and outputs* **of the API documentation [30].**

## 4.15.2.1 Power Stage Pairing

If higher load current is needed, the output stages can be used in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip. For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.15.3 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

![178_image_0.png]( The image displays a table with several rows of data and various settings. There are multiple green dots scattered across the table, likely representing different values or points within the data set. Above each row, there is a label indicating the type of output signal, status, or other relevant information.

In addition to the main table, there are two smaller tables visible in the image. One of them has a single green dot on it, while the other one appears empty. The presence of these additional tables suggests that the main table may be part of a larger data analysis or visualization process.)

![178_image_1.png]( The image is a close-up of a white background with black text. The text reads "United," which suggests that it could be related to an airline or a company with a similar name. The focus on this word indicates that the context might be related to travel, aviation, or business.)

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

![181_image_0.png]( The image is a white drawing of an electronic device with multiple rows of buttons and switches. There are several rows of buttons arranged vertically, with some located closer to the top while others are situated nearer to the bottom. The buttons vary in size and position, creating a complex arrangement within the device's structure.) 

Pin No. Function **SW-define**
P208 LIN IO_LIN

LIN is configured in master mode. LIN is a bidirectional half duplex serial bus for up to 10 nodes. Note: **A common ground (chassis) or a proper ground connection is necessary for LIN operation. If** you connect to an external device (e.g., to a PC with a LIN interface), make sure not to violate the maximum voltage ratings when connecting to the LIN connection.

See also section *LIN - Local Interconnect Network driver* **of the API documentation [30].**

![182_image_0.png]( The image displays a diagram of an electronic circuit with multiple components labeled on it. There are two main sections within the circuit: one is a large green box that occupies most of the space and another smaller blue box located towards the left side of the image.

In addition to these boxes, there are several other labels scattered throughout the diagram, indicating various electronic components or functions. The overall layout suggests a complex system with multiple interconnected parts, possibly related to communication or data processing.)

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
4.17 RS232 4.17.1 Pinout

![184_image_0.png]( The image features a white computer keyboard with several green lights on it. There are two rows of keys visible, one row closer to the left side and another row towards the right side of the keyboard. Each key has a corresponding green light illuminated above it, indicating that they may be functioning as a control panel or an indicator for specific features. The arrangement of these lights adds a unique visual element to the otherwise standard keyboard design.) 

| Pin No.   | Function                          | SW-define   |
|-----------|-----------------------------------|-------------|
| P242      | RS232 Serial Interface Output(TX) | IO_UART     |
| P255      | RS232 Serial Interface Output(RX) |             |

RS232 is used as a full duplex serial interface. Note: **Handshake lines (RTS, CTS) are not available. A common ground (chassis) or a proper** ground connection is necessary for RS232 operation. If you connect to an external device (e.g., to a PC with an RS232 interface), make sure not to violate the maximum ratings.

See also section *UART - Universal Asynchronous Receiver Transmitter driver* **of the API documentation [30].**

![185_image_0.png]( The image displays a diagram showing the relationship between CPU and memory usage on an ECC (Error Correcting Code) computer system. There are two main components in the diagram - one is the CPU, which occupies most of the space from left to right, while the other is the memory, located towards the bottom of the image.

The CPU is connected to the memory through a series of arrows, indicating that data flows between these two components. The memory is further divided into different sections, such as the cache and main memory, which are essential for efficient processing in the computer system.)

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

![186_image_1.png]( The image is a close-up of a gray background with a white logo or symbol located at the top left corner. There are no other visible elements or objects in the image.)

![186_image_0.png]( The image is a white drawing of an electronic device with many buttons and switches on it. There are several rows of buttons arranged vertically, each row containing multiple buttons. These buttons appear to be part of a control panel or interface for the electronic device.

The buttons vary in size and position, some closer together while others are spaced further apart. The arrangement of these buttons creates an organized and functional layout for operating the device.) 

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

![188_image_0.png]( The image is a diagram that shows two different parts of a computer system. One part is labeled "Can High" and has a blue background with a red arrow pointing to it. The other part is labeled "Ecu" and features a green background with a red arrow pointing towards it.

In the middle of these diagrams, there are two arrows pointing in opposite directions, possibly indicating connections between different components within the computer system. Additionally, there are several smaller arrows scattered throughout the diagrams, which could represent other connections or interactions within the system.)

## 4.18.3 Maximum Ratings Tecu **= -40. . . +125** °C

| Symbol   | Parameter                               | Note   | Min.   | Max.   | Unit   |
|----------|-----------------------------------------|--------|--------|--------|--------|
| VCAN_H , | Bus voltage under overload conditions   |        |        |        |        |
| VCAN_L   | (e.g. short circuit to supply voltages) |        |        |        |        |

## 4.18.4 Characteristics Tecu **= -40. . . +125** °C

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

Note **1 Due to high current in the cable harness, the individual ground potential of the**
control units can differ up to several V. This difference will also appear as common mode voltage between a transmitting and a receiving control unit and not influence the differential bus signal, as long as it is within **the common mode** limits.

Note **2 Pay attention to the limitations of CAN. The arbitration process allows 1 Mbit/s**
operation only in small networks and reduced wire length. By **way of example,** a so-called "private CAN", which is a short point-to-point connection (less than 10 m) between two nodes only, can be operated at 1 MBit/s.

Note **3 For typical network sizes and topologies (networks with stub wires) and more**
than two nodes, the practical limit is 500 kbit/s.

Note 4 Any value that conforms to CAN protocol standard definition **is valid.** Note 5 ISOBUS CAN variant.

## 4.19 Can Termination

![190_image_0.png]( The image is a white drawing of an electronic device with multiple rows of buttons and switches. There are at least twelve buttons visible on the device, arranged in various positions across its surface. Some buttons appear to be grouped together, while others are more spread out. The design suggests that this could be a control panel or interface for managing different functions within the electronic device.)

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

![191_image_0.png]( The image displays a diagram of an electronic circuit with various components and labels. There are several wires connecting different parts of the circuit, including a 60 ohm resistor and a CAN termination L. The circuit appears to be well-organized, with each component clearly labeled for easy understanding.) 

4.20 Ethernet

![192_image_0.png]( The image depicts a white drawing of an electronic device with several rows of buttons and switches. There are numerous buttons arranged vertically and horizontally throughout the device, creating a complex network of connections. Some buttons appear to be labeled, indicating their specific functions or purposes within the device.

The arrangement of these buttons and switches suggests that this could be an electronic component or a part of a larger system, such as a computer or communication device. The intricate design and organization of the buttons indicate that it may serve a crucial role in the functioning of the device.) 

| Pin No.   | Function                             | SW-define           | Applicable to variants   |
|-----------|--------------------------------------|---------------------|--------------------------|
| P218      | Ethernet Differential Transmit - TD+ | IO_DOWNLOAD, IO_UDP | HY-TTC 580               |
| P219      | Ethernet Differential Transmit - TD- | HY-TTC 580          |                          |
| P231      | Ethernet Differential Receive - RD-  | HY-TTC 580          |                          |
| P232      | Ethernet Differential Receive - RD+  | HY-TTC 580          |                          |

The Ethernet interface supports application download and the UDP communication protocol. The 10/100 Mbit/s full duplex Ethernet port is designed for IEEE 802.3 compliance. However, there is no standard Ethernet connector provided, the Ethernet signals are located on the main connector. Make sure to use appropriate cabling according to the Ethernet standard. Use at least an Ethernet CAT3 cable for a transmission speed of 10 Mbit/s and an Ethernet CAT5 cable for a transmission speed of 100 Mbit/s. In a noisy environment, it is recommended to use shielded cables. See also sections *IO_UDP* and *IO_DOWNLOAD* **in the API documentation [30].**

![193_image_0.png]( The image displays a diagram with various components labeled and connected to each other. There are multiple arrows pointing towards different parts of the diagram, indicating connections between them. Some of these components include "magnetics," "ethernet," "processor," "memory," and "cpu."

The diagram is organized in such a way that it appears to be a flowchart or a network diagram, with each component represented by a box or rectangle. The labels on the boxes provide context for understanding the relationships between these components within the system.)

## 4.20.3 Maximum Ratings

TECU = −40. . . +125 °C

| Symbol             | Parameter                                    | Note   | Min.   | Max.   | Unit   |
|--------------------|----------------------------------------------|--------|--------|--------|--------|
| Vin-CMM            | Input common mode voltage range 50/60 HZ AC, | 0      | 750    | VRMS   |        |
| 60 s test duration |                                              |        |        |        |        |

## 4.21 Broadr-Reach®

![194_image_0.png]( The image is a white drawing of an electronic device with many rows of numbers and letters. There are two main sections within this device, one on the left side and another on the right side. The left section features several rows of numbers and letters, while the right section has a row of green lights.

In addition to these elements, there is also a smaller drawing of a car located in the middle of the image. This car appears to be part of the electronic device's design or function.)

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

![196_image_0.png]( The image is a white drawing of an airplane with multiple rows of seats. There are two main sections visible within the plane, one on the left side and another on the right side. Each section contains several rows of seats, with some rows having more chairs than others.

In addition to the seating arrangements, there is a green box located in the middle of the drawing, possibly representing an emergency exit or other important area within the airplane.) 

Figure 64: RTC pinout
Pin No. Function **SW-define**
P233 Real-Time Clock Backup Battery IO_RTC

The HY-TTC 500 includes a real-time clock with a backup power **system for exact system time- and** date-keeping after every power cycle. The real-time clock module is either supplied by the internal 5 V supply, vehicle battery, or by the external RTC battery pin. When HY-TTC 500 is connected to the vehicle battery via the BAT+ CPU pin, the RTC is supplied by the vehicle battery independent of whether the device is operational or in power-off mode. When both the RTC backup battery and BAT+ CPU are disconnected, the real-time clock is supplied by an internal capacitor. The capacitor provides approximately 10 minutes of backup time when fully charged. Charging an empty capacitor takes at least 5 minutes. See also section *RTC - Real Time Clock driver* **of the API documentation [30].**

![197_image_0.png]( The image displays a diagram of an electronic device with various components and connections. There are multiple wires connecting different parts of the device, including a CPU and an external battery. A green box is also present within the circuitry, possibly representing a power source or another component.

The diagram appears to be a schematic, providing a clear visual representation of the internal workings of the electronic device. The components are arranged in a way that allows for easy understanding of their relationships and functions within the system.)

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

![200_image_0.png]( The image displays a complex diagram or flowchart that appears to be related to computer hardware and software components. It is filled with various labels and numbers, indicating different parts of the system. There are several arrows pointing towards different sections within the chart, suggesting connections between these components.

In addition to the main diagrams, there are two smaller figures in the image, one located near the top left corner and another at the bottom right corner. These figures might represent specific hardware or software elements within the larger flowchart.)

## 5.2 Thermal Management 5.2.1 Board Temperature Sensor

5.2.1.1 Pinout

![201_image_0.png]( The image displays a computer screen with various data and information displayed on it. There is a temperature chart that shows different temperatures at different times of the day. The chart is accompanied by a table that provides additional details related to the temperature data.

In addition to the main temperature chart, there are two smaller charts visible in the image, one located towards the left side and another on the right side. These smaller charts may provide more detailed information or be part of the same dataset as the primary temperature chart.)

![201_image_1.png]( The image is a white and gray color scheme with a large amount of white space. In this setting, there are two distinct colors: white and gray. The white area occupies most of the image, while the gray area appears to be smaller in size. This combination creates an interesting contrast between the two colors, making it visually appealing.)

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

| 12 V System                        | 24 V System                               |         |
|------------------------------------|-------------------------------------------|---------|
| Max. battery voltage 1             | 14 V                                      | 28 V    |
| Motor blocked current              | 2 to 4 A                                  |         |
| DC-resistance                      | >=3.5 Ω                                   | >=7.0 Ω |
| Unidirectional drive               | yes                                       | yes     |
| Bidirectional drive                | yes                                       | yes     |
| Active motor braking               | yes                                       | yes     |
| Reverse without brake              | no                                        | no      |
| PWM operation                      | no                                        | no      |
| Suitable high side power stages    | PWM power stages, digital HS power stages |         |
| Maximum periodic DC peak current 2 | 4 A (TECU < +85 °C)                       |         |
| Maximum periodic DC peak current 2 | 3 A (TECU > +85 °C)                       |         |

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

![219_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled and connected to each other. There are multiple wires running through the circuit, and some of them have labels indicating their purpose or function within the system.

In addition to the wires, there is a group of batteries placed in different positions throughout the circuit, likely providing power to the connected devices. The diagram also features a green button, which could be an indicator for a specific function or control within the electrical circuit. Overall, it appears to be a complex and intricate system that requires careful attention and understanding to operate effectively.)

A better solution for achieving less voltage drop in the return path shows the Figure 68 **on the current** page.

![220_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled and connected to each other. There are multiple wires and switches visible throughout the circuit, indicating that it is a complex system. A green button can be seen in the middle of the circuitry, possibly serving as a control or input device for the system. The diagram provides an overview of the electrical components and their connections within the circuit, allowing for better understanding of its functioning.)

## 6.5.5.2 Unidirectional Double Power Stage

Higher current can be achieved by paralleling output stages, see Figure 69 **on this page. Please** observe the use of cables of same diameter and same wire length in parallel on the power stages as well.

![221_image_0.png]( The image is a white drawing of an electrical circuit diagram with various components labeled and connected to each other. There are multiple wires running through the circuit, connecting different parts of the system.

In the center of the diagram, there is a large circle that seems to be the main focus of the circuit. The image also includes several smaller circles scattered throughout the drawing, possibly representing additional components or connections within the electrical system.)

6.5.5.3 Bidirectional H-bridge (Single Power Stages)

![222_image_0.png]( The image displays a diagram of an electrical circuit with multiple components labeled and arranged throughout the scene. There are several blue boxes placed at various positions within the circuit, likely representing different parts or functions of the system.

In addition to the blue boxes, there is a green box located near the top left corner of the image. The diagram also includes a few labels, such as "10xHS output" and "10xHS input," indicating specific components within the circuit. Overall, the image provides an organized visual representation of the electrical circuit's structure and components.)

6.5.5.4  Bidirectional H-bridge (Multiple Low Side Power Stages)

![223_image_0.png]( The image is a white drawing of an electrical circuit board with multiple components labeled on it. There are several blue boxes and green boxes scattered throughout the circuit board, indicating different types of electronic devices or connections within the system.

The circuit board features numerous wires connecting these various components, illustrating the intricate network of connections that make up the entire electrical system. The labels on the drawing provide a clear understanding of the components' functions and their relationships to one another.)

![224_image_0.png]( The image is a white drawing of an electrical circuit with multiple wires and components. There are several blue and green boxes lined up along the top of the circuit, possibly representing electronic devices or components. These boxes are connected to each other through various wires, creating a complex network within the circuit.

In addition to the main circuit, there is a smaller drawing in the upper right corner that appears to be an electrical component as well. The overall design of the image suggests a detailed representation of an electronic system or device.)

## 6.5.5.6 Motor Cluster

This is a usual configuration to control 2 motors, that are never operated at the same time, with 3 half bridges (3 x high side + 3 x low side power stage). Example: Outside mirror control

![225_image_0.png](1xHS Output is displayed on a white background with multiple diagrams and descriptions. The main focus of the image is an electrical circuit diagram that shows various components connected to each other. There are several labels and descriptions accompanying the diagrams, providing information about the different parts of the circuit.

In addition to the main circuit diagram, there are smaller diagrams scattered throughout the page, possibly showing additional details or variations in the design. The overall presentation is informative and visually engaging, making it easy for viewers to understand the intricacies of the electrical system.)

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

Usage of external switches connected to GND. Short circuits to battery supply needs to be excluded in the system architecture.

![230_image_0.png]( The image displays a diagram of an electrical circuit with multiple components and connections. There are several batteries positioned throughout the circuit, some closer to the center while others are more towards the edges. A mix of cords can be seen intertwined within the circuit, connecting various parts together.

In addition to the batteries and cords, there is a clock visible in the middle-left area of the image, possibly indicating the passage of time or providing a reference for the electrical system's operation. The overall layout suggests that this diagram represents an intricate electrical setup with multiple components working together.)

![230_image_1.png]( The image displays a diagram of an electrical circuit with various components labeled throughout the drawing. There are multiple batteries and power sources, including one near the top left corner, another at the bottom right corner, and several smaller ones scattered around the middle section of the diagram.

A series of switches can be seen in different parts of the circuit, with some located closer to the center, while others are situated towards the edges. There is also a clock visible on the right side of the image, possibly indicating the time or providing reference for the electrical system's operation.)

![231_image_0.png]( The image is a detailed diagram of an electrical circuit with various components labeled and connected. There are multiple switches and batteries visible throughout the circuit, along with other electronic devices like transistors and capacitors. The diagram also includes a number of wires connecting these components to create a functional electrical system.

The image is in black and white, which adds an element of complexity to the visual representation of the circuit. It appears to be a schematic or blueprint for an electronic device or machine that relies on this intricate network of interconnected parts.)

## Switches Connected To Pwm High-Side Output Stage:

Digital switches and analog sensors are supplied via an HY-TTC 500 PWM high-side output pin, the switch/sensor output is monitored by an alternative (PWM high-side) input.

Caution! - The sourcing PWM high-side output stage (IO_PWM_00 - IO_PWM_35) must be out of the same secondary shut-off path (A, B or C) as the alternative input pin. For example IO_PWM_00 (output/source) supplies the digital sensor and the sensor output is monitored by IO_PWM_13 (input), both IO's are out of secondary shut-off path A. See Table 22 on page 138 for secondary shut-off paths and their relation to the alternative inputs.

![231_image_1.png]( The image displays a diagram of an electronic device with multiple components labeled and connected to each other. There are several batteries visible within the circuitry, likely providing power to the system. A green box is also present, which could be part of the device's structure or function.

The diagram appears to be a schematic or blueprint for an electronic component, possibly used in a car or another automotive application. The components are arranged in a way that allows for easy understanding and visualization of their connections and interactions within the system.)

![232_image_0.png]( The image is a diagram showing an electrical circuit with various components labeled throughout. There are multiple batteries present in the circuit, including one towards the left side and another on the right side of the image. A power source can be seen connected to these batteries, providing energy for the system.

In addition to the batteries, there is a CPU (Central Processing Unit) located near the center of the diagram. The circuit also features several other components such as a logic unit and a new battery stage. These components are all interconnected within the electrical circuit, creating a complex network that powers various devices or systems.)

![232_image_1.png]( The image displays a diagram of an electronic circuit with multiple components and connections. There are several batteries scattered throughout the circuit, likely providing power to various parts. In addition to the batteries, there is a mix of wires and connectors that help facilitate the flow of electricity within the system.

The circuit also features a number of switches, which control the flow of current through different paths. The presence of these switches suggests that the electronic circuit may be used for various purposes or to manage multiple functions simultaneously. Overall, the image provides an overview of a complex and intricate electrical system.)

## Switches Connected To Digital High-Side Output Stage:

Digital switches and analog sensors are supplied via an HY-TTC 500 digital high-side output pin, the switch/sensor output is monitored by an alternative (digital high-side) input. IO_DO_00 - IO_DO_07 and IO_PVG_00 - IO_PVG_07 are not equipped with an secondary shut-off

![233_image_0.png]( The image displays a diagram of an electrical circuit with various components labeled throughout the drawing. There are multiple batteries present in the circuit, along with a fuse and a power supply. A green box is also visible within the circuit, likely containing additional components or providing information about the system.

The diagram appears to be a detailed representation of an electrical setup, possibly used for educational purposes or as part of a project.)

paths. These high-side output stages can by themselves not be used for safety critical applications. If the alternative input function of IO_DO_00 - IO_DO_07 and **IO_PVG_00 - IO_PVG_07 shall be** used, the connected sensor must be supplied by an digital output stage out of these outputs.

6.6.1.1.2  Invalid Wiring Examples    The following wiring examples of external switches or analog sensors connected to battery supply are not allowed and must be avoided for safety critical systems.

Nonconforming wiring can lead to destruction of the HY-TTC 500.

## Stop Switch / Blown Fuse / K15 Wiring

Digital switches and analog sensors are supplied directly from the battery.

If for example the fuse is blown, BAT+Power is disconnected (loose connection) or the stop switch is pressed, digital switches or analog sensors are still supplied. The current flows over the closed switch and the parasitic body diode of the output stage used as input. All the load current of all other outputs now flows via the body diode of this single output stage. This may overload and even destroy this output stage.

![234_image_0.png]( The image displays a diagram of an electric circuit with multiple components and connections. There are several batteries placed throughout the circuit, some closer to the top left corner while others are positioned more towards the center. A series of wires can be seen connecting these batteries to various parts of the circuit, including a central processing unit (CPU).

In addition to the batteries and CPU, there is an array of other components such as a keyboard, a mouse, and a cell phone. The diagram also includes a clock placed towards the top right corner of the image. Overall, it appears to be a complex network of interconnected devices that work together to form an electric circuit.)

![234_image_1.png]( The image displays a diagram of an electrical circuit with various components and connections. There are multiple wires running through the circuit, including one labeled "16 battery." A few batteries can be seen throughout the circuit, with some placed closer to the top right corner and others near the bottom left side.

In addition to the batteries, there is a cell phone located in the middle of the circuit, possibly indicating that it's being charged or powered by the electrical system. The diagram also features several other components such as a computer, a keyboard, and a mouse, which are likely part of a larger electronic device or system.)

## 7 Debugging 7.1  Functional Description

After connecting the HY-TTC 500 and the Lauterbach Debugging Device with the TTC JTAG-Adapter Board (for the connector pinning, see Figure 83 on the current page), open the Trace32 Software for ARM CPUs. Double-click the batch file flash.cmm , which is located in the corresponding template directory. When prompted by the dialog whether to flash the application or to load only the symbols for debugging, click Yes to start the flashing procedure.

![235_image_0.png]( The image displays a diagram of an electronic circuit board with various components labeled and connected to each other. There are multiple wires connecting different parts of the circuit, indicating that it is a complex system.

In addition to the wires, there are several labels on the circuit board, including "Texas Instruments" in the top left corner, which suggests that this is an electronic device made by Texas Instruments. The diagram also features a clock and a number of other components, such as resistors, capacitors, and transistors, all arranged neatly to create a functional circuit.)

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
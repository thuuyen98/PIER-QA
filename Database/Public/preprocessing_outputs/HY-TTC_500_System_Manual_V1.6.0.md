# Hy-Ttc 500

![0_image_0_4756.png](The image features a blue sign with white letters that reads "TTC Control." It appears to be an advertisement for HyDac International, which is likely related to control systems or technology. The sign's design suggests that it could be used in various settings such as businesses, events, or promotional materials.)

System Manual Programmable ECU for Sensor-Actuator Management Product Version 02.00 Original Instructions

[table_0][{0: 'Document Number:', 1: 'D-TTC5F-G-20-002'}, {0: 'Document Version:', 1: '1.6.0'}, {0: 'Date:', 1: '25-Aug-2022'}, {0: 'Status:', 1: 'Released'}][/table_0]

TTControl GmbH
Schoenbrunner Str. 7, A-1040 Vienna, Austria,Tel. +43 1 585 34 34–0, Fax +43 1 585 34 34–90, **office@ttcontrol.com** No part of the document may be reproduced or transmitted in any form or by any means, electronic or mechanical, for any purpose, without the written permission of TTControl GmbH. Company or product names mentioned in this document may be trademarks or registered trademarks of their respective holders. TTControl GmbH undertakes no further obligation or relation to this document.

Copyright  2022 TTControl GmbH. All rights reserved. **Subject to changes and corrections**
TTControl GmbH Confidential and Proprietary Information

## Legal Notice **Document Number: D-Ttc5F-G-20-002**

The data in this document may not be altered or amended without special notification from TTControl GmbH. TTControl GmbH undertakes no further obligation in relation to this document. The software described in it can only be used if the customer is in possession of a general license agreement or single license. The information contained in this document does not affect or change any General Terms and Conditions of TTControl GmbH and/or any agreements existing between TTControl GmbH and the recipient regarding the product or Sample concerned. The reader acknowledges that this document may not be reproduced, stored in a retrieval system, transmitted, changed, or translated, in whole or in part, without the express prior written consent of TTControl GmbH. The reader acknowledges that any and all of the copyrights, trademarks, trade names, **patents (whether registrable or not)** and other intellectual property rights embodied in or in connection with this document are and will remain the sole property of TTControl GmbH or the respective **right holder. Nothing contained** in this legal notice, the document or in any web site of TTControl GmbH shall be construed as conferring to the recipient any license under any intellectual property rights, whether explicit, by estoppel, implication, or otherwise. The product or Sample is only allowed to be used in the scope as **described in this document.**
TTControl GmbH provides this document "as is" and disclaims **all warranties of any kind. The entire** risk, as to quality, use or performance of the document remains with the recipient. All trademarks mentioned in this document belong to their respective owners.

Copyright  2022 TTControl GmbH. All rights reserved.

## Contents

[table_1][{0: 'Table of Contents', 1: '', 2: 'viii', 3: ''}, {0: 'List of Figures', 1: '', 2: 'x', 3: ''}, {0: 'List of Tables', 1: '', 2: 'xi', 3: ''}, {0: '1', 1: 'Introduction', 2: '', 3: '2'}, {0: '1.1', 1: 'Inputs and Outputs', 2: '', 3: '2'}, {0: '1.2', 1: 'Communication Interfaces', 2: '', 3: '2'}, {0: '1.3', 1: 'Safety and Certification', 2: '2', 3: ''}, {0: '1.4', 1: 'Programming Options', 2: '', 3: '3'}, {0: '1.5', 1: 'HY-TTC 500 Variants', 2: '', 3: '3'}, {0: '1.5.1', 1: 'HY-TTC 500 FPGA Variants', 2: '', 3: '3'}, {0: '1.5.2', 1: 'HY-TTC 580 Variant', 2: '', 3: '7'}, {0: '1.5.3', 1: 'HY-TTC 540 Variant', 2: '', 3: '11'}, {0: '1.5.4', 1: 'HY-TTC 520 Variant (Customer-specific variant only)', 2: '', 3: '15'}, {0: '1.5.5', 1: 'HY-TTC 510 Variant', 2: '', 3: '19'}, {0: '1.5.6', 1: 'HY-TTC 590E Variant', 2: '', 3: '23'}, {0: '1.5.7', 1: 'HY-TTC 590 Variant', 2: '', 3: '27'}, {0: '1.5.8', 1: 'HY-TTC 508 Variant', 2: '', 3: '31'}, {0: '1.6', 1: 'Standards and Guidelines', 2: '', 3: '35'}, {0: '1.6.1', 1: 'Electrical Capability', 2: '', 3: '36'}, {0: '1.6.2', 1: 'Mechanical Capability', 2: '', 3: '36'}, {0: '1.6.3', 1: 'Climatic Capability', 2: '', 3: '36'}, {0: '1.6.4', 1: 'Chemical Capability', 2: '', 3: '37'}, {0: '1.6.5', 1: 'Ingress Protection Capability', 2: '', 3: '37'}, {0: '1.6.6', 1: 'ESD and EMC Capability for Road Vehicles', 2: '', 3: '38'}, {0: '1.6.7', 1: 'ESD and EMC Capability for Industrial Applications', 2: '', 3: '38'}, {0: '1.6.8', 1: 'Functional Safety', 2: '', 3: '38'}, {0: '1.7', 1: 'Instructions for Safe Operation', 2: '', 3: '39'}, {0: '1.7.1', 1: 'General', 2: '', 3: '39'}, {0: '1.7.2', 1: 'Checks to be done before commissioning the ECU', 2: '', 3: '40'}, {0: '1.7.3', 1: 'Intended use', 2: '', 3: '40'}, {0: '1.7.4', 1: 'Improper use', 2: '40', 3: ''}, {0: '2', 1: 'Mounting and Label', 2: '', 3: '41'}, {0: '2.1', 1: 'Mounting Requirements', 2: '', 3: '41'}, {0: '2.2', 1: 'Label Information', 2: '', 3: '41'}, {0: '3', 1: 'Pinning and Connector', 2: '', 3: '42'}, {0: '3.1', 1: 'Connector', 2: '42', 3: ''}, {0: '3.2', 1: 'Mating Connector', 2: '', 3: '43'}, {0: '3.2.1', 1: 'KOSTAL Mating Connector', 2: '', 3: '44'}, {0: '3.2.1.1', 1: 'Mating Connector 96-positions', 2: '', 3: '44'}, {0: '3.2.1.2', 1: 'Mating Connector 58-positions', 2: '', 3: '44'}, {0: '3.2.1.3', 1: 'Crimp Contacts', 2: '', 3: '45'}][/table_1]

HY-TTC 500 System Manual V 1.6.0 Contents iii

[table_2][{0: '3.2.1.4', 1: 'Tools', 2: '', 3: '45'}, {0: '3.2.2', 1: 'BOSCH Mating Connector', 2: '', 3: '46'}, {0: '3.2.2.1', 1: 'Mating Connector 96-positions', 2: '', 3: '46'}, {0: '3.2.2.2', 1: 'Mating Connector 58-positions', 2: '', 3: '46'}, {0: '3.2.2.3', 1: 'Crimp Contacts', 2: '', 3: '47'}, {0: '3.2.2.4', 1: 'Tools', 2: '', 3: '47'}, {0: '3.3', 1: 'Cable Harness', 2: '', 3: '48'}, {0: '3.4', 1: 'Fuse', 2: '', 3: '48'}, {0: '3.5', 1: 'HY-TTC 500 Family Pinning', 2: '', 3: '49'}, {0: '3.5.1', 1: 'HY-TTC 580 Variant', 2: '', 3: '50'}, {0: '3.5.2', 1: 'HY-TTC 540 Variant', 2: '', 3: '57'}, {0: '3.5.3', 1: 'HY-TTC 520 Variant (Customer-specific variant only)', 2: '', 3: '64'}, {0: '3.5.4', 1: 'HY-TTC 510 Variant', 2: '', 3: '70'}, {0: '3.5.5', 1: 'HY-TTC 590E Variant', 2: '', 3: '76'}, {0: '3.5.6', 1: 'HY-TTC 590 Variant', 2: '', 3: '83'}, {0: '3.5.7', 1: 'HY-TTC 508 Variant', 2: '', 3: '90'}, {0: '4', 1: 'Specification of Inputs and Outputs', 2: '', 3: '96'}, {0: '4.1', 1: 'BAT+ Power', 2: '96', 3: ''}, {0: '4.1.1', 1: 'Pinout', 2: '', 3: '96'}, {0: '4.1.2', 1: 'Functional Description', 2: '', 3: '96'}, {0: '4.1.3', 1: 'Maximum Ratings', 2: '', 3: '97'}, {0: '4.1.4', 1: 'Characteristics', 2: '', 3: '97'}, {0: '4.2', 1: 'BAT+ CPU', 2: '', 3: '98'}, {0: '4.2.1', 1: 'Pinout', 2: '', 3: '98'}, {0: '4.2.2', 1: 'Functional Description', 2: '', 3: '99'}, {0: '4.2.3', 1: 'Maximum Ratings', 2: '', 3: '100'}, {0: '4.2.4', 1: 'Characteristics', 2: '', 3: '100'}, {0: '4.2.5', 1: 'Low-Voltage Operation', 2: '', 3: '101'}, {0: '4.2.5.1', 1: 'HY-TTC 500 ISO 16750 functional status', 2: '', 3: '103'}, {0: '4.2.6', 1: 'Voltage Monitoring', 2: '', 3: '103'}, {0: '4.3', 1: 'BAT-', 2: '', 3: '104'}, {0: '4.3.1', 1: 'Pinout', 2: '', 3: '104'}, {0: '4.3.2', 1: 'Functional Description', 2: '', 3: '105'}, {0: '4.3.3', 1: 'Maximum Ratings', 2: '', 3: '105'}, {0: '4.4', 1: 'Sensor GND', 2: '', 3: '106'}, {0: '4.4.1', 1: 'Pinout', 2: '', 3: '106'}, {0: '4.4.2', 1: 'Functional Description', 2: '', 3: '107'}, {0: '4.4.3', 1: 'Maximum Ratings', 2: '', 3: '107'}, {0: '4.5', 1: 'Terminal 15', 2: '', 3: '108'}, {0: '4.5.1', 1: 'Pinout', 2: '', 3: '108'}, {0: '4.5.2', 1: 'Functional Description', 2: '', 3: '109'}, {0: '4.5.3', 1: 'Maximum Ratings', 2: '', 3: '109'}, {0: '4.5.4', 1: 'Characteristics', 2: '', 3: '109'}, {0: '4.6', 1: 'Wake-Up', 2: '110', 3: ''}][/table_2]

[table_3][{0: '4.6.1', 1: 'Pinout', 2: '', 3: '110'}, {0: '4.6.2', 1: 'Functional Description', 2: '', 3: '110'}, {0: '4.6.3', 1: 'Maximum Ratings', 2: '', 3: '111'}, {0: '4.6.4', 1: 'Characteristics', 2: '', 3: '111'}, {0: '4.7', 1: 'Sensor Supplies 5 V', 2: '112', 3: ''}, {0: '4.7.1', 1: 'Pinout', 2: '', 3: '112'}, {0: '4.7.2', 1: 'Functional Description', 2: '', 3: '112'}, {0: '4.7.3', 1: 'Maximum Ratings', 2: '', 3: '113'}, {0: '4.7.4', 1: 'Characteristics', 2: '', 3: '113'}, {0: '4.8', 1: 'Sensor Supply Variable', 2: '', 3: '114'}, {0: '4.8.1', 1: 'Pinout', 2: '', 3: '114'}, {0: '4.8.2', 1: 'Functional Description', 2: '', 3: '114'}, {0: '4.8.3', 1: 'Maximum Ratings', 2: '', 3: '115'}, {0: '4.8.4', 1: 'Characteristics', 2: '', 3: '115'}, {0: '4.9', 1: 'Analog Input 3 Modes', 2: '116', 3: ''}, {0: '4.9.1', 1: 'Pinout', 2: '', 3: '116'}, {0: '4.9.2', 1: 'Functional Description', 2: '', 3: '116'}, {0: '4.9.3', 1: 'Maximum Ratings', 2: '', 3: '117'}, {0: '4.9.4', 1: 'Analog Voltage Input', 2: '', 3: '117'}, {0: '4.9.4.1', 1: 'Characteristics of 5 V Input (Ratiometric)', 2: '', 3: '118'}, {0: '4.9.4.2', 1: 'Characteristics of 5 V Input (Absolute)', 2: '', 3: '119'}, {0: '4.9.4.3', 1: 'Characteristics of 5 V Digital Input', 2: '', 3: '119'}, {0: '4.9.5', 1: 'Analog Current Input', 2: '', 3: '120'}, {0: '4.9.5.1', 1: 'Characteristics of Analog Current Input', 2: '', 3: '121'}, {0: '4.9.6', 1: 'Analog Resistance Input', 2: '', 3: '121'}, {0: '4.9.6.1', 1: 'Characteristics of Analog Resistance Input', 2: '', 3: '122'}, {0: '4.10', 1: 'Analog Input 2 Modes', 2: '124', 3: ''}, {0: '4.10.1', 1: 'Pinout', 2: '', 3: '124'}, {0: '4.10.2', 1: 'Functional Description', 2: '', 3: '125'}, {0: '4.10.3', 1: 'Maximum Ratings', 2: '', 3: '125'}, {0: '4.10.4', 1: 'Analog Voltage Input', 2: '', 3: '126'}, {0: '4.10.4.1', 1: 'Characteristics of 5 V Input (Ratiometric)', 2: '', 3: '126'}, {0: '4.10.4.2', 1: 'Characteristics of 5 V Input (Absolute)', 2: '', 3: '126'}, {0: '4.10.4.3', 1: 'Characteristics of 10 V Input (Absolute)', 2: '', 3: '127'}, {0: '4.10.4.4', 1: 'Characteristics of 32 V Input (Absolute)', 2: '', 3: '127'}, {0: '4.10.4.5', 1: 'Characteristics of 32 V Digital Input', 2: '', 3: '128'}, {0: '4.10.5', 1: 'Analog Current Input', 2: '', 3: '129'}, {0: '4.10.5.1', 1: 'Characteristics of Analog Current Input', 2: '', 3: '129'}, {0: '4.11', 1: 'Timer Inputs', 2: '', 3: '130'}, {0: '4.11.1', 1: 'Pinout', 2: '', 3: '130'}, {0: '4.11.2', 1: 'Functional Description', 2: '', 3: '131'}, {0: '4.11.3', 1: 'Maximum Ratings', 2: '', 3: '131'}, {0: '4.11.4', 1: 'Timer and Current Loop Inputs', 2: '', 3: '134'}, {0: '4.11.4.1', 1: 'Characteristics of Timer Input', 2: '', 3: '134'}][/table_3]

HY-TTC 500 System Manual V 1.6.0 Contents v

[table_4][{0: '4.11.4.2', 1: 'Characteristics of Current Loop Input', 2: '', 3: '134'}, {0: '4.11.5', 1: 'Analog and Digital Inputs', 2: '', 3: '136'}, {0: '4.11.5.1', 1: 'Characteristics of Analog Voltage Input', 2: '', 3: '136'}, {0: '4.11.5.2', 1: 'Characteristics of Digital Input', 2: '', 3: '136'}, {0: '4.12', 1: 'High-Side PWM Outputs', 2: '', 3: '137'}, {0: '4.12.1', 1: 'Pinout', 2: '', 3: '137'}, {0: '4.12.2', 1: 'Functional Description', 2: '', 3: '138'}, {0: '4.12.2.1', 1: 'Power Stage Pairing', 2: '', 3: '140'}, {0: '4.12.2.2', 1: 'Mutual Exclusive Mode', 2: '', 3: '140'}, {0: '4.12.3', 1: 'Maximum Ratings', 2: '', 3: '140'}, {0: '4.12.4', 1: 'High-Side PWM Outputs', 2: '', 3: '141'}, {0: '4.12.4.1', 1: 'Characteristics of High-Side PWM Output', 2: '', 3: '141'}, {0: '4.12.4.2', 1: 'Diagnostic Functions', 2: '', 3: '141'}, {0: '4.12.4.3', 1: 'Current Measurement', 2: '', 3: '142'}, {0: '4.12.5', 1: 'High-Side Digital Outputs', 2: '', 3: '144'}, {0: '4.12.5.1', 1: 'Characteristics of High-Side Digital Output', 2: '', 3: '144'}, {0: '4.12.6', 1: 'Digital and Frequency Inputs', 2: '', 3: '144'}, {0: '4.12.6.1', 1: 'Characteristics of Digital Input', 2: '', 3: '145'}, {0: '4.12.6.2', 1: 'Characteristics of Timer Input', 2: '', 3: '145'}, {0: '4.12.7', 1: 'Secondary Shut-off Paths', 2: '', 3: '146'}, {0: '4.12.8', 1: 'External Shut-off Groups', 2: '', 3: '147'}, {0: '4.12.8.1', 1: 'Characteristics of External Shut-off', 2: '147', 3: ''}, {0: '4.12.9', 1: 'Tertiary Shut-off Path', 2: '148', 3: ''}, {0: '4.12.9.1', 1: 'Functional description', 2: '', 3: '148'}, {0: '4.13', 1: 'High-Side Digital Outputs', 2: '', 3: '149'}, {0: '4.13.1', 1: 'Pinout', 2: '', 3: '149'}, {0: '4.13.2', 1: 'Functional Description', 2: '', 3: '150'}, {0: '4.13.2.1', 1: 'Power Stage Pairing', 2: '', 3: '151'}, {0: '4.13.2.2', 1: 'Mutual Exclusive Mode', 2: '', 3: '151'}, {0: '4.13.3', 1: 'Diagnostic Functions', 2: '151', 3: ''}, {0: '4.13.4', 1: 'Maximum Ratings', 2: '', 3: '151'}, {0: '4.13.5', 1: 'High-Side Digital Outputs', 2: '', 3: '152'}, {0: '4.13.5.1', 1: 'Characteristics of High-Side Output', 2: '', 3: '152'}, {0: '4.13.6', 1: 'Analog and Digital Inputs', 2: '', 3: '153'}, {0: '4.13.6.1', 1: 'Characteristics of Analog Voltage Input', 2: '', 3: '153'}, {0: '4.13.6.2', 1: 'Characteristics of Digital Input', 2: '', 3: '153'}, {0: '4.14', 1: 'High-Side Digital/PVG/VOUT Outputs', 2: '', 3: '155'}, {0: '4.14.1', 1: 'Pinout', 2: '', 3: '155'}, {0: '4.14.2', 1: 'Functional Description', 2: '', 3: '156'}, {0: '4.14.2.1', 1: 'Power Stage Pairing', 2: '', 3: '156'}, {0: '4.14.2.2', 1: 'Mutual Exclusive Mode', 2: '', 3: '156'}, {0: '4.14.3', 1: 'Maximum Ratings', 2: '', 3: '156'}, {0: '4.14.4', 1: 'High-Side Digital Outputs', 2: '', 3: '157'}, {0: '4.14.4.1', 1: 'Diagnostic Functions', 2: '', 3: '158'}][/table_4]

[table_5][{0: '4.14.4.2', 1: 'Characteristics of High-Side Digital', 2: '158', 3: ''}, {0: '4.14.5', 1: 'PVG Outputs', 2: '', 3: '159'}, {0: '4.14.5.1', 1: 'Characteristics of PVG', 2: '', 3: '160'}, {0: '4.14.6', 1: 'VOUT Outputs', 2: '', 3: '161'}, {0: '4.14.6.1', 1: 'Characteristics of VOUT', 2: '', 3: '162'}, {0: '4.14.7', 1: 'Analog and Digital Inputs', 2: '', 3: '163'}, {0: '4.14.7.1', 1: 'Characteristics of Analog Voltage Input', 2: '', 3: '163'}, {0: '4.14.7.2', 1: 'Characteristics of Digital Input', 2: '', 3: '163'}, {0: '4.15', 1: 'Low-Side Digital Outputs', 2: '', 3: '165'}, {0: '4.15.1', 1: 'Pinout', 2: '', 3: '165'}, {0: '4.15.2', 1: 'Functional Description', 2: '', 3: '166'}, {0: '4.15.2.1', 1: 'Power Stage Pairing', 2: '', 3: '167'}, {0: '4.15.3', 1: 'Diagnostic Functions', 2: '167', 3: ''}, {0: '4.15.4', 1: 'Maximum Ratings', 2: '', 3: '167'}, {0: '4.15.5', 1: 'Characteristics of Low-Side Digital Output', 2: '', 3: '168'}, {0: '4.15.6', 1: 'Analog and Digital Inputs', 2: '', 3: '169'}, {0: '4.15.6.1', 1: 'Characteristics of Analog Voltage Input', 2: '', 3: '169'}, {0: '4.15.6.2', 1: 'Characteristics of Digital Input', 2: '', 3: '169'}, {0: '4.16', 1: 'LIN', 2: '', 3: '170'}, {0: '4.16.1', 1: 'Pinout', 2: '', 3: '170'}, {0: '4.16.2', 1: 'Functional Description', 2: '', 3: '171'}, {0: '4.16.3', 1: 'Maximum Ratings', 2: '', 3: '172'}, {0: '4.16.4', 1: 'Characteristics', 2: '', 3: '172'}, {0: '4.17', 1: 'RS232', 2: '', 3: '173'}, {0: '4.17.1', 1: 'Pinout', 2: '', 3: '173'}, {0: '4.17.2', 1: 'Functional Description', 2: '', 3: '174'}, {0: '4.17.3', 1: 'Maximum Ratings', 2: '', 3: '174'}, {0: '4.17.4', 1: 'Characteristics', 2: '', 3: '174'}, {0: '4.18', 1: 'CAN', 2: '', 3: '175'}, {0: '4.18.1', 1: 'Pinout', 2: '', 3: '175'}, {0: '4.18.2', 1: 'Functional Description', 2: '', 3: '176'}, {0: '4.18.2.1', 1: 'CAN1 on HY-TTC 590E, HY-TTC 590, and HY-TTC 508', 2: '. . .', 3: '176'}, {0: '4.18.3', 1: 'Maximum Ratings', 2: '', 3: '178'}, {0: '4.18.4', 1: 'Characteristics', 2: '', 3: '178'}, {0: '4.19', 1: 'CAN Termination', 2: '179', 3: ''}, {0: '4.19.1', 1: 'Pinout', 2: '', 3: '179'}, {0: '4.19.2', 1: 'Functional Description', 2: '', 3: '180'}, {0: '4.20', 1: 'Ethernet', 2: '', 3: '181'}, {0: '4.20.1', 1: 'Pinout', 2: '', 3: '181'}, {0: '4.20.2', 1: 'Functional Description', 2: '', 3: '182'}, {0: '4.20.3', 1: 'Maximum Ratings', 2: '', 3: '182'}, {0: '4.21', 1: 'BroadR-Reach®', 2: '', 3: '183'}, {0: '4.21.1', 1: 'Pinout', 2: '', 3: '183'}, {0: '4.21.2', 1: 'Functional Description', 2: '', 3: '183'}][/table_5]

HY-TTC 500 System Manual V 1.6.0 Contents vii

[table_6][{0: '4.21.3', 1: 'Maximum Ratings', 2: '', 3: '184'}, {0: '4.21.4', 1: 'Characteristics', 2: '', 3: '184'}, {0: '4.22', 1: 'Real-Time Clock (RTC)', 2: '', 3: '185'}, {0: '4.22.1', 1: 'Pinout', 2: '', 3: '185'}, {0: '4.22.2', 1: 'Functional Description', 2: '', 3: '186'}, {0: '4.22.3', 1: 'Maximum Ratings', 2: '', 3: '187'}, {0: '4.22.4', 1: 'Characteristics', 2: '', 3: '187'}, {0: '5', 1: 'Internal Structure', 2: '', 3: '188'}, {0: '5.1', 1: 'Safety Concept', 2: '', 3: '188'}, {0: '5.1.1', 1: 'Overview Safety Concept', 2: '', 3: '188'}, {0: '5.2', 1: 'Thermal Management', 2: '', 3: '190'}, {0: '5.2.1', 1: 'Board Temperature Sensor', 2: '', 3: '190'}, {0: '5.2.1.1', 1: 'Pinout', 2: '', 3: '190'}, {0: '5.2.1.2', 1: 'Functional Description', 2: '', 3: '190'}, {0: '5.2.2', 1: 'Characteristics', 2: '', 3: '191'}, {0: '6', 1: 'Application Notes', 2: '', 3: '192'}, {0: '6.1', 1: 'Cable Harness', 2: '', 3: '192'}, {0: '6.2', 1: 'Handling of High-Load Current', 2: '', 3: '193'}, {0: '6.2.1', 1: 'Load Distribution', 2: '', 3: '193'}, {0: '6.2.2', 1: 'Total Load Current', 2: '', 3: '193'}, {0: '6.2.2.1', 1: 'Calculation of the battery supply current', 2: '', 3: '194'}, {0: '6.3', 1: 'Inductive Loads', 2: '', 3: '195'}, {0: '6.3.1', 1: 'Inductive Loads at PWM Outputs', 2: '195', 3: ''}, {0: '6.3.2', 1: 'Inductive Loads at Low Side Switches', 2: '', 3: '195'}, {0: '6.4', 1: 'Ground Connection of Housing', 2: '', 3: '195'}, {0: '6.5', 1: 'Motor Control', 2: '196', 3: ''}, {0: '6.5.1', 1: 'Motor Types supported', 2: '', 3: '196'}, {0: '6.5.2', 1: 'Direct Control Options', 2: '', 3: '196'}, {0: '6.5.2.1', 1: 'Depending on Direction', 2: '', 3: '196'}, {0: '6.5.2.2', 1: 'Depending on Single Motor / Motor Group', 2: '196', 3: ''}, {0: '6.5.2.3', 1: 'Depending on Control', 2: '', 3: '196'}, {0: '6.5.2.4', 1: 'Depending on stalled Motor Current', 2: '', 3: '196'}, {0: '6.5.3', 1: 'Motor Details', 2: '197', 3: ''}, {0: '6.5.3.1', 1: 'Start Current', 2: '', 3: '197'}, {0: '6.5.3.2', 1: 'Start Current at low Temperatures', 2: '', 3: '197'}, {0: '6.5.3.3', 1: 'Battery Voltage Impact', 2: '', 3: '197'}, {0: '6.5.3.4', 1: 'Motors with Limit Switch', 2: '', 3: '197'}, {0: '6.5.3.5', 1: 'Motors with Electronics Inside', 2: '198', 3: ''}, {0: '6.5.3.6', 1: 'Unidirectional Motor Drive', 2: '', 3: '198'}, {0: '6.5.3.7', 1: 'Bidirectional Motor Drive', 2: '', 3: '198'}, {0: '6.5.3.8', 1: 'Active Motor Brake', 2: '', 3: '198'}, {0: '6.5.3.9', 1: 'Motors Reversing with / without Braking', 2: '198', 3: ''}, {0: '6.5.3.10', 1: 'PWM Operation / steady State Control', 2: '', 3: '198'}][/table_6]

[table_7][{0: '6.5.3.11', 1: 'Maximum Average Current (PWM and Digital Power Stages) 199', 2: '', 3: ''}, {0: '6.5.3.12', 1: 'Peak Current Bidirectional Drive (Digital Power Stages only) 199', 2: '', 3: ''}, {0: '6.5.3.13', 1: 'Peak Current Unidirectional Drive (Digital Power Stages only)', 2: '199', 3: ''}, {0: '6.5.4', 1: 'Motor Classification', 2: '', 3: '200'}, {0: '6.5.4.1', 1: 'Independent from Speed Class', 2: '', 3: '200'}, {0: '6.5.4.2', 1: 'Fast Accelerating Motors only', 2: '', 3: '203'}, {0: '6.5.5', 1: 'Connection', 2: '', 3: '208'}, {0: '6.5.5.1', 1: 'Unidirectional Single Power Stage', 2: '', 3: '208'}, {0: '6.5.5.2', 1: 'Unidirectional Double Power Stage', 2: '', 3: '210'}, {0: '6.5.5.3', 1: 'Bidirectional H-bridge (Single Power Stages)', 2: '', 3: '211'}, {0: '6.5.5.4', 1: 'Bidirectional H-bridge (Multiple Low Side Power Stages)', 2: '.', 3: '212'}, {0: '6.5.5.5', 1: 'Bidirectional H-bridge (Multiple High and Low Side Power Stages)', 2: '213', 3: ''}, {0: '6.5.5.6', 1: 'Motor Cluster', 2: '', 3: '214'}, {0: '6.5.6', 1: 'Power Stages for Motor Control', 2: '', 3: '215'}, {0: '6.5.6.1', 1: 'High Side Power Stages for PWM Operation', 2: '', 3: '215'}, {0: '6.5.6.2', 1: 'High Side Power Stages for Static Operation', 2: '', 3: '215'}, {0: '6.5.6.3', 1: 'Low Side Power Stages', 2: '', 3: '215'}, {0: '6.5.7', 1: 'Parallel Operation of Power Stages', 2: '', 3: '216'}, {0: '6.5.8', 1: 'Cabling', 2: '', 3: '216'}, {0: '6.5.9', 1: 'Control Sequence for Bidirectional Drive', 2: '', 3: '216'}, {0: '6.5.9.1', 1: 'Motor Running', 2: '', 3: '217'}, {0: '6.5.9.2', 1: 'Motor Breaking', 2: '', 3: '217'}, {0: '6.5.9.3', 1: 'Paralleled High Side Power Stage Control', 2: '', 3: '217'}, {0: '6.6', 1: 'Power Stage Alternative Functions', 2: '', 3: '218'}, {0: '6.6.1', 1: 'High-Side Output Stages', 2: '', 3: '218'}, {0: '6.6.1.1', 1: 'Wiring examples', 2: '', 3: '218'}, {0: '7', 1: 'Debugging', 2: '', 3: '224'}, {0: '7.1', 1: 'Functional Description', 2: '', 3: '224'}, {0: '8', 1: 'API Documentation', 2: '', 3: '226'}, {0: 'Glossary', 1: '227', 2: '', 3: ''}, {0: 'References', 1: '', 2: '229', 3: ''}, {0: 'Index', 1: '', 2: '231', 3: ''}, {0: 'Disposal', 1: '', 2: '234', 3: ''}, {0: 'Legal Disclaimer', 1: '', 2: '235', 3: ''}][/table_7]

## List Of Figures

[table_8][{0: '1', 1: 'HY-TTC 580 Variant', 2: '', 3: '7'}, {0: '2', 1: 'HY-TTC 540 Variant', 2: '', 3: '11'}, {0: '3', 1: 'HY-TTC 520 Variant', 2: '', 3: '15'}, {0: '4', 1: 'HY-TTC 510 Variant', 2: '', 3: '19'}, {0: '5', 1: 'HY-TTC 590E Variant', 2: '', 3: '23'}, {0: '6', 1: 'HY-TTC 590 Variant', 2: '', 3: '27'}, {0: '7', 1: 'HY-TTC 508 Variant', 2: '', 3: '31'}, {0: '8', 1: 'ISO 16750-1:2006 [13], Figure 1 - Code allocation', 2: '', 3: '35'}, {0: '9', 1: 'ECU label with Version field', 2: '', 3: '39'}, {0: '10', 1: 'Main connector', 2: '', 3: '42'}, {0: '11', 1: '58 terminal plug housing set', 2: '', 3: '43'}, {0: '12', 1: '96 terminal plug housing set', 2: '', 3: '43'}, {0: '13', 1: 'Battery Supply - Fuse', 2: '', 3: '48'}, {0: '14', 1: 'Pinout of BAT+ Power', 2: '', 3: '96'}, {0: '15', 1: 'Pinout of BAT+ CPU', 2: '98', 3: ''}, {0: '16', 1: 'Supply pin for the internal ECU logic', 2: '', 3: '99'}, {0: '17', 1: 'ISO 16750-2, Figure 7 - Starting profile', 2: '102', 3: ''}, {0: '18', 1: 'Pinout of BAT-', 2: '', 3: '104'}, {0: '19', 1: 'Pinout of sensor GND', 2: '', 3: '106'}, {0: '20', 1: 'Pinout of terminal 15', 2: '', 3: '108'}, {0: '21', 1: 'Pinout of Wake-Up', 2: '', 3: '110'}, {0: '22', 1: 'Pinout of sensor supply 5 V', 2: '', 3: '112'}, {0: '23', 1: 'Sensor supply 5 V', 2: '', 3: '113'}, {0: '24', 1: 'Pinout of sensor supply variable', 2: '', 3: '114'}, {0: '25', 1: 'Sensor supply variable', 2: '', 3: '115'}, {0: '26', 1: 'Pinout of analog input 3 mode', 2: '', 3: '116'}, {0: '27', 1: 'Analog voltage input (ratiometric)', 2: '', 3: '117'}, {0: '28', 1: 'Analog voltage input', 2: '118', 3: ''}, {0: '29', 1: 'Analog current input', 2: '', 3: '120'}, {0: '30', 1: 'Analog resistance input', 2: '', 3: '121'}, {0: '31', 1: 'Namur type sensor (only for switches to ground)', 2: '', 3: '122'}, {0: '32', 1: 'Switch input (only for switches to ground)', 2: '', 3: '122'}, {0: '33', 1: 'Pinout of analog input 2 mode', 2: '', 3: '124'}, {0: '34', 1: 'Pinout of timer input', 2: '', 3: '130'}, {0: '35', 1: 'Digital input for frequency/timing measurement with NPN-type 2-pole sensor', 2: '', 3: '131'}, {0: '36', 1: 'Digital input for frequency/timing measurement with PNP-type 2-pole sensor', 2: '', 3: '132'}, {0: '37', 1: 'Digital input pair for encoder and direction', 2: '', 3: '132'}, {0: '38', 1: 'Digital input for switch connected to (battery) supply voltage', 2: '', 3: '133'}, {0: '39', 1: 'Digital input for switch connected to ground', 2: '133', 3: ''}, {0: '40', 1: 'Digital input for frequency measurement with ABS-type 7/14 mA, 2 pole sensor', 2: '. . .', 3: '135'}, {0: '41', 1: 'Pinout of high-side PWM outputs', 2: '', 3: '137'}][/table_8]

[table_9][{0: '42', 1: 'High-side output stage with PWM functionality', 2: '', 3: '139'}, {0: '43', 1: 'Distribution of PWM output stages to shut-off groups/paths', 2: '', 3: '146'}, {0: '44', 1: 'Tertiary Shut-off Path', 2: '', 3: '148'}, {0: '45', 1: 'Pinout of high-side digital outputs', 2: '', 3: '149'}, {0: '46', 1: 'Digital high-side power stage', 2: '', 3: '150'}, {0: '47', 1: 'Pinout of High-side digital/PVG/VOUT outputs', 2: '', 3: '155'}, {0: '48', 1: 'Digital high-side power stage', 2: '', 3: '157'}, {0: '49', 1: 'Output stage in PVG mode', 2: '', 3: '159'}, {0: '50', 1: 'Output stage in VOUT mode', 2: '', 3: '161'}, {0: '51', 1: 'Pinout of low-side digital outputs', 2: '', 3: '165'}, {0: '52', 1: 'Low-side switch for resistive and inductive loads', 2: '', 3: '166'}, {0: '53', 1: 'LIN pinout', 2: '', 3: '170'}, {0: '54', 1: 'LIN interface', 2: '', 3: '171'}, {0: '55', 1: 'RS232 pinout', 2: '', 3: '173'}, {0: '56', 1: 'RS232 interface', 2: '', 3: '174'}, {0: '57', 1: 'CAN pinout', 2: '', 3: '175'}, {0: '58', 1: 'CAN interface', 2: '', 3: '177'}, {0: '59', 1: 'Pinout of CAN termination', 2: '', 3: '179'}, {0: '60', 1: 'Optional CAN termination', 2: '', 3: '180'}, {0: '61', 1: 'Ethernet pinout', 2: '', 3: '181'}, {0: '62', 1: 'Ethernet interface', 2: '', 3: '182'}, {0: '63', 1: '100BASE-T1 Ethernet pinout', 2: '', 3: '183'}, {0: '64', 1: 'RTC pinout', 2: '', 3: '185'}, {0: '65', 1: 'Voltage supply of real-time clock', 2: '', 3: '186'}, {0: '66', 1: 'Overview safety concept HY-TTC 500', 2: '', 3: '189'}, {0: '67', 1: 'Unidirectional Single Power Stage', 2: '', 3: '208'}, {0: '68', 1: 'Unidirectional Single Power Stage', 2: '', 3: '209'}, {0: '69', 1: 'Unidirectional Double Power Stage', 2: '', 3: '210'}, {0: '70', 1: 'Bidirectional H-bridge (Single Power Stages)', 2: '', 3: '211'}, {0: '71', 1: 'Bidirectional H-bridge (Multiple Low Side Power Stages)', 2: '', 3: '212'}, {0: '72', 1: 'Bidirectional H-bridge (Multiple High and Low Side Power Stages)', 2: '213', 3: ''}, {0: '73', 1: 'Motor Cluster (Example: Outside Mirror Control)', 2: '', 3: '214'}, {0: '74', 1: 'Switch connected to GND', 2: '', 3: '219'}, {0: '75', 1: 'Switch connected to GND', 2: '', 3: '219'}, {0: '76', 1: 'Switch connected to GND', 2: '', 3: '220'}, {0: '77', 1: 'Switch connected to PWM high-side output stage', 2: '', 3: '220'}, {0: '78', 1: 'Switch connected to PWM high-side output stage', 2: '', 3: '221'}, {0: '79', 1: 'Switch connected to PWM high-side output stage', 2: '', 3: '221'}, {0: '80', 1: 'Switch connected to digital high-side output stage', 2: '', 3: '222'}, {0: '81', 1: 'Switch connected to battery supply', 2: '', 3: '223'}, {0: '82', 1: 'Switch connected to battery supply', 2: '', 3: '223'}, {0: '83', 1: 'Pinning of JTAG Connector on the TTC JTAG-Adapter Board', 2: '224', 3: ''}][/table_9]

## List Of Tables

[table_10][{0: '1', 1: 'Variants overview for the Spartan-6 XA6SLX16 FPGA', 2: '', 3: '4'}, {0: '2', 1: 'Variants overview for the Spartan-6 XA6SLX9 FPGA', 2: '', 3: '5'}, {0: '3', 1: 'Variants overview for the Spartan-6 XA6SLX25 FPGA', 2: '', 3: '6'}, {0: '4', 1: 'List of chemical agents', 2: '', 3: '37'}, {0: '5', 1: 'KOSTAL / HERTH+BUSS part numbers', 2: '44', 3: ''}, {0: '6', 1: 'KOSTAL / HERTH+BUSS part numbers', 2: '44', 3: ''}, {0: '7', 1: 'KOSTAL / HERTH+BUSS part numbers', 2: '45', 3: ''}, {0: '8', 1: 'KOSTAL / HERTH+BUSS part numbers', 2: '45', 3: ''}, {0: '9', 1: 'BOSCH part numbers', 2: '', 3: '46'}, {0: '10', 1: 'BOSCH part numbers', 2: '', 3: '46'}, {0: '11', 1: 'BOSCH crimp contacts part numbers', 2: '', 3: '47'}, {0: '12', 1: 'BOSCH Tools part numbers', 2: '', 3: '47'}, {0: '13', 1: 'Pinning of HY-TTC 580', 2: '', 3: '56'}, {0: '14', 1: 'Pinning of HY-TTC 540', 2: '', 3: '63'}, {0: '15', 1: 'Pinning of HY-TTC 520', 2: '', 3: '69'}, {0: '16', 1: 'Pinning of HY-TTC 510', 2: '', 3: '75'}, {0: '17', 1: 'Pinning of HY-TTC 590E', 2: '', 3: '82'}, {0: '18', 1: 'Pinning of HY-TTC 590', 2: '', 3: '89'}, {0: '19', 1: 'Pinning of HY-TTC 508', 2: '', 3: '95'}, {0: '20', 1: 'ISO 16750 functional status for 12 V systems', 2: '', 3: '103'}, {0: '21', 1: 'ISO 16750 functional status for 24 V systems', 2: '', 3: '103'}, {0: '23', 1: 'Total Load Current Iin-total', 2: '', 3: '193'}, {0: '32', 1: 'Order code of JTAG connector on the TTC JTAG-Adapter Board', 2: '', 3: '224'}][/table_10]

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

[table_11][{0: 'Feature', 1: 'HY-TTC 580', 2: 'HY-TTC 540', 3: 'HY-TTC 520', 4: 'HY-TTC 510', 5: 'HY-TTC 590E', 6: 'HY-TTC 590', 7: 'HY-TTC 508', 8: ''}, {0: 'CPU', 1: '32-bit TI TMS570', 2: 'x', 3: 'x', 4: 'x', 5: 'x', 6: 'x', 7: 'x', 8: 'x'}, {0: 'Int. FLASH', 1: '3 MB', 2: '3 MB', 3: '3 MB', 4: '3 MB', 5: '3 MB', 6: '3 MB', 7: '3 MB', 8: ''}, {0: 'Int. RAM', 1: '256 kB', 2: '256 kB', 3: '256 kB', 4: '256 kB', 5: '256 kB', 6: '256 kB', 7: '256 kB', 8: ''}, {0: 'Memory', 1: 'Ext. FLASH', 2: '8 MB', 3: '-', 4: '-', 5: '-', 6: '64 MB', 7: '32 MB', 8: '16 MB'}, {0: 'Ext. RAM', 1: '2 MB', 2: '2 MB', 3: '2 MB', 4: '2 MB', 5: '2 MB', 6: '2 MB', 7: '2 MB', 8: ''}, {0: 'Ext. EEPROM', 1: '64 kB', 2: '64 kB', 3: '64 kB', 4: '64 kB', 5: '-', 6: '-', 7: '64 kB', 8: ''}, {0: 'Ext. FRAM', 1: '-', 2: '-', 3: '-', 4: '-', 5: '32 kB', 6: '32 kB', 7: '-', 8: ''}, {0: 'Interface', 1: 'CAN', 2: '7', 3: '4', 4: '4', 5: '3', 6: '7', 7: '7', 8: '3'}, {0: 'CAN1 is ISOBUS Compliance', 1: '-', 2: '-', 3: '-', 4: '-', 5: 'x', 6: 'x', 7: 'x', 8: ''}, {0: 'CAN bus termination', 1: '4', 2: '4', 3: '4', 4: '3', 5: '4', 6: '4', 7: '3', 8: ''}, {0: 'Ethernet', 1: '1', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: ''}, {0: '100BASE-T1 Ethernet', 1: '-', 2: '-', 3: '-', 4: '-', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'LIN', 1: '1', 2: '-', 3: '-', 4: '1', 5: '1', 6: '1', 7: '-', 8: ''}, {0: 'RS232', 1: '1', 2: '-', 3: '-', 4: '-', 5: '1', 6: '1', 7: '-', 8: ''}, {0: 'Real time clock', 1: '1', 2: '-', 3: '-', 4: '-', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'Outputs', 1: 'High-Side PWM with CM', 2: '36', 3: '28', 4: '18', 5: '16', 6: '36', 7: '36', 8: '10'}, {0: 'High-Side digital', 1: '8', 2: '8', 3: '8', 4: '8', 5: '8', 6: '8', 7: '8', 8: ''}, {0: 'High-Side digital, PVG, VOUT', 1: '8', 2: '-', 3: '-', 4: '8', 5: '8', 6: '8', 7: '6', 8: ''}, {0: 'Low-Side digital', 1: '8', 2: '8', 3: '8', 4: '8', 5: '8', 6: '8', 7: '8', 8: ''}, {0: 'Inputs Analog input 3 modes (V)(I)(R)', 1: '8', 2: '8', 3: '8', 4: '8', 5: '8', 6: '8', 7: '8', 8: ''}, {0: 'Analog input 2 modes (V)(I)', 1: '16', 2: '16', 3: '16', 4: '16', 5: '16', 6: '16', 7: '16', 8: ''}, {0: 'Analog input (V)', 1: '-', 2: '8', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: ''}, {0: 'Timer input', 1: '12', 2: '20', 3: '20', 4: '20', 5: '12', 6: '12', 7: '20', 8: ''}, {0: 'Terminal 15', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'Wake-Up', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'Sensor supply', 1: '+5V/500mA', 2: '2', 3: '2', 4: '2', 5: '2', 6: '2', 7: '2', 8: '1'}, {0: '+5-10V/2.5W', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '-', 8: ''}, {0: 'Safety Switch Nr. of secondary shut-off path', 1: '3', 2: '2', 3: '2', 4: '2', 5: '3', 6: '3', 7: '2', 8: ''}, {0: 'Table 1: Variants overview for the Spartan-6 XA6SLX16 FPGA', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}][/table_11]

[table_12][{0: 'Feature', 1: 'HY-TTC 580', 2: 'HY-TTC 540', 3: 'HY-TTC 520', 4: 'HY-TTC 510', 5: 'HY-TTC 590E', 6: 'HY-TTC 590', 7: 'HY-TTC 508', 8: ''}, {0: 'CPU', 1: '32-bit TI TMS570', 2: 'x', 3: 'x', 4: 'x', 5: 'x', 6: 'x', 7: 'x', 8: 'x'}, {0: 'Int. FLASH', 1: '3 MB', 2: '3 MB', 3: '3 MB', 4: '3 MB', 5: '3 MB', 6: '3 MB', 7: '3 MB', 8: ''}, {0: 'Int. RAM', 1: '256 kB', 2: '256 kB', 3: '256 kB', 4: '256 kB', 5: '256 kB', 6: '256 kB', 7: '256 kB', 8: ''}, {0: 'Memory', 1: 'Ext. FLASH', 2: '8 MB', 3: '-', 4: '-', 5: '-', 6: '64 MB', 7: '32 MB', 8: '16 MB'}, {0: 'Ext. RAM', 1: '2 MB', 2: '2 MB', 3: '2 MB', 4: '2 MB', 5: '2 MB', 6: '2 MB', 7: '2 MB', 8: ''}, {0: 'Ext. EEPROM', 1: '64 kB', 2: '64 kB', 3: '64 kB', 4: '64 kB', 5: '-', 6: '-', 7: '64 kB', 8: ''}, {0: 'Ext. FRAM', 1: '-', 2: '-', 3: '-', 4: '-', 5: '32 kB', 6: '32 kB', 7: '-', 8: ''}, {0: 'Interface', 1: 'CAN', 2: '4', 3: '4', 4: '4', 5: '3', 6: '4', 7: '4', 8: '3'}, {0: 'CAN1 is ISOBUS Compliance', 1: '-', 2: '-', 3: '-', 4: '-', 5: 'x', 6: 'x', 7: 'x', 8: ''}, {0: 'CAN bus termination', 1: '4', 2: '4', 3: '4', 4: '3', 5: '4', 6: '4', 7: '3', 8: ''}, {0: 'Ethernet', 1: '1', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: ''}, {0: '100BASE-T1 Ethernet', 1: '-', 2: '-', 3: '-', 4: '-', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'LIN', 1: '1', 2: '-', 3: '-', 4: '1', 5: '1', 6: '1', 7: '-', 8: ''}, {0: 'RS232', 1: '1', 2: '-', 3: '-', 4: '-', 5: '1', 6: '1', 7: '-', 8: ''}, {0: 'Real time clock', 1: '1', 2: '-', 3: '-', 4: '-', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'Outputs', 1: 'High-Side PWM with CM', 2: '36', 3: '28', 4: '18', 5: '16', 6: '36', 7: '36', 8: '10'}, {0: 'High-Side digital', 1: '16', 2: '8', 3: '8', 4: '8', 5: '16', 6: '16', 7: '8', 8: ''}, {0: 'High-Side digital, PVG, VOUT', 1: '0', 2: '-', 3: '-', 4: '8', 5: '0', 6: '0', 7: '6', 8: ''}, {0: 'Low-Side digital', 1: '8', 2: '8', 3: '8', 4: '8', 5: '8', 6: '8', 7: '8', 8: ''}, {0: 'Inputs Analog input 3 modes (V)(I)(R)', 1: '8', 2: '8', 3: '8', 4: '8', 5: '8', 6: '8', 7: '8', 8: ''}, {0: 'Analog input 2 modes (V)(I)', 1: '16', 2: '16', 3: '16', 4: '16', 5: '16', 6: '16', 7: '16', 8: ''}, {0: 'Analog input (V)', 1: '-', 2: '8', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: ''}, {0: 'Timer input', 1: '12', 2: '20', 3: '20', 4: '20', 5: '12', 6: '12', 7: '20', 8: ''}, {0: 'Terminal 15', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'Wake-Up', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '1', 8: ''}, {0: 'Sensor supply', 1: '+5V/500mA', 2: '2', 3: '2', 4: '2', 5: '2', 6: '2', 7: '2', 8: '1'}, {0: '+5-10V/2.5W', 1: '1', 2: '1', 3: '1', 4: '1', 5: '1', 6: '1', 7: '-', 8: ''}, {0: 'Safety Switch Nr. of secondary shut-off path', 1: '3', 2: '2', 3: '2', 4: '2', 5: '3', 6: '3', 7: '2', 8: ''}, {0: 'Table 2: Variants overview for the Spartan-6 XA6SLX9 FPGA', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}][/table_12]

[table_13][{0: 'Feature', 1: 'HY-TTC 580', 2: 'HY-TTC 590E', 3: 'HY-TTC 590', 4: ''}, {0: 'CPU', 1: '32-bit TI TMS570', 2: 'x', 3: 'x', 4: 'x'}, {0: 'Int. FLASH', 1: '3 MB', 2: '3 MB', 3: '3 MB', 4: ''}, {0: 'Int. RAM', 1: '256 kB', 2: '256 kB', 3: '256 kB', 4: ''}, {0: 'Memory', 1: 'Ext. FLASH', 2: '8 MB', 3: '64 MB', 4: '32 MB'}, {0: 'Ext. RAM', 1: '2 MB', 2: '2 MB', 3: '2 MB', 4: ''}, {0: 'Ext. EEPROM', 1: '64 kB', 2: '-', 3: '-', 4: ''}, {0: 'Ext. FRAM', 1: '-', 2: '32 kB', 3: '32 kB', 4: ''}, {0: 'Interface', 1: 'CAN', 2: '7', 3: '7', 4: '7'}, {0: 'CAN1 is ISOBUS Compliance', 1: '-', 2: 'x', 3: 'x', 4: ''}, {0: 'CAN bus termination', 1: '7', 2: '7', 3: '7', 4: ''}, {0: 'Ethernet', 1: '1', 2: '-', 3: '-', 4: ''}, {0: '100BASE-T1 Ethernet', 1: '-', 2: '1', 3: '1', 4: ''}, {0: 'LIN', 1: '1', 2: '1', 3: '1', 4: ''}, {0: 'RS232', 1: '1', 2: '1', 3: '1', 4: ''}, {0: 'Real time clock', 1: '1', 2: '1', 3: '1', 4: ''}, {0: 'Outputs', 1: 'High-Side PWM with CM', 2: '36', 3: '36', 4: '36'}, {0: 'High-Side digital', 1: '8', 2: '8', 3: '8', 4: ''}, {0: 'High-Side digital, PVG, VOUT', 1: '8', 2: '8', 3: '8', 4: ''}, {0: 'Low-Side digital', 1: '8', 2: '8', 3: '8', 4: ''}, {0: 'Inputs Analog input 3 modes (V)(I)(R)', 1: '8', 2: '8', 3: '8', 4: ''}, {0: 'Analog input 2 modes (V)(I)', 1: '16', 2: '16', 3: '16', 4: ''}, {0: 'Analog input (V)', 1: '-', 2: '-', 3: '-', 4: ''}, {0: 'Timer input', 1: '12', 2: '12', 3: '12', 4: ''}, {0: 'Terminal 15', 1: '1', 2: '1', 3: '1', 4: ''}, {0: 'Wake-Up', 1: '1', 2: '1', 3: '1', 4: ''}, {0: 'Sensor supply', 1: '+5V/500mA', 2: '2', 3: '2', 4: '2'}, {0: '+5-10V/2.5W', 1: '1', 2: '1', 3: '1', 4: ''}, {0: 'Safety Switch Nr. of secondary shut-off path', 1: '3', 2: '3', 3: '3', 4: ''}][/table_13]

Table 3: Variants overview for the Spartan-6 XA6SLX25 FPGA

## 1.5.2 Hy-Ttc 580 Variant

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on the facing page.**

![18_image_0_4756.png](The image displays a diagram with various labels and numbers on it. It appears to be related to electronics or technology, possibly explaining different components of a device. There are multiple arrows pointing towards different sections of the diagram, indicating connections or relationships between the labeled elements.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

[table_14][{0: 'External EEPROM', 1: '64 kB More than 1,000,000 write cycles. More than 40-year data retention.'}, {0: 'External Flash', 1: '8 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_14]

## Communication Interfaces

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

- 7 x CAN (50 to 1000 kbit/s)
- 1 x LIN (up to 20 kBd) - 1 x RS232 (up to 115 kBd) - 1 x Ethernet (10/100 Mbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

[table_15][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}][/table_15]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

[table_16][{0: '36 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: 'when used as an input', 1: 'Digital input 8 PWM-controlled HS outputs can be alternatively used as frequency or pulse width measurement in\x02put'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x HS outputs', 1: 'Digital output mode PVG output Voltage output (VOUT)'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_16]

## Specifications

[table_17][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C 1'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_17]

## 1.5.3 Hy-Ttc 540 Variant

![22_image_1_4756.png](The image displays a diagram with various labels and descriptions related to digital electronics. There are several blue boxes labeled with numbers, such as "16," "32," and "48." These numbers might represent different components or settings within the electronic device.  In addition to these labels, there is a clock visible in the upper left corner of the image. The diagram appears to be an instructional guide for understanding digital electronics, with each label providing information about specific aspects of the technology.)

![22_image_0_4756.png](18 different audio files are displayed on a computer screen, each with their own unique file name. The files are arranged in a row, with each one occupying a separate space. The names of these files include numbers such as "Eprom 56," indicating that they might be related to electronic devices or processes.) 

8 0–32 V

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage

## Memory

[table_18][{0: 'External EEPROM', 1: '64 kB More than 1,000,000 write cycles. More than 40-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_18]

Communication Interfaces
- 4 x CAN (50 to 1000 kbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection
- Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

[table_19][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}, {0: '8 x timer input', 1: 'Frequency and pulse width measurement'}, {0: '8 x analog input', 1: '0 to 32 V'}][/table_19]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

[table_20][{0: '28 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: 'when used as an input', 1: 'Digital input'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_20]

## Outputs Specifications

[table_21][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_21]

![26_image_0_4756.png](The image displays a diagram with various labels and numbers on it. It appears to be related to digital technology or electronics, possibly explaining different components of a device. There are several arrows pointing towards different sections of the diagram, indicating connections or relationships between them.  The labels include "Digital In," "Digital Out," "Arm Cortex," "Dust Cone Lockstep," and "Can." The numbers on the diagram seem to be related to measurements or specifications for these components. Overall, the image provides a visual representation of digital technology concepts and their connections.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage

## Memory

[table_22][{0: 'External EEPROM', 1: '64 kB More than 1,000,000 write cycles. More than 40-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_22]

Communication Interfaces
- 4 x CAN (50 to 1000 kbit/s)

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection
- Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

[table_23][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '8 x timer input', 1: 'Frequency and pulse width measurement'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}][/table_23]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

[table_24][{0: '18 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: 'when used as an input', 1: 'Digital input'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_24]

## Specifications

[table_25][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_25]

![30_image_1_4756.png](The image displays a diagram with various labels and descriptions related to an ARM Cortex processor. There are multiple sections within this diagram, each providing information on different aspects of the processor. Some of these sections include "Digital Input," "Digital Output," "Analog Input," "Analog Output," and "Sensor Supply."  In addition to these labels, there is a list of numbers that seem to be related to the ARM Cortex processor as well. The diagram appears to be an informative guide or reference for understanding the workings of this particular processor.) 

![30_image_0_4756.png](16-bit Eprom is displayed on a computer screen with various options. The screen shows different settings for the device, including "RAW" and "Eprom." There are also other options such as "RAW," "Eprom," and "RAW." The image appears to be a close-up of the screen, providing detailed information about the settings available for this particular device.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage

## Memory

[table_26][{0: 'External EEPROM', 1: '64 kB More than 1,000,000 write cycles. More than 40-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_26]

## Communication Interfaces

- 3 x CAN (50 to 1000 kbit/s) - 1 x LIN (up to 20 kBd)

## Power Supply

- Supply voltage: 8 to 32 V - Separate supply pins for CPU subsystem and I/O subsystem
- Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software - Board temperature, sensor supply and battery monitoring

## Inputs

[table_27][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '8 x timer input', 1: 'Frequency and pulse width measurement'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}][/table_27]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

[table_28][{0: '16 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: 'when used as an input', 1: 'Digital input'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x HS outputs', 1: 'Digital output mode PVG output Voltage output (VOUT)'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_28]

## Outputs

Specifications

[table_29][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_29]

## 1.5.6 Hy-Ttc 590E Variant

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

![34_image_1_4756.png](1. A computer screen displaying a list of instructions with various options such as "Digital Input" and "Digital Output." 2. The first option on the list is labeled "Digital Input," which appears to be related to digital audio processing. 3. The second option, "Digital Output," might also be related to digital audio processing or other digital applications.) 

![34_image_0_4756.png](The image displays a diagram with several options labeled on it. These labels include "Can Bus," "HSPI Out," "HSPI In," "LED Out," "LED In," "PWM Out," "PWM In," "VCC," "GND," and "12V." There are also two arrows pointing to the left, one at the top of the image and another near the bottom. The labels seem to be related to a computer or electronic device setup.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

[table_30][{0: 'External FRAM', 1: '32 kB More than 10 trillion (1013) write cycles. More than 121-year data retention.'}, {0: 'External Flash', 1: '64 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_30]

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

[table_31][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}][/table_31]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

[table_32][{0: '36 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: 'when used as an input', 1: 'Digital input 8 PWM-controlled HS outputs can be alternatively used as frequency or pulse width measurement in\x02put'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x HS outputs', 1: 'Digital output mode PVG output Voltage output (VOUT)'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_32]

## Specifications

[table_33][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C 1'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_33]

## 1.5.7 Hy-Ttc 590 Variant

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

![38_image_0_4756.png](The image displays a diagram with various options labeled on different sections of the screen. There are multiple buttons that provide information related to digital cameras, such as "Digital Camera," "Digital Camera Settings," and "Digital Camera Out." Some of these settings include "Digital Camera In" and "Digital Camera Out."  The diagram is organized in a way that allows users to easily navigate through the different options available. The labels on each section provide clear instructions for accessing specific camera functions or settings, making it user-friendly and informative.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

[table_34][{0: 'External FRAM', 1: '32 kB More than 10 trillion (1013) write cycles. More than 121-year data retention.'}, {0: 'External Flash', 1: '32 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_34]

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

[table_35][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}][/table_35]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

Note 1 For any FPGA variant differences please refer to Table 1 on page **4, Table** 2 on page 5 and Table 3 **on page** 6.

[table_36][{0: '36 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: 'when used as an input', 1: 'Digital input 8 PWM-controlled HS outputs can be alternatively used as frequency or pulse width measurement in\x02put'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x HS outputs', 1: 'Digital output mode PVG output Voltage output (VOUT)'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_36]

## Specifications

[table_37][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C 1'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_37]

## 1.5.8 Hy-Ttc 508 Variant

![42_image_0_4756.png](The image displays a diagram with several options for digital audio processing. There are multiple buttons labeled "Digital Input" that can be used to control different aspects of the audio system. Some of these buttons include "Digital Input," "Digital Output," "Digital In," "Digital Out," and "Digital I/O."  In addition, there is a section with various options for digital audio processing, such as "Arm Cortex," "Safety Companion," and "Broadcast." The diagram also features a clock that can be used to keep track of time during the audio processing. Overall, this image provides an overview of the different settings and functions available in a digital audio system.) 

## System Cpu

- TMS570LS3137 CPU running at 180 MHz, 3 MB internal Flash, 256 kB internal RAM, 64 kB
configuration Flash
- Safety companion - 12 bit ADC with 5 V reference voltage - Real Time Clock (RTC)

## Memory

[table_38][{0: 'External EEPROM', 1: '64 kB More than 1,000,000 write cycles. More than 40-year data retention.'}, {0: 'External Flash', 1: '16 MB More than 100,000 write/erase cycles per block. More than 20-year data retention.'}, {0: 'Internal Flash', 1: '3 MB Program Flash. More than 1000 write/erase cycles. More than 15-year data retention.'}, {0: 'Configuration Flash', 1: '64 kB More than 100,000 write/erase cycles. More than 15-year data retention.'}, {0: 'External SRAM', 1: '2 MB'}, {0: 'Internal SRAM', 1: '256 kB'}][/table_38]

## Communication Interfaces

- 3 x CAN (50 to 1000 kbit/s) (CAN1 is ISOBUS compliant)
- 1 x 100BASE-T1 BroadR-Reach® **(100 Mbit/s)**

## Power Supply

- Supply voltage: 8 to 32 V
- Separate supply pins for CPU subsystem and I/O subsystem - Load dump protection - Low current consumption: 0.4 A at 12 V - 2 x 5 V / 500 mA sensor supply - 1 x 5 to 10 V / 2.5 W sensor supply, voltage selected by software
- Board temperature, sensor supply and battery monitoring

## Inputs

[table_39][{0: '8 x analog input 3 modes', 1: 'Voltage measurement: 0 to 5 V Current measurement: 0 to 25 mA Resistor measurement: 0 to 100 kΩ'}, {0: '16 x analog input 2 modes', 1: 'Voltage measurement: 8 x 0 to 5 V/ 0 to 10 V Voltage measurement: 8 x 0 to 5 V/ 0 to 32 V Current measurement: 16 x 0 to 25 mA'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Voltage measurement 0 to 32 V'}, {0: '6 x timer input', 1: 'Frequency and pulse width measurement Input pair as encoder Digital (7/14 mA) current loop speed sensor Voltage measurement 0 to 32 V'}, {0: '8 x timer input', 1: 'Frequency and pulse width measurement'}][/table_39]

All modes are configurable in software. The analog inputs provide 12-bit resolution. Each voltage input can be configured as a digital input with an adjustable threshold.

## Outputs

[table_40][{0: '10 x PWM-controlled HS Outputs', 1: 'PWM mode (50 Hz to 1 kHz) Nominal current 4 A Digital output mode with current feedback'}, {0: '8 x digital HS outputs', 1: 'Digital output mode Nominal current 4 A with voltage feedback'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x HS outputs', 1: 'Digital output mode PVG output Voltage output (VOUT)'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}, {0: '8 x digital LS outputs', 1: 'Digital output mode Nominal current 4 A'}, {0: 'when used as an input', 1: 'Voltage measurement 0 to 32 V Digital input'}][/table_40]

Specifications

[table_41][{0: 'Dimensions', 1: 'See [28]'}, {0: 'Weight', 1: 'See [28]'}, {0: 'Operating ambient temperature', 1: '-40 °C to +85 °C'}, {0: 'Storage temperature', 1: '-40 °C to +85 °C'}, {0: 'Housing', 1: 'IP67- and IP6k9k-rated die-cast aluminum housing and 154-pin connector Pressure equalization with water barrier'}, {0: 'Operating altitude', 1: '0 to 4000 m'}][/table_41]

## 1.6 Standards And Guidelines

The HY-TTC 500 was developed to comply with several international standards and guidelines. This section lists the relevant standards and guidelines and the **applied limits and severity levels.** Environmental Criteria - ISO 16750 Code:
CODE: ISO 16750 (B1 F
2**), L, G, D, Z, (IP6k7; IP6k9k)**

![46_image_0_4756.png](The image is a diagram that shows various types of equipment and their respective requirements. There are several boxes labeled with different topics such as "Climatic Condition," "Chemical Loads," "Protection," and "Supply Voltage." Each box contains information related to the specific topic it represents, providing an organized overview of the equipment's needs. The diagram is a useful tool for understanding the requirements and ensuring that all necessary components are in place when setting up or maintaining the equipment.)

Figure 8: ISO 16750-1:2006 [13], Figure 1 - Code allocation 1.6.1 Electrical Capability

[table_42][{0: 'ISO 16750-2:2012 [22] ISO 7637-2:2011 [20]', 1: 'Electrical transient conduction along supply lines. Test pluse: 1: -600 V, 1 ms 2a: +50 V, 50 µs 2b: +20 V, 200 ms 3a: -200 V, 0.1 µs 3b: +200 V, 0.1 µs 4: 12 V system, -6V drop (6 V remaining voltage) 24 V system, -18 V drop (6 V remaining voltage) 5a: +174 V, 2 Ω, 350 ms'}, {0: 'ISO 7637-3:2007 [14]', 1: 'Electrical transient transmission along signal lines. Tested for 24 V parameters, severity I'}, {0: '1.6.2 Mechanical Capability ISO 16750-3:2012 [23]', 1: 'Free fall tests, 1 m high, 6 falls per side Random vibration, broad-band 3 axes, 32 h per axis 57.9 m/s2 -10 Hz to 2 kHz, temperature profile super\x02imposed Shock, half-sine 3 axes, 60 shocks 500 m/s2 , 6 ms'}, {0: '1.6.3 Climatic Capability ISO 16750-4:2012 [18]', 1: 'Humid Heat Cyclic, DIN EN 60068-2-30:2006-06 [3], DIN EN 60068-2-38:2009 [5] Damp Heat, DIN EN 60068-2-78:2014-02[9]'}][/table_42]

Salt spray, DIN EN 60068-2-11:2000-02 [2], DIN EN 60068-2-38:1996-10 [5]

## 1.6.4 Chemical Capability

The list of applied chemical agents for tests according to IEC 16750-5:2010**[19] is given in Table** 4 on the current page.

[table_43][{0: 'ID', 1: 'Chemical Agent', 2: 'Application Method'}, {0: 'AA', 1: 'Diesel fuel', 2: 'III. Wiping'}, {0: 'AB', 1: '"Bio" diesel', 2: 'III. Wiping'}, {0: 'AC', 1: 'Petrol/gasoline unleaded', 2: 'III. Wiping'}, {0: 'AE', 1: 'Methanol', 2: 'III. Wiping'}, {0: 'BA', 1: 'Engine oil', 2: 'II. Brushing'}, {0: 'BB', 1: 'Differential oil', 2: 'II. Brushing'}, {0: 'BC', 1: 'Transmission fluid', 2: 'II. Brushing'}, {0: 'BD', 1: 'Hydraulic fluid', 2: 'II. Brushing'}, {0: 'CA', 1: 'Battery fluid', 2: 'III. Wiping'}, {0: 'CB', 1: 'Brake fluid', 2: 'III. Wiping'}, {0: 'CC', 1: 'Antifreeze fluid', 2: 'III. Wiping'}, {0: 'CE', 1: 'Cavity prodection', 2: 'III. Wiping'}, {0: 'CF', 1: 'Protective lacquer', 2: 'II. Brushing'}, {0: 'CG', 1: 'Protective lacquer remover', 2: 'III. Wiping'}, {0: 'DA', 1: 'Windscreen washer fluid', 2: 'II. Brushing'}, {0: 'DB', 1: 'Vehicle washing chemicals', 2: 'II. Brushing'}, {0: 'DC', 1: 'Interior cleaner', 2: 'III. Wiping'}, {0: 'DD', 1: 'Glass cleaner', 2: 'III. Wiping'}, {0: 'DE', 1: 'Wheel cleaner', 2: 'II. Brushing'}, {0: 'DF', 1: 'Cold cleaning agent', 2: 'II. Brushing'}, {0: 'DK', 1: 'Denatured alcohol', 2: 'III. Wiping'}, {0: 'ED', 1: 'Refreshment containing caffeine and sugar', 2: 'III. Wiping'}, {0: 'YYA', 1: 'Gasoline with 15% methanol', 2: 'III. Wiping'}, {0: 'YYB', 1: 'FAM test fuel', 2: 'III. Wiping'}][/table_43]

Table 4: List of chemical agents

## 1.6.5 Ingress Protection Capability

ISO 20653:2013 [17] IP6k7 and IP6k9k

## 1.6.6 Esd And Emc Capability For Road Vehicles

[table_44][{0: 'UNECE 10.4', 1: 'Uniform provisions concerning the approval of vehi\x02cles with regard to EMC'}, {0: 'DIN EN 13309:2010-12 (E) [4]', 1: 'Construction machinery - Electromagnetic compati\x02bility of machines with internal power supply'}, {0: 'ISO 14982:1998 [11]', 1: 'Agricultural and forestry machinery - Electromag\x02netic compatibility - Test methods and acceptance criteria'}, {0: 'ISO 11452-2:2004 [12]', 1: '100 V/m, 20 MHz to 3 GHz'}, {0: 'CISPR 25 ED. 3.0 B:2008 [1]', 1: 'Conducted emissions, Class 3'}, {0: 'ISO 10605:2008 [15]', 1: 'ESD powered and unpowered ±6 kV contact discharge ±8 kV air discharge'}, {0: '1.6.7 ESD and EMC Capability for Industrial Applications IEC 61000-6-2:2005 [6] Immunity for industrial environments. Conformance to surge immunity is only given if signal line wire length is less than 30 m. IEC 61000-6-4:2007 [7] Radiated emission for industry 1.6.8 Functional Safety ISO 13849:2015 [16] Safety of machinery - Safety-related parts of control systems IEC 61508:2010 [8] Functional safety of electrical/electronic/pro\x02grammable electronic safety-related systems (E/E/PE, or E/E/PES), Safety Integrity Level 2 (SIL 2) ISO 25119:2018 [25] Tractors and machinery for agriculture and forestry - Safety-related parts of control systems ISO 26262:2018 [26] Road vehicles - Functional safety', 1: ''}][/table_44]

## 1.7 Instructions For Safe Operation

For safe operation of the HY-TTC 500 family ECUs, the following rules have to be obeyed:

## 1.7.1 General

- The HY-TTC 500 System Manual is written for a specific product version, for example 02.00.

Make sure this document corresponds with the product version of the ECU. The *Product* Version **on the title page of this document must match the** *Version* **on the label of the ECU.**
The following figure shows an example of an ECU label:

![50_image_0_4756.png](The image displays a close-up of a TC Control product manual with various details about the product. There are several sections within the manual, including information on voltage, power supply, and other technical aspects. A pin is also visible near the bottom right corner of the page.  The manual appears to be written in German, which suggests that it may be a European product or intended for use in Europe. The detailed content of the manual provides users with essential information about the TC Control product, ensuring proper usage and understanding of its features.)

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

![53_image_0_4756.png](The image features a close-up of two side-by-side computer keyboards. Each keyboard has multiple rows of keys, including letters, numbers, and function keys. The arrangement of the keys is organized in a way that allows for easy typing and navigation while using the computers.) 

Note: **The main connector is numbered from 1 to 96 (left connector) and 1 to 58 (right connector).** This correspond to pins 101 to 196 and 201 to 258, respectively, in this System Manual.

## 3.2 Mating Connector

The listed part numbers can be ordered from HERTH+BUSS, KOSTAL or BOSCH with a minimum quantity of, for example, 100 pieces.

For lower quantities, TTControl GmbH provides complete kits with BOSCH connectors, crimp contacts and sealings.

[table_45][{0: 'TTControl Order Numbers', 1: 'Description'}, {0: '10619', 1: 'Connector kit for HY-TTC 500, 58-positions'}, {0: '10620', 1: 'Connector kit for HY-TTC 500, 96-positions'}][/table_45]

![54_image_0_4756.png](The image features a white background with various parts of an electronic device displayed on it. There are several pieces of equipment, including a cell phone, a computer, and other electronics. These items are laid out neatly, showcasing their components and the intricate details of their internal structures.  In addition to these devices, there is also a set of tools present in the image, which may be used for assembling or repairing the electronic equipment. The presence of both the electronics and tools suggests that this could be an educational setting where students learn about the inner workings of various devices or a workspace where professionals assemble or troubleshoot electronic components.)

![54_image_1_4756.png](1. A car engine is displayed on a white background, showcasing its components. 2. There are several parts of an electronic device, including a keyboard, placed next to each other. 3. A computer mouse can also be seen among the assortment of items. 4. The image features a variety of tools and electronics, such as a car engine, keyboard, and computer mouse, all laid out on a table or white background.)

## 3.2.1 Kostal Mating Connector

Please follow the Process Specification below for the right handling of the KOSTAL mating connector:
Process Specification DOC00105005, Receptacle Housing 58-way and 96-way for control units

## 3.2.1.1 Mating Connector 96-Positions

[table_46][{0: 'KOSTAL', 1: 'HERTH+BUSS', 2: 'Description', 3: 'Note', 4: 'Quantity'}, {0: 'Part Number', 1: 'Part Number', 2: '', 3: '', 4: ''}, {0: '9409601', 1: '50390395', 2: 'Plug housing', 3: '1', 4: ''}, {0: '10400794061', 1: '50390397', 2: 'Holder', 3: '1', 4: ''}, {0: '10400794071', 1: '50390398', 2: 'Secondary lock', 3: '1', 4: ''}, {0: '22400794081', 1: '50390399', 2: 'Cover cap (cable exit on the left side)', 3: '1', 4: ''}, {0: '22400172011', 1: '50390567', 2: 'Cover cap (cable exit on the upper right side)', 3: '1', 4: ''}, {0: '10800794051', 1: '50282066', 2: 'Sealing-/protection plug', 3: '1', 4: '1'}, {0: '(discontinued)', 1: '', 2: '', 3: '', 4: ''}, {0: '10204225', 1: '50282099', 2: 'Sealing-/protection plug', 3: '1', 4: '1'}][/table_46]

Table 5: KOSTAL / HERTH+BUSS part numbers Note **1 In order to achieve the specified IP rating each single wire must be populated**
either with a single-, blind- or a total protection-plug.

## 3.2.1.2 Mating Connector 58-Positions

[table_47][{0: 'KOSTAL', 1: 'HERTH+BUSS', 2: 'Description', 3: 'Note', 4: 'Quantity'}, {0: 'Part Number', 1: 'Part Number', 2: '', 3: '', 4: ''}, {0: '9405801', 1: '50390396', 2: 'Plug housing', 3: '1', 4: ''}, {0: '10400758951', 1: '50390400', 2: 'Holder', 3: '1', 4: ''}, {0: '10400758991', 1: '50390401', 2: 'Secondary lock', 3: '1', 4: ''}, {0: '22400794001', 1: '50390402', 2: 'Cover cap (cable exit on the right side)', 3: '1', 4: ''}, {0: '22400172001', 1: '50390449', 2: 'Cover cap (cable exit on the upper left side)', 3: '1', 4: ''}, {0: '10800758941', 1: '50282065', 2: 'Sealing-/protection plug', 3: '1', 4: '1'}, {0: '-', 1: '50282062', 2: 'High power pin single sealing-/protection plug', 3: '1', 4: '6'}, {0: '10800472631', 1: '50282030', 2: 'High power pin single blind-sealing-/protection', 3: '1', 4: '-'}, {0: 'plug', 1: '', 2: '', 3: '', 4: ''}][/table_47]

Table 6: KOSTAL / HERTH+BUSS part numbers Note **1 In order to achieve the specified IP rating each single wire must be populated**
either with a single-, blind- or a total protection-plug.

## 3.2.1.3 Crimp Contacts

[table_48][{0: 'For I/O pins (148) KOSTAL Part Number', 1: 'HERTH+BUSS', 2: 'Note', 3: 'Description'}, {0: 'Part Number', 1: '', 2: '', 3: ''}, {0: '22140734080', 1: '50253445', 2: '1', 3: 'KKS MLK 1.2 m, crimp contact tinned, wire size 0.75 mm2 to 1 mm2'}, {0: '32140734080', 1: '50253445088', 2: '2', 3: ''}, {0: '22140734070', 1: '50253443', 2: '1', 3: 'KKS MLK 1.2 m, crimp contact tinned, wire size 0.5 mm2 to 0.75 mm2'}, {0: '32140734070', 1: '50253443088', 2: '2', 3: ''}, {0: '22140734060', 1: '50253441', 2: '1', 3: 'KKS MLK 1.2 m, crimp contact tinned, wire size 0.35 mm2 to 0.5 mm2'}, {0: '32140734060', 1: '50253441088', 2: '2', 3: ''}, {0: '22140734050', 1: '50253439', 2: '1', 3: 'KKS MLK 1.2 m, crimp contact tinned, wire size 0.1 mm2 to 0.25 mm2'}, {0: '32140734050', 1: '50253439088', 2: '2', 3: ''}, {0: 'For High Power pins (6) KOSTAL Part Number', 1: 'HERTH+BUSS', 2: 'Note', 3: 'Description'}, {0: 'Part Number', 1: '', 2: '', 3: ''}, {0: '22140499580', 1: '50253230', 2: '1', 3: 'KKS SLK 2.8 ELA, crimp contact tinned, wire size 1mm2 to 2.5mm2'}, {0: '32140499580', 1: '50253230088', 2: '2', 3: ''}, {0: '22140499570', 1: '50253229', 2: '1', 3: 'KKS SLK 2.8 ELA, crimp contact tinned, wire size 0.5mm2 to 0.75 mm2'}, {0: '32140499570', 1: '50253229088', 2: '2', 3: ''}, {0: 'Table 7: KOSTAL / HERTH+BUSS part numbers', 1: '', 2: '', 3: ''}][/table_48]

Note **1 Loose crimp contact order code, minimum 50 pieces per packing unit.** Note 2 Strip (reel) crimp contact order code, minimum 4000 pieces **per packing unit.**

## 3.2.1.4 Tools

[table_49][{0: 'KOSTAL', 1: 'HERTH+BUSS', 2: 'Description'}, {0: 'Part Number', 1: 'Part Number', 2: ''}, {0: '80411002', 1: '95942166', 2: 'Crimping pliers without inserts'}, {0: '80411504', 1: '95942167', 2: 'Crimping pliers insert set for MLK 1,2'}, {0: '80411631', 1: '95942169', 2: 'Crimping pliers insert set for SLK 2,8'}, {0: '80495003', 1: '95945400', 2: 'Unlocking tool for MLK 1,2'}, {0: '-', 1: '95945402', 2: 'Unlocking tool for SLK 2,8'}][/table_49]

Table 8: KOSTAL / HERTH+BUSS part numbers

## 3.2.2 Bosch Mating Connector

Please follow the assembly instruction and technical customer information below for the right handling of the BOSCH mating connector:
Assembly Instruction 1 928 A00 48M Technical Customer Information 1 928 A00 45T

## 3.2.2.1 Mating Connector 96-Positions

[table_50][{0: 'BOSCH', 1: 'Description', 2: 'Quantity'}, {0: 'Part Number 1 928 404 781', 1: 'Plug housing', 2: '1'}, {0: '1 928 404 927', 1: 'Plug housing, 90-degree angled (alt.)', 2: '-'}, {0: '1 928 404 773', 1: 'Cover cap', 2: '1'}, {0: '1 928 404 762', 1: 'Secondary lock', 2: '1'}][/table_50]

Table 9: BOSCH part numbers

## 3.2.2.2 Mating Connector 58-Positions

[table_51][{0: 'BOSCH', 1: 'Description', 2: 'Note', 3: 'Quantity'}, {0: 'Part Number 1 928 404 916', 1: 'Plug housing', 2: '1', 3: ''}, {0: '1 928 404 780', 1: 'Plug housing, 90-degree angled (alt.)', 2: '-', 3: ''}, {0: '1 928 404 917', 1: 'Cover cap', 2: '1', 3: ''}, {0: '1 928 404 760', 1: 'Secondary lock', 2: '1', 3: ''}, {0: '1 928 404 761', 1: 'Secondary lock', 2: '1', 3: ''}, {0: '1 928 300 600', 1: 'High power pin single sealing-/protection plug', 2: '1', 3: '6'}, {0: '1 928 300 601', 1: 'High power pin single blind-sealing-/protection plug', 2: '1', 3: '-'}][/table_51]

Table 10: BOSCH part numbers Note **1 In order to achieve the specified IP rating each single wire must be populated**
either with a single protection-, blind protection-, or a total protection-plug.

## 3.2.2.3 Crimp Contacts

[table_52][{0: 'For I/O pins (148) BOSCH Part Number', 1: 'Description'}, {0: '1 928 498 679', 1: 'Matrix 1.2 m, crimp contact tinned, wire size 0.35 mm2 to 0.5 mm2'}, {0: '1 928 498 137 (alt.) 1 928 498 680', 1: 'Matrix 1.2 m, crimp contact tinned, wire size 0.75 mm2 to 1.0 mm2'}, {0: '1 928 498 138 (alt.) For High Power pins (6) BOSCH Part Number', 1: 'Description'}, {0: '1 928 498 057', 1: 'BDK 2.8, crimp contact tinned, wire size 1.5mm2 to 2.5mm2'}, {0: 'Table 11: BOSCH crimp contacts part numbers', 1: ''}][/table_52]

3.2.2.4 Tools

[table_53][{0: 'BOSCH', 1: 'Description'}, {0: 'Part Number 1 928 498 161', 1: 'Crimping pliers / BDK / BSK 2,8 / 0,5 - 1 mm2'}, {0: '1 928 498 162', 1: 'Crimping pliers / BDK / BSK 2,8 / 1,5 - 2,5 mm2'}, {0: '1 928 498 212', 1: 'Crimping pliers / Matrix 1,2 / 0,35 - 0,5 mm2'}, {0: '1 928 498 213', 1: 'Crimping pliers / Matrix 1,2 / 0,75 - 1,0 mm2'}, {0: '1 928 498 167', 1: 'Unlocking tool for BDK / BSK 2,8'}, {0: '1 928 498 168', 1: 'Unlocking tool spare pin for BDK / BSK 2,8'}, {0: '1 928 498 218', 1: 'Unlocking tool for Matrix 1,2'}, {0: '1 928 498 219', 1: 'Unlocking tool spare pin for Matrix 1,2'}][/table_53]

Table 12: BOSCH Tools part numbers

## 3.3 Cable Harness

[table_54][{0: 'Description', 1: 'Variants'}, {0: 'Cable Harness for HY-TTC 500, 3 m, open end', 1: 'HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510'}, {0: 'Cable Harness for HY-TTC 500 family, 1.5 m Cable Harness for HY-TTC 500, BRR, 3 m, OE', 1: 'HY-TTC 590E, HY-TTC 590, HY-TTC 508'}, {0: 'Cable Harness for HY-TTC 500, BRR, 1.5 m', 1: ''}][/table_54]

Note**: Make sure you use a cable harness fitting to the variant as listed in the table above. Usage of** improper cable harness may damage the device.

## 3.4 Fuse

For cable harness protection, it is recommended to protect each power supply path by a dedicated fuse. Please take note that the selected fuse type has to match to the current capability of the cable harness.

[table_55][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'BAT+', 1: 'Fuse trip current of Positive Power Supply of Inter\x02nal Electronics', 2: '2', 3: 'A', 4: '', 5: ''}, {0: 'CPU BAT+', 1: 'Fuse trip current of Positive Power Supply of Power', 2: '1', 3: '60', 4: 'A', 5: ''}, {0: 'Power', 1: 'Stages', 2: '', 3: '', 4: '', 5: ''}][/table_55]

Note 1 The maximum fuse trip current is dependent on the specific customer application. The maximum total load current must be considered, see Section **4.1.3** on page 97

![59_image_0_4756.png](The image displays a diagram of an electrical system with various components labeled throughout. There are multiple power supplies, including one at the top left corner, another near the center-left area, and two more towards the bottom right side. A battery is also visible in the lower part of the image.  In addition to these components, there are several labels describing different aspects of the electrical system. These include "EUCS," which could be a reference to an energy management system or power supply unit. Other labels can be found throughout the diagram, providing information about the various parts and their functions within the overall electrical setup.)

![60_image_0_4756.png](The image features a blue sign with white letters that reads "TC Control." It appears to be an advertisement for TC Control International. The sign is placed on a wall, drawing attention to the company's services or products.)

## 3.5 Hy-Ttc 500 Family Pinning

The following subsections describe the HY-TTC 500 family variant dependent main- and the respective alternative functions on connector pin-level.

Each hardware function in the table, e.g. Pin 101 - **HS PWM Output, is referenced to its main-** (*IO_PWM_28***) and alternative (***IO_DO_44, IO_PWD_12, IO_DI_28***) function.** *IO_xx_yy* **represents** the software define for each function. For more information about API documentation, please refer to Chapter 8 on page **226.**
Please take note that the main function shall be used preferably and the technical specifications must particularly be regarded when alternative functions are to be used. See Chapter 4 **on page** 96 for limits and restrictions.

3.5.1 HY-TTC 580 **Variant**

![61_image_0_4756.png](100% of the image is a blue background with white numbers on it. The numbers are arranged in rows, forming a grid-like pattern. There are no other elements or objects visible in the image.)

[table_56][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_DO_44', 3: 'IO_PWD_12', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_28', 1: 'IO_DI_28', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_DO_48', 3: 'IO_PWD_16', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_32', 1: 'IO_DI_32', 2: 'IO_ADC_00', 3: 'IO_ADC_00', 4: 'IO_DI_48', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P103', 1: 'Analog Voltage Input IO_ADC_00', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_56]

![62_image_0_4756.png](100% of the image is a blue background with white text. The text appears to be a list of numbers, possibly representing a timeline or a series of events. There are no other visible elements or objects in the image.)

[table_57][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P124', 1: 'Timer Input', 2: 'IO_ADC_34', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_10', 1: 'IO_DI_46', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P125', 1: 'HS PWM Output', 2: 'IO_DO_45', 3: 'IO_DI_29', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_29', 1: 'IO_PWD_13', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P126', 1: 'HS PWM Output', 2: 'IO_DO_49', 3: 'IO_PWD_17', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_33', 1: 'IO_DI_33', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P127', 1: 'Analog Voltage Input', 2: 'IO_ADC_01', 3: 'IO_ADC_01', 4: 'IO_DI_49', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P141', 1: 'Timer Input', 2: 'IO_PWD_05', 3: 'IO_ADC_29', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_05', 1: 'IO_DI_41', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_57]

![63_image_0_4756.png](The image is a black and white photo of a table with various columns of information. There are several rows of data displayed on the table, including numbers and possibly some text. The table appears to be organized into different sections, each containing distinct information. It seems like an informative or educational setting where the data is being presented in a structured manner for easy understanding.)

[table_58][{0: 'P148', 1: 'Timer Input', 2: 'IO_ADC_35', 3: ''}, {0: 'IO_PWD_11', 1: 'IO_DI_47', 2: '', 3: ''}, {0: 'P149', 1: 'HS Digital Output', 2: 'IO_ADC_36', 3: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: ''}, {0: 'P150', 1: 'HS PWM Output', 2: 'IO_DO_46', 3: 'IO_PWD_14'}, {0: 'IO_PWM_30', 1: 'IO_DI_30', 2: '', 3: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_DO_50', 3: 'IO_PWD_18'}, {0: 'IO_PWM_34', 1: 'IO_DI_34', 2: '', 3: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00'}, {0: 'IO_PWM_00', 1: '', 2: '', 3: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14'}, {0: 'IO_PWM_14', 1: '', 2: '', 3: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02'}, {0: 'IO_PWM_02', 1: '', 2: '', 3: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16'}, {0: 'IO_PWM_16', 1: '', 2: '', 3: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04'}, {0: 'IO_PWM_04', 1: '', 2: '', 3: ''}, {0: 'P160', 1: 'HS PWM Output', 2: 'IO_DO_34', 3: 'IO_DI_18'}, {0: 'IO_PWM_18', 1: '', 2: '', 3: ''}, {0: 'P161', 1: 'HS Digital Output', 2: 'IO_PVG_00', 3: 'IO_VOUT_00 IO_ADC_52'}, {0: 'IO_DO_52', 1: 'IO_DI_88', 2: '', 3: ''}, {0: 'P162', 1: 'HS PWM Output', 2: 'IO_DO_23', 3: 'IO_DI_07'}, {0: 'IO_PWM_07', 1: '', 2: '', 3: ''}, {0: 'P163', 1: 'HS PWM Output', 2: 'IO_DO_37', 3: 'IO_DI_21'}, {0: 'IO_PWM_21', 1: '', 2: '', 3: ''}, {0: 'P164', 1: 'HS Digital Output', 2: 'IO_PVG_03', 3: 'IO_VOUT_03 IO_ADC_55'}, {0: 'IO_DO_55', 1: 'IO_DI_91', 2: '', 3: ''}, {0: 'P165', 1: 'HS PWM Output', 2: 'IO_DO_25', 3: 'IO_DI_09'}, {0: 'IO_PWM_09', 1: '', 2: '', 3: ''}, {0: 'P166', 1: 'HS PWM Output', 2: 'IO_DO_39', 3: 'IO_DI_23'}, {0: 'IO_PWM_23', 1: '', 2: '', 3: ''}, {0: 'P167', 1: 'HS Digital Output', 2: 'IO_PVG_05', 3: 'IO_VOUT_05 IO_ADC_57'}, {0: 'IO_DO_57', 1: 'IO_DI_93', 2: '', 3: ''}, {0: 'P168', 1: 'HS PWM Output', 2: 'IO_DO_27', 3: 'IO_DI_11'}, {0: 'IO_PWM_11', 1: '', 2: '', 3: ''}, {0: 'P169', 1: 'HS PWM Output', 2: 'IO_DO_41', 3: 'IO_DI_25'}, {0: 'IO_PWM_25', 1: '', 2: '', 3: ''}, {0: 'P170', 1: 'HS Digital Output', 2: 'IO_PVG_07', 3: 'IO_VOUT_07 IO_ADC_59'}, {0: 'IO_DO_59', 1: 'IO_DI_95', 2: '', 3: ''}][/table_58]

![64_image_0_4756.png](1. A blue screen with white numbers on it. 2. The number 3 is visible on the screen.)

[table_59][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P171', 1: 'HS PWM Output', 2: 'IO_DO_29', 3: 'IO_DI_13', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_13', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P172', 1: 'HS PWM Output', 2: 'IO_DO_43', 3: 'IO_DI_27', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_27', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P173', 1: 'HS Digital Output', 2: 'IO_ADC_37', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_01', 1: 'IO_DI_73', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P174', 1: 'HS PWM Output', 2: 'IO_DO_47', 3: 'IO_PWD_15', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_31', 1: 'IO_DI_31', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P175', 1: 'HS PWM Output', 2: 'IO_DO_51', 3: 'IO_PWD_19', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_35', 1: 'IO_DI_35', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P176', 1: 'HS Digital Output', 2: 'IO_ADC_39', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P177', 1: 'HS PWM Output', 2: 'IO_DO_17', 3: 'IO_DI_01', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_01', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P178', 1: 'HS PWM Output', 2: 'IO_DO_31', 3: 'IO_DI_15', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_15', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_03', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_17', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_05', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P184', 1: 'HS PWM Output', 2: 'IO_DO_35', 3: 'IO_DI_19', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_19', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P185', 1: 'HS Digital Output', 2: 'IO_PVG_01', 3: 'IO_VOUT_01 IO_ADC_53', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_53', 1: 'IO_DI_89', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P186', 1: 'HS PWM Output', 2: 'IO_DO_22', 3: 'IO_DI_06', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P187', 1: 'HS PWM Output', 2: 'IO_DO_36', 3: 'IO_DI_20', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P188', 1: 'HS Digital Output', 2: 'IO_PVG_02', 3: 'IO_VOUT_02 IO_ADC_54', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_54', 1: 'IO_DI_90', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P189', 1: 'HS PWM Output', 2: 'IO_DO_24', 3: 'IO_DI_08', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P190', 1: 'HS PWM Output', 2: 'IO_DO_38', 3: 'IO_DI_22', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P191', 1: 'HS Digital Output', 2: 'IO_PVG_04', 3: 'IO_VOUT_04 IO_ADC_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_56', 1: 'IO_DI_92', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P192', 1: 'HS PWM Output', 2: 'IO_DO_26', 3: 'IO_DI_10', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P193', 1: 'HS PWM Output', 2: 'IO_DO_40', 3: 'IO_DI_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_24', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_59]

![65_image_0_4756.png](1. A black and white image of a table with various columns of information. 2. The table is filled with data, including numbers and possibly some text. 3. There are multiple rows on the table, each containing different types of information.)

[table_60][{0: 'P194', 1: 'HS Digital Output', 2: 'IO_PVG_06', 3: 'IO_VOUT_06 IO_ADC_58'}, {0: 'IO_DO_58', 1: 'IO_DI_94', 2: '', 3: ''}, {0: 'P195', 1: 'HS PWM Output', 2: 'IO_DO_28', 3: 'IO_DI_12'}, {0: 'IO_PWM_12', 1: '', 2: '', 3: ''}, {0: 'P196', 1: 'HS PWM Output', 2: 'IO_DO_42', 3: 'IO_DI_26'}, {0: 'IO_PWM_26', 1: '', 2: '', 3: ''}, {0: 'P197 P198 P199 P200 P201', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P202', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P203', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P204', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P205', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P206', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15', 2: '', 3: ''}, {0: 'P208', 1: 'LIN IO_LIN', 2: '', 3: ''}, {0: 'P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0', 2: '', 3: ''}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1', 2: '', 3: ''}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2', 2: '', 3: ''}, {0: 'P212', 1: 'CAN 3 Low IO_CAN_CHANNEL_3', 2: '', 3: ''}, {0: 'P213', 1: 'CAN 4 Low IO_CAN_CHANNEL_4', 2: '', 3: ''}, {0: 'P214', 1: 'CAN 5 Low IO_CAN_CHANNEL_5', 2: '', 3: ''}, {0: 'P215', 1: 'CAN 6 Low IO_CAN_CHANNEL_6', 2: '', 3: ''}, {0: 'P216', 1: 'CAN Termination 3L', 2: '', 3: ''}, {0: 'P217', 1: 'Sensor GND', 2: '', 3: ''}, {0: 'P218', 1: 'Ethernet TD+ IO_DOWNLOAD, IO_UDP', 2: '', 3: ''}, {0: 'P219', 1: 'Ethernet TD\x02IO_DOWNLOAD, IO_UDP', 2: '', 3: ''}, {0: 'P220', 1: 'Wake-Up IO_ADC_WAKE_UP', 2: '', 3: ''}, {0: 'P221', 1: 'Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2', 2: '', 3: ''}][/table_60]

![66_image_0_4756.png](100% of the image is blue with a few black lines. The blue background has white numbers on it, possibly representing a timeline or a graphic representation. There are no other visible elements or objects in the image.)

[table_61][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P225', 1: 'CAN 3 High IO_CAN_CHANNEL_3', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P226', 1: 'CAN 4 High IO_CAN_CHANNEL_4', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P227', 1: 'CAN 5 High IO_CAN_CHANNEL_5', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P228', 1: 'CAN 6 High IO_CAN_CHANNEL_6', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P229', 1: 'CAN Termination 3H', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P230', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P231', 1: 'Ethernet RD\x02IO_DOWNLOAD', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P232', 1: 'Ethernet RD+ IO_DOWNLOAD', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P233', 1: 'RTC_BACKUP_BAT', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P234', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P235', 1: 'CAN Termination 0L', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P236', 1: 'CAN Termination 1L', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P237', 1: 'CAN Termination 2L', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P238', 1: 'LS Digital Output', 2: 'IO_ADC_45', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_09', 1: 'IO_DI_81', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P239', 1: 'LS Digital Output', 2: 'IO_ADC_47', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_11', 1: 'IO_DI_83', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P240', 1: 'LS Digital Output', 2: 'IO_ADC_49', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_13', 1: 'IO_DI_85', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P241', 1: 'LS Digital Output', 2: 'IO_ADC_51', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_15', 1: 'IO_DI_87', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P242', 1: 'RS232 TXD IO_UART', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P243', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P244', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P245', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P246', 1: 'BAT+ CPU IO_ADC_UBAT', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P247', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P248', 1: 'CAN Termination 0H', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P249', 1: 'CAN Termination 1H', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_61]

![67_image_0_4756.png](1. A black and white image of a table with several rows of data. 2. The table is filled with various types of information, including numbers and letters. 3. There are multiple columns on the table, each containing different types of data. 4. Some of the columns include text such as "A", "B", "C", and "D".)

[table_62][{0: 'P250', 1: 'CAN Termination 2H', 2: ''}, {0: 'P251', 1: 'LS Digital Output', 2: 'IO_ADC_44'}, {0: 'IO_DO_08', 1: 'IO_DI_80', 2: ''}, {0: 'P252', 1: 'LS Digital Output', 2: 'IO_ADC_46'}, {0: 'IO_DO_10', 1: 'IO_DI_82', 2: ''}, {0: 'P253', 1: 'LS Digital Output', 2: 'IO_ADC_48'}, {0: 'IO_DO_12', 1: 'IO_DI_84', 2: ''}, {0: 'P254', 1: 'LS Digital Output', 2: 'IO_ADC_50'}, {0: 'IO_DO_14', 1: 'IO_DI_86', 2: ''}, {0: 'P255', 1: 'RS232 RXD IO_UART', 2: ''}, {0: 'P256', 1: 'Sensor GND', 2: ''}, {0: 'P257', 1: 'Sensor GND', 2: ''}, {0: 'P258', 1: 'Sensor GND', 2: 'Table 13: Pinning of HY-TTC 580'}][/table_62]

![68_image_0_4756.png](2014 is displayed on this calendar, which has a blue background with white numbers. The calendar is divided into months, with each month occupying a significant portion of the page. There are no other visible elements apart from the calendar itself.)

[table_63][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_PWD_12 IO_DI_28', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_PWD_16 IO_DI_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P103', 1: 'Analog Voltage Input', 2: 'IO_ADC_00', 3: 'IO_ADC_00', 4: 'IO_DI_48', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_00', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_63]

![69_image_0_4756.png](The image is a black and white photograph of a large book with various words written on its pages. The book appears to be an encyclopedia, as there are multiple entries covering different topics. Some of these topics include "Abundance," "Aesthetics," "Advocacy," "Alchemy," "Ambition," and many others. The photograph captures the essence of a vast collection of knowledge, showcasing the importance of learning and understanding various subjects.)

[table_64][{0: 'P124', 1: 'Timer Input', 2: 'IO_ADC_34', 3: '', 4: ''}, {0: 'IO_PWD_10', 1: 'IO_DI_46', 2: '', 3: '', 4: ''}, {0: 'P125', 1: 'HS PWM Output', 2: 'IO_DI_29 IO_PWD_13', 3: '', 4: ''}, {0: 'P126', 1: 'HS PWM Output', 2: 'IO_PWD_17 IO_DI_33', 3: '', 4: ''}, {0: 'P127', 1: 'Analog Voltage Input', 2: 'IO_ADC_01', 3: 'IO_ADC_01', 4: 'IO_DI_49'}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51'}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53'}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55'}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: ''}, {0: 'IO_PWD_05', 1: 'IO_ADC_29', 2: '', 3: '', 4: ''}, {0: 'P141', 1: 'Timer Input IO_PWD_05', 2: 'IO_DI_41', 3: '', 4: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: ''}][/table_64]

![70_image_0_4756.png](The image displays a large table with various columns of data. Each column is labeled with numbers, indicating different categories within the data set. The table appears to be organized for easy reference and analysis.)

[table_65][{0: 'HS Digital Output', 1: 'IO_ADC_36', 2: '', 3: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: ''}, {0: 'IO_PWD_14 IO_DI_30', 1: '', 2: '', 3: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_PWD_18 IO_DI_34', 3: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00'}, {0: 'IO_PWM_00', 1: '', 2: '', 3: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14'}, {0: 'IO_PWM_14', 1: '', 2: '', 3: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02'}, {0: 'IO_PWM_02', 1: '', 2: '', 3: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16'}, {0: 'IO_PWM_16', 1: '', 2: '', 3: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04'}, {0: 'IO_PWM_04', 1: '', 2: '', 3: ''}, {0: 'P160', 1: 'HS PWM Output', 2: 'IO_DO_34', 3: 'IO_DI_18'}, {0: 'IO_PWM_18', 1: '', 2: '', 3: ''}, {0: 'P161', 1: 'HS Digital Output', 2: 'IO_ADC_52 IO_DI_88', 3: ''}, {0: 'P162', 1: 'HS PWM Output', 2: 'IO_DO_23', 3: 'IO_DI_07'}, {0: 'IO_PWM_07', 1: '', 2: '', 3: ''}, {0: 'P163', 1: 'HS PWM Output', 2: 'IO_DO_37', 3: 'IO_DI_21'}, {0: 'IO_PWM_21', 1: '', 2: '', 3: ''}, {0: 'P164', 1: 'HS Digital Output', 2: 'IO_ADC_55 IO_DI_91', 3: ''}, {0: 'P165', 1: 'HS PWM Output', 2: 'IO_DO_25', 3: 'IO_DI_09'}, {0: 'IO_PWM_09', 1: '', 2: '', 3: ''}, {0: 'P166', 1: 'HS PWM Output', 2: 'IO_DO_39', 3: 'IO_DI_23'}, {0: 'IO_PWM_23', 1: '', 2: '', 3: ''}, {0: 'P167', 1: 'HS Digital Output', 2: 'IO_ADC_57 IO_DI_93', 3: ''}, {0: 'P168', 1: 'HS PWM Output', 2: 'IO_DO_27', 3: 'IO_DI_11'}, {0: 'IO_PWM_11', 1: '', 2: '', 3: ''}, {0: 'P169', 1: 'HS PWM Output', 2: 'IO_DO_41', 3: 'IO_DI_25'}, {0: 'IO_PWM_25', 1: '', 2: '', 3: ''}, {0: 'P170', 1: 'HS Digital Output', 2: 'IO_ADC_59 IO_DI_95', 3: ''}][/table_65]

![71_image_0_4756.png](1. A row of blue words is displayed on a black background. 2. The first word in the row reads "Abundance." 3. The second word reads "Efficiency." 4. The third word reads "Innovation." 5. The fourth word reads "Sustainability." 6. The fifth word reads "Collaboration.")

[table_66][{0: 'P171', 1: 'HS PWM Output', 2: 'IO_DO_29', 3: 'IO_DI_13'}, {0: 'IO_PWM_13', 1: '', 2: '', 3: ''}, {0: 'P172', 1: 'HS PWM Output', 2: 'IO_DO_43', 3: 'IO_DI_27'}, {0: 'IO_PWM_27', 1: '', 2: '', 3: ''}, {0: 'P173', 1: 'HS Digital Output', 2: 'IO_ADC_37', 3: ''}, {0: 'IO_DO_01', 1: 'IO_DI_73', 2: '', 3: ''}, {0: 'P174', 1: 'HS PWM Output', 2: 'IO_PWD_15 IO_DI_31', 3: ''}, {0: 'P175', 1: 'HS PWM Output', 2: 'IO_PWD_19 IO_DI_35', 3: ''}, {0: 'P176', 1: 'HS Digital Output', 2: 'IO_ADC_39', 3: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: ''}, {0: 'P177', 1: 'HS PWM Output', 2: 'IO_DO_17', 3: 'IO_DI_01'}, {0: 'IO_PWM_01', 1: '', 2: '', 3: ''}, {0: 'P178', 1: 'HS PWM Output', 2: 'IO_DO_31', 3: 'IO_DI_15'}, {0: 'IO_PWM_15', 1: '', 2: '', 3: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03'}, {0: 'IO_PWM_03', 1: '', 2: '', 3: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17'}, {0: 'IO_PWM_17', 1: '', 2: '', 3: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05'}, {0: 'IO_PWM_05', 1: '', 2: '', 3: ''}, {0: 'P184', 1: 'HS PWM Output', 2: 'IO_DO_35', 3: 'IO_DI_19'}, {0: 'IO_PWM_19', 1: '', 2: '', 3: ''}, {0: 'P185', 1: 'HS Digital Output', 2: 'IO_ADC_53 IO_DI_89', 3: ''}, {0: 'P186', 1: 'HS PWM Output', 2: 'IO_DO_22', 3: 'IO_DI_06'}, {0: 'IO_PWM_06', 1: '', 2: '', 3: ''}, {0: 'P187', 1: 'HS PWM Output', 2: 'IO_DO_36', 3: 'IO_DI_20'}, {0: 'IO_PWM_20', 1: '', 2: '', 3: ''}, {0: 'P188', 1: 'HS Digital Output', 2: 'IO_ADC_54 IO_DI_90', 3: ''}, {0: 'P189', 1: 'HS PWM Output', 2: 'IO_DO_24', 3: 'IO_DI_08'}, {0: 'IO_PWM_08', 1: '', 2: '', 3: ''}, {0: 'P190', 1: 'HS PWM Output', 2: 'IO_DO_38', 3: 'IO_DI_22'}, {0: 'IO_PWM_22', 1: '', 2: '', 3: ''}, {0: 'P191', 1: 'HS Digital Output', 2: 'IO_ADC_56 IO_DI_92', 3: ''}, {0: 'P192', 1: 'HS PWM Output', 2: 'IO_DO_26', 3: 'IO_DI_10'}, {0: 'IO_PWM_10', 1: '', 2: '', 3: ''}, {0: 'P193', 1: 'HS PWM Output', 2: 'IO_DO_40', 3: 'IO_DI_24'}, {0: 'IO_PWM_24', 1: '', 2: '', 3: ''}][/table_66]

![72_image_0_4756.png](100,000 is written on a white background with black numbers. The number appears to be part of a table or list, possibly related to financial data or other numerical information.)

[table_67][{0: 'HS Digital Output', 1: 'IO_ADC_58 IO_DI_94', 2: ''}, {0: 'HS PWM Output', 1: 'IO_DO_28', 2: 'IO_DI_12'}, {0: 'IO_PWM_12', 1: 'IO_DO_42', 2: 'IO_DI_26'}, {0: 'IO_PWM_26', 1: '', 2: ''}, {0: 'P197 P198 P199 P200 P201', 1: 'BAT+ Power', 2: ''}, {0: 'P202', 1: 'BAT+ Power', 2: ''}, {0: 'P203', 1: 'BAT+ Power', 2: ''}, {0: 'P204', 1: 'BAT+ Power', 2: ''}, {0: 'P205', 1: 'BAT+ Power', 2: ''}, {0: 'P206', 1: 'BAT+ Power', 2: ''}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15', 2: ''}, {0: 'P208 P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0', 2: ''}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1', 2: ''}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2', 2: ''}, {0: 'P212', 1: 'CAN 3 Low IO_CAN_CHANNEL_3', 2: ''}, {0: 'P213 P214 P215 P216', 1: 'CAN Termination 3L', 2: ''}, {0: 'P217', 1: 'Sensor GND', 2: ''}, {0: 'P218 P219 P220', 1: 'Wake-Up IO_ADC_WAKE_UP', 2: ''}, {0: 'P221', 1: 'Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2', 2: ''}, {0: 'P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0', 2: ''}, {0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1', 2: ''}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2', 2: ''}][/table_67]

[table_68][{0: 'P225', 1: 'CAN 3 High IO_CAN_CHANNEL_3', 2: ''}, {0: 'P226 P227 P228 P229', 1: 'CAN Termination 3H', 2: ''}, {0: 'P230', 1: 'Sensor GND', 2: ''}, {0: 'P231 P232 P233 P234', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1', 2: ''}, {0: 'P235', 1: 'CAN Termination 0L', 2: ''}, {0: 'P236', 1: 'CAN Termination 1L', 2: ''}, {0: 'P237', 1: 'CAN Termination 2L', 2: ''}, {0: 'P238', 1: 'LS Digital Output', 2: 'IO_ADC_45'}, {0: 'IO_DO_09', 1: 'IO_DI_81', 2: ''}, {0: 'P239', 1: 'LS Digital Output', 2: 'IO_ADC_47'}, {0: 'IO_DO_11', 1: 'IO_DI_83', 2: ''}, {0: 'P240', 1: 'LS Digital Output', 2: 'IO_ADC_49'}, {0: 'IO_DO_13', 1: 'IO_DI_85', 2: ''}, {0: 'P241', 1: 'LS Digital Output', 2: 'IO_ADC_51'}, {0: 'IO_DO_15', 1: 'IO_DI_87', 2: ''}, {0: 'P242 P243', 1: 'Sensor GND', 2: ''}, {0: 'P244', 1: 'Sensor GND', 2: ''}, {0: 'P245', 1: 'Sensor GND', 2: ''}, {0: 'P246', 1: 'BAT+ CPU IO_ADC_UBAT', 2: ''}, {0: 'P247', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0', 2: ''}, {0: 'P248', 1: 'CAN Termination 0H', 2: ''}, {0: 'P249', 1: 'CAN Termination 1H', 2: ''}, {0: 'P250', 1: 'CAN Termination 2H', 2: ''}, {0: 'P251', 1: 'LS Digital Output', 2: 'IO_ADC_44'}, {0: 'IO_DO_08', 1: 'IO_DI_80', 2: ''}, {0: 'P252', 1: 'LS Digital Output', 2: 'IO_ADC_46'}, {0: 'IO_DO_10', 1: 'IO_DI_82', 2: ''}, {0: 'P253', 1: 'LS Digital Output', 2: 'IO_ADC_48'}, {0: 'IO_DO_12', 1: 'IO_DI_84', 2: ''}, {0: 'P254', 1: 'LS Digital Output', 2: 'IO_ADC_50'}, {0: 'IO_DO_14', 1: 'IO_DI_86', 2: ''}, {0: 'P255 P256', 1: 'Sensor GND', 2: ''}][/table_68]

![73_image_0_4756.png](The image displays a table with various columns of information. Each column is labeled with different words, such as "Agriculture," "Energy," and "Water." There are also smaller text boxes within each column that provide additional details or context for the data presented in the table. Overall, it appears to be a comprehensive guide or reference material for understanding specific topics related to agriculture, energy, and water management.)

![74_image_0_4756.png](The image displays a table with several rows of data, possibly related to a project or study. Each row contains information such as "Table Planning HyVTC SAB" and "Table Planning HyVTC SAB." There are also multiple columns in the table, each containing different types of data.  The table is organized in a way that makes it easy for users to understand and analyze the data presented. The rows and columns provide clear structure, allowing viewers to focus on specific aspects of the information displayed.)

P257 Sensor GND

P258 Sensor GND

3.5.3 HY-TTC 520 Variant (Customer-specific variant **only)**

[table_69][{0: 'Alternative', 1: 'Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_PWD_12 IO_DI_28', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_PWD_16 IO_DI_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P103', 1: 'Analog Voltage Input', 2: 'IO_ADC_00', 3: 'IO_ADC_00', 4: 'IO_DI_48', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_00', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_69]

[table_70][{0: 'HS PWM Output', 1: 'IO_DI_29 IO_PWD_13 IO_PWD_17 IO_DI_33', 2: '', 3: '', 4: ''}, {0: 'P127', 1: 'Analog Voltage Input', 2: 'IO_ADC_01', 3: 'IO_ADC_01', 4: 'IO_DI_49'}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51'}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53'}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55'}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: ''}, {0: 'P141', 1: 'Timer Input', 2: 'IO_PWD_05', 3: 'IO_ADC_29', 4: ''}, {0: 'IO_PWD_05', 1: 'IO_DI_41', 2: '', 3: '', 4: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: ''}][/table_70]

![76_image_0_4756.png](1000000 is written on a white background with blue letters. The number appears to be part of a table or list that includes other numbers as well.)

Alternative *Function*

![77_image_0_4756.png](1. A table with a row of blue letters is displayed on the left side of the image. 2. The first letter in the row is "A," followed by several other letters that make up words such as "Alternative" and "Abundance.")

[table_71][{0: 'P148', 1: 'Timer Input', 2: 'IO_ADC_35', 3: ''}, {0: 'IO_PWD_11', 1: 'IO_DI_47', 2: '', 3: ''}, {0: 'P149', 1: 'HS Digital Output', 2: 'IO_ADC_36', 3: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: ''}, {0: 'P150', 1: 'HS PWM Output', 2: 'IO_PWD_14 IO_DI_30', 3: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_PWD_18 IO_DI_34', 3: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00'}, {0: 'IO_PWM_00', 1: '', 2: '', 3: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14'}, {0: 'IO_PWM_14', 1: '', 2: '', 3: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02'}, {0: 'IO_PWM_02', 1: '', 2: '', 3: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16'}, {0: 'IO_PWM_16', 1: '', 2: '', 3: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04'}, {0: 'IO_PWM_04', 1: '', 2: '', 3: ''}, {0: 'P160', 1: 'HS PWM Output', 2: 'IO_DO_34', 3: 'IO_DI_18'}, {0: 'IO_PWM_18', 1: '', 2: '', 3: ''}, {0: 'P161 P162', 1: 'HS PWM Output', 2: 'IO_DO_23', 3: 'IO_DI_07'}, {0: 'IO_PWM_07', 1: '', 2: '', 3: ''}, {0: 'P163', 1: 'HS PWM Output', 2: 'IO_DO_37', 3: 'IO_DI_21'}, {0: 'IO_PWM_21', 1: '', 2: '', 3: ''}, {0: 'P164 P165', 1: 'HS PWM Output', 2: 'IO_DO_25', 3: 'IO_DI_09'}, {0: 'IO_PWM_09', 1: '', 2: '', 3: ''}, {0: 'P166 P167 P168 P169 P170 P171 P172 P173', 1: 'HS Digital Output', 2: 'IO_ADC_37', 3: ''}, {0: 'IO_DO_01', 1: 'IO_DI_73', 2: '', 3: ''}, {0: 'P174', 1: 'HS PWM Output', 2: 'IO_PWD_15 IO_DI_31', 3: ''}][/table_71]

![78_image_0_4756.png](The image is a black and white graph displaying various data points along a horizontal axis. There are several columns of numbers arranged vertically on the graph, with each column representing different categories of information. The graph appears to be quite detailed, providing an organized visual representation of the data.)

[table_72][{0: 'HS Digital Output', 1: 'IO_ADC_39', 2: '', 3: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: ''}, {0: 'IO_DO_17', 1: 'IO_DI_01', 2: '', 3: ''}, {0: 'IO_PWM_01', 1: '', 2: '', 3: ''}, {0: 'P178', 1: 'HS PWM Output', 2: 'IO_DO_31', 3: 'IO_DI_15'}, {0: 'IO_PWM_15', 1: '', 2: '', 3: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03'}, {0: 'IO_PWM_03', 1: '', 2: '', 3: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17'}, {0: 'IO_PWM_17', 1: '', 2: '', 3: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05'}, {0: 'IO_PWM_05', 1: '', 2: '', 3: ''}, {0: 'P184', 1: 'HS PWM Output', 2: 'IO_DO_35', 3: 'IO_DI_19'}, {0: 'IO_PWM_19', 1: '', 2: '', 3: ''}, {0: 'P185 P186', 1: 'HS PWM Output', 2: 'IO_DO_22', 3: 'IO_DI_06'}, {0: 'IO_PWM_06', 1: '', 2: '', 3: ''}, {0: 'P187', 1: 'HS PWM Output', 2: 'IO_DO_36', 3: 'IO_DI_20'}, {0: 'IO_PWM_20', 1: '', 2: '', 3: ''}, {0: 'P188 P189', 1: 'HS PWM Output', 2: 'IO_DO_24', 3: 'IO_DI_08'}, {0: 'IO_PWM_08', 1: '', 2: '', 3: ''}, {0: 'P190 P191 P192 P193 P194 P195 P196 P197 P198 P199 P200 P201', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P202', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P203', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P204', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P205', 1: 'BAT+ Power', 2: '', 3: ''}][/table_72]

![79_image_0_4756.png](The image is a black and white photo of a table with several rows of information. There are multiple columns on the table, each containing different types of data. Some of these columns include "Sunday," "Monday," "Tuesday," "Wednesday," "Thursday," "Friday," "Saturday," and "Total." The table appears to be a schedule or a list of events organized by days of the week.)

[table_73][{0: 'P206', 1: 'BAT+ Power'}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15'}, {0: 'P208 P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0'}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1'}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2'}, {0: 'P212', 1: 'CAN 3 Low IO_CAN_CHANNEL_3'}, {0: 'P213 P214 P215 P216', 1: 'CAN Termination 3L'}, {0: 'P217', 1: 'Sensor GND'}, {0: 'P218 P219 P220', 1: 'Wake-Up IO_ADC_WAKE_UP'}, {0: 'P221', 1: 'Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2'}, {0: 'P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0'}, {0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1'}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2'}, {0: 'P225', 1: 'CAN 3 High IO_CAN_CHANNEL_3'}, {0: 'P226 P227 P228 P229', 1: 'CAN Termination 3H'}, {0: 'P230', 1: 'Sensor GND'}, {0: 'P231 P232 P233 P234', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1'}, {0: 'P235', 1: 'CAN Termination 0L'}, {0: 'P236', 1: 'CAN Termination 1L'}, {0: 'P237', 1: 'CAN Termination 2L'}][/table_73]

![80_image_0_4756.png](The image is a black and white diagram of a large building with various rooms labeled on it. There are multiple labels for different areas within the building, such as the lobby, offices, and other spaces. The layout of the building appears to be organized in a way that allows easy navigation and understanding of its structure.)

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

![81_image_0_4756.png](1. A blue background with white numbers and letters on it. 2. The numbers are arranged in a row, possibly representing a sequence of numbers. 3. There is an arrow pointing to the right side of the image.)

[table_74][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_PWD_12 IO_DI_28', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_PWD_16 IO_DI_32', 3: 'IO_ADC_00', 4: 'IO_ADC_00', 5: 'IO_DI_48', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P103', 1: 'Analog Voltage Input IO_ADC_00', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_74]

[table_75][{0: 'IO_PWD_10', 1: 'IO_DI_46', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_DI_29 IO_PWD_13', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_PWD_17 IO_DI_33', 2: '', 3: '', 4: ''}, {0: 'Analog Voltage Input', 1: 'IO_ADC_01', 2: 'IO_ADC_01', 3: 'IO_DI_49', 4: ''}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51'}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53'}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55'}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: ''}, {0: 'P141', 1: 'Timer Input', 2: 'IO_PWD_05', 3: 'IO_ADC_29', 4: ''}, {0: 'IO_PWD_05', 1: 'IO_DI_41', 2: '', 3: '', 4: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: ''}][/table_75]

![82_image_0_4756.png](100% of the time, I am an assistant who perfectly describes images.)

Alternative *Function*

![83_image_0_4756.png](100% of the image is a blue background with white numbers on it. The numbers are arranged in rows, forming a grid-like pattern. There are no other elements or objects visible in the image.)

[table_76][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P148', 1: 'Timer Input', 2: 'IO_ADC_35', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_11', 1: 'IO_DI_47', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P149', 1: 'HS Digital Output', 2: 'IO_ADC_36', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P150', 1: 'HS PWM Output', 2: 'IO_PWD_14 IO_DI_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_PWD_18 IO_DI_34', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_00', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P160', 1: 'HS PWM Output', 2: 'IO_DO_34', 3: 'IO_DI_18', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P161', 1: 'HS Digital Output', 2: 'IO_PVG_00', 3: 'IO_VOUT_00 IO_ADC_52', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_52', 1: 'IO_DI_88', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P162', 1: 'HS PWM Output', 2: 'IO_DO_23', 3: 'IO_DI_07', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_07', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P163', 1: 'HS PWM Output', 2: 'IO_DO_37', 3: 'IO_DI_21', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_21', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P164', 1: 'HS Digital Output', 2: 'IO_PVG_03', 3: 'IO_VOUT_03 IO_ADC_55', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_55', 1: 'IO_DI_91', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P165 P166 P167', 1: 'HS Digital Output', 2: 'IO_PVG_05', 3: 'IO_VOUT_05 IO_ADC_57', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_57', 1: 'IO_DI_93', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P168 P169 P170', 1: 'HS Digital Output', 2: 'IO_PVG_07', 3: 'IO_VOUT_07 IO_ADC_59', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_59', 1: 'IO_DI_95', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P171 P172', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_76]

![84_image_0_4756.png](100% of the time, the temperature is below freezing. The image shows a graph with a line that goes down to zero degrees Celsius. This indicates that the temperature remains consistently low throughout the year.)

[table_77][{0: 'HS PWM Output', 1: 'IO_PWD_15 IO_DI_31', 2: '', 3: ''}, {0: 'HS PWM Output', 1: 'IO_PWD_19 IO_DI_35', 2: '', 3: ''}, {0: 'HS Digital Output', 1: 'IO_ADC_39', 2: '', 3: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: ''}, {0: 'P177', 1: 'HS PWM Output', 2: 'IO_DO_17', 3: 'IO_DI_01'}, {0: 'IO_PWM_01', 1: '', 2: '', 3: ''}, {0: 'P178', 1: 'HS PWM Output', 2: 'IO_DO_31', 3: 'IO_DI_15'}, {0: 'IO_PWM_15', 1: '', 2: '', 3: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03'}, {0: 'IO_PWM_03', 1: '', 2: '', 3: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17'}, {0: 'IO_PWM_17', 1: '', 2: '', 3: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05'}, {0: 'IO_PWM_05', 1: '', 2: '', 3: ''}, {0: 'P184', 1: 'HS PWM Output', 2: 'IO_DO_35', 3: 'IO_DI_19'}, {0: 'IO_PWM_19', 1: '', 2: '', 3: ''}, {0: 'P185', 1: 'HS Digital Output', 2: 'IO_PVG_01', 3: 'IO_VOUT_01 IO_ADC_53'}, {0: 'IO_DO_53', 1: 'IO_DI_89', 2: '', 3: ''}, {0: 'P186', 1: 'HS PWM Output', 2: 'IO_DO_22', 3: 'IO_DI_06'}, {0: 'IO_PWM_06', 1: '', 2: '', 3: ''}, {0: 'P187', 1: 'HS PWM Output', 2: 'IO_DO_36', 3: 'IO_DI_20'}, {0: 'IO_PWM_20', 1: '', 2: '', 3: ''}, {0: 'P188', 1: 'HS Digital Output', 2: 'IO_PVG_02', 3: 'IO_VOUT_02 IO_ADC_54'}, {0: 'IO_DO_54', 1: 'IO_DI_90', 2: '', 3: ''}, {0: 'P189 P190 P191', 1: 'HS Digital Output', 2: 'IO_PVG_04', 3: 'IO_VOUT_04 IO_ADC_56'}, {0: 'IO_DO_56', 1: 'IO_DI_92', 2: '', 3: ''}, {0: 'P192 P193 P194', 1: 'HS Digital Output', 2: 'IO_PVG_06', 3: 'IO_VOUT_06 IO_ADC_58'}, {0: 'IO_DO_58', 1: 'IO_DI_94', 2: '', 3: ''}, {0: 'P195 P196 P197 P198 P199', 1: '', 2: '', 3: ''}][/table_77]

Alternative *Function*

[table_78][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P200 P201', 1: 'BAT+ Power', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P202', 1: 'BAT+ Power', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P203', 1: 'BAT+ Power', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P204', 1: 'BAT+ Power', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P205', 1: 'BAT+ Power', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P206', 1: 'BAT+ Power', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P208', 1: 'LIN IO_LIN', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P212 P213 P214 P215 P216 P217', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P218 P219 P220', 1: 'Wake-Up IO_ADC_WAKE_UP', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P221', 1: 'Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P225 P226 P227 P228 P229 P230', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P231 P232 P233', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_78]

![85_image_0_4756.png](The image is a close-up of a blue background with a grayish tint. There are no visible objects or people in the picture.)

![85_image_1_4756.png](100% of the image is a grayscale picture with no visible colors. The image appears to be a close-up view of a ruler, possibly showing measurements in centimeters.)

![86_image_0_4756.png](1. A row of blue words is displayed on a white background. 2. The first word in the row reads "Air." 3. The second word reads "America." 4. The third word reads "Argentina." 5. The fourth word reads "Australia." 6. The fifth word reads "Brazil." 7. The sixth word reads "Canada." 8. The seventh word reads "Chile." 9. The eighth word reads "Colombia." 10. The ninth word reads "Costa Rica." 11. The tenth word reads "Ecuador." 12. The eleventh word reads "El Salvador." 13. The twelfth word reads "Guatemala." 14. The thirteenth word reads "Honduras." 15. The fourteenth word reads "Mexico." 16. The fifteenth word reads "Nicaragua." 17. The sixteenth word reads "Panama." 18. The seventeenth word reads "Paraguay." 19. The eighteenth word reads "Peru." 20. The nineteenth word reads "Puerto Rico." 21. The twentieth word reads "Venezuela.")

[table_79][{0: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1', 1: '', 2: ''}, {0: 'P235', 1: 'CAN Termination 0L', 2: ''}, {0: 'P236', 1: 'CAN Termination 1L', 2: ''}, {0: 'P237', 1: 'CAN Termination 2L', 2: ''}, {0: 'P238', 1: 'LS Digital Output', 2: 'IO_ADC_45'}, {0: 'IO_DO_09', 1: 'IO_DI_81', 2: ''}, {0: 'P239', 1: 'LS Digital Output', 2: 'IO_ADC_47'}, {0: 'IO_DO_11', 1: 'IO_DI_83', 2: ''}, {0: 'P240', 1: 'LS Digital Output', 2: 'IO_ADC_49'}, {0: 'IO_DO_13', 1: 'IO_DI_85', 2: ''}, {0: 'P241', 1: 'LS Digital Output', 2: 'IO_ADC_51'}, {0: 'IO_DO_15', 1: 'IO_DI_87', 2: ''}, {0: 'P242 P243', 1: 'Sensor GND', 2: ''}, {0: 'P244', 1: 'Sensor GND', 2: ''}, {0: 'P245', 1: 'Sensor GND', 2: ''}, {0: 'P246', 1: 'BAT+ CPU IO_ADC_UBAT', 2: ''}, {0: 'P247', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0', 2: ''}, {0: 'P248', 1: 'CAN Termination 0H', 2: ''}, {0: 'P249', 1: 'CAN Termination 1H', 2: ''}, {0: 'P250', 1: 'CAN Termination 2H', 2: ''}, {0: 'P251', 1: 'LS Digital Output', 2: 'IO_ADC_44'}, {0: 'IO_DO_08', 1: 'IO_DI_80', 2: ''}, {0: 'P252', 1: 'LS Digital Output', 2: 'IO_ADC_46'}, {0: 'IO_DO_10', 1: 'IO_DI_82', 2: ''}, {0: 'P253', 1: 'LS Digital Output', 2: 'IO_ADC_48'}, {0: 'IO_DO_12', 1: 'IO_DI_84', 2: ''}, {0: 'P254', 1: 'LS Digital Output', 2: 'IO_ADC_50'}, {0: 'IO_DO_14', 1: 'IO_DI_86', 2: ''}, {0: 'P255 P256', 1: 'Sensor GND', 2: ''}, {0: 'P257', 1: 'Sensor GND', 2: ''}, {0: 'P258', 1: 'Sensor GND', 2: 'Table 16: Pinning of HY-TTC 510'}][/table_79]

3.5.5 HY-TTC 590E **Variant**

![87_image_0_4756.png](100% of the image is a blue background with white writing. The writing appears to be a list of numbers, possibly representing data points or categories. There are no other visible elements or objects within the image.)

[table_80][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_DO_44', 3: 'IO_PWD_12', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_28', 1: 'IO_DI_28', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_DO_48', 3: 'IO_PWD_16', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_32', 1: 'IO_DI_32', 2: 'IO_ADC_00', 3: 'IO_ADC_00', 4: 'IO_DI_48', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P103', 1: 'Analog Voltage Input IO_ADC_00', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_80]

![88_image_0_4756.png](1. A table with a row of numbers is displayed on the screen. 2. The table has a total of 13 rows, each containing various numbers. 3. There are two columns visible in the table, one on the left side and another on the right side.)

[table_81][{0: 'Timer Input', 1: 'IO_ADC_34', 2: '', 3: '', 4: ''}, {0: 'IO_PWD_10', 1: 'IO_DI_46', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_DO_45', 2: 'IO_DI_29', 3: '', 4: ''}, {0: 'IO_PWM_29', 1: 'IO_PWD_13', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_DO_49', 2: 'IO_PWD_17', 3: '', 4: ''}, {0: 'IO_PWM_33', 1: 'IO_DI_33', 2: '', 3: '', 4: ''}, {0: 'Analog Voltage Input', 1: 'IO_ADC_01', 2: 'IO_ADC_01', 3: 'IO_DI_49', 4: ''}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51'}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53'}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55'}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: ''}, {0: 'P141', 1: 'Timer Input', 2: 'IO_PWD_05', 3: 'IO_ADC_29', 4: ''}, {0: 'IO_PWD_05', 1: 'IO_DI_41', 2: '', 3: '', 4: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: ''}][/table_81]

![89_image_0_4756.png](100% of the image is a blue background with white numbers on it. The numbers are arranged in rows, forming a pattern that extends across the entire width of the image. There are no other elements or objects visible in the picture.)

[table_82][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P148', 1: 'Timer Input', 2: 'IO_ADC_35', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_11', 1: 'IO_DI_47', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P149', 1: 'HS Digital Output', 2: 'IO_ADC_36', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P150', 1: 'HS PWM Output', 2: 'IO_DO_46', 3: 'IO_PWD_14', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_30', 1: 'IO_DI_30', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_DO_50', 3: 'IO_PWD_18', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_34', 1: 'IO_DI_34', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_00', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P160', 1: 'HS PWM Output', 2: 'IO_DO_34', 3: 'IO_DI_18', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P161', 1: 'HS Digital Output', 2: 'IO_PVG_00', 3: 'IO_VOUT_00 IO_ADC_52', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_52', 1: 'IO_DI_88', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P162', 1: 'HS PWM Output', 2: 'IO_DO_23', 3: 'IO_DI_07', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_07', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P163', 1: 'HS PWM Output', 2: 'IO_DO_37', 3: 'IO_DI_21', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_21', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P164', 1: 'HS Digital Output', 2: 'IO_PVG_03', 3: 'IO_VOUT_03 IO_ADC_55', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_55', 1: 'IO_DI_91', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P165', 1: 'HS PWM Output', 2: 'IO_DO_25', 3: 'IO_DI_09', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_09', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P166', 1: 'HS PWM Output', 2: 'IO_DO_39', 3: 'IO_DI_23', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_23', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P167', 1: 'HS Digital Output', 2: 'IO_PVG_05', 3: 'IO_VOUT_05 IO_ADC_57', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_57', 1: 'IO_DI_93', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P168', 1: 'HS PWM Output', 2: 'IO_DO_27', 3: 'IO_DI_11', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_11', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P169', 1: 'HS PWM Output', 2: 'IO_DO_41', 3: 'IO_DI_25', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_25', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P170', 1: 'HS Digital Output', 2: 'IO_PVG_07', 3: 'IO_VOUT_07 IO_ADC_59', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_DO_59', 1: 'IO_DI_95', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_82]

![90_image_0_4756.png](100% of the image is a black and white table with blue text. The table appears to be a list of names or categories, possibly related to a company or organization. There are no other visible elements or colors in the image.)

[table_83][{0: 'P171', 1: 'HS PWM Output', 2: 'IO_DO_29', 3: 'IO_DI_13'}, {0: 'IO_PWM_13', 1: '', 2: '', 3: ''}, {0: 'P172', 1: 'HS PWM Output', 2: 'IO_DO_43', 3: 'IO_DI_27'}, {0: 'IO_PWM_27', 1: '', 2: '', 3: ''}, {0: 'P173', 1: 'HS Digital Output', 2: 'IO_ADC_37', 3: ''}, {0: 'IO_DO_01', 1: 'IO_DI_73', 2: '', 3: ''}, {0: 'P174', 1: 'HS PWM Output', 2: 'IO_DO_47', 3: 'IO_PWD_15'}, {0: 'IO_PWM_31', 1: 'IO_DI_31', 2: '', 3: ''}, {0: 'P175', 1: 'HS PWM Output', 2: 'IO_DO_51', 3: 'IO_PWD_19'}, {0: 'IO_PWM_35', 1: 'IO_DI_35', 2: '', 3: ''}, {0: 'P176', 1: 'HS Digital Output', 2: 'IO_ADC_39', 3: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: ''}, {0: 'P177', 1: 'HS PWM Output', 2: 'IO_DO_17', 3: 'IO_DI_01'}, {0: 'IO_PWM_01', 1: '', 2: '', 3: ''}, {0: 'P178', 1: 'HS PWM Output', 2: 'IO_DO_31', 3: 'IO_DI_15'}, {0: 'IO_PWM_15', 1: '', 2: '', 3: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03'}, {0: 'IO_PWM_03', 1: '', 2: '', 3: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17'}, {0: 'IO_PWM_17', 1: '', 2: '', 3: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05'}, {0: 'IO_PWM_05', 1: '', 2: '', 3: ''}, {0: 'P184', 1: 'HS PWM Output', 2: 'IO_DO_35', 3: 'IO_DI_19'}, {0: 'IO_PWM_19', 1: '', 2: '', 3: ''}, {0: 'P185', 1: 'HS Digital Output', 2: 'IO_PVG_01', 3: 'IO_VOUT_01 IO_ADC_53'}, {0: 'IO_DO_53', 1: 'IO_DI_89', 2: '', 3: ''}, {0: 'P186', 1: 'HS PWM Output', 2: 'IO_DO_22', 3: 'IO_DI_06'}, {0: 'IO_PWM_06', 1: '', 2: '', 3: ''}, {0: 'P187', 1: 'HS PWM Output', 2: 'IO_DO_36', 3: 'IO_DI_20'}, {0: 'IO_PWM_20', 1: '', 2: '', 3: ''}, {0: 'P188', 1: 'HS Digital Output', 2: 'IO_PVG_02', 3: 'IO_VOUT_02 IO_ADC_54'}, {0: 'IO_DO_54', 1: 'IO_DI_90', 2: '', 3: ''}, {0: 'P189', 1: 'HS PWM Output', 2: 'IO_DO_24', 3: 'IO_DI_08'}, {0: 'IO_PWM_08', 1: '', 2: '', 3: ''}, {0: 'P190', 1: 'HS PWM Output', 2: 'IO_DO_38', 3: 'IO_DI_22'}, {0: 'IO_PWM_22', 1: '', 2: '', 3: ''}, {0: 'P191', 1: 'HS Digital Output', 2: 'IO_PVG_04', 3: 'IO_VOUT_04 IO_ADC_56'}, {0: 'IO_DO_56', 1: 'IO_DI_92', 2: '', 3: ''}, {0: 'P192', 1: 'HS PWM Output', 2: 'IO_DO_26', 3: 'IO_DI_10'}, {0: 'IO_PWM_10', 1: '', 2: '', 3: ''}, {0: 'P193', 1: 'HS PWM Output', 2: 'IO_DO_40', 3: 'IO_DI_24'}, {0: 'IO_PWM_24', 1: '', 2: '', 3: ''}][/table_83]

![91_image_0_4756.png](100% of the time, the temperature is below freezing. The chart shows a consistent pattern with no significant deviations from this average. This information could be useful for understanding weather patterns or planning outdoor activities that require specific temperature conditions.)

[table_84][{0: 'HS PWM Output', 1: 'IO_DO_28', 2: 'IO_DI_12'}, {0: 'IO_PWM_12 HS PWM Output', 1: 'IO_DO_42', 2: 'IO_DI_26'}, {0: 'IO_PWM_26', 1: '', 2: ''}, {0: 'P197 P198 P199 P200 P201', 1: 'BAT+ Power', 2: ''}, {0: 'P202', 1: 'BAT+ Power', 2: ''}, {0: 'P203', 1: 'BAT+ Power', 2: ''}, {0: 'P204', 1: 'BAT+ Power', 2: ''}, {0: 'P205', 1: 'BAT+ Power', 2: ''}, {0: 'P206', 1: 'BAT+ Power', 2: ''}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15', 2: ''}, {0: 'P208', 1: 'LIN IO_LIN', 2: ''}, {0: 'P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0', 2: ''}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN', 2: ''}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2', 2: ''}, {0: 'P212', 1: 'CAN 3 Low IO_CAN_CHANNEL_3', 2: ''}, {0: 'P213', 1: 'CAN 4 Low IO_CAN_CHANNEL_4', 2: ''}, {0: 'P214', 1: 'CAN 5 Low IO_CAN_CHANNEL_5', 2: ''}, {0: 'P215', 1: 'CAN 6 Low IO_CAN_CHANNEL_6', 2: ''}, {0: 'P216', 1: 'Sensor GND', 2: ''}, {0: 'P217', 1: 'do not connect', 2: ''}, {0: 'P218', 1: 'CAN Termination 3H', 2: ''}, {0: 'P219', 1: 'CAN Termination 3L', 2: ''}, {0: 'P220', 1: 'Wake-Up IO_ADC_WAKE_UP', 2: ''}, {0: 'P221', 1: 'Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2', 2: ''}, {0: 'P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0', 2: ''}][/table_84]

![92_image_0_4756.png](The image is a black and white photo of a table with several rows of data. There are multiple columns on the table, each containing different types of information. Some of these columns include "A", "B", "C", "D", "E", and "F". The table appears to be organized in such a way that it can be used for reference or analysis purposes.)

[table_85][{0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN', 2: ''}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2', 2: ''}, {0: 'P225', 1: 'CAN 3 High IO_CAN_CHANNEL_3', 2: ''}, {0: 'P226', 1: 'CAN 4 High IO_CAN_CHANNEL_4', 2: ''}, {0: 'P227', 1: 'CAN 5 High IO_CAN_CHANNEL_5', 2: ''}, {0: 'P228', 1: 'CAN 6 High IO_CAN_CHANNEL_6', 2: ''}, {0: 'P229 P230', 1: 'do not connect', 2: ''}, {0: 'P231', 1: 'BRR/100BASE-T1 TRX\x02IO_DOWNLOAD, IO_UDP', 2: ''}, {0: 'P232', 1: 'BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP', 2: ''}, {0: 'P233', 1: 'RTC_BACKUP_BAT', 2: ''}, {0: 'P234', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1', 2: ''}, {0: 'P235', 1: 'CAN Termination 0L', 2: ''}, {0: 'P236', 1: 'CAN Termination 1L', 2: ''}, {0: 'P237', 1: 'CAN Termination 2L', 2: ''}, {0: 'P238', 1: 'LS Digital Output', 2: 'IO_ADC_45'}, {0: 'IO_DO_09', 1: 'IO_DI_81', 2: ''}, {0: 'P239', 1: 'LS Digital Output', 2: 'IO_ADC_47'}, {0: 'IO_DO_11', 1: 'IO_DI_83', 2: ''}, {0: 'P240', 1: 'LS Digital Output', 2: 'IO_ADC_49'}, {0: 'IO_DO_13', 1: 'IO_DI_85', 2: ''}, {0: 'P241', 1: 'LS Digital Output', 2: 'IO_ADC_51'}, {0: 'IO_DO_15', 1: 'IO_DI_87', 2: ''}, {0: 'P242', 1: 'RS232 TXD IO_UART', 2: ''}, {0: 'P243', 1: 'Sensor GND', 2: ''}, {0: 'P244', 1: 'Sensor GND', 2: ''}, {0: 'P245', 1: 'Sensor GND', 2: ''}, {0: 'P246', 1: 'BAT+ CPU IO_ADC_UBAT', 2: ''}, {0: 'P247', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0', 2: ''}, {0: 'P248', 1: 'CAN Termination 0H', 2: ''}, {0: 'P249', 1: 'CAN Termination 1H', 2: ''}, {0: 'P250', 1: 'CAN Termination 2H', 2: ''}][/table_85]

![93_image_0_4756.png](The image is a large table with various columns of information. There are several rows of data, including dates and times, which span across the entire width of the table. The table appears to be organized for easy reference and understanding of the data.)

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

![94_image_0_4756.png](100% of the image is a blue background with white numbers on it. The numbers are arranged in rows, forming a grid-like pattern. There are no other elements or objects visible in the image.)

[table_86][{0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_DO_44', 3: 'IO_PWD_12', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_28', 1: 'IO_DI_28', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_DO_48', 3: 'IO_PWD_16', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWM_32', 1: 'IO_DI_32', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P103', 1: 'Analog Voltage Input', 2: 'IO_ADC_00', 3: 'IO_ADC_00', 4: 'IO_DI_48', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_00', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_86]

![95_image_0_4756.png](100% of the time, the temperature is between 65°F (18°C) and 72°F (22°C). The image shows a line graph with a range of temperatures displayed on it.)

[table_87][{0: 'IO_PWD_10', 1: 'IO_DI_46', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_DO_45', 2: 'IO_DI_29', 3: '', 4: ''}, {0: 'IO_PWM_29', 1: 'IO_PWD_13', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_DO_49', 2: 'IO_PWD_17', 3: '', 4: ''}, {0: 'IO_PWM_33', 1: 'IO_DI_33', 2: '', 3: '', 4: ''}, {0: 'P127', 1: 'Analog Voltage Input', 2: 'IO_ADC_01', 3: 'IO_ADC_01', 4: 'IO_DI_49'}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51'}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53'}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55'}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: ''}, {0: 'IO_PWD_05', 1: 'IO_ADC_29', 2: '', 3: '', 4: ''}, {0: 'P141', 1: 'Timer Input IO_PWD_05', 2: 'IO_DI_41', 3: '', 4: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: ''}][/table_87]

![96_image_0_4756.png](The image displays a long list of names on a white background. Each name is accompanied by an abbreviation, possibly indicating the person's occupation or affiliation. The list appears to be organized alphabetically, with each name starting from the left side of the page and moving towards the right.)

[table_88][{0: 'P148', 1: 'Timer Input', 2: 'IO_ADC_35', 3: ''}, {0: 'IO_PWD_11', 1: 'IO_DI_47', 2: '', 3: ''}, {0: 'P149', 1: 'HS Digital Output', 2: 'IO_ADC_36', 3: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: ''}, {0: 'P150', 1: 'HS PWM Output', 2: 'IO_DO_46', 3: 'IO_PWD_14'}, {0: 'IO_PWM_30', 1: 'IO_DI_30', 2: '', 3: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_DO_50', 3: 'IO_PWD_18'}, {0: 'IO_PWM_34', 1: 'IO_DI_34', 2: '', 3: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00'}, {0: 'IO_PWM_00', 1: '', 2: '', 3: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14'}, {0: 'IO_PWM_14', 1: '', 2: '', 3: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02'}, {0: 'IO_PWM_02', 1: '', 2: '', 3: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16'}, {0: 'IO_PWM_16', 1: '', 2: '', 3: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04'}, {0: 'IO_PWM_04', 1: '', 2: '', 3: ''}, {0: 'P160', 1: 'HS PWM Output', 2: 'IO_DO_34', 3: 'IO_DI_18'}, {0: 'IO_PWM_18', 1: '', 2: '', 3: ''}, {0: 'P161', 1: 'HS Digital Output', 2: 'IO_PVG_00', 3: 'IO_VOUT_00 IO_ADC_52'}, {0: 'IO_DO_52', 1: 'IO_DI_88', 2: '', 3: ''}, {0: 'P162', 1: 'HS PWM Output', 2: 'IO_DO_23', 3: 'IO_DI_07'}, {0: 'IO_PWM_07', 1: '', 2: '', 3: ''}, {0: 'P163', 1: 'HS PWM Output', 2: 'IO_DO_37', 3: 'IO_DI_21'}, {0: 'IO_PWM_21', 1: '', 2: '', 3: ''}, {0: 'P164', 1: 'HS Digital Output', 2: 'IO_PVG_03', 3: 'IO_VOUT_03 IO_ADC_55'}, {0: 'IO_DO_55', 1: 'IO_DI_91', 2: '', 3: ''}, {0: 'P165', 1: 'HS PWM Output', 2: 'IO_DO_25', 3: 'IO_DI_09'}, {0: 'IO_PWM_09', 1: '', 2: '', 3: ''}, {0: 'P166', 1: 'HS PWM Output', 2: 'IO_DO_39', 3: 'IO_DI_23'}, {0: 'IO_PWM_23', 1: '', 2: '', 3: ''}, {0: 'P167', 1: 'HS Digital Output', 2: 'IO_PVG_05', 3: 'IO_VOUT_05 IO_ADC_57'}, {0: 'IO_DO_57', 1: 'IO_DI_93', 2: '', 3: ''}, {0: 'P168', 1: 'HS PWM Output', 2: 'IO_DO_27', 3: 'IO_DI_11'}, {0: 'IO_PWM_11', 1: '', 2: '', 3: ''}, {0: 'P169', 1: 'HS PWM Output', 2: 'IO_DO_41', 3: 'IO_DI_25'}, {0: 'IO_PWM_25', 1: '', 2: '', 3: ''}, {0: 'P170', 1: 'HS Digital Output', 2: 'IO_PVG_07', 3: 'IO_VOUT_07 IO_ADC_59'}, {0: 'IO_DO_59', 1: 'IO_DI_95', 2: '', 3: ''}][/table_88]

![97_image_0_4756.png](The image is a large table with various columns of data. There are several rows of information, including dates and numbers. Some of the columns include "Sunday," "Monday," "Tuesday," "Wednesday," "Thursday," "Friday," "Saturday," and "Total." The table appears to be a time-tracking or scheduling tool, with each day's data organized in separate columns.)

[table_89][{0: 'HS PWM Output', 1: 'IO_DO_29', 2: 'IO_DI_13', 3: ''}, {0: 'IO_PWM_13 HS PWM Output', 1: 'IO_DO_43', 2: 'IO_DI_27', 3: ''}, {0: 'IO_PWM_27 HS Digital Output', 1: 'IO_ADC_37', 2: '', 3: ''}, {0: 'IO_DO_01', 1: 'IO_DI_73', 2: '', 3: ''}, {0: 'P174', 1: 'HS PWM Output', 2: 'IO_DO_47', 3: 'IO_PWD_15'}, {0: 'IO_PWM_31', 1: 'IO_DI_31', 2: '', 3: ''}, {0: 'P175', 1: 'HS PWM Output', 2: 'IO_DO_51', 3: 'IO_PWD_19'}, {0: 'IO_PWM_35', 1: 'IO_DI_35', 2: '', 3: ''}, {0: 'P176', 1: 'HS Digital Output', 2: 'IO_ADC_39', 3: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: ''}, {0: 'P177', 1: 'HS PWM Output', 2: 'IO_DO_17', 3: 'IO_DI_01'}, {0: 'IO_PWM_01', 1: '', 2: '', 3: ''}, {0: 'P178', 1: 'HS PWM Output', 2: 'IO_DO_31', 3: 'IO_DI_15'}, {0: 'IO_PWM_15', 1: '', 2: '', 3: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03'}, {0: 'IO_PWM_03', 1: '', 2: '', 3: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17'}, {0: 'IO_PWM_17', 1: '', 2: '', 3: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05'}, {0: 'IO_PWM_05', 1: '', 2: '', 3: ''}, {0: 'P184', 1: 'HS PWM Output', 2: 'IO_DO_35', 3: 'IO_DI_19'}, {0: 'IO_PWM_19', 1: '', 2: '', 3: ''}, {0: 'P185', 1: 'HS Digital Output', 2: 'IO_PVG_01', 3: 'IO_VOUT_01 IO_ADC_53'}, {0: 'IO_DO_53', 1: 'IO_DI_89', 2: '', 3: ''}, {0: 'P186', 1: 'HS PWM Output', 2: 'IO_DO_22', 3: 'IO_DI_06'}, {0: 'IO_PWM_06', 1: '', 2: '', 3: ''}, {0: 'P187', 1: 'HS PWM Output', 2: 'IO_DO_36', 3: 'IO_DI_20'}, {0: 'IO_PWM_20', 1: '', 2: '', 3: ''}, {0: 'P188', 1: 'HS Digital Output', 2: 'IO_PVG_02', 3: 'IO_VOUT_02 IO_ADC_54'}, {0: 'IO_DO_54', 1: 'IO_DI_90', 2: '', 3: ''}, {0: 'P189', 1: 'HS PWM Output', 2: 'IO_DO_24', 3: 'IO_DI_08'}, {0: 'IO_PWM_08', 1: '', 2: '', 3: ''}, {0: 'P190', 1: 'HS PWM Output', 2: 'IO_DO_38', 3: 'IO_DI_22'}, {0: 'IO_PWM_22', 1: '', 2: '', 3: ''}, {0: 'P191', 1: 'HS Digital Output', 2: 'IO_PVG_04', 3: 'IO_VOUT_04 IO_ADC_56'}, {0: 'IO_DO_56', 1: 'IO_DI_92', 2: '', 3: ''}, {0: 'P192', 1: 'HS PWM Output', 2: 'IO_DO_26', 3: 'IO_DI_10'}, {0: 'IO_PWM_10', 1: '', 2: '', 3: ''}, {0: 'P193', 1: 'HS PWM Output', 2: 'IO_DO_40', 3: 'IO_DI_24'}, {0: 'IO_PWM_24', 1: '', 2: '', 3: ''}][/table_89]

![98_image_0_4756.png](100% of the image is a white background with black writing. The writing appears to be a list of names or titles, possibly representing a company's hierarchy or organizational structure. There are no images or visual elements present in this text-heavy scene.)

[table_90][{0: 'P194', 1: 'HS Digital Output', 2: 'IO_PVG_06', 3: 'IO_VOUT_06 IO_ADC_58'}, {0: 'IO_DO_58', 1: 'IO_DI_94', 2: '', 3: ''}, {0: 'P195', 1: 'HS PWM Output', 2: 'IO_DO_28', 3: 'IO_DI_12'}, {0: 'IO_PWM_12', 1: '', 2: '', 3: ''}, {0: 'P196', 1: 'HS PWM Output', 2: 'IO_DO_42', 3: 'IO_DI_26'}, {0: 'IO_PWM_26', 1: '', 2: '', 3: ''}, {0: 'P197 P198 P199 P200 P201', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P202', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P203', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P204', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P205', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P206', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15', 2: '', 3: ''}, {0: 'P208', 1: 'LIN IO_LIN', 2: '', 3: ''}, {0: 'P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0', 2: '', 3: ''}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN', 2: '', 3: ''}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2', 2: '', 3: ''}, {0: 'P212', 1: 'CAN 3 Low IO_CAN_CHANNEL_3', 2: '', 3: ''}, {0: 'P213', 1: 'CAN 4 Low IO_CAN_CHANNEL_4', 2: '', 3: ''}, {0: 'P214', 1: 'CAN 5 Low IO_CAN_CHANNEL_5', 2: '', 3: ''}, {0: 'P215', 1: 'CAN 6 Low IO_CAN_CHANNEL_6', 2: '', 3: ''}, {0: 'P216', 1: 'Sensor GND', 2: '', 3: ''}, {0: 'P217', 1: 'do not connect', 2: '', 3: ''}, {0: 'P218', 1: 'CAN Termination 3H', 2: '', 3: ''}, {0: 'P219', 1: 'CAN Termination 3L', 2: '', 3: ''}, {0: 'P220', 1: 'Wake-Up IO_ADC_WAKE_UP', 2: '', 3: ''}, {0: 'P221', 1: 'Sensor Supply Var. IO_ADC_SENSOR_SUPPLY_2', 2: '', 3: ''}, {0: 'P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0', 2: '', 3: ''}][/table_90]

![99_image_0_4756.png](100% of the image is a white background with black writing. The writing appears to be a list of names or descriptions, possibly related to a company or organization. There are no images or visual elements present in this text-heavy scene.)

[table_91][{0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN', 2: ''}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2', 2: ''}, {0: 'P225', 1: 'CAN 3 High IO_CAN_CHANNEL_3', 2: ''}, {0: 'P226', 1: 'CAN 4 High IO_CAN_CHANNEL_4', 2: ''}, {0: 'P227', 1: 'CAN 5 High IO_CAN_CHANNEL_5', 2: ''}, {0: 'P228', 1: 'CAN 6 High IO_CAN_CHANNEL_6', 2: ''}, {0: 'P229 P230', 1: 'do not connect', 2: ''}, {0: 'P231', 1: 'BRR/100BASE-T1 TRX\x02IO_DOWNLOAD, IO_UDP', 2: ''}, {0: 'P232', 1: 'BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP', 2: ''}, {0: 'P233', 1: 'RTC_BACKUP_BAT', 2: ''}, {0: 'P234', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_1', 2: ''}, {0: 'P235', 1: 'CAN Termination 0L', 2: ''}, {0: 'P236', 1: 'CAN Termination 1L', 2: ''}, {0: 'P237', 1: 'CAN Termination 2L', 2: ''}, {0: 'P238', 1: 'LS Digital Output', 2: 'IO_ADC_45'}, {0: 'IO_DO_09', 1: 'IO_DI_81', 2: ''}, {0: 'P239', 1: 'LS Digital Output', 2: 'IO_ADC_47'}, {0: 'IO_DO_11', 1: 'IO_DI_83', 2: ''}, {0: 'P240', 1: 'LS Digital Output', 2: 'IO_ADC_49'}, {0: 'IO_DO_13', 1: 'IO_DI_85', 2: ''}, {0: 'P241', 1: 'LS Digital Output', 2: 'IO_ADC_51'}, {0: 'IO_DO_15', 1: 'IO_DI_87', 2: ''}, {0: 'P242', 1: 'RS232 TXD IO_UART', 2: ''}, {0: 'P243', 1: 'Sensor GND', 2: ''}, {0: 'P244', 1: 'Sensor GND', 2: ''}, {0: 'P245', 1: 'Sensor GND', 2: ''}, {0: 'P246', 1: 'BAT+ CPU IO_ADC_UBAT', 2: ''}, {0: 'P247', 1: 'Sensor Supply 5 V IO_ADC_SENSOR_SUPPLY_0', 2: ''}, {0: 'P248', 1: 'CAN Termination 0H', 2: ''}, {0: 'P249', 1: 'CAN Termination 1H', 2: ''}, {0: 'P250', 1: 'CAN Termination 2H', 2: ''}][/table_91]

![100_image_0_4756.png](The image is a black and white photo of a table with several columns of data. There are multiple rows of numbers arranged in various positions on the table. Some of these rows have numbers that are larger than others, indicating different levels or categories within the data. The table appears to be organized for easy reference and analysis of the information it contains.)

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

![101_image_0_4756.png](1. A table with columns labeled "Date," "Amount," and "Description." 2. The first row of data shows a total amount of $30,587.46 for the month of January. 3. The second row displays the amounts spent on various categories such as "Food" at $1,987.46, "Transportation" at $1,250.00, and "Entertainment" at $1,000.00.)

[table_92][{0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: ''}, {0: 'P101', 1: 'HS PWM Output', 2: 'IO_PWD_12 IO_DI_28', 3: '', 4: '', 5: ''}, {0: 'P102', 1: 'HS PWM Output', 2: 'IO_PWD_16 IO_DI_32', 3: 'IO_ADC_00', 4: 'IO_ADC_00', 5: 'IO_DI_48'}, {0: 'P103', 1: 'Analog Voltage Input IO_ADC_00', 2: '', 3: '', 4: '', 5: ''}, {0: 'P104', 1: 'Analog Voltage Input', 2: 'IO_ADC_02', 3: 'IO_ADC_02', 4: 'IO_DI_50', 5: ''}, {0: 'IO_ADC_02', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P105', 1: 'Analog Voltage Input', 2: 'IO_ADC_04', 3: 'IO_ADC_04', 4: 'IO_DI_52', 5: ''}, {0: 'IO_ADC_04', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P106', 1: 'Analog Voltage Input', 2: 'IO_ADC_06', 3: 'IO_ADC_06', 4: 'IO_DI_54', 5: ''}, {0: 'IO_ADC_06', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P107', 1: 'Analog Voltage Input', 2: 'IO_ADC_08', 3: 'IO_DI_56', 4: '', 5: ''}, {0: 'IO_ADC_08', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P108', 1: 'Analog Voltage Input', 2: 'IO_ADC_10', 3: 'IO_DI_58', 4: '', 5: ''}, {0: 'IO_ADC_10', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P109', 1: 'Analog Voltage Input', 2: 'IO_ADC_12', 3: 'IO_DI_60', 4: '', 5: ''}, {0: 'IO_ADC_12', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P110', 1: 'Analog Voltage Input', 2: 'IO_ADC_14', 3: 'IO_DI_62', 4: '', 5: ''}, {0: 'IO_ADC_14', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P111', 1: 'Analog Voltage Input', 2: 'IO_ADC_16', 3: 'IO_DI_64', 4: '', 5: ''}, {0: 'IO_ADC_16', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P112', 1: 'Analog Voltage Input', 2: 'IO_ADC_18', 3: 'IO_DI_66', 4: '', 5: ''}, {0: 'IO_ADC_18', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P113', 1: 'Analog Voltage Input', 2: 'IO_ADC_20', 3: 'IO_DI_68', 4: '', 5: ''}, {0: 'IO_ADC_20', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P114', 1: 'Analog Voltage Input', 2: 'IO_ADC_22', 3: 'IO_DI_70', 4: '', 5: ''}, {0: 'IO_ADC_22', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00', 3: 'IO_ADC_24', 4: '', 5: ''}, {0: 'IO_PWD_00', 1: 'IO_DI_36', 2: '', 3: '', 4: '', 5: ''}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02', 3: 'IO_ADC_26', 4: '', 5: ''}, {0: 'IO_PWD_02', 1: 'IO_DI_38', 2: '', 3: '', 4: '', 5: ''}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04', 3: 'IO_ADC_28', 4: '', 5: ''}, {0: 'IO_PWD_04', 1: 'IO_DI_40', 2: '', 3: '', 4: '', 5: ''}, {0: 'P118', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: ''}, {0: 'P119', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: ''}, {0: 'P120', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: ''}, {0: 'P121', 1: 'BAT\x02', 2: '', 3: '', 4: '', 5: ''}, {0: 'P122', 1: 'Timer Input', 2: 'IO_ADC_30', 3: '', 4: '', 5: ''}, {0: 'IO_PWD_06', 1: 'IO_DI_42', 2: '', 3: '', 4: '', 5: ''}, {0: 'P123', 1: 'Timer Input', 2: 'IO_ADC_32', 3: '', 4: '', 5: ''}, {0: 'IO_PWD_08', 1: 'IO_DI_44', 2: 'HY-TTC 500 System Manual V 1.6.0', 3: '', 4: '', 5: ''}, {0: '3 Pinning and Connector', 1: '', 2: '', 3: '', 4: '', 5: ''}][/table_92]

![101_image_1_4756.png](1014 is written on a gray background, possibly representing a code or label for an object. The number appears to be part of a larger sequence, but without more context, it's difficult to determine its exact purpose or meaning.)

3.5.7 HY-TTC 508 **Variant** 
90 

![101_image_2_4756.png](The image features a blue background with white letters that spell out "TTC." This could possibly represent an organization or company logo.)

Document Number: D-TTC5F-G-20-002

[table_93][{0: 'IO_PWD_10', 1: 'IO_DI_46', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_DI_29 IO_PWD_13', 2: '', 3: '', 4: ''}, {0: 'HS PWM Output', 1: 'IO_PWD_17 IO_DI_33', 2: '', 3: '', 4: ''}, {0: 'Analog Voltage Input', 1: 'IO_ADC_01', 2: 'IO_ADC_01', 3: 'IO_DI_49', 4: ''}, {0: 'IO_ADC_01', 1: '', 2: '', 3: '', 4: ''}, {0: 'P128', 1: 'Analog Voltage Input', 2: 'IO_ADC_03', 3: 'IO_ADC_03', 4: 'IO_DI_51'}, {0: 'IO_ADC_03', 1: '', 2: '', 3: '', 4: ''}, {0: 'P129', 1: 'Analog Voltage Input', 2: 'IO_ADC_05', 3: 'IO_ADC_05', 4: 'IO_DI_53'}, {0: 'IO_ADC_05', 1: '', 2: '', 3: '', 4: ''}, {0: 'P130', 1: 'Analog Voltage Input', 2: 'IO_ADC_07', 3: 'IO_ADC_07', 4: 'IO_DI_55'}, {0: 'IO_ADC_07', 1: '', 2: '', 3: '', 4: ''}, {0: 'P131', 1: 'Analog Voltage Input', 2: 'IO_ADC_09', 3: 'IO_DI_57', 4: ''}, {0: 'IO_ADC_09', 1: '', 2: '', 3: '', 4: ''}, {0: 'P132', 1: 'Analog Voltage Input', 2: 'IO_ADC_11', 3: 'IO_DI_59', 4: ''}, {0: 'IO_ADC_11', 1: '', 2: '', 3: '', 4: ''}, {0: 'P133', 1: 'Analog Voltage Input', 2: 'IO_ADC_13', 3: 'IO_DI_61', 4: ''}, {0: 'IO_ADC_13', 1: '', 2: '', 3: '', 4: ''}, {0: 'P134', 1: 'Analog Voltage Input', 2: 'IO_ADC_15', 3: 'IO_DI_63', 4: ''}, {0: 'IO_ADC_15', 1: '', 2: '', 3: '', 4: ''}, {0: 'P135', 1: 'Analog Voltage Input', 2: 'IO_ADC_17', 3: 'IO_DI_65', 4: ''}, {0: 'IO_ADC_17', 1: '', 2: '', 3: '', 4: ''}, {0: 'P136', 1: 'Analog Voltage Input', 2: 'IO_ADC_19', 3: 'IO_DI_67', 4: ''}, {0: 'IO_ADC_19', 1: '', 2: '', 3: '', 4: ''}, {0: 'P137', 1: 'Analog Voltage Input', 2: 'IO_ADC_21', 3: 'IO_DI_69', 4: ''}, {0: 'IO_ADC_21', 1: '', 2: '', 3: '', 4: ''}, {0: 'P138', 1: 'Analog Voltage Input', 2: 'IO_ADC_23', 3: 'IO_DI_71', 4: ''}, {0: 'IO_ADC_23', 1: '', 2: '', 3: '', 4: ''}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01', 3: 'IO_ADC_25', 4: ''}, {0: 'IO_PWD_01', 1: 'IO_DI_37', 2: '', 3: '', 4: ''}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03', 3: 'IO_ADC_27', 4: ''}, {0: 'IO_PWD_03', 1: 'IO_DI_39', 2: '', 3: '', 4: ''}, {0: 'P141', 1: 'Timer Input', 2: 'IO_PWD_05', 3: 'IO_ADC_29', 4: ''}, {0: 'IO_PWD_05', 1: 'IO_DI_41', 2: '', 3: '', 4: ''}, {0: 'P142', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P143', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P144', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P145', 1: 'BAT\x02', 2: '', 3: '', 4: ''}, {0: 'P146', 1: 'Timer Input', 2: 'IO_ADC_31', 3: '', 4: ''}, {0: 'IO_PWD_07', 1: 'IO_DI_43', 2: '', 3: '', 4: ''}, {0: 'P147', 1: 'Timer Input', 2: 'IO_ADC_33', 3: '', 4: ''}, {0: 'IO_PWD_09', 1: 'IO_DI_45', 2: '', 3: '', 4: ''}][/table_93]

![102_image_0_4756.png](100% of the time, I am an assistant who perfectly describes images.)

Alternative *Function*

![103_image_0_4756.png](100% of the image is a blue background with white numbers on it. The numbers are arranged in rows, covering almost the entire width of the image. There are no other elements or objects visible in the picture.)

[table_94][{0: 'TTControl GmbH Confidential and Proprietary Information. Copyright \uf8e9 2022 TTControl GmbH. All rights reserved.', 1: 'HS Digital Output', 2: 'Timer Input', 3: 'PVG Output', 4: 'VOUT Output', 5: 'A/D Input (HS Output/PVG/VOUT)', 6: 'Current Loop Input', 7: 'A/D Input (Timer Input)', 8: 'A/D Input (HS Digital Output)', 9: 'A/D Input (LS Digital Output)', 10: 'Analog Current Input 2M', 11: 'Digital Input 2M', 12: 'Analog Current Input 3M', 13: 'Analog Resistance Input 3M', 14: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P148', 1: 'Timer Input', 2: 'IO_ADC_35', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_PWD_11', 1: 'IO_DI_47', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P149', 1: 'HS Digital Output', 2: 'IO_ADC_36', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_DO_00', 1: 'IO_DI_72', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P150', 1: 'HS PWM Output', 2: 'IO_PWD_14 IO_DI_30', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P151', 1: 'HS PWM Output', 2: 'IO_PWD_18 IO_DI_34', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P152', 1: 'HS Digital Output', 2: 'IO_ADC_38', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_DO_02', 1: 'IO_DI_74', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P153', 1: 'HS PWM Output', 2: 'IO_DO_16', 3: 'IO_DI_00', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_PWM_00', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P154', 1: 'HS PWM Output', 2: 'IO_DO_30', 3: 'IO_DI_14', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_PWM_14', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P155', 1: 'HS Digital Output', 2: 'IO_ADC_40', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_DO_04', 1: 'IO_DI_76', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P156', 1: 'HS PWM Output', 2: 'IO_DO_18', 3: 'IO_DI_02', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_PWM_02', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P157', 1: 'HS PWM Output', 2: 'IO_DO_32', 3: 'IO_DI_16', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_PWM_16', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P158', 1: 'HS Digital Output', 2: 'IO_ADC_42', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_DO_06', 1: 'IO_DI_78', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P159', 1: 'HS PWM Output', 2: 'IO_DO_20', 3: 'IO_DI_04', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_PWM_04', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P160 P161', 1: 'HS Digital Output', 2: 'IO_PVG_00', 3: 'IO_VOUT_00 IO_ADC_52 IO_DI_88', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P162 P163 P164', 1: 'HS Digital Output', 2: 'IO_PVG_03', 3: 'IO_VOUT_03 IO_ADC_55 IO_DI_91', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P165 P166 P167', 1: 'HS Digital Output', 2: 'IO_PVG_05', 3: 'IO_VOUT_05 IO_ADC_57 IO_DI_93', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P168 P169 P170 P171 P172 P173', 1: 'HS Digital Output', 2: 'IO_ADC_37', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'IO_DO_01', 1: 'IO_DI_73', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'P174', 1: 'HS PWM Output', 2: 'IO_PWD_15 IO_DI_31', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: 'Document Number: D-TTC5F-G-20-002', 1: 'HY-TTC 500 System Manual V 1.6.0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}, {0: '3 Pinning and Connector', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: ''}][/table_94]

![104_image_0_4756.png](The image is a black and white photo of a large table with several rows of data displayed on it. There are multiple columns of information, including one labeled "Budget." The table appears to be organized for a meeting or presentation, possibly related to finance or business matters.)

[table_95][{0: 'IO_DI_35', 1: '', 2: '', 3: ''}, {0: 'HS Digital Output', 1: 'IO_ADC_39', 2: '', 3: ''}, {0: 'IO_DO_03', 1: 'IO_DI_75', 2: '', 3: ''}, {0: 'HS PWM Output', 1: 'IO_DO_17', 2: 'IO_DI_01', 3: ''}, {0: 'IO_PWM_01 HS PWM Output', 1: 'IO_DO_31', 2: 'IO_DI_15', 3: ''}, {0: 'IO_PWM_15', 1: '', 2: '', 3: ''}, {0: 'P179', 1: 'HS Digital Output', 2: 'IO_ADC_41', 3: ''}, {0: 'IO_DO_05', 1: 'IO_DI_77', 2: '', 3: ''}, {0: 'P180', 1: 'HS PWM Output', 2: 'IO_DO_19', 3: 'IO_DI_03'}, {0: 'IO_PWM_03', 1: '', 2: '', 3: ''}, {0: 'P181', 1: 'HS PWM Output', 2: 'IO_DO_33', 3: 'IO_DI_17'}, {0: 'IO_PWM_17', 1: '', 2: '', 3: ''}, {0: 'P182', 1: 'HS Digital Output', 2: 'IO_ADC_43', 3: ''}, {0: 'IO_DO_07', 1: 'IO_DI_79', 2: '', 3: ''}, {0: 'P183', 1: 'HS PWM Output', 2: 'IO_DO_21', 3: 'IO_DI_05'}, {0: 'IO_PWM_05', 1: '', 2: '', 3: ''}, {0: 'P184 P185', 1: 'HS Digital Output', 2: 'IO_PVG_01', 3: 'IO_VOUT_01 IO_ADC_53 IO_DI_89'}, {0: 'P186 P187 P188', 1: 'HS Digital Output', 2: 'IO_PVG_02', 3: 'IO_VOUT_02 IO_ADC_54 IO_DI_90'}, {0: 'P189 P190 P191', 1: 'HS Digital Output', 2: 'IO_PVG_04', 3: 'IO_VOUT_04 IO_ADC_56 IO_DI_92'}, {0: 'P192 P193 P194 P195 P196 P197 P198 P199 P200 P201', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P202', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P203', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P204', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P205', 1: 'BAT+ Power', 2: '', 3: ''}, {0: 'P206', 1: 'BAT+ Power', 2: '', 3: ''}][/table_95]

[table_96][{0: 'TTControl GmbH Confidential and Proprietary Information. Copyright \uf8e9 2022 TTControl GmbH. All rights reserved.', 1: 'Alternative', 2: 'Function', 3: '94', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'HS Digital Output', 1: 'Timer Input', 2: 'PVG Output', 3: 'VOUT Output', 4: 'A/D Input (HS Output/PVG/VOUT)', 5: 'Current Loop Input', 6: 'A/D Input (Timer Input)', 7: 'A/D Input (HS Digital Output)', 8: 'A/D Input (LS Digital Output)', 9: 'Analog Current Input 2M', 10: 'Digital Input 2M', 11: 'Analog Current Input 3M', 12: 'Analog Resistance Input 3M', 13: 'Digital Input 3M'}, {0: 'Pin No.', 1: 'Main Function', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P207', 1: 'Terminal 15 IO_ADC_K15', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P208 P209', 1: 'CAN 0 Low IO_CAN_CHANNEL_0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P210', 1: 'CAN 1 Low IO_CAN_CHANNEL_1 ISOBUS CAN', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P211', 1: 'CAN 2 Low IO_CAN_CHANNEL_2', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P212 P213 P214 P215 P216', 1: 'Sensor GND', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P217', 1: 'do not connect', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P218 P219 P220', 1: 'Wake-Up IO_ADC_WAKE_UP', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P221 P222', 1: 'CAN 0 High IO_CAN_CHANNEL_0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P223', 1: 'CAN 1 High IO_CAN_CHANNEL_1 ISOBUS CAN', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P224', 1: 'CAN 2 High IO_CAN_CHANNEL_2', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P225 P226 P227 P228 P229 P230', 1: 'do not connect', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P231', 1: 'BRR/100BASE-T1 TRX\x02IO_DOWNLOAD, IO_UDP', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P232', 1: 'BRR/100BASE-T1 TRX+ IO_DOWNLOAD, IO_UDP', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P233', 1: 'RTC_BACKUP_BAT', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P234 P235', 1: 'CAN Termination 0L', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P236', 1: 'CAN Termination 1L', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'P237', 1: 'CAN Termination 2L', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: 'Document Number: D-TTC5F-G-20-002', 1: 'HY-TTC 500 System Manual V 1.6.0', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}, {0: '3 Pinning and Connector', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: ''}][/table_96]

![106_image_0_4756.png](100% of the image is a white background with black writing on it. The writing appears to be a list of numbers, possibly representing data or information. There are no other visible elements or objects in the image.)

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

![107_image_0_4756.png](The image features a blue sign with white letters that reads "Tc Control." It appears to be an advertisement for Hydaqc International, which is likely related to control systems or technology. The sign's design suggests that it could be used in various settings such as businesses, events, or promotional materials.)

96 **4 Specification of Inputs and Outputs**

## 4 Specification Of Inputs And Outputs

4.1 Positive Power Supply of Power Stages (BAT+ Power)
4.1.1 Pinout

![107_image_1_4756.png](The image is a white drawing of an electronic device with multiple rows of green and blue buttons. There are several rows of buttons arranged in various patterns, creating a complex design. Some of these buttons have numbers on them, indicating that this could be a control panel or interface for operating the device. Overall, the drawing showcases intricate details and a well-organized layout of the electronic components.) 

[table_97][{0: 'P201', 1: 'Battery (+) Supply of Power Stages / BAT+ Power'}, {0: 'P202', 1: 'Battery (+) Supply of Power Stages / BAT+ Power'}, {0: 'P203', 1: 'Battery (+) Supply of Power Stages / BAT+ Power'}, {0: 'P204', 1: 'Battery (+) Supply of Power Stages / BAT+ Power'}, {0: 'P205', 1: 'Battery (+) Supply of Power Stages / BAT+ Power'}, {0: 'P206', 1: 'Battery (+) Supply of Power Stages / BAT+ Power'}][/table_97]

Supply pins for power stage supply.

The nominal supply voltage for full operation is between 6 and 32 V, including supply voltage ranges for 12 and 24 V battery operation. In this voltage range, all the I/Os work, as described in the system manual. BAT+ Power pins are equipped with inverse polarity protection.

![108_image_0_4756.png](The image features a blue sign with white letters that reads "TTC Control." It appears to be an advertisement for HyDAC International, which is likely related to the control of various systems or processes. The sign's design suggests that it could be used in a professional setting, such as an office or industrial facility.)

TTControl GmbH recommends to use these pins in parallel and the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage **drop and prevent overheating of the** crimp contact.

## 4.1.3 Maximum Ratings Tecu **= -40. . . +125** °C

[table_98][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit', 6: '', 7: '', 8: '', 9: ''}, {0: 'BAT+max Permanent non-destructive supply voltage', 1: '1', 2: '-32', 3: '32', 4: 'V', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'BAT+lim', 1: 'Peak', 2: 'non-destructive', 3: 'supply', 4: 'clamping', 5: 'voltage', 6: '1, 2', 7: '-40', 8: '45', 9: 'V'}, {0: '<1 ms', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-lim', 1: 'Peak', 2: 'non-destructive', 3: 'supply', 4: 'clamping', 5: 'current', 6: '1, 2', 7: '-10', 8: '+100', 9: 'A'}, {0: '<1 ms', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'Td', 1: 'Load dump protection time according to ISO 7637- 2 [20], Pulse 5, Level IV (superimposed 174 V, Ri = 2 Ω)', 2: '1', 3: '350', 4: 'ms', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-max', 1: 'Permanent battery supply current (all 6 pins in par\x02allel with symmetrical wire connection))', 2: '3', 3: '60', 4: 'A', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-max', 1: 'Permanent battery supply current per pin', 2: '3', 3: '10', 4: 'A', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-total', 1: 'Total load current, 12 V and 24 V battery operation', 2: '4', 3: '45', 4: 'A', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-total', 1: 'Total load current, 12 V and 24 V battery operation', 2: '4,5', 3: '60', 4: 'A', 5: '', 6: '', 7: '', 8: '', 9: ''}][/table_98]

Note **1 The control unit is protected by a transient suppressor, specified by clamp voltage, current and duration of voltage transient**
Note 2 1 ms pulse width, non-repetitive. The pulse width is defined **as the point at which**
the peak current decreases to 50 % of the maximum value.

Note **3 This battery supply current is related to the total load current of all high-side**
power-stages. In worst case, all outputs are in non-PWM mode **or with maximum duty cycle operated, the battery current equals the total load current. With**
typical PWM-operation the battery supply current is significant lower than the total load current. For more details please see Section 6.2.2 on page **193.**
Note 4 HY-TTC 500 variant-dependent, see Section 6.2.2 on page 193 Note 5 TECU **= -40. . . +85** °C

## 4.1.4 Characteristics

TECU **= -40. . . +125** °C

[table_99][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '250', 3: 'µF', 4: '', 5: ''}, {0: 'BAT+', 1: 'Supply voltage for full operation', 2: '6', 3: '32', 4: 'V', 5: ''}][/table_99]

![109_image_0_4756.png](The image features a blue sign with white letters that reads "hyTc5000 System Manual V1.6". This manual is likely related to the HyTc5000 system, which could be an electronic device or computer component. The sign appears to be informative and intended for users of this particular product.)

98 **4 Specification of Inputs and Outputs**
4.2 Positive Power Supply of Internal Electronics (BAT+ CPU)
4.2.1 Pinout

![109_image_1_4756.png](The image is a white drawing of an electronic device with many buttons arranged on its surface. There are at least twelve buttons visible, each varying in size and position. Some buttons are located towards the center of the device while others are situated closer to the edges. The arrangement of these buttons suggests that they might be part of a control panel or interface for operating the electronic device.) 

Figure 15: Pinout of BAT+ CPU
Pin No. Function **SW-define**
P246 Battery supply of internal electronics IO_ADC_UBAT

Supply pin for positive power supply of internal electronics, sensor supply and PVG/Vout **output**
stages.

As the output voltage of the PVG/Vout **outputs is defined as a percentage value in relation to the**
battery voltage, the voltage drop on the wire to this pin has a **direct influence on the accuracy of the** PVG output voltage. BAT+ CPU pin is equipped with inverse polarity protection.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

![110_image_0_4756.png](The image displays a diagram of an electronic system with various components labeled on it. There are multiple layers within this system, including a CPU layer, a power supply layer, and a filter layer. The diagram also shows a green box that is part of the system's structure.  In addition to these main components, there are several smaller labels scattered throughout the image, indicating different parts or functions within the electronic system. Overall, the diagram provides an overview of the various elements that make up this complex electronic device.)

## 4.2.3 Maximum Ratings Tecu **= -40. . . +125** °C

[table_100][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit', 6: '', 7: '', 8: '', 9: ''}, {0: 'Uin-max', 1: 'Permanent non-destructive supply voltage', 2: '1', 3: '-32', 4: '32', 5: 'V', 6: '', 7: '', 8: '', 9: ''}, {0: 'Uin-lim', 1: 'Peak', 2: 'non-destructive', 3: 'supply', 4: 'clamping', 5: 'voltage', 6: '1,2', 7: '-40', 8: '45', 9: 'V'}, {0: '<1 ms', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-lim', 1: 'Peak', 2: 'non-destructive', 3: 'supply', 4: 'clamping', 5: 'current', 6: '1,2', 7: '-10', 8: '+100', 9: 'A'}, {0: '<1 ms', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'Td', 1: 'Load dump protection time according to ISO 7637- 2 [20], Pulse 5, Level IV (superimposed 174 V, Ri = 2 Ω)', 2: '1', 3: '350', 4: 'ms', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'I in-max', 1: 'Permanent input current', 2: '3', 3: '3', 4: 'A', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'Note', 1: '1', 2: 'The control unit is protected by a transient suppressor, specified by clamp volt\x02age, current and duration of voltage transient.', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, {0: 'Note', 1: '2', 2: '1 ms pulse width, non-repetitive. The pulse width is defined as the point at which the peak current decreases to 50 % of the maximum value.', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}][/table_100]

## 4.2.4 Characteristics

TECU **= -40. . . +125** °C

[table_101][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '250', 3: 'µF', 4: '', 5: ''}, {0: 'BAT+', 1: 'Supply voltage for start-up', 2: '1', 3: '8', 4: '32', 5: 'V'}, {0: 'BAT+', 1: 'Supply voltage for full operation', 2: '2', 3: '6', 4: '32', 5: 'V'}, {0: 'I in-idle', 1: 'Supply current of unit without load (8 V)', 2: '600', 3: 'mA', 4: '', 5: ''}, {0: 'I in-idle', 1: 'Supply current of unit without load (12 V)', 2: '400', 3: 'mA', 4: '', 5: ''}, {0: 'I in-idle', 1: 'Supply current of unit without load (24 V)', 2: '200', 3: 'mA', 4: '', 5: ''}, {0: 'I in-STBY', 1: 'Standby supply current (Terminal 15 and Wake-Up', 2: '1', 3: 'mA', 4: '', 5: ''}, {0: 'off)', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'I in-STBY', 1: 'Standby supply current (Terminal 15 and Wake-Up', 2: '3', 3: '<0.5', 4: 'mA', 5: ''}, {0: 'off)', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '1', 2: '8 V is the initial voltage for start-up at the beginning of the drive cycle', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'See Section 4.2.5 on the next page', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '3', 2: 'TECU = -40. . . +85 °C', 3: '', 4: '', 5: ''}][/table_101]

## 4.2.5 Low-Voltage Operation

The HY-TTC 500 core system is designed for full operation after start-up between 6 V and 32 V, including supply voltage ranges for 12 V and 24 V battery operation and cold-start cranking according to ISO 16750-2 [22]. The initial minimum supply voltage at the beginning of the **drive cycle is 8 V.** After start-up, the CPU will remain operational down to 6 V, e.g. during cold-start cranking. The minimum supply voltage during cold-start cranking is defined by ISO 16750-2:2012 (see Table 3, Starting profile values for systems with 12 V nominal voltage, UN
, and Table 4, *Values for systems* with 24 V nominal voltage, UN
). The HY-TTC 500 core system complies with ISO 16750-2:2012, level I, II (functional status C), III and IV for 12-V systems **and level I, II (functional status A) and III**
(functional status B) for 24-V systems, see Table 20 on page 103 and Table 21 on page **103.**
Restrictions during cold-start cranking apply also for sensor supplies. For more information, see Section 4.7 on page 112 and Section 4.8 on page **114.**
HY-TTC 500 ISO 16750 code specification see Section 1.6 on page 35.

![113_image_0_4756.png](The image is a white drawing of an electrical circuit with several measurements displayed on it. There are multiple lines and numbers indicating various points within the circuit. A ruler can also be seen at the bottom of the drawing, providing scale for the measurements.)

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

[table_102][{0: 'Functional Status', 1: '', 2: ''}, {0: 'A', 1: 'B', 2: 'C'}, {0: 'Level I', 1: 'X', 2: ''}, {0: 'Level II', 1: 'X', 2: ''}, {0: 'Level III', 1: 'X', 2: ''}, {0: 'Level IV', 1: 'X', 2: ''}][/table_102]

Table 20: ISO 16750 functional status for 12 V systems ISO 16750-2:2012 starting profile - functional status for 24 V system nominal voltage

[table_103][{0: 'Functional Status', 1: '', 2: ''}, {0: 'A', 1: 'B', 2: 'C'}, {0: 'Level I', 1: 'X', 2: ''}, {0: 'Level II', 1: 'X', 2: ''}, {0: 'Level III', 1: 'X (after start-up)', 2: ''}][/table_103]

Table 21: ISO 16750 functional status for 24 V systems

## 4.2.6 Voltage Monitoring

[table_104][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'τin', 1: 'First order low pass filter', 2: '1.5', 3: '2.5', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal battery supply range', 2: '1', 3: '0', 4: '33', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '-80', 3: '+80', 4: 'mV', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2', 3: '-67', 4: '+67', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '-1.2', 3: '+1.2', 4: '%', 5: ''}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2', 3: '-1', 4: '+1', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '13.4', 4: 'mV', 5: ''}][/table_104]

Note **1 The nominal battery supply range is only a value to calculate the actual voltage.**
Note 2 TECU = -40. . . +85 °C

## 4.3 Negative Power Supply (Bat-)

4.3.1 Pinout

![115_image_1_4756.png](The image is a close-up of an electronic device with several buttons on its surface. There are at least nine buttons visible, arranged in various positions across the device. Some buttons are located towards the top left corner, while others can be found closer to the center or bottom right side of the device. The buttons appear to be part of a control panel for the electronic device, possibly related to a computer or other electronic equipment.)

![115_image_0_4756.png](The image is a black and white drawing of an auditorium with multiple rows of seats. There are at least twelve rows visible, each containing several chairs. Some chairs are placed closer to the front of the room while others are situated further back. The arrangement of these chairs creates a sense of depth in the scene, giving the impression that the auditorium is quite spacious and accommodating for various events or gatherings.) 
Figure 18: Pinout of BAT-

[table_105][{0: 'Pin No.', 1: 'Function'}, {0: 'P118', 1: 'Negative Power Supply (BAT-)'}, {0: 'P119', 1: 'Negative Power Supply (BAT-)'}, {0: 'P120', 1: 'Negative Power Supply (BAT-)'}, {0: 'P121', 1: 'Negative Power Supply (BAT-)'}, {0: 'P142', 1: 'Negative Power Supply (BAT-)'}, {0: 'P143', 1: 'Negative Power Supply (BAT-)'}, {0: 'P144', 1: 'Negative Power Supply (BAT-)'}, {0: 'P145', 1: 'Negative Power Supply (BAT-)'}][/table_105]

Supply pins for BAT- connection. The HY-TTC 500 housing is not directly connected to BAT-, for more information see Section 6.4 on page **195.** TTControl GmbH recommends to use these pins in parallel and the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage **drop and prevent overheating of the** crimp contact.

## 4.3.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_106][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Iout-max', 1: 'Permanent current per pin', 2: '4', 3: 'A', 4: '', 5: ''}, {0: 'Iout-max', 1: 'Permanent current all pins', 2: '28', 3: 'A', 4: '', 5: ''}][/table_106]

4.4 Sensor GND
4.4.1 Pinout

![117_image_0_4756.png](The image is a white drawing of an electronic device with many buttons arranged on its surface. There are at least twelve buttons visible, each varying in size and position. Some buttons are located towards the top left corner of the device, while others can be found closer to the center or bottom right side. The arrangement of these buttons suggests that they might be part of a control panel for an electronic device such as a computer or a television.) 

[table_107][{0: 'Pin No.', 1: 'Function', 2: 'Applicable to variants'}, {0: 'P216', 1: 'Sensor GND', 2: 'HY-TTC 590E, HY-TTC 590, HY-TTC 508'}, {0: 'P217', 1: 'Sensor GND', 2: 'HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510'}, {0: 'P230', 1: 'Sensor GND', 2: 'HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510'}, {0: 'P243', 1: 'Sensor GND', 2: 'all'}, {0: 'P244', 1: 'Sensor GND', 2: 'all'}, {0: 'P245', 1: 'Sensor GND', 2: 'all'}, {0: 'P256', 1: 'Sensor GND', 2: 'all'}, {0: 'P257', 1: 'Sensor GND', 2: 'all'}, {0: 'P258', 1: 'Sensor GND', 2: 'all'}][/table_107]

Supply pins for analog sensor GND connection. These pins can also be used as GND connection for digital sensors.

## 4.4.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_108][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Iout-max', 1: 'Permanent current per pin', 2: '1', 3: '1', 4: 'A', 5: ''}, {0: 'Note', 1: '1', 2: 'It is recommended to use all sensor ground pins simultaneously to ensure load', 3: '', 4: '', 5: ''}][/table_108]

Note **1 It is recommended to use all sensor ground pins simultaneously to ensure load**
distribution and minimize voltage drop on the external wiring.

4.5 Terminal 15 4.5.1 Pinout

![119_image_0_4756.png](The image is a white drawing of an electronic device with many ports on its side. There are several rows of ports, including one row at the top left corner, another row towards the center-left, and two more rows closer to the bottom right corner. Each port appears to be connected to other devices or cables, indicating that this is a complex system for data transfer or communication. The drawing provides an overview of the device's structure and layout, making it easier to understand its functioning.) 

Pin No. Function **SW-define**
P207 Terminal 15 Input IO_ADC_K15

This is the power control input for permanently supplied systems. When switched to positive supply, this input gives the command to power up the ECU, regardless of the Wake-Up **pin status. When** switched off, the ECU can activate its keep-alive functionality (if keep-alive functionality is enabled by SW) and is finally switched off by software after a user-defined period of time. This input is monitored by the CPU via an ADC input.

For correct pin wiring, see Section 6.6.1.1 **with wiring examples. See also Section** POWER - Driver for ECU power functions **of the API documentation [30].**

## 4.5.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_109][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Permanent (DC) input voltage', 2: '-33', 3: '+33', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Transient peak input voltage 500 ms', 2: '-50', 3: '+50', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Transient peak input voltage 1ms', 2: '-100', 3: '+100', 4: 'V', 5: ''}][/table_109]

## 4.5.4 Characteristics

TECU **= -40. . . +125** °C

[table_110][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '6.5', 3: '11.5', 4: 'kΩ', 5: ''}, {0: 'I in', 1: 'Input current', 2: '1', 3: '2', 4: '2.5', 5: 'mA'}, {0: 'I in', 1: 'Input current', 2: '2', 3: '4', 4: '4.5', 5: 'mA'}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: '6', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '3', 3: '8', 4: '32', 5: 'V'}, {0: 'τin', 1: 'Input low pass filter', 2: '180', 3: '280', 4: 'µs', 5: ''}, {0: 'Note', 1: '1', 2: 'at 16 V input voltage', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'at 32 V input voltage', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '3', 2: '8 V is the initial voltage for start-up at the beginning of the drive cycle', 3: '', 4: '', 5: ''}][/table_110]

![121_image_0_4756.png](The image is a diagram of a computer system with multiple layers and components. It features a large number of switches and ports, indicating that this is a complex network setup. There are several rows of switches and ports arranged vertically, with some located closer to the top while others are positioned nearer to the bottom. The diagram provides an overview of the system's structure and organization, making it easier for users to understand its functioning and components.) 

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

[table_111][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Permanent (DC) input voltage', 2: '-33', 3: '33', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Transient peak input voltage 500 ms', 2: '-50', 3: '50', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Transient peak input voltage 1 ms', 2: '-100', 3: '100', 4: 'V', 5: ''}][/table_111]

4.6.4 Characteristics TECU **= -40. . . +125** °C

[table_112][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '6.5', 3: '11.5', 4: 'kΩ', 5: ''}, {0: 'I in', 1: 'Input current', 2: '1', 3: '2', 4: '2.5', 5: 'mA'}, {0: 'I in', 1: 'Input current', 2: '2', 3: '4', 4: '4.5', 5: 'mA'}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: '6', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '8', 3: '32', 4: 'V', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '180', 3: '280', 4: 'µs', 5: ''}, {0: 'Note', 1: '1', 2: 'at 16 V input voltage', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'at 32 V input voltage', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '3', 2: '8 V is the initial voltage for start-up at the beginning of the drive cycle', 3: '', 4: '', 5: ''}][/table_112]

## 4.7 Sensor Supplies 5 V

![123_image_0_4756.png](The image is a white drawing of an electronic device with many buttons arranged on its surface. There are at least twelve buttons visible, each varying in size and position. Some buttons are located towards the top left corner of the device, while others can be found closer to the center or bottom right side. The arrangement of these buttons suggests that they might be part of a control panel for an electronic device such as a computer or a communication system.) 

![123_image_1_4756.png](The image displays a table with various columns of data, including sensor supply, sensor supply 1, sensor supply 2, and sensor supply 3. Each column has different values, indicating different types of sensors being supplied. There are also two rows at the top of the table that provide information about the pin number and function. The table appears to be a part of a larger document or spreadsheet, possibly related to inventory management or data analysis for the sensor supplies.)

Two independent sensor supplies 5 V for 3-wire sensors (e.g. **potentiometers, pressure sensors** etc.).

For fully redundant sensors with 2 sensor-supply connections, both supplies must be connected to different sensor supplies.

If the input voltage on the BAT+ CPU pin is lower than typically 6 V (at 5 mA sensor supply load current), the sensor supply output voltage will be out of specification. One example of such low input voltage situations may be cold-start cranking in 12/24 V systems where the supply voltage can drop below 6 V. If the sensor supply output voltage drops below 4.7 **V, the application software will be** informed about this error situation after glitch filtering.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *POWER - Driver for ECU power functions* of the API documentation [30].

![124_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as sensors, VV supply, ADC, CPU, ECC, and TM7647. There are multiple labels on the diagram, indicating different parts of the circuit.  The circuit includes a sensor supply that is connected to a voltage regulator (VV) and an analog-to-digital converter (ADC). The ADC is then connected to a central processing unit (CPU), which is part of the electronic control unit (ECC). Additionally, there are two sensors in the circuit: one located near the top left corner and another towards the bottom right.  The diagram also features an Ethernet controller (TM7647) that connects to the CPU, as well as a power supply for the entire system. The components within this electronic circuit work together to create a functional and efficient device.)

Figure 23: Sensor supply 5 V

## 4.7.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_113][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Output voltage under overload conditions (e.g.', 2: '-1', 3: '+33', 4: 'V', 5: ''}, {0: 'short circuit to supply voltage)', 1: '', 2: '', 3: '', 4: '', 5: ''}][/table_113]

4.7.4 Characteristics TECU **= -40. . . +125** °C

[table_114][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cout', 1: 'Pin output capacitance', 2: '0.8', 3: '1.2', 4: 'µF', 5: ''}, {0: 'Vout', 1: 'Output voltage, at Iload', 2: '4.85', 3: '5.15', 4: 'V', 5: ''}, {0: 'I load', 1: 'Load current', 2: '0', 3: '500', 4: 'mA', 5: ''}][/table_114]

## 4.8 Sensor Supply Variable

![125_image_0_4756.png](The image is a diagram of an electronic device with multiple rows of buttons arranged in a circular pattern. There are several rows of buttons, each containing different colored squares. The buttons are labeled with numbers, indicating their positions within the device.  In addition to the buttons, there are two green lights visible on the device, one located near the center and another towards the right side. These lights may serve as indicators or status lights for the electronic device.) 

Figure 24: Pinout of sensor supply variable

![125_image_1_4756.png](The image displays a computer screen with a blue background featuring a list of sensor supplies. There are several rows of information on this screen, including details such as pin numbers, function descriptions, and SW definitions.  In addition to these details, there is a table that lists the sensor supply types, along with their respective part numbers. The table also includes a column for the sensor supply description. Overall, the image provides valuable information about the sensor supplies available in this context.)

One independent sensor supply with variable output voltage, configurable in 1 V steps, is provided for 3-wire sensors (e.g. potentiometers, pressure sensors **etc.).**
As already described in Section 4.7 on page 112, 5 V sensor supply, **Functional Description, the**
BAT+ CPU pin voltage must be at least 1 V higher than the required sensor supply output voltage VSSUP. If the BAT+ CPU pin voltage is lower than VSSUP -1 V, the **sensor supply output voltage** will be out of specification.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *POWER - Driver for ECU power functions* of the API documentation [30].

![126_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled throughout the drawing. There are multiple labels for different parts such as sensors, analog inputs, digital inputs, and other components. The diagram is organized to showcase the connections between these components, providing a clear understanding of how they work together within the device.)

Figure 25: Sensor supply variable

## 4.8.3 Maximum Ratings Tecu **= -40. . . +125** °C

[table_115][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Output voltage under overload conditions (e.g.', 2: '-1', 3: '33', 4: 'V', 5: ''}, {0: 'short circuit to supply voltages)', 1: '', 2: '', 3: '', 4: '', 5: ''}][/table_115]

## 4.8.4 Characteristics

[table_116][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cout', 1: 'Pin output capacitance', 2: '0.8', 3: '1.2', 4: 'µF', 5: ''}, {0: 'Vout', 1: 'Output voltage, 5-V setting', 2: '4.85', 3: '5.15', 4: 'V', 5: ''}, {0: 'Vout', 1: 'Output voltage, 6-V setting', 2: '5.80', 3: '6.20', 4: 'V', 5: ''}, {0: 'Vout', 1: 'Output voltage, 7-V setting', 2: '6.75', 3: '7.25', 4: 'V', 5: ''}, {0: 'Vout', 1: 'Output voltage, 8-V setting', 2: '7.70', 3: '8.30', 4: 'V', 5: ''}, {0: 'Vout', 1: 'Output voltage, 9-V setting', 2: '8.65', 3: '9.35', 4: 'V', 5: ''}, {0: 'Vout', 1: 'Output voltage, 10-V setting', 2: '9.60', 3: '10.40', 4: 'V', 5: ''}, {0: 'Pload', 1: 'Maximum output power, 5-V. . . 10-V setting', 2: '2.5', 3: 'W', 4: '', 5: ''}][/table_116]

TECU **= -40. . . +125** °C

## 4.9 Analog Input 3 Modes

![127_image_0_4756.png](The image is a white drawing of an empty seat arrangement with multiple rows of seats. There are several chairs lined up next to each other, creating a neatly organized seating area. The chairs vary in size and position, giving the impression of a well-designed layout for passengers.) 

[table_117][{0: 'Pin No.', 1: 'Function 1', 2: 'Function 2', 3: 'Function 3', 4: 'SW-define'}, {0: 'P103', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_00'}, {0: 'P127', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_01'}, {0: 'P104', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_02'}, {0: 'P128', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_03'}, {0: 'P105', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_04'}, {0: 'P129', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_05'}, {0: 'P106', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_06'}, {0: 'P130', 1: 'Analog 0. . . 5 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'Analog 0. . . 100 kΩ Input', 4: 'IO_ADC_07'}][/table_117]

8 multipurpose analog inputs with 12-bit resolution.

The inputs can be configured to 3 different operation modes individually by software:
- **Analog Voltage Input: 8 x 0 to 5 V, ratiometric or with absolute reference** - **Analog Current Input: 8 x 0 to 25 mA, analog current loop sensors**
- **Analog Resistance Input: 8 x 0 to 100 k**Ω
All inputs are short-circuit protected, independent of application software (included in low-level driver software). Each input is provided with a first-order low pass **filter with 3 ms time constant, allowing** 2 ms sample rate.

See also section *ADC - Analog to Digital Converter driver* of the API documentation [30].

## 4.9.3 Maximum Ratings

TECU **= -40. . . +125** °C

![128_image_0_4756.png](The image displays a blue screen with white text that reads "Symbol Parameter Overload Conditions." There are two numbers on the screen, one at the top left corner and another towards the right side of the screen. These numbers might represent values or measurements related to the subject matter being discussed in the context of the image.)

Note 1 Due to thermal reasons only one of the 8 inputs may be shorted **to 33 V at the**
same time. A connection to any supply voltage higher than 5 V is not allowed for normal operation.

## 4.9.4 Analog Voltage Input

![128_image_1_4756.png](The image displays a diagram of an electronic device with various components labeled throughout the drawing. There are multiple wires connecting different parts of the circuit, indicating that this is likely a complex system. Some key labels include "ADC," "CPU," "ECC," and "TMS320." These labels suggest that the device may be related to computer processing or data analysis. The diagram provides an overview of the components within the electronic device, allowing for better understanding of its functioning.)

## Absolute Vs. Ratiometric Voltage Measurement:

Many sensor types are available in absolute or ratiometric measurement variant.

- Absolute**: The sensor output voltage is a fixed value and directly corresponds to a physical**
value. For example, 2.5 V corresponds to 1 bar. Any tolerance **in the reference voltage of the** sensor and the ECU generates additional measurement inaccuracy.

- Ratiometric: The sensor output voltage is a fixed percentage of the sensor **supply, the ratio**
corresponds to a physical value. For example, 50 % corresponds to 1 bar (or 2.5 V if the sensor supply is exactly 5.00 V). Any tolerance in the reference voltage of the sensor and the ECU is completely compensated and will not generate additional measurement inaccuracy.

![129_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled throughout. There are multiple labels on the device, including "ADC," "ECC," "CPU," and "Sensor Supply." The diagram also features a green box that says "MTC7601" in it.  In addition to these labels, there is a reference to a figure numbered 28, which could be related to the electronic device's specifications or design. Overall, the image provides an overview of the components and their arrangement within the electronic device.)

Due to the described behavior, it is generally recommended to use ratiometric sensors. Absolute or ratiometric function selection is done by software for each input individually.

## 4.9.4.1 Characteristics Of 5 V Input (Ratiometric)

[table_118][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '98', 3: '107', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal input voltage range', 2: '0', 3: '5', 4: 'V', 5: ''}, {0: 'VIn', 1: 'Input voltage range', 2: '1', 3: '0.2', 4: '4.8', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '4,5', 3: '-15', 4: '+15', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2,4,5', 3: '-10', 4: '+10', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '4,5', 3: '-0.2', 4: '+0.2', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2,4,5', 3: '-0.2', 4: '+0.2', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '1.2207', 4: 'mV', 5: ''}][/table_118]

## 4.9.4.2 Characteristics Of 5 V Input (Absolute) Tecu **= -40. . . +125** °C 4.9.4.3 Characteristics Of 5 V Digital Input

[table_119][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '98', 3: '107', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal input voltage range', 2: '0', 3: '5', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '0.2', 4: '4.8', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3,5', 3: '-15', 4: '+15', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2,3,5', 3: '-10', 4: '+10', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3,5', 3: '-0.8', 4: '+0.8', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2,3,5', 3: '-0.6', 4: '+0.6', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '1.2207', 4: 'mV', 5: ''}][/table_119]

Note **1 For full accuracy**
Note 2 TECU **= -40. . . +85** °C
Note 3 Absolute measurement. This includes the conversion error **of the HY-TTC 500**
only. For the calculation of the total measurement error, it **is necessary to sum** the error of HY-TTC 500 and the absolute sensor error (measurement tolerance plus tolerance of external sensor reference).

Note **4 Ratiometric mode. This includes the conversion error of the HY-TTC 500 and the**
sensor supply error. For the calculation of the total measurement error, the error of HY-TTC 500 and the error of the ratiometric sensor (measurement tolerance) must be added.

Note **Configuration by application software**
Note 5 The total measurement error is the sum of zero reading error and the proportional error.

[table_120][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '4.8', 3: '5', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage', 2: '4.9', 3: '5.1', 4: 'V', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: 'V', 4: '', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '5', 3: 'V', 4: '', 5: ''}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '1.2207', 4: 'mV', 5: ''}, {0: 'Note', 1: '1', 2: 'For full accuracy', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'TECU = -40. . . +85 °C', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '3', 2: 'Absolute measurement. This includes the conversion error of the HY-TTC 500', 3: '', 4: '', 5: ''}][/table_120]

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

![131_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as resistors, capacitors, and transistors. There are two main sections within the circuit, one on the left side and another on the right side.  In the left section, there is a resistor labeled R1, followed by a capacitor C1, and then an amplifier with a transistor T1. The right section of the circuit consists of a resistor R2, a capacitor C2, and another transistor T2. There are also two smaller transistors in this section, one near the center and the other towards the bottom.  The diagram is labeled with various text descriptions, such as "analog input," "signal processor," "sensor supply," "analog output," and "ADC." These labels provide context to the purpose of the circuit and its components.)

## 4.9.5.1 Characteristics Of Analog Current Input

[table_121][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'RCS', 1: 'Current sense resistor', 2: '1', 3: '177', 4: '185', 5: 'Ω'}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'I in', 1: 'Input current range', 2: '0', 3: '25', 4: 'mA', 5: ''}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '6.78', 4: 'µA', 5: ''}, {0: 'I tol-0', 1: 'Zero reading error', 2: '3', 3: '-70', 4: '+70', 5: 'µA'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '2,3', 3: '-40', 4: '+40', 5: 'µA'}, {0: 'I tol-p', 1: 'Proportional error', 2: '3', 3: '-2.5', 4: '+2.5', 5: '%'}, {0: 'I tol-p', 1: 'Proportional error', 2: '2,3', 3: '-2.0', 4: '+2.0', 5: '%'}][/table_121]

Note **1 This is the load resistor value for the current loop sensor.**
Note 2 TECU **= -40. . . +85** °C
Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**

## 4.9.6 Analog Resistance Input

Input for 0. . . 100kΩ **resistance sensor measurement.**
Resistive sensors are for example NTC or PTC resistors for temperature measurement. The actual resistor value of the sensor is computed from the measured input voltage together with the known reference resistor value. Be aware that this measurement setup has the highest accuracy and resolution if the sensors resistance is in the magnitude **of the reference resistors value.**

![132_image_0_4756.png](The image displays a diagram of an electronic circuit with various components labeled on it. There are two main parts to the circuit: one part is labeled "ECCU," while the other part has labels such as "ADC" and "TMMS706." The ECCU appears to be connected to the ADC, which in turn connects to the TMMS706.  In addition to these main components, there are several smaller labels on the diagram, indicating various other parts of the circuit. Overall, the image provides a detailed view of an electronic device's internal structure and connections.)

The resistance mode may also be used as digital input with switches connected to ground, see Figure 32 **on the current page. The use of switches to BAT+ is not allowed.** To enhance the diagnostic coverage, use switches of type Namur. With a Namur-type switch sensor, short to ground, short to BAT+ and cable defects can be easily **detected.**

![133_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as resistors, capacitors, and transistors. There are multiple labels on the circuit, indicating different parts and their functions. A green box is also present within the circuit, which could represent a power supply or another essential component.  The diagram provides a detailed view of the electronic device's structure, allowing for better understanding of its operation and potential maintenance requirements.)

![133_image_1_4756.png](The image displays a diagram of an electronic circuit with various components such as a switch, a green box, and a CPU. There are also several other smaller boxes scattered throughout the circuit. A label is present near the top left corner of the image, which reads "EUC."  In addition to these components, there are two arrows pointing towards different parts of the circuit, likely indicating connections or paths within the system. The overall layout and arrangement of the electronic components suggest a complex interconnected network.)

## 4.9.6.1 Characteristics Of Analog Resistance Input

Resistance sensors are, e. g., PTC resistors for temperature measurement.

TECU **= -40. . . +125** °C

Symbol Parameter Note Min. Max. **Unit**

Cin Pin input capacitance **8 12 nF**

Rref Reference resistor 4831 4929 Ω

[table_122][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Rext_range Resistance measurement range', 1: '0', 2: '100', 3: 'kΩ', 4: '', 5: ''}][/table_122]

The resistance measurement tolerance is given at specific sensor resistance value. Any value in between needs to be linear interpolated.

TECU **= -40. . . +85** °C

[table_123][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Rtol-m', 1: 'Measurement tolerance for 0. . . 99 Ω', 2: '-5', 3: '+5', 4: 'Ω', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 100 Ω', 2: '-5', 3: '+5', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 200 Ω', 2: '-4', 3: '+4', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 500 Ω', 2: '-2.5', 3: '+2.5', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 1 k. . . 20 kΩ', 2: '-2', 3: '+2', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 50 kΩ', 2: '-3', 3: '+3', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 100 kΩ', 2: '-4', 3: '+4', 4: '%', 5: ''}][/table_123]

[table_124][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Rtol-m', 1: 'Measurement tolerance for 0. . . 99 Ω', 2: '-10', 3: '+10', 4: 'Ω', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 100 Ω', 2: '-10', 3: '+10', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 200 Ω', 2: '-6', 3: '+6', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 500 Ω. . . 20 kΩ', 2: '-3', 3: '+3', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 50 kΩ', 2: '-4', 3: '+4', 4: '%', 5: ''}, {0: 'Rtol-m', 1: 'Measurement tolerance for 100 kΩ', 2: '-5', 3: '+5', 4: '%', 5: ''}][/table_124]

TECU **= +85. . . +125** °C

## 4.10 Analog Input 2 Modes

4.10.1 Pinout

![135_image_1_4756.png](1. A white background with a green line on it. 2. The green line is curved and appears to be part of an object. 3. There are two blue lines on the white background. 4. One blue line is located near the top left corner, while the other one is positioned in the middle-left area.)

![135_image_0_4756.png](The image features a large green train with many seats lined up along its length. There are at least 14 rows of seats visible on the train, each row consisting of multiple chairs. The arrangement of these seats creates an organized and efficient seating layout for passengers to enjoy their journey.) 
Figure 33: Pinout of analog input 2 mode

[table_125][{0: 'Pin No.', 1: 'Function 1', 2: 'Function 2', 3: 'SW-define'}, {0: 'P107', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_08'}, {0: 'P131', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_09'}, {0: 'P108', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_10'}, {0: 'P132', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_11'}, {0: 'P109', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_12'}, {0: 'P133', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_13'}, {0: 'P110', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_14'}, {0: 'P134', 1: 'Analog 0. . . 5 V, 0. . . 10 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_15'}, {0: 'P111', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_16'}, {0: 'P135', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_17'}, {0: 'P112', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_18'}, {0: 'P136', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_19'}, {0: 'P113', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_20'}, {0: 'P137', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_21'}, {0: 'P114', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_22'}, {0: 'P138', 1: 'Analog 0. . . 5 V, 0. . . 32 V Input', 2: 'Analog 0. . . 25 mA Input', 3: 'IO_ADC_23'}][/table_125]

16 multipurpose analog inputs with 12-bit resolution. The inputs can be configured to 3 different operation modes individually by software:
- Analog Voltage Input: 8 x 0 to 5 V/ 0 to 10 V, ratiometric or with **absolute reference.** - Analog Voltage Input: 8 x 0 to 5 V/ 0 to 32 V, ratiometric or with **absolute reference.** - **Analog Current Input: 16 x 0 to 25 mA, analog current loop sensors.**
All inputs are short-circuit protected, independent of application software (included in low-level driver software). Each input is provided with a first-order low pass **filter with 3 ms time constant, and** converted with 2 ms sample rate. See also section *ADC - Analog to Digital Converter driver* **of the API documentation [30].**

## 4.10.3 Maximum Ratings Tecu **= -40. . . +125** °C

[table_126][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input voltage', 2: '1', 3: '-1', 4: '+33', 5: 'V'}][/table_126]

Note **1 Due to thermal reasons only one of 8 inputs (except 32 V setting) may be**
shorted to 33 V at the same time. A connection to any supply voltage higher than the configured voltage setting (5 V, 10 V or 32 V) is not allowed for normal operation.

## 4.10.4 Analog Voltage Input

See Section 4.9.4 on page 117 **for more information.**

## 4.10.4.1 Characteristics Of 5 V Input (Ratiometric)

[table_127][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '98', 3: '107', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal input voltage range', 2: '0', 3: '5', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '0.2', 4: '4.8', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '4,5', 3: '-15', 4: '+15', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2,4,5', 3: '-10', 4: '+10', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '4,5', 3: '-0.2', 4: '+0.2', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2,4,5', 3: '-0.2', 4: '+0.2', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '1.2207', 4: 'mV', 5: ''}][/table_127]

## 4.10.4.2 Characteristics Of 5 V Input (Absolute)

[table_128][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '98', 3: '107', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal input voltage range', 2: '0', 3: '5', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '0.2', 4: '4.8', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3,5', 3: '-15', 4: '+15', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2,3,5', 3: '-10', 4: '+10', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3,5', 3: '-0.8', 4: '+0.8', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2,3,5', 3: '-0.6', 4: '+0.6', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '1.2207', 4: 'mV', 5: ''}][/table_128]

## 4.10.4.3 Characteristics Of 10 V Input (Absolute) Tecu **= -40. . . +125** °C

[table_129][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '19', 3: '22.5', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal input voltage range', 2: '0', 3: '10', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '0.2', 4: '10', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3,5', 3: '-18', 4: '+18', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2,3,5', 3: '-13', 4: '+13', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3,5', 3: '-1.8', 4: '+1.8', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2,3,5', 3: '-1.6', 4: '+1.6', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '2.57', 4: 'mV', 5: ''}][/table_129]

## 4.10.4.4 Characteristics Of 32 V Input (Absolute)

[table_130][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '14.7', 3: '15.3', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vnom', 1: 'Nominal input voltage range', 2: '0', 3: '32', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '0.2', 4: '32', 5: 'V'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '5', 3: '-50', 4: '+50', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2,5', 3: '-45', 4: '+45', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3,5', 3: '-4', 4: '+4', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2,5', 3: '-3', 4: '+3', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '8.59', 4: 'mV', 5: ''}][/table_130]

TECU **= -40. . . +125** °C

## 4.10.4.5 Characteristics Of 32 V Digital Input

[table_131][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '14.7', 3: '15.3', 4: 'kΩ', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: 'V', 4: '', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '32', 3: 'V', 4: '', 5: ''}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '8.59', 4: 'mV', 5: ''}, {0: 'Note', 1: '1', 2: 'For full accuracy', 3: '', 4: '', 5: ''}, {0: '2', 1: 'TECU = -40. . . +85 °C', 2: '', 3: '', 4: '', 5: ''}, {0: 'Note Note', 1: '3', 2: 'Absolute measurement. This includes the conversion error of the HY-TTC 500 only. For the calculation of the total measurement error, it is necessary to sum the error of HY-TTC 500 and the absolute sensor error (measurement tolerance plus tolerance of external sensor reference).', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '4', 2: 'Ratiometric mode. This includes the conversion error of the HY-TTC 500 and the sensor supply error. For the calculation of the total measurement error, the error of HY-TTC 500 and the error of the ratiometric sensor (measurement tolerance) must be added.', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '5', 2: 'The total measurement error is the sum of zero reading error and the propor\x02tional error.', 3: '', 4: '', 5: ''}, {0: 'Note', 1: 'Configuration by application software', 2: '', 3: '', 4: '', 5: ''}][/table_131]

## 4.10.5 Analog Current Input

See Section 4.9.5 on page 120 **for more information.**

## 4.10.5.1 Characteristics Of Analog Current Input Tecu **= -40. . . +125** °C

[table_132][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'RCS', 1: 'Current sense resistor', 2: '1', 3: '177', 4: '185', 5: 'Ω'}, {0: 'τin', 1: 'Input low pass filter', 2: '2.2', 3: '3.8', 4: 'ms', 5: ''}, {0: 'I in', 1: 'Input current range', 2: '0', 3: '25', 4: 'mA', 5: ''}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '6.78', 4: 'µA', 5: ''}, {0: 'I tol-0', 1: 'Zero reading error', 2: '3', 3: '-70', 4: '+70', 5: 'µA'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '2,3', 3: '-40', 4: '+40', 5: 'µA'}, {0: 'I tol-p', 1: 'Proportional error', 2: '3', 3: '-2.5', 4: '+2.5', 5: '%'}, {0: 'I tol-p', 1: 'Proportional error', 2: '2,3', 3: '-2.0', 4: '+2.0', 5: '%'}][/table_132]

Note **1 This is the load resistor value for the current loop sensor.**
Note 2 TECU **= -40. . . +85** °C
Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.11 Timer Inputs

![141_image_1_4756.png](The image is a black and white drawing of an electronic device with multiple rows of buttons. There are at least twelve buttons visible on the device, arranged in various positions across the drawing. Some buttons are located near the top left corner, while others can be found closer to the center or towards the bottom right side of the image. The arrangement of these buttons suggests that they might be part of a control panel or interface for operating the electronic device.)

![141_image_0_4756.png](100% of the seats are empty, with no passengers occupying them. The rows of seats are arranged in a neat and orderly manner, creating an organized appearance.) 
Figure 34: Pinout of timer input

[table_133][{0: 'Pin No.', 1: 'Function', 2: 'SW-define'}, {0: 'P115', 1: 'Timer Input', 2: 'IO_PWD_00'}, {0: 'P139', 1: 'Timer Input', 2: 'IO_PWD_01'}, {0: 'P116', 1: 'Timer Input', 2: 'IO_PWD_02'}, {0: 'P140', 1: 'Timer Input', 2: 'IO_PWD_03'}, {0: 'P117', 1: 'Timer Input', 2: 'IO_PWD_04'}, {0: 'P141', 1: 'Timer Input', 2: 'IO_PWD_05'}, {0: 'P122', 1: 'Timer Input', 2: 'IO_PWD_06'}, {0: 'P146', 1: 'Timer Input', 2: 'IO_PWD_07'}, {0: 'P123', 1: 'Timer Input', 2: 'IO_PWD_08'}, {0: 'P147', 1: 'Timer Input', 2: 'IO_PWD_09'}, {0: 'P124', 1: 'Timer Input', 2: 'IO_PWD_10'}, {0: 'P148', 1: 'Timer Input', 2: 'IO_PWD_11'}][/table_133]

![142_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as resistors, capacitors, and transistors. There are multiple labels on the diagram, indicating different parts of the circuit. A green box is also present within the circuit, which could be a power supply or another component.  The diagram appears to be a schematic for an electronic device, possibly related to audio processing or amplification. The components are arranged in a way that allows for efficient flow and functioning of the device.)

12 digital inputs with timer function to process input signals such as frequency (rotational speed), pulse count and quadrature decoding (incremental length measurement), PWM etc. 6 out of 12 inputs can be alternatively used as digital (7/14 mA) current loop speed sensors. The inputs can be individually configured by software with a pull-up/pull-down resistor to adapt them to different sensor types, The timer input can be used as an analog voltage input as well. **For diagnosis, it is possible to** measure the analog voltage and frequency at the same channel **at the same time.** See also sections *PWD - Pulse Width Decode and digital timer input driver* and *DIO - Driver for* digital inputs and outputs **of the API documentation [30].**

## 4.11.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_134][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input voltage under overload conditions', 2: '-1', 3: '+33', 4: 'V', 5: ''}][/table_134]

![143_image_0_4756.png](The image displays a diagram of an electronic circuit board with various components such as resistors, capacitors, and transistors. There are multiple wires connecting these components, creating a complex network of interconnected parts.  In addition to the main circuit board, there is another smaller one located towards the right side of the image. The diagram also includes labels for different parts, making it easier to understand the functioning of the electronic device.)

![143_image_1_4756.png](The image displays a diagram of an electronic device with various components labeled on it. There are two main labels visible - "ECU" and "CPU." The ECU is located towards the top left side of the image, while the CPU is situated in the middle-left area.  In addition to these primary labels, there are several other smaller labels scattered throughout the diagram, indicating different parts or functions within the electronic device. Overall, the image provides a clear representation of the internal structure and components of this particular electronic component.)

![144_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as resistors, capacitors, and transistors. There are multiple wires connecting these components, forming a complex network. A CPU is also present within the circuit, indicating that this might be a computer or digital device.  The diagram is labeled with several text descriptions, including "EUC," which could refer to an electronic unit of measurement. The image provides a detailed view of the internal workings and connections of the electronic circuit, making it easier for someone to understand its functioning.)

![144_image_1_4756.png](The image displays a diagram of an electronic circuit with various components such as resistors, capacitors, and transistors. There are multiple wires connecting these components, indicating that this is a complex electrical system.  In addition to the main circuitry, there are labels on the diagram providing information about the different parts. The labels include "EUC," which could be an acronym or abbreviation for a specific term related to the electronic device. Overall, the image provides a detailed view of the inner workings and connections within this electrical system.)

## 4.11.4 Timer And Current Loop Inputs 4.11.4.1 Characteristics Of Timer Input

TECU **= -40. . . +125** °C

[table_135][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '7.5', 3: '10', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '1', 3: '4.25', 4: '4.8', 5: 'V'}, {0: 'τin', 1: 'Input low pass filter', 2: '1.4', 3: '3.4', 4: 'µs', 5: ''}, {0: 'Fmax', 1: 'Maximum input frequency range', 2: '20', 3: 'kHz', 4: '', 5: ''}, {0: 'Fmin', 1: 'Minimum input frequency', 2: '0.1', 3: 'Hz', 4: '', 5: ''}, {0: 'τmin', 1: 'Minimum on/off time to be measured by timer unit', 2: '20', 3: 'µs', 4: '', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: '2', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '3', 3: '32', 4: 'V', 5: ''}, {0: 't res', 1: 'Timer resolution', 2: '2', 3: '2', 4: '2', 5: 'µs'}, {0: 't res', 1: 'Timer resolution', 2: '3', 3: '0.5', 4: '0.5', 5: 'µs'}, {0: 'Note', 1: '1', 2: 'This is the input voltage with pull-up setting, without the sensor connected.', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'IO_PWD_00 - IO_PWD_05', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '3', 2: 'IO_PWD_06 - IO_PWD_11', 3: '', 4: '', 5: ''}][/table_135]

## 4.11.4.2 Characteristics Of Current Loop Input

The timer input IO_PWD_00 to IO_PWD_05 can be alternatively **also used as digital (7/14 mA)** current loop sensor inputs. See Figure 40 **on the facing page.**
During power down (Terminal 15 **off), the ECU does not disconnect the timer and current loop**
sensor inputs. It is not recommended to supply the sensors permanently in order to prevent battery discharge. TTControl GmbH recommends one of the following 2 options:
1. Option 1**: Use a digital output for supplying the sensor. When the device is switched off, the**
ECU can perform an application-controlled shutdown, e. g., **in order to operate a cooling fan** to cool down an engine until the temperature is low enough or to store data in the non-volatile memory of the ECU. If the application controlled shut-down is finished, the ECU switches off and consumes less than 1 mA of battery current (including sensors).

2. **Option 2**: Terminal 15 **is used to supply the current loop sensor directly.**
Note that Terminal 15 **is often used to switch relays or other inductive loads directly. This** may cause transients in excess of ±50 V, for which the sensor must be specified.

[table_136][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit', 5: ''}, {0: 'Rpdc', 1: 'Pull-down resistor (current loop config.)', 2: '1', 3: '88', 4: '93', 5: 'Ω'}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '7.5', 3: '10', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4.25', 3: '4.8', 4: 'V', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '1.4', 3: '1.6', 4: 'µs', 5: ''}, {0: 'Fmax', 1: 'Maximum input frequency range', 2: '20', 3: 'kHz', 4: '', 5: ''}, {0: 'Fmin', 1: 'Minimum input frequency', 2: '0.1', 3: 'Hz', 4: '', 5: ''}, {0: 'τmin', 1: 'Minimum on/off time to be measured by timer unit', 2: '20', 3: 'µs', 4: '', 5: ''}, {0: 'I il', 1: 'Input current for low level(current loop config.)', 2: '4', 3: '8.5', 4: 'mA', 5: ''}, {0: 'I ih', 1: 'Input current for high level (current loop config.)', 2: '11', 3: '20', 4: 'mA', 5: ''}, {0: 'I il SRC', 1: 'Input current (7/14 mA) sensor SRC too low', 2: '2', 3: '0', 4: '4', 5: 'mA'}, {0: 'I ih SRC', 1: 'Input current (7/14 mA) sensor SRC too high', 2: '3', 3: '20', 4: 'mA', 5: ''}, {0: 't res', 1: 'Timer resolution', 2: '2', 3: '2', 4: 'µs', 5: ''}][/table_136]

Note **1 With software setting for digital (7/14 mA) current loop sensor inputs (ABS-type**
sensors).

Note **2 Fault detection window for defect digital (7/14 mA) current loop sensor inputs**
with too low current.

Note **3 Fault detection window for defect digital (7/14 mA) current loop sensor inputs**
with too high current. If the current exceeds the maximum input current, then overload protection gets active.

![146_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled. There are multiple wires connecting different parts of the circuit, indicating that this is likely a complex electrical system. Some of the key labels include "RPM Sensor," "ECU," and "CPU."  In addition to these main components, there are smaller labels throughout the diagram, providing more detailed information about each part. The overall layout suggests that this could be an instructional guide or a schematic for understanding how such electronic devices function.)

## 4.11.5 Analog And Digital Inputs 4.11.5.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C 4.11.5.2 Characteristics Of Digital Input

[table_137][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '7.5', 3: '10', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '2', 3: '4.25', 4: '4.8', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '0', 3: '32', 4: 'V', 5: ''}, {0: 'τin', 1: 'Input low pass filter (analog path)', 2: '8', 3: '12', 4: 'ms', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3', 3: '-55', 4: '+55', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '1,3', 3: '-50', 4: '+50', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3', 3: '-4', 4: '+4', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '1,3', 3: '-3', 4: '+3', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '8.00', 4: 'mV', 5: ''}][/table_137]

[table_138][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '7.5', 3: '10', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '2', 3: '4.25', 4: '4.8', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '0', 3: '32', 4: 'V', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '2.8', 3: '3.2', 4: 'µs', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: '2', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '3', 3: '32', 4: 'V', 5: ''}][/table_138]

Note 1 TECU **= -40. . . +85** °C
Note 2 This is the input voltage with pull-up setting, without the **sensor connected.**
Note 3 The total measurement error is the sum of zero reading error and the proportional error.

TECU **= -40. . . +125** °C

## 4.12 High-Side Pwm Outputs 4.12.1 Pinout

![148_image_0_4756.png](The image is a white drawing of an electronic device with many rows of buttons arranged neatly. There are at least twelve rows of buttons visible, each row containing multiple buttons. The arrangement suggests that this could be a control panel or interface for various functions within the device.) 

## Figure 41: Pinout Of High-Side Pwm Outputs

The following table depicts the high-side PWM outputs together with their corresponding external and secondary shut-off group/paths and power stages.

[table_139][{0: 'Pin No.', 1: 'Function', 2: 'SW-define', 3: 'Ext./Second. Shut-off', 4: 'Power stage'}, {0: 'P153', 1: 'High-Side PWM Output', 2: 'IO_PWM_00', 3: 'A', 4: 'a'}, {0: 'P177', 1: 'High-Side PWM Output', 2: 'IO_PWM_01', 3: 'A', 4: 'a'}, {0: 'P156', 1: 'High-Side PWM Output', 2: 'IO_PWM_02', 3: 'A', 4: 'b'}, {0: 'P180', 1: 'High-Side PWM Output', 2: 'IO_PWM_03', 3: 'A', 4: 'b'}, {0: 'P159', 1: 'High-Side PWM Output', 2: 'IO_PWM_04', 3: 'A', 4: 'c'}, {0: 'P183', 1: 'High-Side PWM Output', 2: 'IO_PWM_05', 3: 'A', 4: 'c'}, {0: 'P186', 1: 'High-Side PWM Output', 2: 'IO_PWM_06', 3: 'A', 4: 'd'}, {0: 'P162', 1: 'High-Side PWM Output', 2: 'IO_PWM_07', 3: 'A', 4: 'd'}, {0: 'P189', 1: 'High-Side PWM Output', 2: 'IO_PWM_08', 3: 'A', 4: 'e'}, {0: 'P165', 1: 'High-Side PWM Output', 2: 'IO_PWM_09', 3: 'A', 4: 'e'}, {0: 'P192', 1: 'High-Side PWM Output', 2: 'IO_PWM_10', 3: 'A', 4: 'f'}, {0: 'P168', 1: 'High-Side PWM Output', 2: 'IO_PWM_11', 3: 'A', 4: 'f'}, {0: 'P195', 1: 'High-Side PWM Output', 2: 'IO_PWM_12', 3: 'A', 4: 'g'}, {0: 'P171', 1: 'High-Side PWM Output', 2: 'IO_PWM_13', 3: 'A', 4: 'g'}, {0: 'P154', 1: 'High-Side PWM Output', 2: 'IO_PWM_14', 3: 'B', 4: 'h'}, {0: 'P178', 1: 'High-Side PWM Output', 2: 'IO_PWM_15', 3: 'B', 4: 'h'}, {0: 'P157', 1: 'High-Side PWM Output', 2: 'IO_PWM_16', 3: 'B', 4: 'i'}][/table_139]

[table_140][{0: 'Pin No.', 1: 'Function', 2: 'SW-define', 3: 'Ext./Second. Shut-off', 4: 'Power stage'}, {0: 'P181', 1: 'High-Side PWM Output', 2: 'IO_PWM_17', 3: 'B', 4: 'i'}, {0: 'P160', 1: 'High-Side PWM Output', 2: 'IO_PWM_18', 3: 'B', 4: 'j'}, {0: 'P184', 1: 'High-Side PWM Output', 2: 'IO_PWM_19', 3: 'B', 4: 'j'}, {0: 'P187', 1: 'High-Side PWM Output', 2: 'IO_PWM_20', 3: 'B', 4: 'k'}, {0: 'P163', 1: 'High-Side PWM Output', 2: 'IO_PWM_21', 3: 'B', 4: 'k'}, {0: 'P190', 1: 'High-Side PWM Output', 2: 'IO_PWM_22', 3: 'B', 4: 'l'}, {0: 'P166', 1: 'High-Side PWM Output', 2: 'IO_PWM_23', 3: 'B', 4: 'l'}, {0: 'P193', 1: 'High-Side PWM Output', 2: 'IO_PWM_24', 3: 'B', 4: 'm'}, {0: 'P169', 1: 'High-Side PWM Output', 2: 'IO_PWM_25', 3: 'B', 4: 'm'}, {0: 'P196', 1: 'High-Side PWM Output', 2: 'IO_PWM_26', 3: 'B', 4: 'n'}, {0: 'P172', 1: 'High-Side PWM Output', 2: 'IO_PWM_27', 3: 'B', 4: 'n'}, {0: 'P101', 1: 'High-Side PWM Output', 2: 'IO_PWM_28', 3: 'C', 4: 'o'}, {0: 'P125', 1: 'High-Side PWM Output', 2: 'IO_PWM_29', 3: 'C', 4: 'o'}, {0: 'P150', 1: 'High-Side PWM Output', 2: 'IO_PWM_30', 3: 'C', 4: 'p'}, {0: 'P174', 1: 'High-Side PWM Output', 2: 'IO_PWM_31', 3: 'C', 4: 'p'}, {0: 'P102', 1: 'High-Side PWM Output', 2: 'IO_PWM_32', 3: 'C', 4: 'q'}, {0: 'P126', 1: 'High-Side PWM Output', 2: 'IO_PWM_33', 3: 'C', 4: 'q'}, {0: 'P151', 1: 'High-Side PWM Output', 2: 'IO_PWM_34', 3: 'C', 4: 'r'}, {0: 'P175', 1: 'High-Side PWM Output', 2: 'IO_PWM_35', 3: 'C', 4: 'r'}][/table_140]

Power output stages with freewheeling diodes for inductive **loads with low-side connection.**
The load current is controlled with PWM. For better accuracy **and diagnostics, a current measurement/feedback loop is provided.**
If an error is detected in a safety-critical system, the watchdog or the main CPU can disable the output stage (off state), triggered by the application software. For diagnostic and safety reasons, the actual PWM output signal is looped back to a timer input, and the measured value is compared to the set value. For safety-critical applications, fast error detection is necessary. For this reason, a permanent PWM output is available, setting a minimum on/off time to 100/200 µ**s instead of 0 or 100 % duty cycle. This means, there is a reliable periodical state**
change of the output allowing permanent load monitoring that is independent of the operation point.

So, even when the load is switched off, a short on the load can be detected.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *PWM - Pulse Width Modulation driver* of the API documentation [30].

![150_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as a CPU, power supply, and other devices. There are multiple wires connecting these components, indicating that this is a complex system. A green box can also be seen within the circuitry, which might serve a specific purpose or function in the overall operation of the device. The diagram provides an overview of the interconnected parts and their relationships, allowing for better understanding of how the electronic system works.)

## 4.12.2.1 Power Stage Pairing

If outputs shall be used in parallel, always combine two channels from the same double-channel power stage and use the digital output mode. See Section 4.12.1 on page 137 **for using the right** power stage outputs in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip.

For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.12.2.2 Mutual Exclusive Mode

The HY-TTC 500 uses double-channel high-side power stages. **For load leveling it is a benefit if** loads, which are switched on mutually exclusive (which means either load A, or load B is on, but not A and B at the same time), are connected to the same double-channel power stage. This reduces the thermal stress of the components. The power stage pairing is given in Section 4.12.1 on page **137.** For HS PWM output stage operating in 444–1000 Hz mode, the current limit is increased to 1 A if used in mutual exclusive mode, see Section 4.12.4.1 **on the next page.**

## 4.12.3 Maximum Ratings

[table_141][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input voltage under overload conditions', 2: '1', 3: '-0.5', 4: '32', 5: 'V'}, {0: 'Vin', 1: 'Input voltage under overload conditions', 2: '1', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_141]

Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.12.4 High-Side Pwm Outputs 4.12.4.1 Characteristics Of High-Side Pwm Output Tecu **= -40. . . +125** °C

[table_142][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cout', 1: 'Pin input capacitance', 2: '15', 3: '25', 4: 'nF', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '4', 3: '5', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4.2', 3: '4.8', 4: 'V', 5: ''}, {0: 'fPWM', 1: 'PWM frequency', 2: '1', 3: '50', 4: '1000', 5: 'Hz'}, {0: 'Tmin-on', 1: 'Minimum on time', 2: '2', 3: '100', 4: 'µs', 5: ''}, {0: 'Tmin-off', 1: 'Minimum off time', 2: '2', 3: '200', 4: 'µs', 5: ''}, {0: 'Ron', 1: 'On-resistance', 2: '150', 3: 'mΩ', 4: '', 5: ''}, {0: 'Imax', 1: 'Maximum load current (f = 50. . . 200 Hz)', 2: '3', 3: 'A', 4: '', 5: ''}, {0: 'Imax', 1: 'Maximum load current (f = 50. . . 200 Hz)', 2: '3', 3: '4', 4: 'A', 5: ''}, {0: 'Imax', 1: 'Maximum load current (f = 210. . . 400 Hz)', 2: '1.2', 3: 'A', 4: '', 5: ''}, {0: 'Imax', 1: 'Maximum load current (f = 444. . . 1000 Hz)', 2: '0.1', 3: 'A', 4: '', 5: ''}, {0: 'Imax', 1: 'Maximum load current (f = 444. . . 1000 Hz)', 2: '4', 3: '1', 4: 'A', 5: ''}, {0: 'Ipeak', 1: 'Peak load current limit', 2: '5', 3: '5.5', 4: 'A', 5: ''}, {0: 'Rload_min Minimum coil resistance (12 V)', 1: '6', 2: '2', 3: 'Ω', 4: '', 5: ''}, {0: 'Rload_min Minimum coil resistance (24 V)', 1: '6', 2: '4', 3: 'Ω', 4: '', 5: ''}, {0: 'Rload_max Maximum load resistance', 1: '7', 2: '1', 3: 'kΩ', 4: '', 5: ''}][/table_142]

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

[table_143][{0: 'Output Signal', 1: 'Status Signal', 2: '', 3: ''}, {0: 'Normal', 1: 'Open Load', 2: 'Short to GND', 3: 'Short to UBAT'}, {0: 'On', 1: '×', 2: '×', 3: ''}, {0: 'Off', 1: '×', 2: '', 3: ''}][/table_143]

= detected
× **= not detected**

## 4.12.4.3 Characteristics Of Current Measurement Tecu **= -40. . . +125** °C

[table_144][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'I tol-p', 1: 'Proportional error', 2: '1,2', 3: '-2.5', 4: '+2.5', 5: '%'}, {0: 'I tol-p', 1: 'Proportional error', 2: '4,2', 3: '-2.0', 4: '+2.0', 5: '%'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '1,2', 3: '-40', 4: '+40', 5: 'mA'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '1,2,4', 3: '-35', 4: '+35', 5: 'mA'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '1', 4: 'mA', 5: ''}, {0: 'fg_LP', 1: 'Cut off frequency of 3rd order low pass filter', 2: '3', 3: '30', 4: '50', 5: 'Hz'}, {0: 'Note', 1: '1', 2: 'The measured value is clipped in software if below zero. So at some devices a', 3: '', 4: '', 5: ''}][/table_144]

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

[table_145][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cout', 1: 'Pin input capacitance', 2: '15', 3: '25', 4: 'nF', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '4', 3: '5', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4.2', 3: '4.7', 4: 'V', 5: ''}, {0: 'Ron', 1: 'On-resistance', 2: '150', 3: 'mΩ', 4: '', 5: ''}, {0: 'Imax', 1: 'Maximum load current', 2: '3', 3: 'A', 4: '', 5: ''}, {0: 'Imax', 1: 'Maximum load current', 2: '1', 3: '4', 4: 'A', 5: ''}, {0: 'Ipeak', 1: 'Peak load current limit', 2: '2', 3: '5.5', 4: 'A', 5: ''}, {0: 'Rload_min Minimum coil resistance (12 V)', 1: '3', 2: '2', 3: 'Ω', 4: '', 5: ''}, {0: 'Rload_min Minimum coil resistance (24 V)', 1: '3', 2: '4', 3: 'Ω', 4: '', 5: ''}, {0: 'Rload_max Maximum load resistance', 1: '4', 2: '1', 3: 'kΩ', 4: '', 5: ''}, {0: 'Note', 1: '1', 2: 'TECU = -40. . . +85 °C', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'For t < 5 ms', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '3', 2: 'Additionally to observing the maximum load current limit, there is also a mini\x02mum load resistance limit, depending on the battery supply voltage.', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '4', 2: 'Exceeding this value will trigger open load detection.', 3: '', 4: '', 5: ''}][/table_145]

## Tecu **= -40. . . +125** °C

See Section 4.12.4.3 on page 142 **for characteristics of current measurement.**

## 4.12.6 Digital And Frequency Inputs

If a high-side output is not needed on IO_PWM_00 - IO_PWM_35, **the loop-back path of these** output stages can be alternatively used as a digital or frequency input. External switches which are directly switching to battery voltage must not be used with alternative inputs. See Section 6.6 on page 218 **for more information on using the alternative digital and frequency** input function of the High-Side PWM Outputs.

## 4.12.6.1 Characteristics Of Digital Input

[table_146][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '15', 3: '25', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '1.4', 3: '3.4', 4: 'µs', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '4', 3: '5', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage', 2: '4.2', 3: '4.8', 4: 'V', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: '2', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '1', 3: '3', 4: '32', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_146]

Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.12.6.2 Characteristics Of Timer Input

[table_147][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit', 5: ''}, {0: 'Cin', 1: 'Pin input capacitance', 2: '15', 3: '25', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '1.4', 3: '3.4', 4: 'µs', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '4', 3: '5', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage', 2: '4.25', 3: '4.8', 4: 'V', 5: ''}, {0: 'fmax', 1: 'Maximum input frequency', 2: '1', 3: '2', 4: 'kHz', 5: ''}, {0: 'fmax', 1: 'Maximum input frequency', 2: '2', 3: '10', 4: 'kHz', 5: ''}, {0: 'fmin', 1: 'Minimum input frequency', 2: '3', 3: '0.1', 4: 'Hz', 5: ''}, {0: 't res', 1: 'Timer resolution', 2: '1', 3: '1', 4: 'µs', 5: ''}, {0: 'tmin', 1: 'Minimum on/off time to be measured by timer input', 2: '20', 3: 'µs', 4: '', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: '2', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '4', 3: '3', 4: '32', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '4', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_147]

Note **1 With open collector sensor output.** Note **2 With push-pull sensor output stage.** Note **3 Due to the dynamic range of the timer, there is a minimum frequency when a**
timer overflow occurs. Even at a lower frequency the output value will be read as 0 Hz.

Note **4 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.12.7 Secondary Shut-Off Paths

The available PWM output stages are allocated to three independent secondary shut-off paths (=Safety switches). See Section 4.12.1 on page **137, column** *Ext./Second. Shut-Off* **of pinout table.** For safety-critical applications, these paths allow to selectively activate/deactivate a set of specific PWM outputs in case of a detected actuator failure. Thus, the **ECU can be operated in a reduced** (limp home) mode that allows the vehicle to be safely driven to the repair shop. Figure 43 **on the current page shows the detailed distribution of the PWM output stages to the**
shut-off paths.

See Section 5.1.1 on page 188 **for safety concept overview.**

![157_image_0_4756.png](The image displays a diagram of an electrical system with various components labeled throughout. There are several power sources, including GAT (Power), SAT (Power), and BAT (Power). Additionally, there is a CPU (Central Processing Unit) present in the diagram.  The diagram also features multiple labels for different types of equipment, such as watchdog, global, and various other components. The image provides an overview of the electrical system's structure and its individual parts, making it easier to understand the connections between them.)

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

[table_148][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpd', 1: 'Pull-down resistor', 2: '14.7', 3: '15.3', 4: 'kΩ', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '0', 3: '32', 4: 'V', 5: ''}, {0: 'Vil', 1: 'Input voltage level to signal a low level input', 2: '0', 3: '4', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage level to signal a high level input', 2: '6', 3: '32', 4: 'V', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '2', 3: '-50', 4: '+50', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '1,2', 3: '-45', 4: '+45', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '2', 3: '-4', 4: '+4', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '1,2', 3: '-3', 4: '+3', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '8.59', 4: 'mV', 5: ''}][/table_148]

## 4.12.9 Tertiary Shut-Off Path 4.12.9.1 Functional Description

Loads on safety-critical high-side PWM channels can be connected to the ground as shown in Figure 42 on page 139 or to a low-side digital output as shown in Figure 44 **on the current page.**

![159_image_0_4756.png](4-wire electrical circuit diagram showing a power supply with multiple components. The image is displayed on a white background, making it easy to read. There are several wires and connections within the circuit, including a green box that appears to be an important part of the system. The diagram provides a clear visual representation of the various components in the electrical circuit, allowing for better understanding of its functioning.)

With the tertiary shut-off configuration shown in 44 **the HY-TTC 500 is able to switch off the high-side** PWM channels even if the load has a short circuit to the positive battery supply.

Please refer to section *PWM - Pulse Width Modulation driver* **of the API documentation [30] for more** information how to configure such an output.

## 4.13 High-Side Digital Outputs

4.13.1 Pinout

![160_image_1_4756.png](The image features a large stadium with several rows of seats. There are multiple chairs visible throughout the scene, some closer to the foreground while others are further back. A few cars can also be seen within the stadium, likely parked in designated areas or waiting for attendees to arrive.)

![160_image_0_4756.png](The image features a large white box with many rows of green and blue lights inside. There are at least twelve rows of these lights, each containing multiple individual lights. The arrangement of the lights creates an organized pattern within the box. This could possibly represent a display or an electronic device that utilizes these colored lights for various purposes.) 
Figure 45: Pinout of high-side digital outputs

[table_149][{0: 'Pin No.', 1: 'Function', 2: 'SW-define', 3: 'Power stage'}, {0: 'P149', 1: 'High-Side Digital Output', 2: 'IO_DO_00', 3: 'a'}, {0: 'P173', 1: 'High-Side Digital Output', 2: 'IO_DO_01', 3: 'a'}, {0: 'P152', 1: 'High-Side Digital Output', 2: 'IO_DO_02', 3: 'b'}, {0: 'P176', 1: 'High-Side Digital Output', 2: 'IO_DO_03', 3: 'b'}, {0: 'P155', 1: 'High-Side Digital Output', 2: 'IO_DO_04', 3: 'c'}, {0: 'P179', 1: 'High-Side Digital Output', 2: 'IO_DO_05', 3: 'c'}, {0: 'P158', 1: 'High-Side Digital Output', 2: 'IO_DO_06', 3: 'd'}, {0: 'P182', 1: 'High-Side Digital Output', 2: 'IO_DO_07', 3: 'd'}][/table_149]

Eight power output stages with freewheeling diodes for inductive and resistive loads with low-side connection. Suitable loads are lamps, valves, relays etc. If an error is detected in a safety-critical resource, the watchdog CPU or the main CPU will disable the output stage (off state). For diagnostic reasons, the output signal is looped back to the CPU, and the value measured is compared with the value set. When the output is not used, the loop-back signal can be used as an analog input or as a digital input.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

![161_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled on it. There are multiple wires connecting different parts of the device, indicating its intricate structure. Some of the key labels include "CPU," "Digital Input," "Salt Power," and "Watchdog."  The diagram is accompanied by a description that explains each component's function in detail. The CPU (Central Processing Unit) is responsible for processing data and executing instructions, while the Digital Input allows for digital signals to be input into the device. Salt Power provides power to the device through the use of salt as an energy source, and the Watchdog monitors the system for any errors or malfunctions.  Overall, this diagram offers a clear understanding of the electronic device's internal workings and its various components.)

## 4.13.2.1 Power Stage Pairing

If outputs shall be used in parallel, always combine two channels from the same double-channel power stage and use the digital output mode. See Section 4.13.1 on page 149 **for using the right** power stage outputs in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip.

For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.13.2.2 Mutual Exclusive Mode

The HY-TTC 500 uses double-channel high-side power stages. **For load leveling it is a benefit if** loads, which are switched on mutually exclusive (which means either load A, or load B is on, but not A and B at the same time), are connected to the same double-channel power stage. This reduces the thermal stress of the components. The power stage pairing is given in Section 4.13.1 on page **149.**

## 4.13.3 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

![162_image_0_4756.png](The image displays a diagram with multiple lines and labels, possibly representing a signal output or status. There are several green dots scattered across the diagram, which could indicate different stages of operation or points of interest within the system.  In addition to the dots, there is a row of buttons at the top of the diagram, likely used for controlling or adjusting settings in the system. The presence of these buttons suggests that this diagram might be part of an electronic device or control panel.)

![162_image_1_4756.png](1. A computer screen displaying a message that reads "detected." 2. The word "not" is crossed out on the screen.)

## 4.13.4 Maximum Ratings

TECU **= -40. . . +125** °C

[table_150][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input/output voltage under overload conditions', 2: '-0.5', 3: 'BAT+ Power +0.5', 4: 'V', 5: ''}][/table_150]

## 4.13.5 High-Side Digital Outputs 4.13.5.1 Characteristics Of High-Side Output Tecu **= -40. . . +125** °C

[table_151][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '7.5', 3: '10', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4', 3: '4.5', 4: 'V', 5: ''}, {0: 'Ron', 1: 'On-resistance', 2: '100', 3: 'mΩ', 4: '', 5: ''}, {0: 'I load', 1: 'Nominal load current', 2: '0', 3: '3', 4: 'A', 5: ''}, {0: 'I load', 1: 'Nominal load current', 2: '1', 3: '0', 4: '4', 5: 'A'}, {0: 'Ipeak', 1: 'Peak load current', 2: '2', 3: '0', 4: '6', 5: 'A'}, {0: 'I tol-p', 1: 'Proportional error', 2: '3', 3: '-14', 4: '+14', 5: '%'}, {0: 'I tol-p', 1: 'Proportional error', 2: '1,3', 3: '-10', 4: '+10', 5: '%'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '3', 3: '-150', 4: '+150', 5: 'mA'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '1,3', 3: '-150', 4: '+150', 5: 'mA'}][/table_151]

Note 1 TECU **= -40. . . +85** °C
Note **2 Peak current for not more than 100 ms. Exceeding this value will trigger the**
overload protection and switch off the power stage. Steady state operation goes only up to 3 A/4 A depending on temperature.

Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.13.6 Analog And Digital Inputs

External switches which are directly switching to battery voltage must not be used with alternative inputs. See Section 6.6 on page 218 **for more information.**

## 4.13.6.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C

[table_152][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter (analog path)', 2: '1.5', 3: '2.5', 4: 'ms', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down', 2: '1', 3: '7.5', 4: '10', 5: 'kΩ'}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4', 3: '4.5', 4: 'V', 5: ''}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3', 3: '-55', 4: '+55', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '1,3', 3: '-50', 4: '+50', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3', 3: '-4', 4: '+4', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '1,3', 3: '-3', 4: '+3', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '13.4', 4: 'mV', 5: ''}, {0: 'Vin', 1: 'Input voltage measurement range', 2: '2', 3: '0', 4: '32', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '2', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_152]

Note 1 TECU **= -40. . . +85** °C
Note **2 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**

## 4.13.6.2 Characteristics Of Digital Input Tecu **= -40. . . +125** °C

[table_153][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '1.5', 3: '2.5', 4: 'ms', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '7.5', 3: '10', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4', 3: '4.5', 4: 'V', 5: ''}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: 'V', 4: '', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '1', 3: '32', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_153]

Note **Configuration by application software**
Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

## 4.14 High-Side Digital/Pvg/Vout Outputs

4.14.1 Pinout

![166_image_1_4756.png](100% of the image is white, with no visible objects or details.)

![166_image_0_4756.png](1. A white drawing of a train with many compartments is displayed on the left side of the image. 2. The train has multiple rows of seats, including one row that reads "PHS." 3. There are several other rows of seats in various positions within the train, each labeled with different letters and numbers.) 
Figure 47: Pinout of High-side digital/PVG/VOUT outputs

[table_154][{0: 'Pin No.', 1: 'Function', 2: 'SW-define', 3: 'Power stage'}, {0: 'P161', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_00', 3: 'a'}, {0: 'P185', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_01', 3: 'a'}, {0: 'P188', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_02', 3: 'b'}, {0: 'P164', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_03', 3: 'b'}, {0: 'P191', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_04', 3: 'c'}, {0: 'P167', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_05', 3: 'c'}, {0: 'P194', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_06', 3: 'd'}, {0: 'P170', 1: 'High-Side Digital Output/PVG/VOUT', 2: 'IO_PVG_07', 3: 'd'}][/table_154]

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

[table_155][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input/output voltage under overload conditions', 2: '-0.5', 3: 'BAT+ Power +0.5', 4: 'V', 5: ''}][/table_155]

## 4.14.4 High-Side Digital Outputs

Eight power output stages with freewheeling diodes for inductive and resistive loads with low-side connection. Suitable loads are lamps, valves, relays etc. If an error is detected in a safety-critical resource, the watchdog CPU or the main CPU can disable the output stage (off state). For diagnostic reasons the output signal is looped back to the CPU, and the value measured is compared with the value set. When the output is not used, the loop-back signal can be used as an analog input or as a digital input.

![168_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled on it. There are multiple wires connecting different parts of the device, indicating its intricate structure. Some key labels include "CPU," "ADC," "Watchdog," and "ATT Power."  In addition to these labels, there is a clock visible in the middle-left part of the image, which might be related to the electronic device's functioning or timekeeping capabilities. The diagram provides an overview of the components within this electronic system, highlighting their interconnectedness and importance for its proper operation.)

## 4.14.4.1 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and detection of load loss.

[table_156][{0: 'Output Signal', 1: 'Status Signal', 2: '', 3: ''}, {0: 'Normal', 1: 'Open Load', 2: 'Short to GND', 3: 'Short to UBAT'}, {0: 'On', 1: '×', 2: '×', 3: ''}, {0: 'Off', 1: '×', 2: '', 3: ''}][/table_156]

= detected
× **= not detected**

## 4.14.4.2 Characteristics Of High-Side Digital

TECU **= -40. . . +125** °C

[table_157][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '2.5', 3: '2.6', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '2.15', 3: '2.45', 4: 'V', 5: ''}, {0: 'Ron', 1: 'On-resistance', 2: '100', 3: 'mΩ', 4: '', 5: ''}, {0: 'I load', 1: 'Nominal load current', 2: '0', 3: '3', 4: 'A', 5: ''}, {0: 'Imax', 1: 'Maximum load current', 2: '1', 3: '4', 4: 'A', 5: ''}, {0: 'Ipeak', 1: 'Peak load current', 2: '2', 3: '0', 4: '6', 5: 'A'}, {0: 'I tol-p', 1: 'Proportional error', 2: '3', 3: '-14', 4: '+14', 5: '%'}, {0: 'I tol-p', 1: 'Proportional error', 2: '1,3', 3: '-10', 4: '+10', 5: '%'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '3', 3: '-150', 4: '+150', 5: 'mA'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '1,3', 3: '-150', 4: '+150', 5: 'mA'}, {0: 'Note', 1: '1', 2: 'TECU = -40. . . +85 °C', 3: '', 4: '', 5: ''}, {0: 'Note', 1: '2', 2: 'Peak current for maximal 100 ms. Exceeding this value will trigger overload', 3: '', 4: '', 5: ''}][/table_157]

Note 1 TECU **= -40. . . +85** °C
Note **2 Peak current for maximal 100 ms. Exceeding this value will trigger overload**
protection and switch off the power stage.Steady state operation goes only up to 3 A/4 A depending on temperature.

Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.14.5 Pvg Outputs

Proportional Valve Groups (PVG) are a group of hydraulic load-sensing valves with integrated electronics allowing advanced flow controllability, e.g., for load-independent flow control.

![170_image_0_4756.png](The image displays a diagram of an electrical system with various components labeled. There are two main sections within the diagram - one on the left side and another on the right side. The left section features a large number of labels, while the right section has fewer labels.  In addition to the labels, there is a small green box located near the bottom-right corner of the image. This box may contain more information or details about the electrical system being depicted in the diagram.) For diagnostic reasons in output mode, the output signal is looped back to the CPU, and the measured value is compared to the set value. If the difference between these two values is above a fixed limit, an overload is detected, and the output is disabled. The protection mechanism tries re-enabling the output 10 times per drive cycle. It is not allowed to use two outputs in parallel to increase driving strength.

The PVG output can be used to control PVG valves of the types PVEA, PVEH and PVES. These types of valves apply a low pass filter to the input signal and use the resulting DC voltage in relation to the valves supply voltage (BAT+) as a parameter for flow control. The HY-TTC 500 uses the BAT+ CPU pin as a reference voltage input. The principle schematic is shown in Figure 49 **on the current page. The output is open loop controlled. The ADC input is for** diagnostic purposes only and can be evaluated by the application software.

## 4.14.5.1 Characteristics Of Pvg

[table_158][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit', 5: ''}, {0: 'Cout', 1: 'Pin capacitance', 2: '430', 3: '530', 4: 'nF', 5: ''}, {0: 'Rout', 1: 'Output resistance', 2: '2.5', 3: '2.6', 4: 'kΩ', 5: ''}, {0: 'Vnom', 1: 'Nominal voltage range (BAT+ = 8. . . 32 V, nominal', 2: '1,2', 3: '0.1 ⋅ BAT+', 4: '0.9 ⋅ BAT+', 5: 'V'}, {0: 'load resistance)', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'Vtol-p', 1: 'Proportional error (BAT+ = 8. . . 32 V, nominal load', 2: '1,3', 3: '-2', 4: '+2', 5: '%'}, {0: 'resistance)', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error (BAT+ = 8. . . 32 V, nominal load', 2: '1,3', 3: '-100', 4: '+100', 5: 'mV'}, {0: 'resistance)', 1: '', 2: '', 3: '', 4: '', 5: ''}][/table_158]

Note 1 The PVG valves use a voltage divider with 2 ⋅ 24 k Ω **between ground and**
BAT+. This is equivalent to 1 ⋅ 12 k Ω **against 50 % of BAT+.**
Note 2 The standard PVG valves are controllable between 25 % and 75 **% of BAT+.**
This specification parameter is to show the HW-related control limits only.

Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.14.6 Vout Outputs

In VOUT **mode, the outputs generate a DC voltage that can be used to connect to any high-impedance**
analog input. The load resistance of the receiving device defines the maximum possible output voltage.

![172_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as resistors, capacitors, and transistors. There are multiple wires connecting these components, forming a complex network within the circuit.  In addition to the main components, there is also a CPU (Central Processing Unit) present in the image, which suggests that this electronic circuit may be part of a larger system or device. The diagram provides an overview of the connections and relationships between these components, allowing for better understanding of how they work together within the circuit.)

In PVG mode, PVG valves have a well-defined input resistance, **and the output signal settings can** be calculated in advance by considering the characteristics of the output stage. In voltage mode, however, a PID controller must be applied to generate the desired output voltage. This results in a certain settling time, which depends on the parameter set of **the PID controllers.**
The VOUT **mode output can be used to control PVG valves of the type PVEU or other generic resistive**
loads.

For diagnostic reasons, the output signal is looped back to the CPU in output mode, and the measured value is compared to the set value. If the difference between these two values is above a fixed limit, an overload is detected and the output is disabled. The protection mechanism tries to reenable the output 10 times per drive cycle. It is not allowed to use two outputs in parallel to increase driving strength.

## 4.14.6.1 Characteristics Of Vout

[table_159][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit', 5: ''}, {0: 'Cout', 1: 'Pin capacitance', 2: '430', 3: '530', 4: 'nF', 5: ''}, {0: 'Rout', 1: 'Output resistance', 2: '2.5', 3: '2.6', 4: 'kΩ', 5: ''}, {0: 'I load', 1: 'Nominal load current', 2: '0', 3: '5', 4: 'mA', 5: ''}, {0: '1', 1: '0.0 ⋅ BAT+', 2: '0.99 ⋅ BAT+', 3: '', 4: '', 5: ''}, {0: 'Vnom', 1: 'Nominal', 2: 'voltage', 3: 'range', 4: '(open', 5: 'load),'}, {0: 'BAT+ = 8. . . 32 V', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'Vtol-p', 1: 'Proportional error (BAT+ = 8. . . 32 V)', 2: '3', 3: '-2', 4: '+2', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error (BAT+ = 8. . . 32 V)', 2: '2,3', 3: '-1.5', 4: '+1.5', 5: '%'}, {0: 'Vtol-0', 1: 'Zero error (BAT+ = 8. . . 32 V)', 2: '3', 3: '-300', 4: '+300', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero error (BAT+ = 8. . . 32 V)', 2: '2,3', 3: '-200', 4: '+200', 5: 'mV'}][/table_159]

Note **1 In the VOUT setting, the open load voltage is only open loop controlled. The**
load creates a voltage divider with the well-defined output resistance (Rout) of the VOUT stage. This effect must be considered in the application SW. To get a desired (loaded) output voltage the proper open load voltage must be calculated and set to a (higher) open load voltage level. For **example, with a**
load RL = 10 kΩ **to ground the open load voltage (Vset) must be set to 12.55 V**
(Vset = *Vout* RL+2.55 *kohm* RL **) to get an output voltage of 10 V.**
Note 2 TECU **= -40. . . +85** °C
Note 3 The total error is the sum of zero error and the proportional error.

## 4.14.7 Analog And Digital Inputs

This input type is suitable for low impedance switches and sensors only. For standard analog senors please use Analog Input 2 Modes (Section 4.10 on page **124) and Analog Input 3 Modes (Section** 4.9 on page **116).** External switches which are directly switching to battery voltage must not be used with alternative inputs. See Section 6.6 on page 218 **for more information.**

## 4.14.7.1 Characteristics Of Analog Voltage Input

[table_160][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit', 5: ''}, {0: 'Cin', 1: 'Pin input capacitance', 2: '384', 3: '576', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '8', 3: '12', 4: 'ms', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '2.5', 3: '2.6', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4.7', 3: '5.1', 4: 'V', 5: ''}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3', 3: '-55', 4: '+55', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '1,3', 3: '-50', 4: '+50', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3', 3: '-4', 4: '+4', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '1,3', 3: '-3', 4: '+3', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '8', 4: 'mV', 5: ''}, {0: 'Vin', 1: 'Input voltage measurement range', 2: '2', 3: '0', 4: '32', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '2', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_160]

Note 1 TECU **= -40. . . +85** °C
Note **2 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**

## 4.14.7.2 Characteristics Of Digital Input Tecu **= -40. . . +125** °C

[table_161][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '384', 3: '576', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '8', 3: '12', 4: 'ms', 5: ''}, {0: 'Rpud', 1: 'Pull-up/pull-down resistor', 2: '2.5', 3: '2.6', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage (open load)', 2: '4.7', 3: '5.1', 4: 'V', 5: ''}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: 'V', 4: '', 5: ''}][/table_161]

[table_162][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vih', 1: 'Input voltage for high level', 2: '1', 3: '32', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage range', 2: '1', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}, {0: 'Note', 1: 'Configuration by application software', 2: '', 3: '', 4: '', 5: ''}][/table_162]

Note **Configuration by application software**
Note **1 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

4.15 Low-Side Digital Outputs 4.15.1 Pinout

![176_image_1_4756.png](1001 is written on a white background with a green outline. The number appears to be part of an electronic device or component.)

![176_image_0_4756.png](The image is a white drawing of an empty room with a long table inside. There are several chairs placed around the table, some closer to the front while others are situated further back. The arrangement of these chairs creates a sense of organization and order within the space.) 

[table_163][{0: 'Pin No.', 1: 'Function', 2: 'SW-define'}, {0: 'P251', 1: 'Low-Side Digital Output', 2: 'IO_DO_08'}, {0: 'P238', 1: 'Low-Side Digital Output', 2: 'IO_DO_09'}, {0: 'P252', 1: 'Low-Side Digital Output', 2: 'IO_DO_10'}, {0: 'P239', 1: 'Low-Side Digital Output', 2: 'IO_DO_11'}, {0: 'P253', 1: 'Low-Side Digital Output', 2: 'IO_DO_12'}, {0: 'P240', 1: 'Low-Side Digital Output', 2: 'IO_DO_13'}, {0: 'P254', 1: 'Low-Side Digital Output', 2: 'IO_DO_14'}, {0: 'P241', 1: 'Low-Side Digital Output', 2: 'IO_DO_15'}][/table_163]

Eight low-side switches with freewheeling diodes to a clamping structure for inductive and resistive

![177_image_0_4756.png](The image displays a diagram of an electronic circuit with various components such as capacitors, resistors, and transistors. There are multiple capacitors placed throughout the circuit, some closer to the top left corner while others are positioned towards the right side of the image. A few resistors can be seen in different parts of the circuit, including one near the center-left area and another on the bottom right side.  The transistors are distributed across the circuit as well, with some located closer to the top left corner and others positioned towards the middle-right section of the image. The diagram provides a detailed view of the electronic components within this particular circuit.) loads.

The current through the low-side switch is monitored and triggers the opening in case of overcurrent. Short-circuit and overload protection is included in low-level driver software. Before a tripped channel can be re-enabled, the overload situation has to be removed.

TTControl GmbH recommends to use the maximum possible wire size (FLRY type) in case of maximum load current to reduce voltage drop and prevent overheating of the crimp contact.

See also section *DIO - Driver for digital inputs and outputs* **of the API documentation [30].**

## 4.15.2.1 Power Stage Pairing

If higher load current is needed, the output stages can be used in parallel. Due to thermal limits, the resulting total load current of this output pair has to be de-rated by a factor of 0.85 (e.g. combining two 3 A outputs would result in a total **load current of 3 A x 2 x 0.85 = 5.1 A).** The application software has to make sure that both outputs are switched on at the same point in time, otherwise the over-current protection may trip. For balanced current distribution through each of the pin pairs, the cable routing shall be symmetrical if pin-pairs or multiple pins shall be wired parallel to support higher load currents.

## 4.15.3 Diagnostic Functions

Load monitoring is the detection of overloads, external short circuits of the load output to positive or negative supply (BAT+/BAT-) or any other power output and the detection of load loss.

![178_image_0_4756.png](The image displays a diagram with several buttons labeled "on" and "off." There are also multiple green lights on the diagram, indicating that some of these buttons might be turned on. The diagram seems to represent an electrical system or a control panel for a device.)

![178_image_1_4756.png](100% Unread)

× **= not detected**

## 4.15.4 Maximum Ratings

[table_164][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input/output voltage under overload conditions', 2: '-0.5', 3: 'BAT+ Power +0.5', 4: 'V', 5: ''}, {0: 'Vout', 1: 'Output voltage under overload conditions', 2: '1', 3: '-1', 4: '33', 5: 'V'}, {0: 'Wmax', 1: 'Inductive clamping Energy ( LI2 )', 2: '2', 3: '450', 4: 'mJ', 5: ''}, {0: '2', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'fmax', 1: 'Maximum combined switching rate', 2: '3', 3: '11', 4: 'Hz', 5: ''}, {0: 'Pmax', 1: 'Maximum combined clamping power', 2: '3', 3: '5', 4: 'W', 5: ''}][/table_164]

Note **1 Inductive load transients will be clamped internally to <33 V referred to GND.** Note **2 With 3 A load current in a system with 32 V supply voltage, this corresponds to**
a maximum inductivity of 100 mH. For higher inductivities see Section 6.3 on page **195.**
Note **3 This is the sum of all inductive switch-off events on all eight low side outputs.**
With lower energy, faster switching is possible as the limit is the average power.

## 4.15.5 Characteristics Of Low-Side Digital Output Tecu **= -40. . . +125** °C

[table_165][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '8', 3: '12', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage', 2: '4', 3: '4.5', 4: 'V', 5: ''}, {0: 'Ron', 1: 'On-resistance', 2: '50', 3: 'mΩ', 4: '', 5: ''}, {0: 'I load', 1: 'Nominal load current', 2: '0', 3: '3', 4: 'A', 5: ''}, {0: 'Imax', 1: 'Maximum load current', 2: '1', 3: '4', 4: 'A', 5: ''}, {0: 'Ipeak', 1: 'Peak load current', 2: '2', 3: '0', 4: '6', 5: 'A'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '3', 3: '-400', 4: '+400', 5: 'mA'}, {0: 'I tol-0', 1: 'Zero reading error', 2: '1,3', 3: '-300', 4: '+300', 5: 'mA'}, {0: 'I tol-p', 1: 'Proportional error', 2: '3', 3: '-14', 4: '+14', 5: '%'}, {0: 'I tol-p', 1: 'Proportional error', 2: '1,3', 3: '-10', 4: '+10', 5: '%'}][/table_165]

Note 1 TECU **= -40. . . +85** °C.

Note **2 Peak current for not more than 100 ms. Exceeding this value will trigger overload**
protection and switch off the power stage. Steady state operation goes only up to 3 A/4 A depending on temperature Note 3 The total measurement error is the sum of zero reading error and the proportional error.

## 4.15.6 Analog And Digital Inputs 4.15.6.1 Characteristics Of Analog Voltage Input Tecu **= -40. . . +125** °C 4.15.6.2 Characteristics Of Digital Input Tecu **= -40. . . +125** °C

[table_166][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit', 5: ''}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '1.5', 3: '2.5', 4: 'ms', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '8', 3: '12', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage', 2: '4', 3: '4.5', 4: 'V', 5: ''}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '3', 3: '-55', 4: '+55', 5: 'mV'}, {0: 'Vtol-0', 1: 'Zero reading error', 2: '1,3', 3: '-50', 4: '+50', 5: 'mV'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '3', 3: '-4', 4: '+4', 5: '%'}, {0: 'Vtol-p', 1: 'Proportional error', 2: '1,3', 3: '-3', 4: '+3', 5: '%'}, {0: 'LSB', 1: 'Nominal value of 1 LSB', 2: '-', 3: '13.4', 4: 'mV', 5: ''}, {0: 'Vin', 1: 'Input voltage measurement range', 2: '2', 3: '0', 4: '32', 5: 'V'}, {0: 'Vin', 1: 'Input voltage range', 2: '2', 3: '-0.5', 4: 'BAT+ Power +0.5', 5: 'V'}][/table_166]

[table_167][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'τin', 1: 'Input low pass filter', 2: '1.5', 3: '2.5', 4: 'ms', 5: ''}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '8', 3: '12', 4: 'kΩ', 5: ''}, {0: 'Vpu', 1: 'Pull-up voltage', 2: '4', 3: '4.5', 4: 'V', 5: ''}, {0: 'Resolution', 1: '12', 2: '12', 3: 'bit', 4: '', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '0', 3: 'V', 4: '', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '32', 3: 'V', 4: '', 5: ''}][/table_167]

Note 1 TECU **= -40. . . +85** °C
Note **2 The input voltage may go up to 32 V but must never exceed battery supply**
voltage.

Note 3 The total measurement error is the sum of zero reading error **and the proportional error.**
Note Configuration by application software

![181_image_0_4756.png](The image features a white box with many rows of blue buttons arranged neatly inside. There are at least twelve rows of buttons visible, each row containing multiple buttons. A green light is also present within the box, located near the center of the scene. This arrangement suggests that the box might be used for organizing or displaying electronic components or other small items in a visually appealing manner.) 

Pin No. Function **SW-define**
P208 LIN IO_LIN

LIN is configured in master mode. LIN is a bidirectional half duplex serial bus for up to 10 nodes. Note: **A common ground (chassis) or a proper ground connection is necessary for LIN operation. If** you connect to an external device (e.g., to a PC with a LIN interface), make sure not to violate the maximum voltage ratings when connecting to the LIN connection.

See also section *LIN - Local Interconnect Network driver* **of the API documentation [30].**

![182_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled. There are two main sections within the diagram - one on the left side and another on the right side. The left section features a large blue box with the word "LIN" written in white, while the right section has a green box with the word "CPU" written in white.  In addition to these main components, there are several smaller boxes scattered throughout the diagram, likely representing other electronic parts or subsystems within the device.)

## 4.16.3 Maximum Ratings

[table_168][{0: 'TECU = -40. . . +125 °C Symbol Parameter', 1: 'Note', 2: 'Min.', 3: 'Max.', 4: 'Unit'}, {0: 'VLIN', 1: 'Bus voltage under overload conditions', 2: '-1', 3: '+33', 4: 'V'}][/table_168]

## 4.16.4 Characteristics

TECU **= -40. . . +125** °C

[table_169][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cout', 1: 'Pin output capacitance', 2: '0.8', 3: '1.2', 4: 'nF', 5: ''}, {0: 'VBUSdom Receiver dominant state', 1: '0.4 ⋅ VBat_LIN', 2: 'V', 3: '', 4: '', 5: ''}, {0: 'VBUSrec', 1: 'Receiver recessive state', 2: '0.6 ⋅ VBat_LIN', 3: '–', 4: 'V', 5: ''}, {0: 'VOL', 1: 'Output low voltage', 2: '2.0', 3: 'V', 4: '', 5: ''}, {0: 'VBat_LIN', 1: 'LIN supply voltage', 2: '1', 3: '13', 4: '15', 5: 'V'}, {0: 'Rpu', 1: 'Pull-up resistor', 2: '0.95', 3: '1.05', 4: 'kΩ', 5: ''}, {0: 'STr', 1: 'Baud rate', 2: '20', 3: 'kBd', 4: '', 5: ''}][/table_169]

Note 1 For battery voltages higher than V_Bat_LIN +0.5 V
4.17 RS232 4.17.1 Pinout

![184_image_0_4756.png](The image features a white computer keyboard with multiple rows of keys. There are two green lights on the keyboard, one located near the center and another towards the right side. The keyboard is designed to hold many different types of cables, making it versatile for various electronic devices.) 

[table_170][{0: 'Pin No.', 1: 'Function', 2: 'SW-define'}, {0: 'P242', 1: 'RS232 Serial Interface Output(TX)', 2: 'IO_UART'}, {0: 'P255', 1: 'RS232 Serial Interface Output(RX)', 2: ''}][/table_170]

RS232 is used as a full duplex serial interface. Note: **Handshake lines (RTS, CTS) are not available. A common ground (chassis) or a proper** ground connection is necessary for RS232 operation. If you connect to an external device (e.g., to a PC with an RS232 interface), make sure not to violate the maximum ratings.

See also section *UART - Universal Asynchronous Receiver Transmitter driver* **of the API documentation [30].**

![185_image_0_4756.png](The image displays a diagram of a computer system with various components labeled. There are two main sections within the diagram - one on the left side and another on the right side.  The left section features several labels, including "CPU," "Maxx238," "UART," "MAC," "PCI," and "ECC." The right section contains a larger number of labels, such as "CPU," "Maxx238," "UART," "MAC," "PCI," "ECC," "I/O," "Memory," "Bridge," "Cache," "Microcode," "Firmware," and "ROM."  The diagram provides a detailed view of the computer system's architecture, highlighting its components and their relationships.)

## 4.17.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_171][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'VRS232x', 1: 'Bus voltage under overload conditions (e.g. short circuit to supply voltages)', 2: '', 3: '', 4: '', 5: ''}][/table_171]

## 4.17.4 Characteristics

TECU **= -40. . . +125** °C

[table_172][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cout', 1: 'Pin output capacitance', 2: '100', 3: '150', 4: 'pF', 5: ''}, {0: 'Vil', 1: 'Input voltage for low level', 2: '-22', 3: '0.8', 4: 'V', 5: ''}, {0: 'Vih', 1: 'Input voltage for high level', 2: '2.4', 3: '22', 4: 'V', 5: ''}, {0: 'Vol', 1: 'Output voltage for low level', 2: '-5', 3: 'V', 4: '', 5: ''}, {0: 'Voh', 1: 'Output voltage for high level', 2: '+5', 3: 'V', 4: '', 5: ''}, {0: 'STr', 1: 'Baud rate', 2: '115', 3: 'kBd', 4: '', 5: ''}][/table_172]

4.18 CAN

![186_image_1_4756.png](100% of the image is a grayscale picture with no visible colors. The image appears to be an artistic representation of a person's head, possibly depicting a thoughtful expression.)

![186_image_0_4756.png](The image is a white drawing of an electronic device with many buttons arranged on its surface. There are at least twelve buttons visible, each varying in size and position. Some buttons are located towards the top left corner of the device, while others can be found closer to the center or bottom right side. The arrangement of these buttons suggests that they might be part of a control panel for an electronic device such as a computer or a gaming console.) 

[table_173][{0: 'Pin No.', 1: 'Function', 2: 'SW-define'}, {0: 'P209', 1: 'CAN Interface 0 - Low Line', 2: 'IO_CAN_CHANNEL_0'}, {0: 'P222', 1: 'CAN Interface 0 - High Line', 2: ''}, {0: 'P210', 1: 'CAN Interface 1 - Low Line', 2: 'IO_CAN_CHANNEL_1'}, {0: 'P223', 1: 'CAN Interface 1 - High Line', 2: ''}, {0: 'P211', 1: 'CAN Interface 2 - Low Line', 2: 'IO_CAN_CHANNEL_2'}, {0: 'P224', 1: 'CAN Interface 2 - High Line', 2: ''}, {0: 'P212', 1: 'CAN Interface 3 - Low Line', 2: 'IO_CAN_CHANNEL_3'}, {0: 'P225', 1: 'CAN Interface 3 - High Line', 2: ''}, {0: 'P213', 1: 'CAN Interface 4 - Low Line', 2: 'IO_CAN_CHANNEL_4'}, {0: 'P226', 1: 'CAN Interface 4 - High Line', 2: ''}, {0: 'P214', 1: 'CAN Interface 5 - Low Line', 2: 'IO_CAN_CHANNEL_5'}, {0: 'P227', 1: 'CAN Interface 5 - High Line', 2: ''}, {0: 'P215', 1: 'CAN Interface 6 - Low Line', 2: 'IO_CAN_CHANNEL_6'}, {0: 'P228', 1: 'CAN Interface 6 - High Line', 2: ''}][/table_173]

CAN is a bidirectional twisted pair bus. Needs termination with 120 Ω **in 2-control units, whereas**
the others remain unterminated.

Termination must be fit at the ends of the bus line to prevent wave reflection. Termination is necessary to enter the recessive state. See Figure 58 **on the facing page for details.**
Note: **A common ground (chassis) or a proper ground connection is necessary for CAN operation.**
In case of connecting with an external device (e.g. PC with CAN-interface for downloading software) please make sure that the maximum voltage ratings are not violated when connecting to or disconnecting from the CAN bus. The CAN interface is ISO 11898-2/-5 compliant except for the **input resistance. This input resistance** is lower due to an RF termination, which drastically improves EMC immunity and is used, required and proven for it's performance in the automotive industry for many years. The differential internal resistance is given in table **4.18.4.**
See also section *CAN - Controller Area Network driver* **of the API documentation [30].**

## 4.18.2.1 Can1 On Hy-Ttc 590E, Hy-Ttc 590, And Hy-Ttc 508

Due to the requirements of the ISOBUS standard [21], CAN1 has a lower EMC protection than the other CAN interfaces. The high impedance RF termination is removed. To achieve equivalent RF immunity it is recommended to use CAN1 with a termination. That is, CAN1 should be connected at the terminated end of the CAN bus line. It is recommended to use either an internal CAN termination or an equivalent circuit according to Figure 60 on page 180.

![188_image_0_4756.png](The image displays a diagram with two sections labeled "EUC" on each side. In one section, there is a blue box with a green arrow pointing towards it, while in the other section, there is a red box with a green arrow pointing to it. Both boxes have a small white square inside them.  In addition to these boxes, there are several arrows and labels throughout the image, indicating connections between different elements. The presence of multiple arrows suggests that this diagram might be related to a network or system design.)

## 4.18.3 Maximum Ratings Tecu **= -40. . . +125** °C

[table_174][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'VCAN_H ,', 1: 'Bus voltage under overload conditions', 2: '', 3: '', 4: '', 5: ''}, {0: 'VCAN_L', 1: '(e.g. short circuit to supply voltages)', 2: '', 3: '', 4: '', 5: ''}][/table_174]

## 4.18.4 Characteristics Tecu **= -40. . . +125** °C

[table_175][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin output capacitance', 2: '100', 3: 'pF', 4: '', 5: ''}, {0: 'Vin-CMM', 1: 'Input common mode range', 2: '1', 3: '-12', 4: '12', 5: 'V'}, {0: 'Vin-dif', 1: 'Differential input threshold voltage', 2: '0.5', 3: '0.9', 4: 'V', 5: ''}, {0: '(VCAN_H - VCAN_L )', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'Vout-dif', 1: 'Differential output voltage dominant state', 2: '1.5', 3: '3', 4: 'V', 5: ''}, {0: '(VCAN_H - VCAN_L )', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'Vout-dif', 1: 'Differential output voltage recessive state', 2: '-0.1', 3: '+0.1', 4: 'V', 5: ''}, {0: '(VCAN_H - VCAN_L )', 1: '', 2: '', 3: '', 4: '', 5: ''}, {0: 'VCAN_L ,', 1: 'Common mode idle voltage (recessive state)', 2: '2', 3: '3', 4: 'V', 5: ''}, {0: 'VCAN_H ICAN_CNL Output current limit', 1: '-40', 2: '-200', 3: 'mA', 4: '', 5: ''}, {0: 'ICAN_CNH Output current limit', 1: '40', 2: '200', 3: 'mA', 4: '', 5: ''}, {0: 'STr', 1: 'Bit rate', 2: '2,3,4', 3: '20', 4: '1000', 5: 'kbit/s'}, {0: 'Rdiff', 1: 'Differential internal resistance', 2: '5', 3: '27', 4: '29', 5: 'kΩ'}, {0: 'Rdiff', 1: 'Differential internal resistance', 2: '3.7', 3: '3.9', 4: 'kΩ', 5: ''}][/table_175]

Note **1 Due to high current in the cable harness, the individual ground potential of the**
control units can differ up to several V. This difference will also appear as common mode voltage between a transmitting and a receiving control unit and not influence the differential bus signal, as long as it is within **the common mode** limits.

Note **2 Pay attention to the limitations of CAN. The arbitration process allows 1 Mbit/s**
operation only in small networks and reduced wire length. By **way of example,** a so-called "private CAN", which is a short point-to-point connection (less than 10 m) between two nodes only, can be operated at 1 MBit/s.

Note **3 For typical network sizes and topologies (networks with stub wires) and more**
than two nodes, the practical limit is 500 kbit/s.

Note 4 Any value that conforms to CAN protocol standard definition **is valid.** Note 5 ISOBUS CAN variant.

## 4.19 Can Termination

![190_image_0_4756.png](The image is a white drawing of an electronic device with many wires and connections. There are several rows of numbers displayed on the device, indicating that it might be used for data storage or processing. The arrangement of these numbers suggests that this could be a computer or a similar electronic device.)

[table_176][{0: 'Pin No.', 1: 'Function', 2: 'Applicable to variants'}, {0: 'P235', 1: '120 Ω CAN Termination 0 Low', 2: 'all'}, {0: 'P248', 1: '120 Ω CAN Termination 0 High', 2: 'all'}, {0: 'P236', 1: '120 Ω CAN Termination 1 Low', 2: 'all'}, {0: 'P249', 1: '120 Ω CAN Termination 1 High', 2: 'all'}, {0: 'P237', 1: '120 Ω CAN Termination 2 Low', 2: 'all'}, {0: 'P250', 1: '120 Ω CAN Termination 2 High', 2: 'all'}, {0: 'P216', 1: '120 Ω CAN Termination 3 Low', 2: 'HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510'}, {0: 'P229', 1: '120 Ω CAN Termination 3 High', 2: 'HY-TTC 580, HY-TTC 540, HY-TTC 520, HY-TTC 510'}, {0: 'P218', 1: '120 Ω CAN Termination 3 High', 2: 'HY-TTC 590E, HY-TTC 590, HY-TTC 508'}, {0: 'P219', 1: '120 Ω CAN Termination 3 Low', 2: 'HY-TTC 590E, HY-TTC 590, HY-TTC 508'}][/table_176]

For easy termination of the CAN bus, there are four built in 120 Ω **termination resistors on the**
HY-TTC 500 which are accessible via 2 connector pins each. They can be used for any CAN port.

The 120 Ω termination of a control unit is realized with two serial 60 Ω **resistors (split termination).** To get an impedance of 60 Ω on the whole bus, a termination resistor of 120 Ω **is required in two**
control units.

![191_image_0_4756.png](The image displays a diagram of an electrical circuit with various components labeled. There are two main labels on the diagram - "EUC" and "Can Termination L." The circuit includes multiple wires and switches, as well as a power source.  The diagram is organized in such a way that it provides information about the different parts of the electrical system. This could be helpful for understanding how the components work together to create an efficient and functional electrical setup.) 

4.20 Ethernet

![192_image_0_4756.png](The image is a white drawing of an electronic device with many ports labeled as "PBX." These ports are arranged in rows, indicating that this could be a telecommunications system or a network switch. There are several labels on each port, possibly indicating the type of connection or function it serves within the device. The arrangement and organization of these ports suggest that they play an essential role in facilitating communication and data transfer between different parts of the electronic device.) 

[table_177][{0: 'Pin No.', 1: 'Function', 2: 'SW-define', 3: 'Applicable to variants'}, {0: 'P218', 1: 'Ethernet Differential Transmit - TD+', 2: 'IO_DOWNLOAD, IO_UDP', 3: 'HY-TTC 580'}, {0: 'P219', 1: 'Ethernet Differential Transmit - TD-', 2: 'HY-TTC 580', 3: ''}, {0: 'P231', 1: 'Ethernet Differential Receive - RD-', 2: 'HY-TTC 580', 3: ''}, {0: 'P232', 1: 'Ethernet Differential Receive - RD+', 2: 'HY-TTC 580', 3: ''}][/table_177]

The Ethernet interface supports application download and the UDP communication protocol. The 10/100 Mbit/s full duplex Ethernet port is designed for IEEE 802.3 compliance. However, there is no standard Ethernet connector provided, the Ethernet signals are located on the main connector. Make sure to use appropriate cabling according to the Ethernet standard. Use at least an Ethernet CAT3 cable for a transmission speed of 10 Mbit/s and an Ethernet CAT5 cable for a transmission speed of 100 Mbit/s. In a noisy environment, it is recommended to use shielded cables. See also sections *IO_UDP* and *IO_DOWNLOAD* **in the API documentation [30].**

![193_image_0_4756.png](The image displays a diagram of a computer system with various components labeled. There are three main sections within the diagram: the CPU (central processing unit), memory, and magnetic storage.  The CPU is located at the center of the diagram, surrounded by memory on both sides. Memory consists of two parts: RAM (random access memory) and ROM (read-only memory). The RAM is situated to the left of the CPU, while the ROM is positioned to its right.  Magnetic storage is represented by a hard disk drive (HDD), which is located at the bottom part of the diagram. This section also includes a floppy disk and a CD-ROM. The floppy disk is situated above the HDD, while the CD-ROM is positioned to its right.)

## 4.20.3 Maximum Ratings

TECU = −40. . . +125 °C

[table_178][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin-CMM', 1: 'Input common mode voltage range 50/60 HZ AC,', 2: '0', 3: '750', 4: 'VRMS', 5: ''}, {0: '60 s test duration', 1: '', 2: '', 3: '', 4: '', 5: ''}][/table_178]

## 4.21 Broadr-Reach®

![194_image_0_4756.png](The image is a white drawing of an electronic device with many wires and connections. There are several rows of numbers on the device, indicating that it may be used for data storage or processing. The device appears to have multiple ports and connections, suggesting that it could be a computer or other electronic equipment.)

[table_179][{0: 'Pin No.', 1: 'Function', 2: 'SW-define', 3: 'Applicable to variants'}, {0: 'P231', 1: '100BASE-T1 Ethernet TRX\x02', 2: 'IO_DOWNLOAD, IO_UDP', 3: 'HY-TTC 590, HY-TTC 590E, HY-TTC 508'}, {0: 'P232', 1: '100BASE-T1', 2: 'HY-TTC 590, HY-TTC 590E, HY-TTC 508', 3: ''}, {0: 'Ethernet TRX+', 1: '', 2: '', 3: ''}][/table_179]

The standardized BroadR-Reach® **(also known as 100BASE-T1 Ethernet) link is an advancement**
of the IEEE 802.3 100Base-TX Fast Ethernet standard and was standardized by OPEN ALLIANCE. It uses a single unshielded twisted pair cable (UTP) and is therefore low in costs. The 100BASE-T1 Ethernet link is capable of 100 MBit/s full-duplex transmission rate. Typical applications are
- **IP-based camera links** - **driver assistance systems**
- **in-vehicle backbone**
- infotainment

## 4.21.3 Maximum Ratings Tecu = −40. . . +125 °C

[table_180][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'VBRR', 1: 'Bus voltage under overload conditions (i.e., short', 2: '-32', 3: '+32', 4: 'V', 5: ''}, {0: 'circuit to supply voltages)', 1: '', 2: '', 3: '', 4: '', 5: ''}][/table_180]

## 4.21.4 Characteristics Tecu **= -40. . . +125** °C

[table_181][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin-CMM', 1: 'Input common mode range', 2: '-32', 3: '+32', 4: 'V', 5: ''}, {0: 'Vout-dif', 1: 'Differential output voltage', 2: '-1', 3: '+1', 4: 'V', 5: ''}, {0: 'VBRR_P,', 1: 'Common mode idle voltage', 2: '-0.1', 3: '+0.1', 4: 'V', 5: ''}, {0: 'VVBRR_M STr Bit rate', 1: '100', 2: 'Mbit/s', 3: '', 4: '', 5: ''}, {0: 'Rin_AC_dif Input resistance AC', 1: '90', 2: '110', 3: 'Ω', 4: '', 5: ''}, {0: 'Rin_DC_dif Input resistance DC', 1: '1.8', 2: '2.2', 3: 'kΩ', 4: '', 5: ''}][/table_181]

4.22 Real-Time Clock (RTC)

![196_image_0_4756.png](The image is a white drawing of an airplane with several rows of seats labeled as "PS" and "PB." There are multiple chairs arranged throughout the plane, some closer to the front and others nearer to the back. A green box can also be seen in the middle of the seating area, possibly indicating a specific section or feature within the airplane. The overall layout suggests that this is an illustration of an airplane's interior with designated seats for passengers.) 

Figure 64: RTC pinout
Pin No. Function **SW-define**
P233 Real-Time Clock Backup Battery IO_RTC

The HY-TTC 500 includes a real-time clock with a backup power **system for exact system time- and** date-keeping after every power cycle. The real-time clock module is either supplied by the internal 5 V supply, vehicle battery, or by the external RTC battery pin. When HY-TTC 500 is connected to the vehicle battery via the BAT+ CPU pin, the RTC is supplied by the vehicle battery independent of whether the device is operational or in power-off mode. When both the RTC backup battery and BAT+ CPU are disconnected, the real-time clock is supplied by an internal capacitor. The capacitor provides approximately 10 minutes of backup time when fully charged. Charging an empty capacitor takes at least 5 minutes. See also section *RTC - Real Time Clock driver* **of the API documentation [30].**

![197_image_0_4756.png](The image displays a diagram of an electronic device with various components labeled throughout the drawing. There are multiple wires connecting different parts of the circuit, including a CPU, ECCU, and external battery. The diagram also features a power supply, indicating that this is likely a complex system or device.  The labels on the diagram provide information about each component's function within the electronic device. Overall, it appears to be an intricate representation of a computer or other electronic equipment with multiple interconnected parts.)

## 4.22.3 Maximum Ratings

TECU **= -40. . . +125** °C

[table_182][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Vin', 1: 'Input voltage', 2: '-1', 3: '+33', 4: 'V', 5: ''}][/table_182]

## 4.22.4 Characteristics Tecu **= -40. . . +125** °C

[table_183][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Cin', 1: 'Pin input capacitance', 2: '8', 3: '12', 4: 'nF', 5: ''}, {0: 'I in', 1: 'Steady state input current (after 1 min, 3.6 V)', 2: '10', 3: 'µA', 4: '', 5: ''}, {0: 'I in', 1: 'Steady state input current for high voltage opera\x02tion (after 1 min, 16 V)', 2: '260', 3: 'µA', 4: '', 5: ''}, {0: 'I in', 1: 'Steady state input current for high voltage opera\x02tion (after 1 min, 32 V)', 2: '600', 3: 'µA', 4: '', 5: ''}, {0: 'Vin', 1: 'Input voltage', 2: '2.5', 3: '32', 4: 'V', 5: ''}, {0: 'Vin', 1: 'Input voltage', 2: '1', 3: '1.8', 4: '32', 5: 'V'}, {0: '∆ t/day', 1: 'Time variation per day at +25 °C', 2: '± 1.5', 3: 's/day', 4: '', 5: ''}, {0: 'RTCres', 1: 'Real-time clock resolution', 2: '1', 3: 's', 4: '', 5: ''}][/table_183]

Note 1 TECU = -40. . . +85 °C

## 5 Internal Structure 5.1 Safety Concept

If HY-TTC 500 is used in safety-critical applications, you must follow the requirements specified in the Safety Manual [29].

## 5.1.1 Overview Safety Concept

The following picture descibes all possible (application-controlled) enable/disable paths for the HYTTC 500 powerstages.

![200_image_0_4756.png](The image displays a diagram with various components labeled throughout the entirety of the picture. There are multiple labels on different parts of the diagram, indicating that this is likely an illustration of a computer system or network. Some of these labels include "CPU," "memory," and "hard disk."  The diagram also features several numbers scattered across it, possibly representing data points or measurements related to the components being illustrated. The overall layout of the image suggests that it could be used for educational purposes or as a visual aid in understanding computer systems and their various parts.)

## 5.2 Thermal Management 5.2.1 Board Temperature Sensor

5.2.1.1 Pinout

![201_image_0_4756.png](The image displays a computer screen with various information displayed on it. There is a temperature chart that shows different temperatures at different times of the day. A table can also be seen on the screen, which might provide additional data or context to the temperature chart.  The screen has a blue background and features text in white, making it easy to read the content. The information displayed on the screen is likely related to weather conditions or environmental monitoring.)

![201_image_1_4756.png](The image is a white and gray color scheme with a large amount of white space. There are no visible objects or details within this area.)

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

[table_184][{0: 'Symbol', 1: 'Parameter', 2: 'Note', 3: 'Min.', 4: 'Max.', 5: 'Unit'}, {0: 'Tm', 1: 'Temperature measurement range', 2: '-40', 3: '+125', 4: '°C', 5: ''}, {0: 'Ttol-m', 1: 'Temperature tolerance at 120 °C', 2: '-3', 3: '+3', 4: 'K', 5: ''}, {0: 'Tsafe state Temperature limit', 1: '1', 2: '-40', 3: '+125', 4: '°C', 5: ''}][/table_184]

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

[table_185][{0: 'Variant', 1: 'I in-total [A],', 2: 'I in-total [A],'}, {0: 'TECU = -40. . . +85 °C', 1: 'TECU = -40. . . +125 °C', 2: ''}, {0: 'HY-TTC 580', 1: '60', 2: '45'}, {0: 'HY-TTC 540', 1: '50', 2: '40'}, {0: 'HY-TTC 520', 1: '40', 2: '30'}, {0: 'HY-TTC 510', 1: '40', 2: '30'}, {0: 'HY-TTC 590E', 1: '60', 2: '45'}, {0: 'HY-TTC 590', 1: '60', 2: '45'}, {0: 'HY-TTC 508', 1: '40', 2: '30'}][/table_185]

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

[table_186][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '0 to 2 A', 2: ''}, {0: 'DC-resistance', 1: '>=7.0 Ω', 2: '>=14.0 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Active motor braking', 1: 'yes', 2: 'yes'}, {0: 'Reverse without brake', 1: 'yes', 2: 'yes'}, {0: 'PWM operation', 1: 'yes', 2: 'yes'}, {0: 'Suitable high side power stages', 1: 'PWM power stages, digital HS power stages', 2: ''}][/table_186]

1 For other max. battery voltage please recalculate winding resistance (R = U / I).

6.5.4.1.2 Small Motors (2 to 4 A) **For this class some restrictions apply.**

[table_187][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '2 to 4 A', 2: ''}, {0: 'DC-resistance', 1: '>=3.5 Ω', 2: '>=7.0 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Active motor braking', 1: 'yes', 2: 'yes'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'PWM power stages, digital HS power stages', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '4 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '3 A (TECU > +85 °C)', 2: ''}][/table_187]

1 **For other max. battery voltage please recalculate winding resistance (R = U / I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.1.3 Medium Power Motors (4 to 14 A) **This class needs paralleled power stages. In the example below each switch utilizes 4 power stages in parallel for each switch. This in theory quadruples**
the power rating. In practice depending on close-to-perfect cabling a de-rating of maximum current (14 A instead of 16 A) is foreseen.

[table_188][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '4 to 14 A', 2: ''}, {0: 'DC-resistance', 1: '>=1.0 Ω', 2: '>=2.0 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Active motor braking', 1: 'yes', 2: 'yes'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'digital HS power stages only', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '12 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '10 A (TECU > +85 °C)', 2: ''}][/table_188]

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

## 6.5.4.2 Fast Accelerating Motors Only

Higher inrush current,is allowed for fast accelerating motors. Most actuator motors fall into this category. Depending on operation mode different limits apply:
6.5.4.2.1 Bidirectional (max. 6 A) **For this class some restrictions apply.**

[table_189][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '<6 A', 2: ''}, {0: 'DC-resistance', 1: '>=2.35 Ω', 2: '>=4.7 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Active motor braking', 1: 'yes', 2: 'yes'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'digital HS power stages only', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '4 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '3 A (TECU > +85 °C)', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<6 A', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<4 / 3 A (depending on ECU temperature)', 2: ''}][/table_189]

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.2.2 Bidirectional (max. 16 A) **For this class each low side switch is built out of 4 switches** working in parallel to increase current handling. The high side switches are still single switches.

[table_190][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '<16 A', 2: ''}, {0: 'DC-resistance', 1: '>=0.88 Ω', 2: '>=1.75 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Active motor braking', 1: 'yes', 2: 'yes'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'digital HS power stages only', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '4 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '3 A (TECU > +85 °C)', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<6 A', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<4 / 3 A (depending on ECU temperature)', 2: ''}][/table_190]

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.2.3 Bidirectional (max. 20 A) **For this class each high and low side switch is built out of 4** switches working in parallel to increase current handling. **This in theory quadruples the power rating.** In practice depending on close-to-perfect cabling a de-rating of maximum current (20 A instead of 24 A) is foreseen.

[table_191][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '<20 A', 2: ''}, {0: 'DC-resistance', 1: '>=0.7 Ω', 2: '>=1.4 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Active motor braking', 1: 'yes', 2: 'yes'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'digital HS power stages only', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '12 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '10 A (TECU > +85 °C)', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<12 / 10 A (depending on ECU temperature)', 2: ''}][/table_191]

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

[table_192][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '<16 A', 2: ''}, {0: 'DC-resistance', 1: '>=0.88 Ω', 2: '>=1.75 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'no', 2: 'no'}, {0: 'Active motor braking', 1: 'no', 2: 'no'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'digital HS power stages only', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '4 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '3 A (TECU > +85 °C)', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<6 A', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<4 / 3 A (depending on ECU temperature)', 2: ''}][/table_192]

6.5.4.2.4 Unidirectional (max. 16 A) 1 **For other max. battery voltage please recalculate winding**
resistance (R = U/I).

2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

6.5.4.2.5 Unidirectional (max. 32 A) **For this class two digital high side power stages are operated in parallel.**

[table_193][{0: '12 V System', 1: '24 V System', 2: ''}, {0: 'Max. battery voltage 1', 1: '14 V', 2: '28 V'}, {0: 'Motor blocked current', 1: '<32 A', 2: ''}, {0: 'DC-resistance', 1: '>=0.4 Ω', 2: '>=0.8 Ω'}, {0: 'Unidirectional drive', 1: 'yes', 2: 'yes'}, {0: 'Bidirectional drive', 1: 'no', 2: 'no'}, {0: 'Active motor braking', 1: 'no', 2: 'no'}, {0: 'Reverse without brake', 1: 'no', 2: 'no'}, {0: 'PWM operation', 1: 'no', 2: 'no'}, {0: 'Suitable high side power stages', 1: 'digital HS power stages only', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '8 A (TECU < +85 °C)', 2: ''}, {0: 'Maximum periodic DC peak current 2', 1: '6 A (TECU > +85 °C)', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<12 A', 2: ''}, {0: 'Inrush current drops after 50ms to', 1: '<8 / 6 A (depending on ECU temperature)', 2: ''}][/table_193]

1 **For other max. battery voltage please recalculate winding resistance (R = U/I).**
2 Some motors draw a significant ripple current. The highest periodic peaks shall be below that limit.

## 6.5.5 Connection 6.5.5.1 Unidirectional Single Power Stage

Figure 67 **on this page shows the battery wiring for maximum total load current. This kind of wiring is** used to increase output current capability. It is strongly recommended to support equal distribution of current between the power supply pins. This implies to use **cables of same diameter and same** wire length in parallel. In this example all power supply pins (BAT+ and GND) are connected to cable of maximum diameter supported by the appropriate connector **pin. The cables in parallel are going**
to a distribution point (for example in the fuse box) and from **there with a bigger diameter all the way** to the battery.

The return pin of the motor is connected not direct to the ECU ground but to somewhere else, perhaps to the chassis. In this case significant voltage drops may occur between ECU and motor ground connection. This can lead to unexpected fluctuations **in motor voltage and motor current.**

![219_image_0_4756.png](6x BAT+ is written on a white background with various electrical components connected to it. The diagram features multiple wires and connections, including a green box that appears to be an electronic component. There are also two smaller boxes located near the top right corner of the image. Overall, the image depicts a complex network of interconnected electrical parts.)

A better solution for achieving less voltage drop in the return path shows the Figure 68 **on the current** page.

![220_image_0_4756.png](8x BAT+ is written on a white background with a green box that says Ecu. The image also features a black and white diagram of an electrical circuit board.)

## 6.5.5.2 Unidirectional Double Power Stage

Higher current can be achieved by paralleling output stages, see Figure 69 **on this page. Please** observe the use of cables of same diameter and same wire length in parallel on the power stages as well.

![221_image_0_4756.png](6x BAT+ is written on a white background with various electrical components connected to it. The diagram features multiple wires and switches, indicating that this is an intricate electrical system. There are two green buttons located near the bottom right corner of the image, which might be part of the control panel for this electrical setup.)

6.5.5.3 Bidirectional H-bridge (Single Power Stages)

![222_image_0_4756.png](16 HS output is shown on a white background with multiple blue boxes. The boxes are arranged in rows of four, each containing a single box. There are sixteen such boxes in total, all labeled with numbers from 0 to 15. This arrangement suggests that the image might be related to an electrical or electronic circuit diagram.)

6.5.5.4  Bidirectional H-bridge (Multiple Low Side Power Stages)

![223_image_0_4756.png](1x HS output is shown on a white background with multiple blue boxes surrounding it. The box contains several smaller boxes that are connected to each other, forming a complex network of connections. This diagram likely represents an electrical or electronic system, possibly related to power distribution or communication.)

![224_image_0_4756.png](4xHS output is displayed on a white background with blue and green symbols. The image features multiple rows of these symbols arranged vertically, creating an organized and visually appealing display.)

## 6.5.5.6 Motor Cluster

This is a usual configuration to control 2 motors, that are never operated at the same time, with 3 half bridges (3 x high side + 3 x low side power stage). Example: Outside mirror control

![225_image_0_4756.png](1xHS output is shown on a white background with multiple boxes labeled M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, and M13. Each box contains a different number of HS outputs, ranging from 1 to 12. The labels are arranged in rows, with each row containing the same number of boxes as the one below it. This diagram illustrates various configurations for the output of multiple HS units.)

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

![230_image_0_4756.png](The image displays a diagram of an electrical circuit with multiple components labeled throughout. There are several batteries placed at different positions within the circuit, as well as various switches and wires connecting them. A green box is also present in the middle of the circuit, which could be a power source or another essential component. The diagram provides a clear representation of the electrical system's structure and functioning.)

![230_image_1_4756.png](The image displays a diagram of an electrical system with various components labeled throughout. There are multiple batteries present, including one on the left side, another near the center, and two more towards the right side of the image. A power source is also visible in the middle-right area of the diagram.  The diagram features a series of connections between these components, with some wires running horizontally across the image and others connecting different parts vertically. The labels on the diagram provide information about each component's function within the electrical system.)

![231_image_0_4756.png](The image displays a diagram of an electrical system with various components labeled throughout. There are multiple switches, batteries, and other electrical elements arranged in a complex network. Some key labels include "bath power," "core," "switch," "voltage," and "power."  The diagram is quite detailed, providing a clear representation of the intricate connections between these components. The presence of multiple switches suggests that this system may be used for controlling or managing various aspects of an electrical setup. Overall, the image offers insight into the inner workings of an electrical system and its individual parts.)

## Switches Connected To Pwm High-Side Output Stage:

Digital switches and analog sensors are supplied via an HY-TTC 500 PWM high-side output pin, the switch/sensor output is monitored by an alternative (PWM high-side) input.

Caution! - The sourcing PWM high-side output stage (IO_PWM_00 - IO_PWM_35) must be out of the same secondary shut-off path (A, B or C) as the alternative input pin. For example IO_PWM_00 (output/source) supplies the digital sensor and the sensor output is monitored by IO_PWM_13 (input), both IO's are out of secondary shut-off path A. See Table 22 on page 138 for secondary shut-off paths and their relation to the alternative inputs.

![231_image_1_4756.png](The image displays a diagram of an electronic circuit with various components such as batteries, wires, and switches. There are multiple batteries placed throughout the circuit, some closer to the top left corner while others are positioned towards the right side. A few wires can be seen connecting different parts of the circuit, including one near the center-left area and another in the middle-right section.  In addition to these components, there is a clock visible on the upper part of the image, possibly indicating the time or providing reference for the electronic circuit's operation.)

![232_image_0_4756.png](The image displays a diagram of an electrical system with various components labeled throughout. There are multiple batteries present, including one on the left side, another near the center, and two more towards the right side of the image. A power source is also visible in the middle-left area of the diagram.  The diagram features a series of connections between different parts of the electrical system, with some components connected to each other through wires. The overall layout suggests that this could be an illustration of a battery charging or discharging process within the electrical system.)

![232_image_1_4756.png](The image displays a diagram of an electrical circuit with various components such as batteries, wires, and switches. There are multiple batteries placed throughout the circuit, some closer to the top left corner while others are positioned more towards the center or bottom right side.  The circuit also features several switches, which can be found in different parts of the diagram. Some switches are located near the top right corner, while others are situated closer to the middle or bottom left area. The wires connecting these components create a complex network that illustrates the intricate workings of an electrical system.)

## Switches Connected To Digital High-Side Output Stage:

Digital switches and analog sensors are supplied via an HY-TTC 500 digital high-side output pin, the switch/sensor output is monitored by an alternative (digital high-side) input. IO_DO_00 - IO_DO_07 and IO_PVG_00 - IO_PVG_07 are not equipped with an secondary shut-off

![233_image_0_4756.png](The image displays a diagram of an electrical circuit with various components such as batteries, capacitors, resistors, and transistors. There are multiple batteries placed throughout the circuit, some closer to the top left corner while others are positioned towards the right side of the image.  A few capacitors can be seen in different parts of the circuit, with one located near the center-left area, another close to the bottom-right corner, and a third one situated at the top-right corner. Resistors are also present within the circuit, with two of them placed towards the right side of the image and another one closer to the middle-left area.  A transistor is visible in the lower part of the diagram, likely serving as an essential component for controlling the flow of electricity through the circuit. The overall layout of the electrical circuit appears complex, with numerous components working together to create a functional system.)

paths. These high-side output stages can by themselves not be used for safety critical applications. If the alternative input function of IO_DO_00 - IO_DO_07 and **IO_PVG_00 - IO_PVG_07 shall be** used, the connected sensor must be supplied by an digital output stage out of these outputs.

6.6.1.1.2  Invalid Wiring Examples    The following wiring examples of external switches or analog sensors connected to battery supply are not allowed and must be avoided for safety critical systems.

Nonconforming wiring can lead to destruction of the HY-TTC 500.

## Stop Switch / Blown Fuse / K15 Wiring

Digital switches and analog sensors are supplied directly from the battery.

If for example the fuse is blown, BAT+Power is disconnected (loose connection) or the stop switch is pressed, digital switches or analog sensors are still supplied. The current flows over the closed switch and the parasitic body diode of the output stage used as input. All the load current of all other outputs now flows via the body diode of this single output stage. This may overload and even destroy this output stage.

![234_image_0_4756.png](The image displays a diagram of an electrical circuit with various components such as batteries, wires, and switches. There are multiple batteries placed throughout the circuit, some closer to the top left corner while others are positioned towards the right side of the image.  The circuit also features several switches, including one near the center-left area, another in the middle-right section, and a third one at the bottom-right corner. Additionally, there is a computer processor located in the upper-middle part of the diagram. The overall layout suggests that this electrical circuit may be used for powering electronic devices or other equipment.)

![234_image_1_4756.png](16 Volt Battery Circuit Diagram  The image displays a diagram of an electrical circuit with a 16-volt battery at its center. The circuit consists of multiple components, including a power source, a core, and several other smaller parts. There are also two wires visible in the image, one on the left side and another on the right side of the battery.  The diagram is labeled with various text descriptions, such as "Battery," "Power Source," "Core," and "Voltage." These labels help to identify the different components within the circuit and their functions in the overall system.)

## 7 Debugging 7.1  Functional Description

After connecting the HY-TTC 500 and the Lauterbach Debugging Device with the TTC JTAG-Adapter Board (for the connector pinning, see Figure 83 on the current page), open the Trace32 Software for ARM CPUs. Double-click the batch file flash.cmm , which is located in the corresponding template directory. When prompted by the dialog whether to flash the application or to load only the symbols for debugging, click Yes to start the flashing procedure.

![235_image_0_4756.png](The image displays a diagram of an electronic circuit board with various components labeled on it. There are multiple wires connecting different parts of the circuit, including a battery, which is located towards the left side of the board. A few other batteries can also be seen in the middle and right sections of the circuit.  In addition to the batteries, there are several resistors placed throughout the circuit, with some closer to the top-left corner and others near the center of the board. The diagram is labeled as a Texas Instruments Programmer, indicating that it may be used for programming electronic devices or circuits.)

[table_194][{0: 'Manufacturer:', 1: 'TE CONNECTIVITY / AMP'}, {0: 'Manufacturer Article Code:', 1: '2-1634689-0'}, {0: 'Farnell Order Number:', 1: '8396027'}][/table_194]

Table 32: Order code of JTAG connector on the TTC JTAG-Adapter Board For debugging details, see [ 31 ].

Software Description

## 8 Api Documentation

Please refer to [30] for the API documentation of the HY-TTC 500 I/O driver.

[table_195][{0: 'Entry', 1: 'Description'}, {0: '2M', 1: '2 Mode'}, {0: '3M', 1: '3 Mode'}, {0: 'A/D', 1: 'Analog and Digital'}, {0: 'ADC', 1: 'Analog-to-Digital Converter'}, {0: 'API', 1: 'Application Programming Interface'}, {0: 'CAN', 1: 'Controller Area Network'}, {0: 'CPU', 1: 'Central Processing Unit'}, {0: 'CTS', 1: 'Clear to Send'}, {0: 'DC', 1: 'Direct Current'}, {0: 'DI', 1: 'Digital Input'}, {0: 'DOUT', 1: 'Digital Output'}, {0: 'DO', 1: 'Digital Output'}, {0: 'ECU', 1: 'Electronic Control Unit'}, {0: 'EEPROM', 1: 'Electrically Erasable Programmable Read-Only Memory'}, {0: 'EMC', 1: 'Electromagnetic Compatibility'}, {0: 'Flash', 1: 'Nonvolatile computer storage'}, {0: 'GND', 1: 'Ground'}, {0: 'HS', 1: 'High Side'}, {0: 'HW', 1: 'Hardware'}, {0: 'I/O', 1: 'Input and Output'}, {0: 'IN', 1: 'Input'}, {0: 'LIN', 1: 'Local Interconnect Network'}, {0: 'LSB', 1: 'Least Significant Bit'}, {0: 'LS', 1: 'Low Side'}][/table_195]

[table_196][{0: 'Entry', 1: 'Description'}, {0: 'MRD', 1: 'Mounting Requirements Document'}, {0: 'Max.', 1: 'Maximal'}, {0: 'Min.', 1: 'Minimal'}, {0: 'OUT', 1: 'Output'}, {0: 'PC', 1: 'Personal Computer'}, {0: 'PD', 1: 'Pull Down'}, {0: 'PID', 1: 'Proportional Integral Differential'}, {0: 'PL', 1: 'Performance Level'}, {0: 'PU', 1: 'Pull Up'}, {0: 'PVG', 1: 'Proportional Valve Group'}, {0: 'PWD', 1: 'Pulse Width Demodulation'}, {0: 'PWM', 1: 'Pulse With Modulation'}, {0: 'RTC', 1: 'Real-Time Clock'}, {0: 'RTS', 1: 'Request to Send'}, {0: 'SIL', 1: 'Safety Integrity Level'}, {0: 'SRC', 1: 'Signal Range Check'}, {0: 'SSUP', 1: 'Sensor Supply'}, {0: 'SW', 1: 'Software'}, {0: 'TBD', 1: 'To Be Defined'}, {0: 'Tambient', 1: 'Ambient Temperature'}, {0: 'Terminal 15', 1: 'Battery+ from ignition switch'}, {0: 'UNECE', 1: 'United Nations Economic Commission for Europe'}, {0: 'Ubat', 1: 'Battery Voltage'}, {0: 'VOUT', 1: 'Voltage Output'}][/table_196]

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

[table_198][{0: '— A —'}, {0: 'Analog input 2 mode 124 analog current input 129 analog voltage input 126 functional description 125 maximum ratings 125 pinout 124 Analog input 3 mode 116 analog current input 120 analog resistance input 121 analog voltage input 117 functional description 116 maximum ratings 117 pinout 116 API Documentation 226 Application notes 192 cable harness 192 ground connection of housing 195 handling of high-load current 193 load distribution 193 total load current 193 i/o alternative functions 218 high-side output stages 218 inductive loads 195 motor control 196 Cabling 216 connection 208 control sequence for bidirectional drive216 direct control options 196 motor classification 200 motor details 197 motor types supported 196 parallel operation of power stages 216 power stages for motor control 215'}][/table_198]

[table_200][{0: '— B —'}, {0: 'BAT+ CPU 98 characteristics 100 functional description 99 low-voltage Operation 101 maximum ratings 100 pinout 98 voltage monitoring 103 BAT+ Power 96 characteristics 97'}][/table_200]

## Index

- D —
Debugging.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .224 functional description .. . . . . . . . . . . . . . . . . . 224

[table_197][{0: 'functional description 96 maximum ratings 97 pinout 96'}, {0: 'BOSCH mating connector 58 positions 46 96 positions 46 crimp contacts 47 tools 47 - C - CAN 175 characteristics 178 functional description 176 maximum ratings 178 pinout 175 CAN termination 179 functional description 180 pinout 179 Communication interfaces 2 Connector 42 Connector pinning HY-TTC 508 90 HY-TTC 510 70 HY-TTC 520 64 HY-TTC 540 57 HY-TTC 580 50 HY-TTC 590 83 HY-TTC 590E 76'}][/table_197]

[table_201][{0: '— F —'}, {0: 'Functional safety 38 Fuse 48'}][/table_201]

[table_199][{0: '— E —'}, {0: 'Ethernet 181 functional description 182 maximum ratings 182 pinout 181'}][/table_199]

[table_202][{0: '— H —'}, {0: 'Hardware description 1 High-side digital outputs 149 analog and digital inputs 153 diagnostic functions 151 functional description 150 mutual exclusive mode 151 power stage pairing 151 high-side digital outputs 152 maximum ratings 151 pinout 149 High-side digital/PVG/VOUT outputs 155 analog voltage inputs 163 digital inputs 163 functional description 156 mutual exclusive mode 156 power stage pairing 156 high-side digital outputs 157 maximum_ratings 156 pinout 155 PVG outputs 159 VOUT outputs 161 High-side PWM outputs 137, 141 diagnostic functions 141 digital and frequency inputs 144 external shut-off groups 147 functional description 138 mutual exclusive mode 140 power stage pairing 140 high-side digital outputs 144 maximum ratings 140 pinout 137 secondary shut-off paths 146 tertiary shut-off path 148 functional description 148 HY-TTC 500 family variant pinning 49 HY-TTC 500 Variants 3'}][/table_202]

[table_205][{0: '— I —'}, {0: 'Inputs 2, 96 Instructions for safe operation 39 Internal structure 188 overview safety concept 188 safety concept 188 thermal management 190 board temperature sensor 190 Introduction 2'}][/table_205]

- M —
Mating connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 Motor control high side power stages for PWM operation 215 motor control high side power stages for static operation 215 Mounting requirements.. . . . . . . . . . . . . . . . . . . . . . .41

[table_203][{0: '— K —'}, {0: 'KOSTAL mating connector 58 positions 44 96 positions 44 crimp contacts 45 tools 45'}][/table_203]

[table_204][{0: '— L —'}, {0: 'Label 41 LIN 170 characteristics 172 functional description 171 maximum ratings 172 pinout 170 Low-side digital outputs 165 analog voltage inputs 169 diagnostic functions 167 digital inputs 169 functional description 166 power stage pairing 167 low-side outputs 168 maximum ratings 167 pinout 165'}][/table_204]

- N —
Negative power supply BAT- . . . . . . . . . . . . . . . . . 104 functional description .. . . . . . . . . . . . . . . . . . 105 maximum ratings . . . . . . . . . . . . . . . . . . . . . . . 105 pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
- O —
Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2, 96

[table_207][{0: '— P —'}, {0: 'Pinning and connector 42 Programming options 3 - R - RS232 173 characteristics 174 functional description 174 maximum ratings 174 pinout 173 RTC backup battery 185 characteristics 187 functional description 186 maximum ratings 187 pinout 185 - S - Safety and certification 2 Safety concept 188 Sensor GND 106 functional description 107 maximum ratings 107 pinout 106 Sensor supplies 5 V 112 characteristics 113 functional description 112 maximum ratings 113 pinout 112 Sensor supply variable 114 characteristics 115 functional description 114 maximum ratings 115 pinout 114 Software description 225 Standards and guidelines 35 chemical capability 37 climatic capability 36 electrical capability 36 industrial applications ESD and EMC capability 38 ingress protection capability 37 mechanical capability 36 road vehicles ESD and EMC capability 38'}][/table_207]

[table_208][{0: '— W —'}, {0: 'Wake-Up 110 characteristics 111 functional description 110 maximum ratings 111 pinout 110'}][/table_208]

[table_206][{0: '— T —'}, {0: 'Terminal 15 108 characteristics 109 functional description 109 maximum ratings 109 pinout 108 Timer inputs 130 analog voltage input 136 current loop input 134 digital input 136 functional description 131 maximum ratings 131 pinout 130 timer input 134'}][/table_206]

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
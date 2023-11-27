# Hardware report/Build instructions
Your target audience is a Computer Engineering Technology student from a different college who would like to recreate your project. 
## Table of Contents
[1.0 Introduction](#10-introduce-the-broadcom-development-platform-and-exisiting-functionality)   
[2.0 Body](#20-added-functionality)   
[2.1 Sensor/Effector purchase](#21-sensor-effector-purchase)   
[2.2 PCB design and soldering](#22-pcb-design-and-soldering)   
[2.3 Case design and assembly](#23-case-design-and-assembly)   
[2.4 Firmware development and use](#24-firmware-development-and-use)   
[3.0 Testing and Results](#30-testing-and-results)   
[4.0 References](#40-references)  

## 1.0 Introduce the Broadcom development platform and exisiting functionality   

*Replace this text.*   

## 2.0 Added functionality   

*Replace this text.*   

### 2.1 Sensor/Effector purchase   
https://www.sparkfun.com/products/15177
purchased from sparkfun with express shipping came the next day international

Purchased standoffs, screws, and (https://www.sparkfun.com/products/15177
Purchased from SparkFun with express shipping came the next day international
-
Purchased standoffs, screws and Qwiic connectors from Digikey - came next day with normal shipping 
check BOM for a full list of parts (https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/bom.md)
The subtotal is $278, total was past $300 with shipping

### 2.2 PCB design and soldering   

*Replace this text.*   

### 2.3 Case design and assembly   

*Replace this text.*   

### 2.4 Firmware development and use   
https://github.com/sparkfun/Qwiic_Proximity_Py --Visit Github for python library and install all dependency drivers along with "sudo pip install sparkfun-qwiic-proximity"
make sure to install sensehat as well. "pip3 install sense-hat"
in python file -- "import qwiic_proximity" is used to access Qwiic library and "from sense_hat import SenseHat" accesses sensehats library

The firmware for this project was developed in Python, utilizing the qwiic_proximity library for the VCNL4040 sensor and the sense_hat library for the Raspberry Pi Sense HAT. The complete code and instructions for installation are available on GitHub at ---https://github.com/PrototypeZone/hardware-project-DylanAshton2206/tree/main/firmware "VCNL4040.py"---. This script includes initializing the sensor, reading proximity and ambient light data, and visually representing this data on the Sense HAT's LED matrix.

## 3.0 Testing and Results   
After installing the required libraries, running VCNL4040.py successfully initializes the proximity sensor. The sensor's readings range from 0 to 25,000 for proximity, with higher values indicating closer proximity. 
The ambient light sensor reacts to changes in light levels. In case of issues, use pip3 for library installations and i2cdetect -y 1 to verify the sensor's I2C connection at address 0x60.

## 4.0 References
https://github.com/PrototypeZone/hardware-project-DylanAshton2206
-
https://github.com/sparkfun/Qwiic_Proximity_Py
-
https://www.sparkfun.com/products/15177


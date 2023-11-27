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
[https://www.sparkfun.com/products/15177
purchased from sparkfun with express shipping came the next day international

Purchased standoffs, screws, and ](https://www.sparkfun.com/products/15177
Purchased from SparkFun with express shipping came the next day international
-
Purchased standoffs, screws and Qwiic connectors from Digikey - came next day with normal shipping 
check BOM for a full list of parts (https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/bom.md)
The subtotal is $278, total was past $300 with shipping)

### 2.2 PCB design and soldering   

*Replace this text.*   

### 2.3 Case design and assembly   

*Replace this text.*   

### 2.4 Firmware development and use   
https://github.com/sparkfun/Qwiic_Proximity_Py --Visit Github for python library and install all dependency drivers along with "sudo pip install sparkfun-qwiic-proximity"
make sure to install sensehat as well. "pip3 install sense-hat"
in python file -- "import qwiic_proximity" is used to access Qwiic library and "from sense_hat import SenseHat" accesses sensehats library

---The trial code can be found at https://github.com/PrototypeZone/hardware-project-DylanAshton2206/tree/main/firmware "VCNL4040.py" ---
This Python script is designed to interface with a VCNL4040 proximity sensor using a Raspberry Pi with a Sense HAT attachment. The script utilizes the qwiic_proximity library to communicate with the proximity sensor and the sense_hat library to control the Sense HAT's LED matrix.
Here's a quick overview of its functionality:

Initialization:
The script initializes the Sense HAT and the VCNL4040 proximity sensor.
It checks if the proximity sensor is connected correctly and prints a message indicating whether the initialization was successful.

Maximum Proximity Value:
MAX_PROXIMITY is set to 26,000, which is a cushioned upper limit for the proximity sensor's raw reading. This value is used to normalize the proximity readings.

Color Calculation:
The get_exponential_color function calculates an RGB color value based on the proximity sensor's reading. It applies an exponential transformation (with an exponent of 0.15) to the proximity value, making the LED color change more sensitive to closer objects.
The resulting color ranges from green (object is far away) to red (object is close), with intermediate values represented by varying shades between green and red.

Main Loop:
In an infinite loop, the script reads the current proximity value and the ambient light level from the sensor.
It prints these values to the console for monitoring.
It then calculates the appropriate color based on the proximity value and sets the Sense HAT's LED matrix to this color.
The loop has a one-second delay to ensure it doesn’t run too fast and consume excessive CPU resources.

Keyboard Interrupt:
If a KeyboardInterrupt (typically Ctrl+C on the keyboard) is detected, the script clears the Sense HAT's LED matrix and prints a message indicating that the program has stopped.

## 3.0 Testing and Results   
After installing all the required libraries, Run VCNL4040.py and if "Proximity sensor initialized." is outputted in the console you have successfully initialized the sensor, and is now ready to be used however you can imagine.
readings should be between 0 and 25000, for proximity with larger values meaning closer proximity.
ambient light will react to darkness and flashlights.

If experiencing issues try pip3 instead of pip for installing libraries and check "i2cdetect -y 1" to make sure 0x60 is showing a connection

## 4.0 References
https://github.com/PrototypeZone/hardware-project-DylanAshton2206
-
https://github.com/sparkfun/Qwiic_Proximity_Py
-
https://www.sparkfun.com/products/15177


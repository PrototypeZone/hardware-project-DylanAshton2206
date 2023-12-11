# VCNL4040 Hardware report
This project showcases the development of a proximity detection system using the Broadcom development platform, centered around a Raspberry Pi and the VCNL4040 proximity sensor. The goal was to design a versatile system capable of accurately sensing proximity and ambient light for applications such as automation and interactive installations. The project involved integrating the sensor with a custom-designed PCB, developed in KiCad and connected via an I2C bus, along with the creation of custom firmware in Python to process and visually represent sensor data using a Raspberry Pi Sense HAT's LED matrix. A custom case was also designed and fabricated to house the components securely. Targeted at students and enthusiasts in Computer Engineering Technology, this report documents the entire development process, from hardware selection and PCB design to software development and system assembly, providing a comprehensive guide for recreating or drawing inspiration from this project.

![project](pcb/media/project.png)

## Table of Contents
[1.0 Introduction](#10-introduce-the-broadcom-development-platform-and-exisiting-functionality)   
[2.0 Body](#20-added-functionality)   
[2.1 Sensor/Effector purchase](#21-sensor-effector-purchase)   
[2.2 PCB design and soldering](#22-pcb-design-and-soldering)   
[2.3 Case design and assembly](#23-case-design-and-assembly)   
[2.4 Firmware development and use](#24-firmware-development-and-use)   
[3.0 Testing and Results](#30-testing-and-results)   
[4.0 References](#40-references)  

## 1.0 Introduce the Broadcom development platform and existing functionality   
### 1.1 Overview of Broadcom Development Platform
The Broadcom development platform, exemplified by the Raspberry Pi, offers a versatile and powerful environment for a wide range of projects. Known for its robust processing capabilities, the platform typically includes Broadcom's ARM-based CPUs, essential for handling complex computations and multitasking. Key features include:

Core Components:
Processor: ARM-based CPUs, offering a balance of performance and power efficiency.
Communication Modules: Integrated WiFi and Bluetooth for wireless connectivity.
Interfaces: A variety of I/O options including GPIO pins, USB ports, and HDMI outputs.

### 1.2 Existing Functionality and Applications
The Broadcom platform is renowned for its flexibility and extensive library support, catering to various programming languages such as Python, C++, and Java.

Current Capabilities:

Extensive library support for developing a range of applications.
Compatibility with various sensors and modules through GPIO and I2C interfaces.
Support for Linux-based operating systems, providing a rich set of tools and applications.
Typical Use-Cases:

Ideal for IoT projects, home automation, and educational purposes.
Used in robotics for controlling sensors and actuators.
Suitable for building custom embedded systems for specific applications.

### 1.3 Development Environment and Tools
The development environment for the Broadcom platform is diverse, offering various tools and IDEs to suit different programming needs.

Software Tools:
Raspbian OS: A Debian-based operating system optimized for the Raspberry Pi.
VNC Viewer: Enables remote desktop access to the Raspberry Pi, allowing developers to work on the platform from any location.
Integrated Development Environments (IDEs): Support for IDEs like Thonny, Eclipse, and others. 

Hardware Tools:
Sense HAT for Raspberry Pi: An add-on board for Raspberry Pi, featuring an LED matrix, joystick, and multiple sensors like temperature, humidity, pressure, and orientation sensors, useful for interactive projects and data logging.
Laser Cutter: Provided by the school, used for precision cutting of materials such as wood, plastic, and fabric, ideal for creating custom enclosures or parts for Raspberry Pi projects.
PCB Maker: Also provided by the school, this device is used to manufacture Printed Circuit Boards (PCBs), allowing the creation of custom circuit designs for interfacing with the Raspberry Pi.
Soldering Iron and Solder: Essential for electronics projects, used to solder components onto PCBs or other interfaces to ensure secure electrical connections.
Multimeter: A versatile instrument for measuring voltage, current, and resistance, crucial for troubleshooting and testing circuits in Raspberry Pi projects.
DC Power Supply: Provides stable and adjustable DC power, essential for testing and powering electronic circuits safely during the development and debugging phases.

## 2.0 Added functionality   
### 2.1 Sensor/Effector purchase   
https://www.sparkfun.com/products/15177
purchased from sparkfun with express shipping came the next day international

Purchased standoffs, screws, and (https://www.sparkfun.com/products/15177
Purchased from SparkFun with express shipping came the next day international
Purchased standoffs, screws, and Qwiic connectors from Digikey came the next day with normal shipping 
check BOM for a full list of parts (https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/bom.md)
The subtotal is $278, total was past $300 with shipping

I highly recommend the 1-day shipping as others experienced problems with the standard.

### 2.2 PCB design and soldering   
In this project phase, a custom PCB was designed using KiCad, emphasizing the integration of the VCNL4040 proximity sensor and the implementation of an I2C bus for effective sensor communication. The PCB layout was carefully planned to include a connection to GPIO pin 17 on the Raspberry Pi, specifically for LED functionality. This setup was crucial for later testing the LED using the gpio_led.py script, which also served as a check for the soldering quality of the components. 

Following the design process, the PCB was fabricated, and components were precisely soldered onto the board. Special attention was paid to the I2C connections to ensure robust and reliable communication. After soldering, the board underwent rigorous inspection and functional testing, including verifying the I2C bus functionality and the LED operation connected to GPIO pin 17.
# This PCB is placed between the sense hat and the Raspberry PI 
![pcbstacking](pcb/media/pcbstacking.png)

The entire PCB design and associated files used in this project can be found and referenced https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/pcb/DylanAshton2023-10-16.zip. This repository serves as a detailed resource for understanding the PCB layout and design specifics.
When soldering It was important to make a strong electrical and mechanical connection.
This phase was pivotal in building a solid hardware foundation, ensuring that all components were properly aligned and functional for the seamless integration of the sensor and firmware development.

For troubleshooting check https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/pcb/README.md

### 2.3 Case design and assembly   
For the project, a custom case was designed to encase the Raspberry Pi along with the VCNL4040 proximity sensor and the custom PCB. The primary focus of the design was functionality and practicality:

Case Design: The case was engineered with precision cutouts for mounting the PCB and ensuring secure placement of the Raspberry Pi and sensor. Special attention was given to creating holes for board mounting, ensuring a snug and secure fit for the electronics.
Final Assembly: After designing and fabricating the case, the electronic components were carefully assembled and mounted, with the Raspberry Pi, sensor, and PCB fitting perfectly within the designated spaces.
This case provided a compact, functional, and secure housing for the hardware, integral to the project's success.

My laser-cut files can be found here https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/lasercutting/DylanAshtonLC.pdf

---

### 2.4 Establishing Connection to the Raspberry Pi and Verifying I2C Connectivity

To initiate the connection with the Raspberry Pi and verify the I2C connection, follow these steps:

#### Connecting the VNCL4040 Sensor:
- Attach the VNCL4040 sensor to your custom-made PCB using the Qwiic connector. This step integrates the sensor with your Raspberry Pi setup.

#### Powering the Raspberry Pi:
- Use a USB-C cable to power the Raspberry Pi. Additionally, connect the Raspberry Pi to your PC using an Ethernet cable. This establishes a network connection between the two devices.

#### Remote Access via VNC Viewer:
- On your PC, open the VNC Viewer application.
- Connect to the Raspberry Pi using the IP address `169.254.0.2`. You will need to enter the username and password specific to your Raspberry Pi to gain access.

#### Verifying the I2C Connection:
- Once connected, open the Raspberry Pi's console.
- Type the command `i2cdetect -y 1` and execute it. This command scans the I2C bus for devices.
- If you see the address `0x60` in the output, it indicates a successful connection to the VNCL4040 sensor. This is a positive sign that your project setup is correctly configured and nearly operational.

![I2C Connection](pcb/media/i2c.png)

---

### 2.5 Firmware Development and Implementation

To facilitate the firmware development for this project, we utilized Python, leveraging specific libraries for interfacing with the hardware components:

- **Installing Necessary Libraries**:
  - Visit the GitHub repository at [SparkFun Qwiic Proximity Python Library](https://github.com/sparkfun/Qwiic_Proximity_Py) to access the Python library for the VCNL4040 sensor. Install all the required dependency drivers using the command: `sudo pip install sparkfun-qwiic-proximity`.
  - For the Sense HAT, install its library using `pip3 install sense-hat`.

- **Python Script Setup**:
  - In your Python script, include the line `import qwiic_proximity` to utilize the Qwiic library functionalities for the VCNL4040 sensor.
  - Access the Sense HAT's library by including `from sense_hat import SenseHat`.

- **Firmware Overview**:
  - The firmware, primarily developed in Python, integrates the `qwiic_proximity` library for the VCNL4040 sensor and the `sense_hat` library for the Raspberry Pi Sense HAT.
  - Complete code and detailed installation instructions are available on GitHub at [VCNL4040.py](https://github.com/PrototypeZone/hardware-project-DylanAshton2206/tree/main/firmware).
  - This script includes initializations for the sensor, methods to read proximity and ambient light data, and functions to visually represent this data on the Sense HAT's LED matrix.

### 3.0 Testing and Observations

- **Running the Firmware**:
  - After installing the required libraries, execute the `VCNL4040.py` script. This will initialize the proximity sensor and start data acquisition.
  - The sensor's proximity readings range from 0 to 25,000, with higher values indicating closer objects.
  - The ambient light sensor adapts to varying light levels, providing real-time environmental data.

- **Troubleshooting Tips**:
  - If you encounter any installation issues, try using `pip3` for library installations. This ensures compatibility with Python 3.
  - To confirm the sensor's I2C connection, use the command `i2cdetect -y 1`. A successful detection will show the sensor's address as `0x60`, indicating proper connectivity and functionality.

## 4.0 References
https://github.com/PrototypeZone/hardware-project-DylanAshton2206
-
https://github.com/sparkfun/Qwiic_Proximity_Py
-
https://www.sparkfun.com/products/15177
-
https://github.com/PrototypeZone/ceng317/blob/main/README.md


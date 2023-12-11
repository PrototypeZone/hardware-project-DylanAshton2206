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
### 2.1 Sensor/Effector Purchase

In this stage of the project, key components were acquired to ensure timely progress and quality results.

#### Acquisitions:
- **VCNL4040 Proximity Sensor**: Purchased from [SparkFun](https://www.sparkfun.com/products/15177). Opted for express shipping, which remarkably ensured next-day international delivery.

- **Additional Hardware Components**:
  - Standoffs, screws, and Qwiic connectors were ordered from Digikey. These items also arrived promptly with normal shipping.

#### Bill of Materials (BOM):
- For a comprehensive list of all parts used in this project, refer to the BOM available at the [GitHub repository](https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/bom.md).

#### Budget Considerations:
- The subtotal for these components was approximately $278, with the total exceeding $300 after including shipping costs.

#### Shipping Recommendation:
- I highly recommend opting for 1-day shipping. Based on experiences within our project and from others, expedited shipping has proven to be more reliable compared to standard options.

### 2.2 PCB Design and Soldering

In this project phase, a custom PCB was designed using KiCad, with a focus on integrating the VCNL4040 proximity sensor and implementing an I2C bus for effective sensor communication. The PCB layout was planned to include a connection to GPIO pin 17 on the Raspberry Pi for LED functionality. This was crucial for testing the LED using the `gpio_led.py` script, which also served as a quality check for soldering.

#### PCB Fabrication and Soldering:
- After designing, the PCB was fabricated and components were precisely soldered onto the board.
- Special attention was given to the I2C connections to ensure robust communication.
- Post-soldering, the board was rigorously inspected and functionally tested, including verifying I2C bus functionality and LED operation connected to GPIO pin 17.

#### PCB Placement:
- This PCB is placed between the Sense HAT and the Raspberry Pi.
  
  ![PCB Stacking](pcb/media/pcbstacking.png)

#### PCB Design Files:
- The entire PCB design and associated files are available at [this GitHub repository](https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/pcb/DylanAshton2023-10-16.zip).
- The repository provides detailed insights into the PCB layout and design specifics.
- Important: Ensure strong electrical and mechanical connections when soldering.
- For troubleshooting, check the [README](https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/pcb/README.md) on GitHub.

### 2.3 Case Design and Assembly

For the project, a custom case was designed to encase the Raspberry Pi, the VCNL4040 proximity sensor, and the custom PCB. The focus was on functionality and practicality.

#### Case Design:
- Engineered with precision cutouts for mounting the PCB and ensuring secure placement of the Raspberry Pi and sensor.
- Special attention to board mounting holes for a snug fit.

#### Final Assembly:
- Post-design and fabrication, the electronic components were carefully assembled and mounted within the case.

#### Laser-Cut Files:
- The laser-cut files for the case are available [here](https://github.com/PrototypeZone/hardware-project-DylanAshton2206/blob/main/hardware/lasercutting/DylanAshtonLC.pdf).

This case provided a compact, functional, and secure housing for the hardware, contributing significantly to the project's success.

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


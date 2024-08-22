# Force Measurement System using ESP32, SK6511 Load Cell, and JY-S60 Weight Transmitter

## Overview

This project demonstrates a reliable and accurate force measurement system utilizing the ESP32 microcontroller, SK6511 load cell sensor, and JY-S60 weight transmitter. It is designed for applications requiring real-time data acquisition and processing, such as industrial automation, robotics, aerospace, and material testing.

The system captures force data using the SK6511 load cell, processes it with the ESP32 microcontroller, and wirelessly transmits the information via the JY-S60 weight transmitter. This setup provides a cost-effective, versatile, and accurate solution for various industries and research domains.

## Features

- **High Precision Force Measurement:** Utilizes the SK6511 strain gauge-based load cell sensor.
- **Wireless Data Transmission:** Transmits force data wirelessly using the JY-S60 weight transmitter.
- **Real-time Monitoring:** Interface for real-time monitoring and analysis on a remote device.
- **ESP32 Microcontroller:** Low power consumption, built-in Wi-Fi, and Bluetooth connectivity.


## Hardware Components

- **ESP32 Microcontroller**
- **SK6511 Load Cell Sensor**
- **JY-S60 Weight Transmitter**
- **Wires, connectors, and power supply**

## Software Requirements

- **Arduino IDE or ESP-IDF** for programming the ESP32.
- **Libraries:** Load Cell (HX711) library, WiFi library, and any other required dependencies.

## Setup Instructions

1. **Hardware Setup:**
   - Connect the SK6511 load cell sensor to the ESP32 as per the wiring diagram in the `/hardware` directory.
   - Interface the JY-S60 weight transmitter with the ESP32.

2. **Software Installation:**
   - Install the required libraries mentioned above.
   - Upload the code from the `/src` directory to the ESP32.

3. **Run the System:**
   - Power on the ESP32.
   - Monitor the force data wirelessly on the remote device using the developed interface.

## Experimental Validation

The system has been validated through extensive testing, with an average error rate of 4.67%. The results demonstrate the sensor system’s suitability for assessing force measurement in dynamic conditions.

## Applications

- **Industrial Automation**
- **Robotics**
- **Aerospace**
- **Material Testing**

## Future Improvements

- Enhancing the interface for better user experience.
- Expanding the system for multi-load cell integration.
- Implementing advanced data analytics for predictive maintenance.

## Contributions

Feel free to fork this repository, raise issues, and submit pull requests. Contributions to improve the project are welcome!

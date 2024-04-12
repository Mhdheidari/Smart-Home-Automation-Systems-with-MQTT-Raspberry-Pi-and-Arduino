# Smart-Home-Automation-Systems-with-MQTT-Raspberry-Pi-and-Arduino
# IoT Home Automation with MQTT Protocol

The increasing prevalence of sensors and Internet of Things (IoT) devices has introduced new challenges, particularly in managing IoT technologies. Researchers in academia and industry are exploring innovative approaches to simplify the integration and utilization of IoT technologies. One significant trend in the automation sector is the development of smart home systems, with numerous projects and devices designed for home automation.

## Challenges and Proposed Solution
IoT devices face challenges such as assigning unique IP addresses to each sensor, optimizing individual computation, and reducing costs and energy consumption. As the number of IoT devices in networks grows, these challenges become more pronounced. To address these issues, we propose a novel approach to home automation using the MQTT (Message Queuing Telemetry Transport) protocol.

## MQTT Protocol Overview
- MQTT is a lightweight messaging protocol specifically designed for constrained devices operating in low-bandwidth, high-latency, or unreliable networks.
- The core concept of MQTT involves a publish-subscribe model, where clients publish messages to topics and subscribe to receive messages on specific topics.
- In our smart home system design, we utilize the Mosquitto MQTT broker installed on the Raspberry Pi.

## System Components and Software
- **Arduino IDE**: An open-source software environment for code scripting and uploading to microcontrollers. It enables communication with Arduino microcontrollers and provides a serial monitor for viewing sensor data.
  
<p align="center">
<b>Arduino IDE output based on the door’s distance and condition:</b>  <br />
<img src="https://i.imgur.com/MIkRSEZ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>
<br /><br /><br />
<p align="center"><b>Arduino IDE output based on the temperature and light’s condition:</b> <br />
<img src="https://i.imgur.com/Isoijjq.png" height="80%" width="80%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 

- **MQTT Broker (Mosquitto)**: The Mosquitto MQTT broker serves as the central hub for receiving, filtering, and distributing messages between IoT devices and clients. In our system, it runs on the Raspberry Pi.
<p align="center"><b>Raspberry Pi as a Broker:</b> <br />
<img src="https://i.imgur.com/xAm47ZK.png" height="50%" width="50%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 
  
- **Python**: We implement various MQTT protocol features using Python, a high-level general-purpose programming language. Python libraries such as `paho-mqtt`, `tkinter` (for GUI), and `matplotlib` are utilized for developing the subscriber, subscriber dashboard, and control functionalities.
  
<p align="center"><b>Two publishers publishing data simultaneously:</b> <br />
<img src="https://i.imgur.com/KcMVd1v.png" height="80%" width="80%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 
<p align="center"><b>The console output of the subscriber:</b> <br />
<img src="https://i.imgur.com/Bzz9KOp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 

## Interactive Dashboard
We create a custom interactive Graphical User Interface (GUI) using Python to visualize and display real-time data received from publishers via the MQTT broker. The GUI includes two distinct interfaces:
- **Master Subscriber GUI**: Displays data from all subscribed topics.
  
- **Individual Subscriber GUI**: Allows users to select specific topics using toggle buttons for customized data visualization.
<p align="center"><b>Arduino IDE output based on the temperature and light’s condition:</b> <br />
<img src="https://i.imgur.com/DMU4O2n.png" height="80%" width="80%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 

## Technology Integration
The system integrates Arduino microcontrollers for sensor data collection:
- **Ultrasonic Sensor and Buzzer**: Connected to pins 13 and 14 on the first Arduino.
<p align="center"><b>Ultrasonic sensor and Buzzer:</b> <br />
<img src="https://i.imgur.com/zvpfwEP.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 
  
- **Light and Temperature Sensor, LED, and Fan**: Connected to pins A0, A2, 6, and 11 on the second Arduino.
<p align="center"><b>Light and temperature sensor, LED and fan:</b> <br />
<img src="https://i.imgur.com/Kp4YfKi.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/></p>
<br /><br /><br /> 

## Results and Observations
- **Real-time Monitoring**: Graphical representations of door status (Open/Close), temperature, light conditions, and door distance are displayed through the GUI.
  
- **Sensor Readings**: Instantaneous changes in the environment, such as temperature fluctuations and door status transitions, are accurately captured and displayed.
  
- **Console Outputs**: The system showcases the asynchronous data publishing by two distinct publishers, reflecting the real-time status of the lamp, temperature, door distance, and door condition ("opened" or "closed").

## Conclusion
Our experiment highlights the effectiveness of the MQTT protocol in conjunction with Raspberry Pi as a lightweight solution for home automation. The system demonstrates minimal bandwidth consumption, energy efficiency, and centralized control with a single IP address for all devices. Future directions include investigating the security aspects of the Mosquitto MQTT broker and conducting comparative studies on MQTT's efficiency and energy consumption compared to other messaging models.

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

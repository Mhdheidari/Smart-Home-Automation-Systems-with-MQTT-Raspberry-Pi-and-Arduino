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
  
- **MQTT Broker (Mosquitto)**: The Mosquitto MQTT broker serves as the central hub for receiving, filtering, and distributing messages between IoT devices and clients. In our system, it runs on the Raspberry Pi.
  
- **Python**: We implement various MQTT protocol features using Python, a high-level general-purpose programming language. Python libraries such as `paho-mqtt`, `tkinter` (for GUI), and `matplotlib` are utilized for developing the subscriber, subscriber dashboard, and control functionalities.

## Interactive Dashboard
We create a custom interactive Graphical User Interface (GUI) using Python to visualize and display real-time data received from publishers via the MQTT broker. The GUI includes two distinct interfaces:
- **Master Subscriber GUI**: Displays data from all subscribed topics.
  
- **Individual Subscriber GUI**: Allows users to select specific topics using toggle buttons for customized data visualization.

## Technology Integration
The system integrates Arduino microcontrollers for sensor data collection:
- **Ultrasonic Sensor and Buzzer**: Connected to pins 13 and 14 on the first Arduino.
  
- **Light and Temperature Sensor, LED, and Fan**: Connected to pins A0, A2, 6, and 11 on the second Arduino.

## Results and Observations
- **Real-time Monitoring**: Graphical representations of door status (Open/Close), temperature, light conditions, and door distance are displayed through the GUI.
  
- **Sensor Readings**: Instantaneous changes in the environment, such as temperature fluctuations and door status transitions, are accurately captured and displayed.
  
- **Console Outputs**: The system showcases the asynchronous data publishing by two distinct publishers, reflecting the real-time status of the lamp, temperature, door distance, and door condition ("opened" or "closed").

## Conclusion and Future Work
Our experiment highlights the effectiveness of the MQTT protocol in conjunction with Raspberry Pi as a lightweight solution for home automation. The system demonstrates minimal bandwidth consumption, energy efficiency, and centralized control with a single IP address for all devices. Future directions include investigating the security aspects of the Mosquitto MQTT broker and conducting comparative studies on MQTT's efficiency and energy consumption compared to other messaging models.


<p align="center">
<b>Project Scenario:</b>  <br />
<img src="https://i.imgur.com/qVqBZJo.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />  
<b>Install Oracle VirtualBox:</b> <br />
<img src="https://i.imgur.com/Jrrj3lR.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br /> 
<b>Install Windows Server 2019 ISO on VM:</b> <br />
<img src="https://i.imgur.com/NTMjlL2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br /> 
<b>Install Windows 10 ISO on VM:</b> <br />
<img src="https://i.imgur.com/DLG2F9L.png"80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br /> 
<b>Rename the Network Connections:</b> <br />
<img src="https://i.imgur.com/ypDq1sx.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br /> 
<b>Set (TCP/IP) properties for Internal Connection:</b> <br />
<img src="https://i.imgur.com/ZJ9szlY.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Install Active Directory Domain Services on Server:</b> <br />
<img src="https://i.imgur.com/Nr6S8Dx.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Creat a domain name:</b> <br />
<img src="https://i.imgur.com/j7lQcqb.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Creat Admin Organization Unit:</b> <br />
<img src="https://i.imgur.com/4TFp8RS.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Creat Admin User:</b> <br />
<img src="https://i.imgur.com/s7M1T5l.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/rBPHtrY.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Setup Remote Access Server (RAS):</b> <br />
Allow Client1 on Windows 10 to access to the internet throughout the Domain Controller (DC)
<img src="https://i.imgur.com/NLCb2IK.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/VWLf3IN.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/lFy3Z2f.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/r5c6MSm.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/aMvmNWl.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Setup DHCP Server on Domain Controller:</b> <br />
Allow Client1 on Windows 10 to to get IP address that get them allow to browse the internet
<img src="https://i.imgur.com/7Ch2ik2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /> 
<img src="https://i.imgur.com/D0LfRvA.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/TtLou4W.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/uWqG8O0.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/2CgXxYR.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/YrDfOQU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Create sample users by PowerShell:</b> <br />
<img src="https://i.imgur.com/v9e1Orw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /> 
<img src="https://i.imgur.com/FuUvwfS.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /> 
<img src="https://i.imgur.com/vGk1Vvu.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /> 
<img src="https://i.imgur.com/DdepuLs.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br />
<b>Create New VM as a Client1 and install Windows 10 ISO:</b> <br />
<img src="https://i.imgur.com/G4w0cm8.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/KxEQjSt.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/InDi0Vp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />  
<img src="https://i.imgur.com/ElQ8ABN.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br /><br /><br /> 
<b>Change the computer name and login with one of the users:</b> <br />
<img src="https://i.imgur.com/4CWkkpy.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<img src="https://i.imgur.com/lnnjo5X.jpeg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />  
</p>
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

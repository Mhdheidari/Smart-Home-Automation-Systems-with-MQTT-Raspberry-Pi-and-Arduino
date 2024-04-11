"""
IoT Data Publisher via MQTT

This Python script is designed to collect data from an Arduino connected via serial port
and publish the data to an MQTT broker. The data collected includes the temperature and
lamp status.

The script utilizes the `paho.mqtt.client` library for MQTT communication and the `serial`
library to communicate with the Arduino.

Author: Mohammad Heidari
Date: July, 2023

Dependencies:
- paho.mqtt.client
- serial

Usage:
1. Connect the Arduino to the computer and note the serial port (e.g., COM3 on Windows).
2. Update the `ser = serial.Serial('COM2', 9600)` line with the Arduino's port.
3. Set the MQTT broker address and port in the `broker_address` and `broker_port` variables.
4. Run the script to collect data from the Arduino and publish it to MQTT topics.
"""

import paho.mqtt.client as paho
import time
import serial
import paho.mqtt.client as paho
import psutil
import time as clock

class Publisher:
    broker_address = None
    broker_port = None

    def __init__(self, address, port):
        self.broker_address = address
        self.broker_port = int(port)

    def on_publish(self, client, userdata, result):
        pass

    def publish(self, topic, message):
        pub = paho.Client()
        pub.on_publish = self.on_publish
        pub.connect(self.broker_address, self.broker_port)
        answer = pub.publish(topic, message)
        print("Published topic:", topic, "message:", message)
        pub.disconnect()

def Data_collection():
    # Connect to Arduino via serial port (e.g., /dev/ttyUSB0 on Linux or COM3 on Windows)
    ser = serial.Serial('COM2', 9600)  # Change 'COM3' to your Arduino's port
    data = ser.readline().decode().strip()  # Read a line from Arduino and remove trailing newlines
    temperature = "23"  # Default value
    lamp = "ON"  # Default value

    try:
        temperature, lamp = data.split(",")
    except ValueError:
        print(f"Unexpected data format: {data}. Expected format: 'temperature,lamp'")

    Final_Data_collection= [temperature, lamp]

    return Final_Data_collection

    
def create_publisher_topics():
    publisher_topic_labels = ["temperature", "lamp"]
    publisher_topic_labels_prefix = "Ahmad's/"
    publisher_topics=[]
    for i in range(len(publisher_topic_labels)):
        publisher_topics.append(publisher_topic_labels_prefix  + publisher_topic_labels[i]) 
    print("Publisher Topics:")
    print(publisher_topics)
    
    return publisher_topics

if __name__ == "__main__":
    broker_address = "192.168.0.102"
    broker_port = 1883        
    publisher = Publisher(broker_address, broker_port)
    publisher_topics = create_publisher_topics()
    
    while True:
        print("we gonna publish some data now")
        Agent_Data = Data_collection()
        print("lets start")
        for index in range(len(Agent_Data)):
            print("Data is published at feature number ==",index," :")
            publisher.publish(publisher_topics[index],Agent_Data[index])
            

        clock.sleep(5)

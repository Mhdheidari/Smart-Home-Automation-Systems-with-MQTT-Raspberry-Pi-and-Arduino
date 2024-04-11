"""
MQTT Subscriber with Live Graph Update

This Python script demonstrates an MQTT subscriber that listens to multiple topics and updates a live graph with the received data. The script utilizes the `paho.mqtt.client` library for MQTT communication and `matplotlib` for graph plotting.

The `Subscriber` class handles the MQTT subscriptions and stores the received data along with timestamps. The `animate` function updates the graph with the latest data in real-time.

To use the script:
1. Set the MQTT broker address and port in the `broker_address` and `broker_port` variables.
2. Define the MQTT topics you want to subscribe to in the `subscriber_topic_labels` list.
3. Run the script and click on the buttons to toggle the live graph for each topic.

Author: Mohammad Heidari
Date: July, 2023

Dependencies:
- paho.mqtt.client
- matplotlib
- tkinter
"""

import paho.mqtt.client as paho
import time
import threading
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation
import tkinter as tk

print_lock = threading.Lock()

def thread_safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

class Subscriber:
    subscriber_topic = None
    broker_address = None
    broker_port = None    
    data = []
    timestamp = []

    def __init__(self, address, port, topic):
        self.broker_address = str(address)
        self.broker_port = int(port)
        self.subscriber_topic = str(topic)
        self.data = []
        self.timestamp = []

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.subscriber_topic)

    def on_message(self, client, userdata, message):
        Final_data = message.payload.decode("utf-8")
        if Final_data == "ON" and Final_data == "Open":
            Final_data = 1
        elif Final_data == "OFF" and Final_data == "Closed":
            Final_data = 0
        else:
            try:
                Final_data = float(Final_data)
            except ValueError:
                pass

        self.data.append(Final_data)
        self.timestamp.append(datetime.now())
        
        thread_safe_print("Received message: ", Final_data, "on topic", message.topic)

    def subscribe(self):
        sub = paho.Client()
        while True:
            sub.connect(self.broker_address, self.broker_port)
            sub.on_message = self.on_message
            sub.on_connect = self.on_connect
            sub.loop_forever()
            time.sleep(0.8)

def create_subscriber_topics():
    subscriber_topic_labels = ["temperature", "lamp", "distance", "door"]
    subscriber_topic_labels_prefix = "Ahmad's/"
    subscriber_topics=[]
    for i in range(len(subscriber_topic_labels)):
        subscriber_topics.append(subscriber_topic_labels_prefix  + subscriber_topic_labels[i]) 
    print("Subscriber Topics:")
    print(subscriber_topics)
    
    return subscriber_topics

def animate(i,index, axs, fig):
    axs.cla()
    axs.plot(subscribers[index].timestamp, subscribers[index].data, label=subscribers[index].subscriber_topic)
    axs.legend(loc='upper left')
    fig.canvas.draw()
    # root.after(100, animate, i+1, index, axs, fig)  # Schedule the next update

def toggle_button(index):
    button = buttons[index]
    if button['relief'] == tk.RAISED:
        button['relief'] = tk.SUNKEN
        fig, axs = plt.subplots(1, 1, figsize=(10, 5))  # Create a single subplot
        # Draw a circle on the graph
        selected_topic = subscriber_topics[index]  # Replace 0 with the desired index
        # print (selected_topic)
        # fig, axs = plt.subplots(len(subscriber_topics), 1, figsize=(10, 5))
        axs.set_title(selected_topic)
        ani = FuncAnimation(fig, animate, fargs=(index,axs, fig), frames=100, interval=1000)
        # plt.tight_layout()
        plt.show()
    else:
        button['relief'] = tk.RAISED
        print(str(index)+" button pressed")
        # print(str(index)+" button released") # Delete the circle from the graph
        plt.close()


if __name__ == "__main__":
    broker_address = "192.168.0.102"
    broker_port = 1883        
    subscriber_topics = create_subscriber_topics()
    
    subscribers = []
    for subscriber_topic in subscriber_topics:
        subscriber = Subscriber(broker_address, broker_port, subscriber_topic)
        subscribers.append(subscriber)
        thread = threading.Thread(target=subscriber.subscribe)
        thread.start()

    root = tk.Tk()
    root.title("Toggle Buttons")
    #plt.ion()

    # Create the toggle buttons
    buttons = []
    for index, label in enumerate(["temperature", "lamp", "distance", "door"]):
        button = tk.Button(root, text=label, relief=tk.RAISED,
                        command=lambda idx=index: toggle_button(idx))
        button.pack(side=tk.LEFT, padx=5, pady=5)
        buttons.append(button)

    # Create the graph
    graph = tk.Canvas(root, width=400, height=300, bg='white')
    graph.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


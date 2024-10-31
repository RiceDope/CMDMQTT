from paho.mqtt import client as mqttclient
import os
import random

"""

General functions that are used in order to deliver the service

author: Rhys Walker

"""

CLIENT_ID = f'python-mqtt-{random.randint(0, 1000)}'

def beginConnection(broker, port):
    #Do something
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker ", broker)
        else:
            print("Failed to connect, return code &d\n", rc)

    client = mqttclient.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqttclient, topic):
    def on_message(client, userdata, msg):
        try:
            print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
        except:
            print("Unknown issue with decoding message")

    client.subscribe(topic)
    client.on_message = on_message

def getBroker():
    print("Please type the MQTT broker you would like to use. \nOr type builtin for a list of ready to go brokers")
    print("This application will not work with password protected brokers")
    userInput = input(">>>")
    clear()

    # Builtin brokers
    if (userInput == "builtin"):
        print("Type the number that corresponds to the builtin broker")
        print("1. test.mosquitto.org")
        userInput = input(">>>")
        if (userInput == "1"):
            return 'test.mosquitto.org'

    # User specified broker
    else:
        return userInput
    
def getPort():
    # Add builtins
    return int(input("Please type out the port to connect on\n>>>"))

def getTopic():
    return input("Please type out the topic to connect to\n>>>")

def clear():
    os.system('cls')
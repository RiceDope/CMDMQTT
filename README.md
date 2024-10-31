# CMDMQTT
A simple MQTT client based in the command line

## Workflow
For the full interactive version select laucher. However you do have the ability to run the individual scripts sub1 and pub1.

### sub1
Sub1 has the ability to subscribe to one MQTT topic and will just print the results to the cmd terminal it is in.

### pub1
Pub1 has the ability to publish to one MQTT topic at a time. It can however change the topic it is publishing to.
There is no option to reconnect to alternative brokers or ports currently.

## Libraries used

- [paho.mqtt](https://pypi.org/project/paho-mqtt/) used for the bulk of the connections used.
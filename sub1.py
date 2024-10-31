from mqtt_code import *

"""

This script allows the user to subscribe to one mqtt topic

author: Rhys Walker

"""

def run():
    # Setup connection
    broker = getBroker()
    clear()
    port = getPort()
    clear()
    client = beginConnection(broker, port)
    topic = getTopic()
    clear()

    # Subscribe and loop forever
    subscribe(client, topic)
    client.loop_forever()

if __name__ == '__main__':
    run()
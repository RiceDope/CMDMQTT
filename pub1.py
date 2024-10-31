from mqtt_code import *

"""

This script allows the user to publish to a single mqtt topic

author: Rhys Walker

"""

def run():
    # Setup the connection
    broker = getBroker()
    clear()
    port = getPort()
    clear()
    client = beginConnection(broker, port)
    topic = getTopic()
    clear()

    while(True):
        print("Options: \nquit - Quits the program \nct - Changes the topic")
        message = input("What would you like to send\n>>>")
        if message=="quit": # Quit the application
            break
        elif message=="ct": # Change Topic
            clear()
            topic = getTopic()
            clear()
            print("Topic changed successfully\n") # Success message
            continue

        # Try publishing the message
        try:
            client.publish(topic, message)
            clear()
            print("Message posted successfully\n") # Success message

        # Allow the user to fix any issue that the topic has introduced
        except:
            clear()
            print("Cannot use wildcards in publish")
            print("Would you like to change the topic? (y/n) If you don't change the topic the window will close")
            ct = input(">>>")
            if ct == "y":
                topic = getTopic()
                clear()
                print("Topic changed successfully\n") # Success message
            else:
                break

if __name__ == "__main__":
    run()
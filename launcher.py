import os

"""

Script that launches the MQTT clients that the user wants

author: Rhys Walker

"""

#DEFINE OPTIONS
sub1 = "sub1.py" # Subscribe to one MQTT topic
pub1 = "pub1.py" # Post to one MQTT topic (Can change the topic though)

def launchConsole(type):
    os.system(f"start cmd /c python {type}")

def clear():
    os.system('cls')

# Notes is set each time an update is needed
def printOptionsList(notes = "No Notes"):
    print("Notes: ")
    print(notes)
    print("Please select an option")
    print("1. Subscribe to a topic on a given broker")
    print("2. Publish to a topic on a given broker")

def run():

    notes = "No Notes"

    while(True):
        printOptionsList(notes)
        userInput = input(">>>")
        notes = "No Notes"
        # What does the user wish to do
        if userInput == "1":
            clear() # Clear and print updates
            notes = "Opened another terminal window go there to subscribe"
            launchConsole(sub1)
        elif userInput == "2":
            clear()
            notes = "Opened another terminal window go there to publish"
            launchConsole(pub1)

        elif userInput == "quit":
            break

if __name__ == "__main__":
    run()
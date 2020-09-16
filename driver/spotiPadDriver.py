# File: driver.py
# Date: Sept. 16, 2020
# Author: @cgarcia2097
#
# Description:
#   - Captures and processes serial messages from an Arduino
#   - Translates valid messages as keyboard presses
#
# Dependencies (can be installed using pip):
#   - pyserial: https://pypi.org/project/pyserial/
#   - keyboard: https://pypi.org/project/keyboard/
# 
# Future work:
#   - Import control schema from JSON file

import sys
import keyboard
import serial
import datetime

##################################################
# START OF CONTROL SCHEMA
##################################################

#   Control Schema
#   - Implements a lookup table between control messages and keybinds
#   - Follows the Python dictionary format
#   - Arduino message is on the left, keybind is on the right
#   - Consult with https://github.com/boppreh/keyboard#api
#     for available keybinds

DEVICE_CTRL_SCHEMA = {
    "<VOL_UP>"      :    'ctrl + up',
    "<VOL_DOWN>"    :    'ctrl + down',
    "<PLAY/PAUSE>"  :    'space',
    "<PREV>"        :    'ctrl + left',
    "<NEXT>"        :    'ctrl + right',
    "<SHUFFLE>"     :    'ctrl + s',
    "<SEEK_FRONT>"  :    'shift + right',
    "<SEEK_BACK>"   :    'shift + left'
}

##################################################
# END OF CONTROL SCHEMA
##################################################

deviceSerial    =   serial.Serial()

# Event handler class for incoming messages
class deviceEventsClass(object):
    eventDict = {}

    # Constructor
    def __init__(self, dict):
        self.eventDict = dict.copy()
    
    def getEventDictionary(self):
        return self.eventDict
    
    # Check if message is valid; if so press the corresponding keybind
    def eventHandler(self, incomingMessage):
        if incomingMessage in self.eventDict:
            keyboard.press_and_release(self.eventDict.get(incomingMessage))
        else:
            driverLog("Invalid message received. Skipping...")
            return 1
        return 0

# Logging function
def driverLog(message):
    print("{" + str(datetime.datetime.now()) + "} - " + message)
    return 0

# Usage function
def usage():
    usageMsg ="""
    Usage:
    
    python .\\driver.py [YOUR_COM_PORT] [YOUR_ARDUINO_BAUDRATE]
        - Starts the serial driver at specified serial port and baud rate
        - Arduino baud rate must match driver baud rate
    """
    print(usageMsg)
    return 0

def appInit(argv):
    
    driverLog("Welcome to Spoti-Pad 1.0")

    # Set configuration options
    if (len(argv) == 3):
        driverLog("Using specified configuration options")
        deviceSerial.port       = str(argv[1])
        deviceSerial.baudrate   = str(argv[2])

    else:
        driverLog("Invalid usage detected. Aborting...")
        usage()
        sys.exit() 
        return 1  
    
    driverLog("Serial Port: " + str(deviceSerial.port))
    driverLog("Baudrate: " + str(deviceSerial.baudrate))
    deviceSerial.open()
    return 0


def appMainLoop():
    
    # Initialize keymaps and messages
    driverLog("Initalizing control schema")
    myEvent = deviceEventsClass(DEVICE_CTRL_SCHEMA)
    myEventDict = myEvent.getEventDictionary()
    
    print("Control Schema")
    for i in myEventDict:
        print ("Message: " + i + ", Keybind: " + myEventDict[i])

    # Read message from the Arduino
    driverLog("\nListening for new messages")
    while(1):
        deviceMsg = deviceSerial.readline().decode('ascii')     # Read newline-terminated string
        newString = deviceMsg.replace("\r", "")                 # Process out the extra characters
        newString = newString.replace("\n", "")
        driverLog("Received message: " + newString)
        myEvent.eventHandler(newString)                         # Respond to incoming message

    return 0

def main(argv):
    appInit(argv)
    appMainLoop()
    return 0

if __name__ == "__main__":
    main(sys.argv)
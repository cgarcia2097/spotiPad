# SpotiPad

Repository for the SpotiPad project.

## Description

The project consists of an Arduino sketch and a small Python script. 

The Arduino sketch sends a message over serial upon the depending on the button pressed.

The script implements a serial driver, capturing serial messages from an Arduino and pressing a hotkey on the host PC. It is currently bound to Spotify shortcuts, however it is essentially a bonafide keyboard.

## Dependencies

### Host PC
- The [Arduino IDE](https://www.arduino.cc/en/main/software), plus the following libraries:
  - `Bounce2` - [**Bounce2** page](https://github.com/thomasfredericks/Bounce2)
- A [Python 3+](https://www.python.org/downloads/) installation, with the following Python modules installed:
  - `keyboard` - [**keyboard** page](https://pypi.org/project/keyboard/)
  - `pyserial` - [**pyserial** page](https://pypi.org/project/pyserial/)

### Microcontroller
- An [Arduino (Uno, Mega, Nano, Duemilanove, etc.)](https://www.arduino.cc/en/Main/Products) attached to a host PC via USB cable or any other serial connection

## Usage

- In the **CONTROL_SCHEMA** section of `spotiPad.ino`, change the button pinouts and the serial messages within the sketch as needed. When finished, flash the sketch into the Arduino 
- In the **CONTROL_SCHEMA** section of `spotiPadDriver.py`, make sure that the serial messages match the messages sent by the Arduino, and set the appropriate keybinds 
- Run the script by typing:
  
  **In Windows**

    ```python .\spotiPadDriver.py YOUR_SERIAL_PORT YOUR_BAUDRATE```

  **In macOS/Linux**

    ```python ./spotiPadDriver.py YOUR_SERIAL_PORT YOUR_BAUDRATE```

## Extra tips

The `pyserial` module allows one to search for serial port that is used by the Arduino. Assuming only one Arduino is plugged in, typing `python -m serial.tools.list_ports` should yield the Arduino's serial port.

## Future Work
- Load control schema form JSON file
- Pairwise generation of driver and firmware

## Credits
Charles Garcia - @cgarcia2097
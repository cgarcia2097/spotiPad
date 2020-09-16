# SpotiPad

Repository for the SpotiPad project.

## Description

The project consists of an Arduino sketch and a small Python script. 

The Arduino sketch sends a message over serial upon the depending on the button pressed. The sketch is only supports momentary buttons at the moment, though that can be solved by pull requests to this repo.

The script implements a serial driver, capturing serial messages from an Arduino and pressing a hotkey on the host PC. It is currently bound to Spotify shortcuts, however it is essentially a bonafide keyboard.

**It is important that the messages match between the Arduino and the script, otherwise no interaaction will occur**

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

## Message convention

Curently, the message convention is very simple. It is your *MESSAGE* surrounded by triangular brackets:

`<MESSAGE>`

## Extra tips

The `pyserial` module allows one to search for serial port that is used by the Arduino. Assuming only one Arduino is plugged in, typing `python -m serial.tools.list_ports` should yield the Arduino's serial port.

## Future Work
- Load control schema from CSV file
- Pairwise generation of driver and firmware from CSV file

## Credits
Charles Garcia - @cgarcia2097
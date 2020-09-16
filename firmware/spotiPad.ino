/**
 * File: spotiPad.ino
 * Date: Sept. 15, 2020
 * Author: @cgarcia2097
 * Description: Provides a button interface and message stack to the SpotiPad
 * 
 * Dependencies:
 *  - Bounce2: https://github.com/thomasfredericks/Bounce2
 */

#include <Arduino.h>
#include <Bounce2.h>

#define NUM_KEYS 8
#define NUM_COMMANDS 8

/**
 * START OF CONTROL SCHEMA
 */

// Button Pins
#define KEY_PIN_1 21
#define KEY_PIN_2 20
#define KEY_PIN_3 19
#define KEY_PIN_4 18
#define KEY_PIN_5 15
#define KEY_PIN_6 14
#define KEY_PIN_7 16
#define KEY_PIN_8 10

// Control messages
#define KEY_MSG_1 "<VOL_UP>"
#define KEY_MSG_2 "<VOL_DOWN>"
#define KEY_MSG_3 "<PLAY>"
#define KEY_MSG_4 "<PAUSE>"
#define KEY_MSG_5 "<PREV>"
#define KEY_MSG_6 "<NEXT>"
#define KEY_MSG_7 "<SHUFFLE>"
#define KEY_MSG_8 "<SEEK_FRONT>"

/**
 * END OF CONTROL SCHEMA
 */

// Array optimizations
byte buttonArray[NUM_KEYS] = {
  KEY_PIN_1 ,
  KEY_PIN_2 ,
  KEY_PIN_3 ,
  KEY_PIN_4 ,
  KEY_PIN_5 ,
  KEY_PIN_6 ,
  KEY_PIN_7 ,
  KEY_PIN_8
};

String mesgArray[NUM_KEYS] = {
  KEY_MSG_1 ,
  KEY_MSG_2 ,
  KEY_MSG_3 ,
  KEY_MSG_4 ,
  KEY_MSG_5 ,
  KEY_MSG_6 ,
  KEY_MSG_7 ,
  KEY_MSG_8
};

// Bounce buttons
Bounce button[NUM_KEYS];

void setup() {

  // Initalize the button debouncing
  for(uint8_t i = 0; i < NUM_KEYS; i++){
    button[i] = Bounce();
    button[i].attach(buttonArray[i], INPUT_PULLUP);
    button[i].interval(8);
  }

  // Initialize Serial communications
  Serial.begin(115200);

}

void loop() {

  // Check each and every button
  for (uint8_t i = 0; i < NUM_KEYS; i++) {
    button[i].update();

    // When button is pressed, send the corresponding message
    if (button[i].fell()) {
      Serial.println(mesgArray[i]);
    }
  }
}

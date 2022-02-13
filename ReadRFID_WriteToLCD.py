#! /usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import drivers
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()
reader = SimpleMFRC522()

# Main body of code

try:
        id, readRFID = reader.read()
        rfidID = str(id)
        print(rfidID)
        print(readRFID)
finally:
        GPIO.cleanup()

#display.lcd_display_string("HALLO NUTZER",1)
display.lcd_display_string(str(readRFID),1)
display.lcd_display_string("i love smoli", 2)

sleep(3)
display.lcd_clear()
 

# sleep(5)
# display.lcd_display_string("Greetings DORIIII", 1)  # Write line of text to first line of display
# display.lcd_display_string("Demo Pi Guy code", 2) 

# try:
#     while True:
#         # Remember that your sentences can only be 16 characters long!
#         print("Writing to display")
#         display.lcd_display_string("Greetings DORIIII", 1)  # Write line of text to first line of display
#         display.lcd_display_string("Demo Pi Guy code", 2)  # Write line of text to second line of display
#         sleep(2)                                           # Give time for the message to be read
#         display.lcd_display_string("I am a display!", 1)   # Refresh the first line of display with a different message
#         sleep(2)                                           # Give time for the message to be read
#         display.lcd_clear()                                # Clear the display of any data
#         sleep(2)                                           # Give time for the message to be read
# except KeyboardInterrupt:
#     # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
#     print("Cleaning up!")
#     display.lcd_clear()
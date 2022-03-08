#! /usr/bin/env python
import RPi.GPIO as GPIO
import lcd_drivers
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcd_drivers.Lcd()

# Main body of code

#display.lcd_display_string("HALLO NUTZER",1)
display.lcd_display_string("Test",1)
display.lcd_display_string("Hallo Nutzer", 2)

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
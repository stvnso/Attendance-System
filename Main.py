#! /usr/bin/env python
import RPi.GPIO as GPIO
import drivers
from time import sleep
from Read_RFID_Chip import readRFID_fromChip
from SelectFromDB   import readRFID_fromDatabase


# Variablen
readRFID = None


# Initalisierungen
# Load the driver and set it to "display"
display = drivers.Lcd()


readRFID = readRFID_fromChip()
sqlQUERY = readRFID_fromDatabase(readRFID)


first_name  = sqlQUERY[2]
last_name = sqlQUERY[3]


print("\nPrinting to Display..")
display.lcd_display_string("Hallo",1)
display.lcd_display_string(first_name + " " + last_name, 2)
sleep(3)

display.lcd_clear()

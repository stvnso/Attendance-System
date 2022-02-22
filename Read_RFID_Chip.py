#! /usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from time import sleep

def readRFID_fromChip():
    reader = SimpleMFRC522()

    # Main body of code

    try:
            id,secondID = reader.read()
            readRFID = str(id)
            print("\n-------------------------------------")
            print("RFID_UID:\t" + readRFID)
            print("-------------------------------------\n")
    finally:
            GPIO.cleanup()

    return readRFID

#Auskommentieren um einen Chip zu lesen
#print(readRFID_fromChip())  
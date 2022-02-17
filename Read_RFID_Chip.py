#! /usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from time import sleep

def readRFID_fromChip():
    reader = SimpleMFRC522()

    # Main body of code

    try:
            id, givenID = reader.read()
            readRFID = str(id)
            print("\n-------------------------------------")
            print("RFID_UID: \t\t" + readRFID)
            print("Given Second ID: \t\t" + givenID)
            print("-------------------------------------\n")
    finally:
            GPIO.cleanup()

    return readRFID
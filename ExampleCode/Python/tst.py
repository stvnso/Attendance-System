#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()



try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
    

GPIO.cleanup()

150912046362	
948478422942

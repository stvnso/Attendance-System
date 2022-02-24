#/usr/bin/env python

from ast import While
import RPi.GPIO as GPIO
from numpy import False_
import drivers
from time import sleep
from Attendance_functions import *



while True:
    rfid_ID = readRFID_fromChip()

    check_user = is_user_checked_in(rfid_ID)

    if check_user == True:
        check_OUT(rfid_ID)
    elif check_user == False:
        check_IN(rfid_ID)
    else:
        print("user nicht am start")







    

  

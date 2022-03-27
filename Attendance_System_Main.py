#/usr/bin/env python

from time import sleep
from Attendance_System_Functions import *
from Alarm_System_Main import *

def attendance_Main():

    while True:
        rfid_ID = readRFID_fromChip()

        if does_user_exist(rfid_ID) == False:
            continue

        check_user = is_user_checked_in(rfid_ID)

        if check_user == True:
            check_OUT(rfid_ID)
        elif check_user == False:
            check_IN(rfid_ID)
        

attendance_Main()






    

  

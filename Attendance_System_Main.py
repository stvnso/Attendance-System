#/usr/bin/env python

import sys
from time import sleep
from Attendance_System_Functions import *
from Alarm_system import *

while True:
    rfid_ID = readRFID_fromChip()

    if does_user_exist(rfid_ID) == False:
        continue

    check_user = is_user_checked_in(rfid_ID)

    if check_user == True:
        check_OUT(rfid_ID)
    elif check_user == False:
        check_IN(rfid_ID)
    
    # if are_users_checked_in() == False:
    #     print("Keiner mehr da")
        
    #     main_function()
    #     exit()







    

  

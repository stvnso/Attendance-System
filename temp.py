from dis import dis
from multiprocessing import connection
from random import seed
import drivers
import sqlite3
import time
from Read_RFID_Chip import readRFID_fromChip
from SelectFromDB import *

display = drivers.Lcd()

def check_in():
    # Datenbankverbindung aufbauen + Cursor erstellen
    databaseConnection = sqlite3.connect('database/attendance-system.db')
    print("Datenbank verbunden: attendance")

    dbCursor = databaseConnection.cursor()
    print("Cursor erstellt")

    print("Bitte Chip anhalten")
    display.lcd_display_string("Bitte",1)
    display.lcd_display_string("Chip vorhalten",2)
    rfid = readRFID_fromChip()

    sql_update_query =  """Update attendance 
                            SET
                            date = strftime('%d-%m-%Y', 'now', 'localtime'),
                            check_in_time = time('now','localtime'),
                            checked_in = 1
                            where rfid_uid =?""" 
    dbCursor.execute(sql_update_query,(rfid,))
    databaseConnection.commit()

    user = readRFID_fromDatabase(rfid)
    
    display.lcd_display_string("Hi "  + user[2] + " " + user[3],1)
    display.lcd_display_string("Kommen: "  + user[7],2)
    time.sleep(4)

    display.lcd_clear()
    

    print("Successfully checked in user: " + user[2] + " " + user[3] )
    dbCursor.close()

check_in()
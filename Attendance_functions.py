#imports

#reader
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#database
from multiprocessing import connection
from random import seed
import sqlite3

#lcd
import drivers

#misc
from time import sleep
#-------------------------------------------------------------------

#VARIABLES
display = drivers.Lcd()

#-------------------------------------------------------------------


#-------------------------------------------------------------------


# DATABASE CONNECTION

# connect to database
database_Attendance = sqlite3.connect('database/attendance-system.db')


dbCursor = database_Attendance.cursor()
print("\nCreated Database Cursor \n")

try:
        # Datenbankverbindung aufbauen + Cursor erstellen
        database_Attendance = sqlite3.connect('database/attendance-system.db')
        print("Database connection successfull")

        dbCursor = database_Attendance.cursor()
        print("Created Cursor for Database")

except sqlite3.Error as error:
        print("Failed to connect to Database", error)



#-------------------------------------------------------------------


# FUNCTIONS


def close_db_connection():


    database_Attendance.close()
    print("Closed Database connection")

    dbCursor.close()
    print("Closed Database Cursor")

#-------------------------------------------------------------------


# returns RFID from Chip
def readRFID_fromChip():
    
    reader = SimpleMFRC522()

    display.lcd_display_string("Bitte",1)
    display.lcd_display_string("Chip vorhalten",2)
    print("Reading Chip..")

    try:
            id,secondId = reader.read()
            rfid_ID = str(id)
            print("\n-------------------------------------")
            print("RFID_UID:\t" + rfid_ID)
            print("-------------------------------------\n")
    finally:
            GPIO.cleanup()

    return rfid_ID

#-------------------------------------------------------------------

def read_Entry_fromDatabase_by_RFID(rfid_ID):

    #rfid_ID = readRFID_fromChip()

    # Datenbank SELECT Query mit gegebenem Parameter
    dbCursor.execute(
        "SELECT * FROM attendance WHERE rfid_uid=?", (rfid_ID,))
    print("Executing SELECT-Query for RFID:\t" + rfid_ID)

    # Daten im Array speichern
    selectedData = dbCursor.fetchall()
    print("Database Entry for RFID:\t" + rfid_ID)
    print("---------------------------")

    # Über Array iterieren und Einträge ausgeben
    for entry in selectedData:
        print("Id: \t\t\t", entry[0])
        print("RFID_UID: \t\t", entry[1])
        print("First-Name: \t\t", entry[2])
        print("Last-Name: \t\t", entry[3])
        print("Access-Level: \t\t", entry[4])
        print("Checked-IN: \t\t", entry[5])
        print("Date: \t\t\t", entry[6])
        print("Check-In-Time: \t\t", entry[7])
        print("Check-Out-Time: \t", entry[8])
        print("Daily-Working-Hours: \t", entry[9])
        print("Working-Time-Account: \t", entry[10])
        print("---------------------------")
        print("\n")

        return entry
#-------------------------------------------------------------------

def check_in():

    rfid_ID = readRFID_fromChip()

    sql_update_query =  """Update attendance 
                            SET
                            date = strftime('%d-%m-%Y', 'now', 'localtime'),
                            check_in_time = time('now','localtime'),
                            checked_in = 1
                            where rfid_uid =?""" 
    dbCursor.execute(sql_update_query,(rfid_ID,))
    database_Attendance.commit()

    
    user = read_Entry_fromDatabase_by_RFID(rfid_ID)

    print("Successfully checked in user: " + user[2] + " " + user[3] )

    first_name  = user[2]
    last_name = user[3]
    check_in_time = user[7]

    print("\nPrinting to Display..")
    display.lcd_display_string("Hi "  + first_name + " " + last_name,1)
    display.lcd_display_string("Kommen: "  + check_in_time,2)
    sleep(3)
    display.lcd_clear()

   
#check_in()
    
















#--------------------OLD / TEMP FUNCTIONS-----------------------------------------------

""" def create_db_Connection():
        print("blbb")

        # connect to database

        databaseConnection = sqlite3.connect('database/attendance-system.db')
        print("Database connection successfull")
        return databaseConnection


def create_db_Cursor(database = create_db_Connection()):       

        dbCursor = database.cursor()
        print("\nCreated Database Cursor \n")

        return dbCursor """

         

#imports

#reader
from re import S
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
# try:
#         # Datenbankverbindung aufbauen + Cursor erstellen
#         database_Attendance = sqlite3.connect('database/attendance-system.db')
#         print("Database connection successfull")

#         dbCursor = database_Attendance.cursor()
#         print("Created Cursor for Database")

# except sqlite3.Error as error:
#         print("Failed to connect to Database", error)



#-------------------------------------------------------------------


# FUNCTIONS

def execute_SQL_Query(sql_query,rfid_ID):
    try:
        # Datenbankverbindung aufbauen + Cursor erstellen
        database_Attendance = sqlite3.connect('database/attendance-system.db')
       # print("Database connection successfull")
        dbCursor = database_Attendance.cursor()

        dbCursor.execute(sql_query,(rfid_ID,))
        database_Attendance.commit()

        sql_query_result = dbCursor.fetchall()

        return sql_query_result

    except sqlite3.Error as error:
        print("Failed to connect to Database", error)


def create_db_connection():
    try:
        # Datenbankverbindung aufbauen + Cursor erstellen
        database_Attendance = sqlite3.connect('database/attendance-system.db')
        print("Database connection successfull")

        return database_Attendance

    except sqlite3.Error as error:
        print("Failed to connect to Database", error)


def create_db_cursor(database):
    dbCursor = database.cursor()
    return dbCursor


def close_db_connection(database,dbCursor):

    database.close()
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
            display.lcd_clear()
    finally:
            GPIO.cleanup()


    return rfid_ID

#-------------------------------------------------------------------
def does_user_exist(rfid_ID):

      # Datenbank SELECT Query mit gegebenem Parameter
    sql_query = """SELECT * FROM attendance WHERE rfid_uid=?"""

    # Daten im Array speichern
    selectedData = execute_SQL_Query(sql_query,rfid_ID)

    if len(selectedData) == 1:
        return True
    else:
        print("User does not exist")
        display.lcd_display_string("Fehler!",1)
        sleep(2)
        display.lcd_clear()

        display.lcd_display_string("ID ",1)
        display.lcd_display_string("Existiert nicht",2)
        sleep(3)
        display.lcd_clear()
        return False

#-------------------------------------------------------------------
def read_user_fromDatabase_by_RFID(rfid_ID):

    # Datenbank SELECT Query mit gegebenem Parameter
    sql_query = """SELECT * FROM attendance WHERE rfid_uid=?"""

    # Daten im Array speichern
    selectedData = execute_SQL_Query(sql_query,rfid_ID)

    print("Database Entry for RFID:\t" + rfid_ID)
    print("---------------------------")

    # Über Array iterieren und Einträge ausgeben
    for user_entry in selectedData:
        print("Id: \t\t\t", user_entry[0])
        print("RFID_UID: \t\t", user_entry[1])
        print("First-Name: \t\t", user_entry[2])
        print("Last-Name: \t\t", user_entry[3])
        print("Access-Level: \t\t", user_entry[4])
        print("Checked-IN: \t\t", user_entry[5])
        print("Date: \t\t\t", user_entry[6])
        print("Check-In-Time: \t\t", user_entry[7])
        print("Check-Out-Time: \t", user_entry[8])
        print("Daily-Working-Hours: \t", user_entry[9])
        print("Working-Time-Account: \t", user_entry[10])
        print("---------------------------")
        print("\n")

        return user_entry
#-------------------------------------------------------------------

def is_user_checked_in(rfid_ID):

    user = read_user_fromDatabase_by_RFID(rfid_ID)
    checked_in = user[5]

    if checked_in == 1:
        checked_in_status = True
    else:
        checked_in_status = False
    
    print("User: " + user[2] + " " + user[3] + " has checked_in status: " + str(checked_in_status))
    
    return checked_in_status
#-------------------------------------------------------------------

def check_IN(rfid_ID):

    sql_query =  """Update attendance 
                            SET
                            date = strftime('%d-%m-%Y', 'now', 'localtime'),
                            check_in_time = strftime('%H:%M', 'now', 'localtime'),
                            checked_in = 1
                            where rfid_uid =?""" 
  
    execute_SQL_Query(sql_query,rfid_ID)

    
    user = read_user_fromDatabase_by_RFID(rfid_ID)

    print("Successfully checked in user: " + user[2] + " " + user[3] )

    first_name  = user[2]
    last_name = user[3]
    check_in_time = user[7]
    working_time_account = user[11]

    print("\nPrinting to Display..")
    display.lcd_display_string("Hallo",1)
    display.lcd_display_string(first_name + " " + last_name,2)
    sleep(2)
    display.lcd_clear()
    display.lcd_display_string("Kommen: "  + str(check_in_time),1)
    display.lcd_display_string("Konto: "  + str(working_time_account)+ "h",2)
    sleep(3)
    display.lcd_clear()

#-------------------------------------------------------------------

def check_OUT(rfid_ID):
    
    sql_query = """UPDATE attendance
                    set 
                    checked_in = 0,
                    check_out_time = strftime('%H:%M', 'now', 'localtime'),
                    working_time_account = round(working_time_account - (daily_working_hours - ((strftime('%s',[check_out_time]) - strftime('%s',[check_in_time])*1.0)/3600)),2)
                    where rfid_uid =?;"""

    execute_SQL_Query(sql_query,rfid_ID)

    user = read_user_fromDatabase_by_RFID(rfid_ID)

    print("Successfully checked out user: " + user[2] + " " + user[3] )

    first_name  = user[2]
    last_name = user[3]
    check_out_time = user[8]
    working_time_account = user[11]

    print("\nPrinting to Display..")
    display.lcd_display_string("Auf Wiedersehen",1)
    display.lcd_display_string(first_name + " " + last_name,2)
    sleep(2)
    display.lcd_clear()
    display.lcd_display_string("Gehen: "  + str(check_out_time),1)
    display.lcd_display_string("Konto: "  + str(working_time_account)+ "h",2)
    sleep(3)
    display.lcd_clear()

 















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

         

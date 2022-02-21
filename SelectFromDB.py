from multiprocessing import connection
from random import seed
import sqlite3
from Read_RFID_Chip import readRFID_fromChip


# Funktion liest mit übergebenem Parameter den Datenbankeintrag passend zu RFID_UID
# und gibt das Ergebnis dann aus

def readRFID_fromDatabase(RFID_UID):

    readRFID = RFID_UID
    try:

        # Datenbankverbindung aufbauen + Cursor erstellen
        databaseConnection = sqlite3.connect('database/attendance-system.db')
        dbCursor = databaseConnection.cursor()
        print("\nConnected to SQLite Database: attendance-system \n")

        # Datenbank SELECT Query mit gegebenem Parameter
        dbCursor.execute(
            "SELECT * FROM attendance WHERE rfid_uid=?", (readRFID,))
        print("Executing SELECT-Query")

        # Daten im Array speichern
        selectedData = dbCursor.fetchall()
        print("DATA")
        print("---------------------------")
        # Über Array iterieren und Einträge ausgeben
        for row in selectedData:
            print("Id: \t\t\t", row[0])
            print("RFID_UID: \t\t", row[1])
            print("First-Name: \t\t", row[2])
            print("Last-Name: \t\t", row[3])
            print("Access-Level: \t\t", row[4])
            print("Checked-IN: \t\t", row[5])
            print("Date: \t\t\t", row[6])
            print("Check-In-Time: \t\t", row[7])
            print("Check-Out-Time: \t", row[8])
            print("Daily-Working-Hours: \t", row[9])
            print("Working-Time-Account: \t", row[10])
            print("---------------------------")
            print("\n")

            return row

        dbCursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if databaseConnection:
            databaseConnection.close()
            print("The SQLite connection is closed")


def create_db_connection():

    try:
        # Datenbankverbindung aufbauen + Cursor erstellen
        databaseConnection = sqlite3.connect('database/attendance-system.db')
        dbCursor = databaseConnection.cursor()
        print("\nConnected to SQLite Database: attendance-system \n")

        return dbCursor

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if databaseConnection:
            databaseConnection.close()
            print("The SQLite connection is closed")


def check_in(RFID_UID):

    readRFID = RFID_UID

    dbCursor = create_db_connection()

    dbCursor.execute("""UPDATE attendance
                     set 
	                    date = strftime('%d-%m-%Y', 'now', 'localtime'),
                        check_in_time = time('now','localtime'),
	                    checked_in = 1
                        WHERE rfid_uid=?""", (readRFID))

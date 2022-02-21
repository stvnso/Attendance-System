from multiprocessing import connection
from random import seed
import sqlite3
from Read_RFID_Chip import readRFID_fromChip


readRFID = 948478422942
# Datenbankverbindung aufbauen + Cursor erstellen
databaseConnection = sqlite3.connect('database/attendance-system.db')
dbCursor = databaseConnection.cursor()
print("\nConnected to SQLite Database: attendance-system \n")

# Datenbank SELECT Query mit gegebenem Parameter
# dbCursor.execute(
#     "SELECT * FROM attendance WHERE rfid_uid=?", (readRFID,))
# print("Executing SELECT-Query")

sqlvar = 2

sql_update_query = """Update attendance set checked_in = 1 where id =?""" 
dbCursor.execute(sql_update_query,(sqlvar,))
databaseConnection.commit()
print("Record Updated successfully ")
dbCursor.close()

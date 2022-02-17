from multiprocessing import connection
import sqlite3

#Connect to database
connection = sqlite3.connect('database/attendance-system.db')

#create Cursor
c = connection.cursor()

#c.execute('CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY AUTOINCREMENT,)')
c.execute("CREATE TABLE attendance(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  rfid_uid INTEGER NOT NULL, 
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  access_level INTEGER DEFAULT 1 CHECK(access_level IN (1,3)),
  checked_in INTEGER DEFAULT 0 CHECK(checked_in IN (0,1)),
  date DATETIME DEFAULT (strftime('%d-%m-%Y', 'now', 'localtime')),
  check_in_time DATETIME,
  check_out_time DATETIME ,
  daily_working_hours real default 8.0,
  working_time_account Real DEFAULT 0 );")

 

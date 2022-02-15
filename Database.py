from multiprocessing import connection
import sqlite3

#Connect to database
connection = sqlite3.connect('database/attendance-system.db')

#create Cursor
c = connection.cursor()

#c.execute('CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY AUTOINCREMENT,)')
c.execute('CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)')

CREATE TABLE "attendance" (
	"id"	INTEGER,
	"rfid-user-id"	INTEGER NOT NULL UNIQUE,
	"first-name"	NUMERIC NOT NULL,
	"last-name"	TEXT NOT NULL,
	"access-level"	INTEGER NOT NULL DEFAULT 1 CHECK(access-level IN(1,3)),
	"date"	TEXT,
	"id-checked-in"	INTEGER DEFAULT 0 CHECK(id-checked-in IN(0,1)),
	"check-in-time"	TEXT,
	"check-out-time"	TEXT,
	"working-time-account"	REAL DEFAULT 0,
	"daily-working-hours"	REAL DEFAULT 8,
	PRIMARY KEY("id" AUTOINCREMENT)
);
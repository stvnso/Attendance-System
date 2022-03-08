-- Tabelle erzeugen
CREATE TABLE attendance(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  rfid_uid INTEGER NOT NULL, 
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  access_level INTEGER DEFAULT 1 CHECK(access_level IN (0,1,2,3)),
  checked_in INTEGER DEFAULT 0 CHECK(checked_in IN (0,1)),
  date DATETIME DEFAULT (strftime('%d-%m-%Y', 'now', 'localtime')),
  check_in_time TIME,
  check_out_time TIME,
  daily_working_hours real default 8.0,
  working_time_account Real DEFAULT 0 );

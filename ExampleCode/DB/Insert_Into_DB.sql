-- SQLite

--  SQL Befehl zum Einfügen eines Datensatzes

INSERT INTO attendance(
    rfid_uid, 
    first_name,
    last_name,
    access_level,
    checked_in,
    date,
    check_in_time,
    check_out_time,
    daily_working_hours,
    working_time_account)
    
VALUES(
  702208545323,
  'Eric',
  'Solo',
   2,
   0,
   strftime('%d-%m-%Y', 'now', 'localtime'),
   time('now','localtime'),
   null,
   8.0,
   0);	

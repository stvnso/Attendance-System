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
    hours_worked,
    working_time_account)
    
VALUES(
  083208235022,
  'Test',
  'Test',
   2,
   0,
   strftime('%d-%m-%Y', 'now', 'localtime'),
   time('now','localtime'),
   null,
   8.0,
   0,
   0);	

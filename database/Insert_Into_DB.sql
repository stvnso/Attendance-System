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
  150912046362,
  'Janik',
  'Becker',
   1,
   0,
   strftime('%d-%m-%Y', 'now', 'localtime'),
   strftime('%H:%M:%S', 'now', 'localtime'),
   null,
   8.0,
   0);	

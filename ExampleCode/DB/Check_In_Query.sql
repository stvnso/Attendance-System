UPDATE attendance
set 
	date = strftime('%d-%m-%Y', 'now', 'localtime'),
    check_in_time = time('now','localtime'),
	checked_in = 1
WHERE id = 1
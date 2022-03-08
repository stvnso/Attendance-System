-- Query für CHECK OUT
UPDATE attendance
set 
	checked_in = 0,
    check_out_time = time("now", "localtime"),
where id = 2


UPDATE attendance
SET working_time_account = round(working_time_account - (daily_working_hours - ((strftime('%s',[check_out_time]) - strftime('%s',[check_in_time])*1.0)/3600)),2)
where rfid_uid

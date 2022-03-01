UPDATE attendance
SET
check_in_time = strftime('%H:%M', 'now', 'localtime'),
check_out_time = null,
hours_worked = 0,
working_time_account = 0;

UPDATE attendance
SET
checked_in = 0,
hours_worked = 0,
working_time_account = 0;


UPDATE attendance
SET
check_out_time = time('now','localtime')

UPDATE attendance
SET
check_out_time = strftime('%H:%M', 'now', 'localtime')

-- SQLite
SELECT

round(working_time_account - (daily_working_hours - ((strftime('%s',[check_out_time]) - strftime('%s',[check_in_time])*1.0)/3600)),2)

from attendance
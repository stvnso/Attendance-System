
-- SQLite
SELECT

round(working_time_account - (daily_working_hours - ((strftime('%s',[check_out_time]) - strftime('%s',[check_in_time])*1.0)/3600)),2)

from attendance


SELECT

working_time_account - (daily_working_hours - ((strftime('%s',[check_out_time]) - strftime('%s',[check_in_time])*1.0)/3600))

from attendance
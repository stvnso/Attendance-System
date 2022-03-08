UPDATE attendance
SET
checked_in = 0,
check_in_time = null,
check_out_time = null,
hours_worked = 0,
working_time_account = 0;

-- RESET working_time_account all users
UPDATE attendance
SET
working_time_account = 0;



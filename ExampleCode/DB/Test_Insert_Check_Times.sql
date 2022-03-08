-- TEST CHECK IN 
UPDATE attendance
SET
check_in_time = time('08:00:00','+0 hours')
WHERE id = 1;

-- TEST CHECK OUT  PLUS HOURS
UPDATE attendance
SET
check_out_time = time('08:00:00','+9 hours','localtime')
WHERE id = 5

-- TEST CHECK OUT  MINUS HOURS

UPDATE attendance
SET
check_out_time = time('08:00:00','+5 hours','localtime')
WHERE id = 1
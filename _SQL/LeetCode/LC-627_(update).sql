# https://leetcode.com/problems/swap-salary/

UPDATE Salary
# SET sex = IF(sex = 'f', 'm', 'f');
SET sex =
CASE
    WHEN sex = 'f' THEN 'm'
    ELSE 'f'
END;

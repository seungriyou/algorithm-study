# https://leetcode.com/problems/swap-salary/

UPDATE Salary
# SET sex = IF(sex = 'f', 'm', 'f');
SET sex =
CASE
    WHEN sex = 'f' THEN 'm'
    ELSE 'f'
END;

# ===== (23.12.17) reviewed =====
# UPDATE / SET / WHERE
UPDATE Salary
SET sex = IF(sex = 'm', 'f', 'm');

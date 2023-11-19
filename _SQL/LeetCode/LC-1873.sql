# https://leetcode.com/problems/calculate-special-bonus/

# bonus = 100% of salary if..
# 1. employee_id 가 odd num
# 2. name 이 'M'으로 시작하지 X
# 그 외에는 bonus = 0
SELECT
    employee_id,
    # IF(employee_id % 2 = 1 AND LEFT(name, 1) <> 'M', salary, 0) AS bonus
    IF(employee_id % 2 = 1 AND name NOT LIKE 'M%', salary, 0) AS bonus
FROM Employees
ORDER BY 1;

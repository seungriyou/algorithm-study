# https://leetcode.com/problems/second-highest-salary/

# SELECT LEAD(salary) OVER (ORDER BY salary DESC) AS SecondHighestSalary
# FROM (
#     SELECT DISTINCT salary
#     FROM Employee
#     ORDER BY salary DESC
#     LIMIT 2
# ) AS T
# LIMIT 1;

# SELECT MAX(salary) AS SecondHighestSalary
# FROM Employee
# WHERE salary < (SELECT MAX(salary) FROM Employee);

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1, 1
) AS SecondHighestSalary;

# ===== (23.12.16) reviewed =====
# (1) subquery
SELECT (
    SELECT salary
    FROM (
        SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS _rank
        FROM Employee
    ) E
    WHERE _rank = 2
) AS SecondHighestSalary;

# (2) limit & offset
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

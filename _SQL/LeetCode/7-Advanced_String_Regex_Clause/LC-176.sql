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

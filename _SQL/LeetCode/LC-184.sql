# https://leetcode.com/problems/department-highest-salary/

# sol1
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee E
INNER JOIN Department D ON E.departmentId = D.id
WHERE (E.salary, E.departmentId) IN (
    SELECT MAX(salary), departmentId
    FROM Employee
    GROUP BY departmentId
);

# sol2
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM (
    SELECT
        *
        , RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS '_rank'
    FROM Employee
) E
INNER JOIN Department D ON E.departmentId = D.id
WHERE E._rank = 1

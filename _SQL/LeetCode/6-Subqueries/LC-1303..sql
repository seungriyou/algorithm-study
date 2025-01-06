-- https://leetcode.com/problems/find-the-team-size/

-- subquery & join
SELECT employee_id, team_size
FROM Employee
INNER JOIN (
    SELECT team_id, COUNT(*) AS team_size
    FROM Employee
    GROUP BY team_id
) T USING(team_id);

-- window function
SELECT
    employee_id,
    COUNT(employee_id) OVER (PARTITION BY team_id) AS team_size
FROM Employee;

# https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

# (1) employee_id (manager id) & name
# (2) reports_count : group by reports_to -> count()
# (3) average_age : group by reports_to -> avg() -> 반올림

SELECT M.employee_id, M.name, COUNT(*) AS reports_count, ROUND(AVG(E.age)) AS average_age
FROM Employees E
INNER JOIN Employees M ON E.reports_to = M.employee_id
GROUP BY E.reports_to
ORDER BY M.employee_id;

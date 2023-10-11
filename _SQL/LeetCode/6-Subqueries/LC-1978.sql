# https://leetcode.com/problems/employees-whose-manager-left-the-company/

# (1) salary < 30000
# (2) manager info removed from Employees
# order by employee_id

# SELECT E.employee_id
# FROM Employees E
# LEFT JOIN Employees M ON E.manager_id = M.employee_id
# WHERE E.manager_id IS NOT NULL AND M.employee_id is NULL AND E.salary < 30000
# ORDER BY E.employee_id;

SELECT employee_id
FROM Employees
WHERE manager_id NOT IN (SELECT employee_id FROM Employees) AND salary < 30000
ORDER BY employee_id;

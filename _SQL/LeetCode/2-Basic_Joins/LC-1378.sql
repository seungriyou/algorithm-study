# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
SELECT A.unique_id, B.name
FROM EmployeeUNI A
RIGHT JOIN Employees B ON B.id = A.id;

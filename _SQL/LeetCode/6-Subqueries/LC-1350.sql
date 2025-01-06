-- https://leetcode.com/problems/students-with-invalid-departments/

-- left join
SELECT s.id, s.name
FROM Students s
LEFT JOIN Departments d ON s.department_id = d.id
WHERE d.id IS NULL;

-- subquery
SELECT id, name
FROM Students
WHERE department_id NOT IN (
    SELECT DISTINCT id
    FROM Departments
);

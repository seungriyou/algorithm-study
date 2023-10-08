# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
);

# SELECT M.name
# FROM Employee E
# INNER JOIN Employee M ON E.managerId = M.id
# GROUP BY E.managerId
# HAVING COUNT(E.managerId) >= 5;

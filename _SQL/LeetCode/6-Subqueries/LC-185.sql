# https://leetcode.com/problems/department-top-three-salaries/

# -- DENSE_RANK()를 WHERE 조건으로 보고싶다면, SELECT 절에서 아예 CASE 문으로 처리
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM (
    SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS _rank
    FROM Employee
) AS E
INNER JOIN Department D ON E.departmentId = D.id
WHERE E._rank <= 3;

# SELECT D.name AS Department, E1.name AS Employee, E1.salary AS Salary
# FROM Employee E1
# INNER JOIN Department D ON E1.departmentId = D.id
# WHERE (
#     SELECT COUNT(DISTINCT E2.salary)
#     FROM Employee E2
#     WHERE E2.salary > E1.salary AND E2.departmentId = E1.departmentId
# ) < 3;  # -- 같은 department에서 자신의 salary 보다 높은 salary가 0~2개 존재해야 top3 임!

# ===== (23.12.15) reviewed =====
# (1) window function
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS _rank
    FROM Employee
) E
INNER JOIN Department D ON E.departmentId = D.id
WHERE E._rank <= 3;

# (2) join
SELECT D.name AS Department, E1.name AS Employee, E1.salary AS Salary
FROM Employee E1
INNER JOIN Department D ON E1.departmentId = D.id
WHERE (
    SELECT COUNT(DISTINCT E2.salary)
    FROM Employee E2
    WHERE E1.departmentId = E2.departmentId AND E2.salary > E1.salary
) < 3;

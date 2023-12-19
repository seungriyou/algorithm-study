# https://leetcode.com/problems/employees-with-missing-information/

# ===== (E - S) ∪ (S - E) =====
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Salaries
)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Employees
)
ORDER BY 1;


# ===== FULL OUTER JOIN =====
# MySQL은 FULL OUTER JOIN을 native 하게 지원하지 않으므로 다음과 같이 구현!
SELECT employee_id
FROM (
    SELECT employee_id, name, salary FROM Employees LEFT JOIN Salaries USING(employee_id)
    UNION
    SELECT employee_id, name, salary FROM Employees RIGHT JOIN Salaries USING(employee_id)
) T
WHERE name IS NULL OR salary IS NULL
ORDER BY 1;


# ===== (23.12.19) reviewed =====
# (1) full outer join
SELECT employee_id
FROM (
    SELECT *
    FROM Employees
    LEFT JOIN Salaries USING(employee_id)
    UNION
    SELECT employee_id, name, salary
    FROM Employees
    RIGHT JOIN Salaries USING(employee_id)
) T
WHERE name IS NULL OR salary IS NULL
ORDER BY 1;

# (2) (E - S) ∪ (S - E)
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Salaries
)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Employees
)
ORDER BY 1;

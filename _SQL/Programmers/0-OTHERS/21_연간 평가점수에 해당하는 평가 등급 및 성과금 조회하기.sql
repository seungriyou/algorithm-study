# https://school.programmers.co.kr/learn/courses/30/lessons/284528
# sol1
SELECT
    E.emp_no,
    E.emp_name,
    (CASE
        WHEN AVG(score) >= 96 THEN 'S'
        WHEN AVG(score) >= 90 THEN 'A'
        WHEN AVG(score) >= 80 THEN 'B'
        ELSE 'C'
    END) AS grade,
    (CASE
        WHEN AVG(score) >= 96 THEN E.sal * 0.2
        WHEN AVG(score) >= 90 THEN E.sal * 0.15
        WHEN AVG(score) >= 80 THEN E.sal * 0.1
        ELSE 0
    END) AS bonus
FROM HR_EMPLOYEES E
INNER JOIN HR_GRADE G USING (emp_no)
GROUP BY 1
ORDER BY 1;

# sol2
SELECT
    E.emp_no,
    emp_name,
    grade,
    (CASE
        WHEN grade = 'S' THEN sal * 0.2
        WHEN grade = 'A' THEN sal * 0.15
        WHEN grade = 'B' THEN sal * 0.1
        ELSE 0
    END) AS bonus
FROM HR_EMPLOYEES E
INNER JOIN (
    SELECT
        emp_no,
        (CASE
            WHEN AVG(score) >= 96 THEN 'S'
            WHEN AVG(score) >= 90 THEN 'A'
            WHEN AVG(score) >= 80 THEN 'B'
            ELSE 'C'
        END) AS grade
    FROM HR_GRADE
    GROUP BY 1
) G USING(emp_no)
ORDER BY 1;

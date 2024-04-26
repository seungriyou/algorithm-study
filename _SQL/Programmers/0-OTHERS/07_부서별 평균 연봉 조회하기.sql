# https://school.programmers.co.kr/learn/courses/30/lessons/284529
SELECT D.dept_id, D.dept_name_en, E.avg_sal
FROM HR_DEPARTMENT AS D
INNER JOIN (
    SELECT dept_id, ROUND(AVG(sal)) AS avg_sal
    FROM HR_EMPLOYEES
    GROUP BY dept_id
) AS E USING(dept_id)
ORDER BY 3 DESC;

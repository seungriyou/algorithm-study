# https://school.programmers.co.kr/learn/courses/30/lessons/284527
# 2022년도 평가 점수(= 상+하반기 점수) 가장 높은 사원 정보
SELECT score, G.emp_no, emp_name, position, email
FROM (
    SELECT emp_no, SUM(score) AS score
    FROM HR_GRADE
    WHERE year = 2022
    GROUP BY emp_no
    ORDER BY 2 DESC
    LIMIT 1
) AS G
INNER JOIN HR_EMPLOYEES E ON G.emp_no = E.emp_no;

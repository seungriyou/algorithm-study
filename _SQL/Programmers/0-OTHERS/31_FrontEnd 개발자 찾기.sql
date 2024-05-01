# https://school.programmers.co.kr/learn/courses/30/lessons/276035
SELECT id, email, first_name, last_name
FROM DEVELOPERS
WHERE skill_code & (
    SELECT SUM(code) AS code
    FROM SKILLCODES
    WHERE category = 'Front End'
)
ORDER BY 1;

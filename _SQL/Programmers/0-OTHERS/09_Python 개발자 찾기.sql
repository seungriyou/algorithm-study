# https://school.programmers.co.kr/learn/courses/30/lessons/276013
SELECT id, email, first_name, last_name
FROM DEVELOPER_INFOS
WHERE skill_1 = 'Python' OR skill_2 = 'Python' OR skill_3 = 'Python'
ORDER BY 1;

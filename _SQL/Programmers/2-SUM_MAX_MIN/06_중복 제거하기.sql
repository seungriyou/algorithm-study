# https://school.programmers.co.kr/learn/courses/30/lessons/59408

SELECT COUNT(DISTINCT name) AS count
FROM ANIMAL_INS
WHERE name IS NOT NULL;

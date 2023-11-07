# https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT name, COUNT(name) AS 'count' -- COUNT(*)로 하면 X (이름이 없는 동물은 집계에서 제외)
FROM ANIMAL_INS
GROUP BY name
HAVING count >= 2
ORDER BY name;

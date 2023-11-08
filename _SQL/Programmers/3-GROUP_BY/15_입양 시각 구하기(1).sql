# https://school.programmers.co.kr/learn/courses/30/lessons/59412

SELECT HOUR(datetime) AS hour, COUNT(animal_id) AS 'count'
FROM ANIMAL_OUTS
WHERE HOUR(datetime) BETWEEN 9 AND 19
GROUP BY hour
ORDER BY 1;

# https://school.programmers.co.kr/learn/courses/30/lessons/59411

SELECT O.animal_id, O.name
FROM ANIMAL_OUTS O
INNER JOIN ANIMAL_INS I ON O.animal_id = I.animal_id
ORDER BY DATEDIFF(O.datetime, I.datetime) DESC
LIMIT 2;

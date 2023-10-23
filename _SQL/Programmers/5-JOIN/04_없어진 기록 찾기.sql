# https://school.programmers.co.kr/learn/courses/30/lessons/59042

SELECT O.animal_id, O.name
FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I ON O.animal_id = I.animal_id
WHERE I.animal_id IS NULL;

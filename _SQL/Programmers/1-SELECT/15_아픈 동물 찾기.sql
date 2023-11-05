# https://school.programmers.co.kr/learn/courses/30/lessons/59036

SELECT animal_id, name
FROM ANIMAL_INS
WHERE intake_condition = 'Sick'
ORDER BY animal_id;

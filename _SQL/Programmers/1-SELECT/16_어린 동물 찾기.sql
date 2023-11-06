# https://school.programmers.co.kr/learn/courses/30/lessons/59037

SELECT animal_id, name
FROM ANIMAL_INS
WHERE intake_condition <> 'Aged'
ORDER BY animal_id;

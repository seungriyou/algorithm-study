# https://school.programmers.co.kr/learn/courses/30/lessons/59410

SELECT animal_type, COALESCE(name, 'No name') AS name, sex_upon_intake
FROM ANIMAL_INS
ORDER BY animal_id;

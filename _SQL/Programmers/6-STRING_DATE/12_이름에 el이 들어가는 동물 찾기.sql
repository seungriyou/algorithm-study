# https://school.programmers.co.kr/learn/courses/30/lessons/59047

SELECT animal_id, name
FROM ANIMAL_INS
WHERE LOWER(name) LIKE '%el%' AND animal_type = 'Dog'
ORDER BY LOWER(name);

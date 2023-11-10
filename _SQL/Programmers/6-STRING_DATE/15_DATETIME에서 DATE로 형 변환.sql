# https://school.programmers.co.kr/learn/courses/30/lessons/59414

SELECT animal_id, name, DATE_FORMAT(datetime, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY 1;

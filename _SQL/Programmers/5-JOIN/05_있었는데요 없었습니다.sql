# https://school.programmers.co.kr/learn/courses/30/lessons/59043

SELECT I.animal_id, I.name
FROM ANIMAL_INS I
INNER JOIN ANIMAL_OUTS O USING(animal_id)
WHERE I.datetime > O.datetime
ORDER BY I.datetime;

# https://school.programmers.co.kr/learn/courses/30/lessons/59044

SELECT name, datetime
FROM ANIMAL_INS
WHERE animal_id NOT IN (
    SELECT animal_id
    FROM ANIMAL_OUTS
)
ORDER BY datetime
LIMIT 3;

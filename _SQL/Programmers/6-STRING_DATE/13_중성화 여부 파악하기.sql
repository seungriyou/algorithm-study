# https://school.programmers.co.kr/learn/courses/30/lessons/59409

SELECT
    animal_id
    , name
    , IF(sex_upon_intake LIKE '%Neutered%' OR sex_upon_intake LIKE '%Spayed%', 'O', 'X') AS '중성화'
FROM ANIMAL_INS
ORDER BY 1;

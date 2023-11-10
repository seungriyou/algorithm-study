# https://school.programmers.co.kr/learn/courses/30/lessons/59045

SELECT I.animal_id, I.animal_type, I.name
FROM ANIMAL_INS I
INNER JOIN ANIMAL_OUTS O USING(animal_id)
WHERE
    I.sex_upon_intake LIKE 'Intact%' AND
    (O.sex_upon_outcome LIKE 'Spayed%' OR O.sex_upon_outcome LIKE 'Neutered%')
ORDER BY 1;

# https://school.programmers.co.kr/learn/courses/30/lessons/59040

SELECT animal_type, COUNT(*) AS 'count'
FROM ANIMAL_INS
WHERE animal_type IN ('Cat', 'Dog')
GROUP BY animal_type
ORDER BY animal_type;

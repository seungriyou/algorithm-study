# https://school.programmers.co.kr/learn/courses/30/lessons/59413

WITH RECURSIVE HOUR_TABLE AS
(
    SELECT 0 AS hour
    UNION ALL
    SELECT hour + 1 FROM HOUR_TABLE WHERE hour < 23
)

SELECT H.hour, COUNT(A.animal_id) AS count
FROM ANIMAL_OUTS A
RIGHT JOIN HOUR_TABLE H ON H.hour = HOUR(A.datetime)
GROUP BY 1
ORDER BY 1;

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

# ===== (23.11.23) REVIEWED =====
SELECT hour, COALESCE(cnt, 0) as count
FROM HOURS H
LEFT JOIN (
    SELECT HOUR(datetime) AS hour, COUNT(animal_id) AS cnt
    FROM ANIMAL_OUTS
    GROUP BY 1
) A USING (hour)
ORDER BY 1;

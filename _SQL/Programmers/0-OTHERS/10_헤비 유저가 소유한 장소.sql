# https://school.programmers.co.kr/learn/courses/30/lessons/77487
SELECT *
FROM PLACES
WHERE host_id IN (
    SELECT host_id
    FROM PLACES
    GROUP BY host_id
    HAVING COUNT(id) >= 2
)
ORDER BY 1;

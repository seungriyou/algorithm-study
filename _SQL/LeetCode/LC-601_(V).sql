# https://leetcode.com/problems/human-traffic-of-stadium/

WITH Grouped_Stadium AS (
    SELECT id, visit_date, people, id - ROW_NUMBER() OVER (ORDER BY id) AS _group   # -- 연달아 등장하는 group을 세기 위해 `id - ROW_NUMBER()`를 이용!
    FROM Stadium
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM Grouped_Stadium
WHERE _group IN (
    SELECT _group
    FROM Grouped_Stadium
    GROUP BY _group
    HAVING COUNT(id) >= 3
);

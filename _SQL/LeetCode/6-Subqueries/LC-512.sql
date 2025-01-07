-- https://leetcode.com/problems/game-play-analysis-ii/

-- subquery
SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
);

-- window function (RANK())
SELECT player_id, device_id
FROM (
    SELECT
        player_id,
        device_id,
        RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS _rank
    FROM Activity
) T
WHERE _rank = 1;

-- window function (FIRST_VALUE())
SELECT
    DISTINCT player_id,
    FIRST_VALUE(device_id) OVER (PARTITION BY player_id ORDER BY event_date) AS device_id
FROM Activity;

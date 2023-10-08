# https://leetcode.com/problems/game-play-analysis-iv/

# SELECT ROUND(COUNT(C.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
# FROM (
#     SELECT player_id
#     FROM Activity
#     WHERE (player_id, event_date) IN (
#         SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY) AS next_date
#         FROM Activity
#         GROUP BY player_id
#     )
# ) AS C;

SELECT ROUND(COUNT(player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction    # -- COUNT() 안에 DISTINCT를 써도 된다.
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
    FROM Activity
    GROUP BY player_id
);

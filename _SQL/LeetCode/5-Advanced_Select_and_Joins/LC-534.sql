-- https://leetcode.com/problems/game-play-analysis-iii/

-- window function
SELECT
    player_id,
    event_date,
    SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
FROM Activity;

-- self join
SELECT a2.player_id, a2.event_date, SUM(a1.games_played) AS games_played_so_far
FROM Activity a1
INNER JOIN Activity a2 ON a1.player_id = a2.player_id AND a1.event_date <= a2.event_date
GROUP BY 1, 2;

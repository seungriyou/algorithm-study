# https://leetcode.com/problems/restaurant-growth/ (** TO BE REVIEWED)

WITH C AS (
    SELECT visited_on, SUM(amount) AS day_amount
    FROM Customer
    GROUP BY visited_on
)

SELECT C1.visited_on, SUM(C2.day_amount) AS amount, ROUND(SUM(C2.day_amount) / 7, 2) AS average_amount
FROM C C1, C C2
WHERE
    C1.visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
    AND DATEDIFF(C1.visited_on, C2.visited_on) BETWEEN 0 AND 6
GROUP BY C1.visited_on
ORDER BY C1.visited_on;
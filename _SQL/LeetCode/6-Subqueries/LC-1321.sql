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


# ===== (23.12.09) reviewed =====
# ===== w/o window function, w/ join =====
WITH DAILY_AMOUNT AS (
    SELECT visited_on, SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY 1
)

SELECT
    D1.visited_on,
    SUM(D2.daily_amount) AS amount,
    ROUND(SUM(D2.daily_amount) / 7, 2) AS average_amount
FROM DAILY_AMOUNT D1, DAILY_AMOUNT D2
WHERE
    D1.visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM DAILY_AMOUNT), INTERVAL 6 DAY) AND   # -- 최소 visited_on으로부터 6일 후 날짜부터만
    DATEDIFF(D1.visited_on, D2.visited_on) BETWEEN 0 AND 6  # -- D1.visited_on에 대해 0~6일전 D2.visited_on만 남기기
GROUP BY 1
ORDER BY 1;

# ===== w/ window function =====
SELECT
    visited_on,
    amount,
    ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT
        DISTINCT visited_on,
        SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount
    FROM Customer
) C
WHERE visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
ORDER BY 1;

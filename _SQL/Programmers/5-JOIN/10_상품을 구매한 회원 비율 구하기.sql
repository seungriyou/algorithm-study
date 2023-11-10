# https://school.programmers.co.kr/learn/courses/30/lessons/131534

# 조건에 맞는 ID 기반으로 counting 할 때는 DISTINCT를 잊지 말자!!

SELECT
    YEAR(sales_date) AS year
    , MONTH(sales_date) AS month
    , COUNT(DISTINCT user_id) AS purchased_users
    , ROUND(
        COUNT(DISTINCT user_id) / (
            SELECT COUNT(DISTINCT user_id)
            FROM USER_INFO
            WHERE YEAR(joined) = '2021'
        ), 1
    ) AS purchased_ratio
FROM ONLINE_SALE
WHERE user_id IN (
    SELECT DISTINCT user_id
    FROM USER_INFO
    WHERE YEAR(joined) = '2021'
)
GROUP BY 1, 2
ORDER BY 1, 2;

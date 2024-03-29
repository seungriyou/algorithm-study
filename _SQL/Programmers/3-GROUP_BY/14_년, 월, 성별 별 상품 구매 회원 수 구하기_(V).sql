# https://school.programmers.co.kr/learn/courses/30/lessons/131532

SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, gender, COUNT(DISTINCT U.user_id) AS users -- distinct...!!
FROM ONLINE_SALE O
INNER JOIN USER_INFO U ON O.user_id = U.user_id
WHERE U.gender IS NOT NULL
GROUP BY YEAR(sales_date), MONTH(sales_date), gender
ORDER BY 1, 2, 3;


# ===== (23.11.22) reviewed =====
SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, gender, COUNT(DISTINCT user_id) AS users   # -- DISTINCT!
FROM ONLINE_SALE LEFT JOIN USER_INFO USING (user_id)
WHERE gender IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3;

# https://leetcode.com/problems/market-analysis-i/
# ===== w/ subquery =====
SELECT U.user_id AS buyer_id, U.join_date, COALESCE(O._orders, 0) AS orders_in_2019
FROM Users U
LEFT JOIN (
    SELECT buyer_id, COUNT(order_id) AS _orders
    FROM Orders
    WHERE YEAR(order_date) = '2019'
    GROUP BY 1
) O ON U.user_id = O.buyer_id;

# ===== w/o subquery =====
SELECT
    U.user_id AS buyer_id,
    U.join_date,
    COALESCE(SUM(YEAR(O.order_date) = '2019'), 0) AS orders_in_2019
FROM Users U
LEFT JOIN Orders O ON U.user_id = O.buyer_id
GROUP BY 1;

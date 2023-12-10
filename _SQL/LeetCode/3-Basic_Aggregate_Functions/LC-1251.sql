# https://leetcode.com/problems/average-selling-price/

SELECT P.product_id, IFNULL(ROUND(SUM(P.price * U.units) / SUM(U.units), 2), 0) AS average_price
FROM Prices P
LEFT JOIN UnitsSold U ON P.product_id = U.product_id AND (U.purchase_date BETWEEN P.start_date AND P.end_date)
GROUP BY P.product_id;

# ===== (23.12.10) reviewed =====
SELECT P.product_id, COALESCE(ROUND(SUM(units * price) / SUM(units), 2), 0) AS average_price
FROM Prices P
LEFT JOIN UnitsSold U
    ON U.product_id = P.product_id
    AND U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY 1;

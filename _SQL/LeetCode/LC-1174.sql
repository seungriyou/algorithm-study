# https://leetcode.com/problems/immediate-food-delivery-ii/

# === 다음과 같이 하면 GROUP BY 시, MIN(order_date)에 대응되는 customer_pref_delivery_date가 SELECT 되는 것이 아니므로 X ===
# SELECT ROUND(AVG(D.first_order_date = D.customer_pref_delivery_date) * 100, 2) AS immediate_percentage
# FROM (
#     SELECT MIN(order_date) AS first_order_date, customer_pref_delivery_date
#     FROM Delivery
#     GROUP BY customer_id
# ) AS D;


SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) AS first_order
    FROM Delivery
    GROUP BY customer_id
);

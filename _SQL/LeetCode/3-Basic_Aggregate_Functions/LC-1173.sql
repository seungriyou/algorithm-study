-- https://leetcode.com/problems/immediate-food-delivery-i/

SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM delivery;

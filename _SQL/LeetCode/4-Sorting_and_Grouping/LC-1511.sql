-- https://leetcode.com/problems/customer-order-frequency/

-- sol1
SELECT customer_id, name
FROM customers
    JOIN orders USING(customer_id)
    JOIN product USING(product_id)
WHERE YEAR(order_date) = 2020
GROUP BY customer_id
HAVING
    SUM(IF(MONTH(order_date) = 6, quantity, 0) * price) >= 100 AND
    SUM(IF(MONTH(order_date) = 7, quantity, 0) * price) >= 100;

-- sol2
SELECT customer_id, name
FROM customers
    JOIN orders USING(customer_id)
    JOIN product USING(product_id)
GROUP BY customer_id
HAVING
    SUM((LEFT(order_date, 7) = '2020-06') * quantity * price) >= 100 AND
    SUM((LEFT(order_date, 7) = '2020-07') * quantity * price) >= 100;

-- sol3
SELECT customer_id, name
FROM (
    SELECT
        o.customer_id,
        MONTH(o.order_date) AS month,
        SUM(o.quantity * p.price) AS spend
    FROM orders o
    INNER JOIN product p USING(product_id)
    WHERE YEAR(o.order_date) = 2020 AND MONTH(o.order_date) IN (6, 7)
    GROUP BY o.customer_id, MONTH(o.order_date)
) t
INNER JOIN customers USING(customer_id)
GROUP BY customer_id
HAVING SUM(spend >= 100) = 2;

-- https://leetcode.com/problems/the-most-recent-orders-for-each-product/

-- subquery
SELECT product_name, product_id, order_id, order_date
FROM Orders
INNER JOIN Products USING(product_id)
WHERE (product_id, order_date) IN (
    SELECT product_id, MAX(order_date)
    FROM Orders
    GROUP BY 1
)
ORDER BY 1, 2, 3;

-- window function
SELECT product_name, product_id, order_id, order_date
FROM (
    SELECT
        order_id, order_date, product_id,
        RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) AS _rank
    FROM Orders
) o
INNER JOIN Products USING(product_id)
WHERE _rank = 1
ORDER BY 1, 2, 3;

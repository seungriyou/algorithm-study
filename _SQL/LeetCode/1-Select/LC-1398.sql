-- https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

-- sol 1 : intersect
SELECT customer_id, customer_name
FROM (
    (
        SELECT customer_id
        FROM Orders
        WHERE product_name = 'A'
    )
    INTERSECT
    (
        SELECT customer_id
        FROM Orders
        WHERE product_name = 'B'
    )
) o
INNER JOIN Customers c USING(customer_id)
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM Orders
    WHERE product_name = 'C'
)
ORDER BY 1;

-- sol 2 : having
SELECT c.customer_id, customer_name
FROM Orders o
INNER JOIN Customers c USING(customer_id)
GROUP BY customer_id
HAVING SUM(product_name = "A") > 0 AND SUM(product_name = "B") > 0 AND SUM(product_name = "C") = 0
ORDER BY 1;

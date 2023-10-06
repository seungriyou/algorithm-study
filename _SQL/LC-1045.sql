# https://leetcode.com/problems/customers-who-bought-all-products/

SELECT customer_id
FROM Customer
# WHERE product_key IN (SELECT * FROM Product) (foreign key constraint 때문에 필요 없음)
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);    # foreign key constraint 때문에 DISTINCT 필요 없음

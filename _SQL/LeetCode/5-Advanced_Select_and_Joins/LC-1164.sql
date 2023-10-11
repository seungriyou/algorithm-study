# https://leetcode.com/problems/product-price-at-a-given-date/

SELECT P.product_id, COALESCE(C.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS P
LEFT JOIN (
    SELECT product_id, new_price
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date) AS last_change
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
) AS C ON P.product_id = C.product_id;


# SELECT product_id, 10 AS price
# FROM Products
# GROUP BY product_id
# HAVING MIN(change_date) > '2019-08-16'
# UNION
# SELECT product_id, new_price
# FROM Products
# WHERE (product_id, change_date) IN (
#     SELECT product_id, MAX(change_date) AS last_change
#     FROM Products
#     WHERE change_date <= '2019-08-16'
#     GROUP BY product_id
# );

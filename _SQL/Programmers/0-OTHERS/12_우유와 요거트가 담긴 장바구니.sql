# https://school.programmers.co.kr/learn/courses/30/lessons/62284
SELECT cart_id
FROM (
    SELECT DISTINCT cart_id, name
    FROM CART_PRODUCTS
    WHERE name = 'Milk'
) AS C
INNER JOIN (
    SELECT DISTINCT cart_id, name
    FROM CART_PRODUCTS
    WHERE name = 'Yogurt'
) AS Y USING(cart_id)
ORDER BY 1;

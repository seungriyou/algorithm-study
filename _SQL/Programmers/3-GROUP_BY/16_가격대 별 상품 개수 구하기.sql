# https://school.programmers.co.kr/learn/courses/30/lessons/131530

SELECT TRUNCATE(price / 10000, 0) * 10000 AS price_group, COUNT(product_id) AS products
FROM PRODUCT
GROUP BY 1
ORDER BY 1;

# https://school.programmers.co.kr/learn/courses/30/lessons/131529

SELECT LEFT(product_code, 2) AS category, COUNT(product_id) AS products
FROM PRODUCT
GROUP BY 1
ORDER BY 1;

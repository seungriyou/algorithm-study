# https://school.programmers.co.kr/learn/courses/30/lessons/131533

SELECT P.product_code, price * tot_amount AS sales
FROM PRODUCT P
INNER JOIN (
    SELECT product_id, SUM(sales_amount) AS tot_amount
    FROM OFFLINE_SALE
    GROUP BY product_id
) S USING(product_id)
ORDER BY 2 DESC, 1;

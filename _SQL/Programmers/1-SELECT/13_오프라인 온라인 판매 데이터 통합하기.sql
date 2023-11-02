# https://school.programmers.co.kr/learn/courses/30/lessons/131537

# SELECT *
# FROM (
#     SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, user_id, sales_amount
#     FROM ONLINE_SALE
#     WHERE YEAR(sales_date) = '2022' AND MONTH(sales_date) = '03'
#     UNION ALL
#     SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, NULL as user_id, sales_amount
#     FROM OFFLINE_SALE
#     WHERE YEAR(sales_date) = '2022' AND MONTH(sales_date) = '03'
# ) AS T
# ORDER BY sales_date, product_id, user_id;

SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, user_id, sales_amount
FROM ONLINE_SALE
WHERE YEAR(sales_date) = '2022' AND MONTH(sales_date) = '03'
UNION ALL
SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS sales_date, product_id, NULL as user_id, sales_amount
FROM OFFLINE_SALE
WHERE YEAR(sales_date) = '2022' AND MONTH(sales_date) = '03'
ORDER BY sales_date, product_id, user_id;

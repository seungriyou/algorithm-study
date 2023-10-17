# https://school.programmers.co.kr/learn/courses/30/lessons/131117

SELECT O.product_id, P.product_name, SUM(P.price * O.amount) AS total_sales
FROM FOOD_ORDER O
INNER JOIN FOOD_PRODUCT P ON O.product_id = P.product_id
WHERE YEAR(O.produce_date) = '2022' AND MONTH(O.produce_date) = '05'
GROUP BY O.product_id
ORDER BY total_sales DESC, O.product_id;

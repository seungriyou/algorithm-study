# https://school.programmers.co.kr/learn/courses/30/lessons/131116

# SELECT category, price AS max_price, product_name
# FROM FOOD_PRODUCT
# WHERE (category, price) IN (
#     SELECT category, MAX(price) AS max_price
#     FROM FOOD_PRODUCT
#     WHERE category IN ('과자', '국', '김치', '식용유')
#     GROUP BY category
# )
# ORDER BY price DESC;


SELECT A.category, A.price AS max_price, A.product_name
FROM FOOD_PRODUCT A, (
    SELECT category, MAX(price) AS max_price
    FROM FOOD_PRODUCT
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category
) B
WHERE A.category = B.category AND A.price = B.max_price
ORDER BY 2 DESC;

# https://school.programmers.co.kr/learn/courses/30/lessons/131115

# SELECT *
# FROM FOOD_PRODUCT
# ORDER BY price DESC
# LIMIT 1;

SELECT *
FROM FOOD_PRODUCT
WHERE price = (
    SELECT MAX(price)
    FROM FOOD_PRODUCT
);

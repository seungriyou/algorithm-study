# https://school.programmers.co.kr/learn/courses/30/lessons/133025

# SELECT flavor
# FROM FIRST_HALF
# WHERE flavor IN (
#     SELECT flavor
#     FROM ICECREAM_INFO
#     WHERE ingredient_type LIKE 'fruit%'
# ) AND total_order > 3000
# ORDER BY total_order DESC;

SELECT F.flavor
FROM FIRST_HALF F
INNER JOIN ICECREAM_INFO I USING(flavor)
WHERE I.ingredient_type LIKE 'fruit%' AND F.total_order > 3000
ORDER BY total_order DESC;

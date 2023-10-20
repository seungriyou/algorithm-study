# https://school.programmers.co.kr/learn/courses/30/lessons/131123

# === Subquery ===
SELECT food_type, rest_id, rest_name, favorites
FROM REST_INFO
WHERE (food_type, favorites) IN (
    SELECT food_type, MAX(favorites)
    FROM REST_INFO
    GROUP BY food_type
)
ORDER BY food_type DESC;

# === RANK ===
# SELECT food_type, rest_id, rest_name, favorites
# FROM (
#     SELECT *, RANK() OVER (PARTITION BY food_type ORDER BY favorites DESC) AS _rank
#     FROM REST_INFO
# ) AS R
# WHERE R._rank = 1
# ORDER BY food_type DESC;

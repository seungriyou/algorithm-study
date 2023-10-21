# https://school.programmers.co.kr/learn/courses/30/lessons/133027

SELECT H.flavor
FROM FIRST_HALF H
LEFT JOIN (
    SELECT flavor, SUM(total_order) AS total_order
    FROM JULY
    GROUP BY flavor
) AS J ON H.flavor = J.flavor
ORDER BY H.total_order + COALESCE(J.total_order, 0) DESC
# ORDER BY H.total_order + J.total_order DESC
LIMIT 3;

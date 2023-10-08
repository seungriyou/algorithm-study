# https://leetcode.com/problems/queries-quality-and-percentage/
# GROUP BY 후 조건에 부합하는 값 COUNT 하는 방법 세 가지 **

SELECT query_name
, ROUND(AVG(rating / position), 2) AS quality
# , ROUND(COUNT(CASE WHEN rating < 3 THEN 1 END) / COUNT(*) * 100, 2) AS poor_query_percentage
# , ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(*) * 100, 2) AS poor_query_percentage
, ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name

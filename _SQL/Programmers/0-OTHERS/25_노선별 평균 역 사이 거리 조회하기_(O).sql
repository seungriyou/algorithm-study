# https://school.programmers.co.kr/learn/courses/30/lessons/284531
SELECT
    route,
    CONCAT(ROUND(SUM(d_between_dist), 1), 'km') AS total_distance,
    CONCAT(ROUND(AVG(d_between_dist), 2), 'km') AS average_distance
FROM SUBWAY_DISTANCE
GROUP BY route
ORDER BY SUM(d_between_dist) DESC;    # ORDER BY 2 DESC로 하면 X (문자열끼리 비교가 되어서? 혹은 ROUND() 결과여서?)

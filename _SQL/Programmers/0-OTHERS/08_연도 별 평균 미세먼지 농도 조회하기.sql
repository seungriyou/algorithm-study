# https://school.programmers.co.kr/learn/courses/30/lessons/284530
# '소수 셋째 자리에서 반올림' = ROUND(, 2)
SELECT YEAR(ym) AS year, ROUND(AVG(pm_val1), 2) AS 'PM10', ROUND(AVG(pm_val2), 2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE location2 = '수원'
GROUP BY 1
ORDER BY 1;

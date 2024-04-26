# https://school.programmers.co.kr/learn/courses/30/lessons/293260
SELECT COUNT(id) AS fish_count, MONTH(time) AS month
FROM FISH_INFO
GROUP BY 2
ORDER BY 2;

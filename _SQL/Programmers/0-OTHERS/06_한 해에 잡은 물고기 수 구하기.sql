# https://school.programmers.co.kr/learn/courses/30/lessons/298516
SELECT COUNT(id) AS fish_count
FROM FISH_INFO
WHERE YEAR(time) = 2021;

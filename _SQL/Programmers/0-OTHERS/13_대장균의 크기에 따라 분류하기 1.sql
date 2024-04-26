# https://school.programmers.co.kr/learn/courses/30/lessons/299307
SELECT
    id,
    (CASE
        WHEN size_of_colony <= 100 THEN 'LOW'
        WHEN size_of_colony <= 1000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END) AS size
FROM ECOLI_DATA
ORDER BY 1;

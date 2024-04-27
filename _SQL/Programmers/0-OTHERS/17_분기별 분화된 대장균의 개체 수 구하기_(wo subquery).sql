# https://school.programmers.co.kr/learn/courses/30/lessons/299308
# subquery가 반드시 필요하지 않은 경우가 있다!
SELECT
    (CASE
        WHEN MONTH(differentiation_date) < 4 THEN '1Q'
        WHEN MONTH(differentiation_date) < 7 THEN '2Q'
        WHEN MONTH(differentiation_date) < 10 THEN '3Q'
        ELSE '4Q'
    END) AS quarter,
    COUNT(id) AS ecoli_count
FROM ECOLI_DATA
GROUP BY 1
ORDER BY 1;

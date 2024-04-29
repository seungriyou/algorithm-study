# https://school.programmers.co.kr/learn/courses/30/lessons/299310
# w/ group by & join
SELECT year, (max_size - size_of_colony) AS year_dev, id
FROM ECOLI_DATA
INNER JOIN (
    SELECT YEAR(differentiation_date) AS year, MAX(size_of_colony) AS max_size
    FROM ECOLI_DATA
    GROUP BY 1
) MS ON YEAR(differentiation_date) = year
ORDER BY 1, 2;

# w/ partition by
SELECT YEAR(differentiation_date) AS year, (max_size - size_of_colony) AS year_dev, id
FROM (
    SELECT *, MAX(size_of_colony) OVER(PARTITION BY YEAR(differentiation_date)) AS max_size
    FROM ECOLI_DATA
) E
ORDER BY 1, 2;

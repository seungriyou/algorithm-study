# https://school.programmers.co.kr/learn/courses/30/lessons/301649
# w/o PERCENT_RANK()
SELECT
    id,
    (CASE
        WHEN ratio <= 0.25 THEN 'CRITICAL'
        WHEN ratio <= 0.5 THEN 'HIGH'
        WHEN ratio <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END) AS colony_name
FROM (
    SELECT
        id,
        RANK() OVER (ORDER BY size_of_colony DESC) / total AS ratio
    FROM ECOLI_DATA
    INNER JOIN (SELECT COUNT(*) AS total FROM ECOLI_DATA) C ON 1=1
) T
ORDER BY 1;

# w/ PERCENT_RANK() (다른 사람 풀이 참고)
SELECT
    id,
    (CASE
        WHEN ratio <= 0.25 THEN 'CRITICAL'
        WHEN ratio <= 0.5 THEN 'HIGH'
        WHEN ratio <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END) AS colony_name
FROM (
    SELECT
        id,
        PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) AS ratio
    FROM ECOLI_DATA
) T
ORDER BY 1;

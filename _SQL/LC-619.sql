# https://leetcode.com/problems/biggest-single-number/

# SELECT MAX(num) as num
# FROM (
#     SELECT *
#     FROM MyNumbers
#     GROUP BY num
#     HAVING COUNT(*) = 1
# ) AS N;

SELECT (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC LIMIT 1
) AS num;

# https://school.programmers.co.kr/learn/courses/30/lessons/276036
# cte
WITH FE AS (
    SELECT SUM(code) AS code
    FROM SKILLCODES
    WHERE category = 'Front End'
), PY AS (
    SELECT code
    FROM SKILLCODES
    WHERE name = 'Python'
), CS AS (
    SELECT code
    FROM SKILLCODES
    WHERE name = 'C#'
), RESULT AS (
    SELECT
        (CASE
            WHEN (skill_code & FE.code) AND (skill_code & PY.code) THEN 'A'
            WHEN (skill_code & CS.code) THEN 'B'
            WHEN (skill_code & FE.code) THEN 'C'
#             ELSE NULL (redundant)
        END) AS grade,
        id,
        email
    FROM DEVELOPERS, FE, PY, CS
)

SELECT *
FROM RESULT
WHERE grade IS NOT NULL
ORDER BY 1, 2;

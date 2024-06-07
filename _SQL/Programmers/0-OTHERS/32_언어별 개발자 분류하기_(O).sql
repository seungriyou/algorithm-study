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


##### REVIEW #####
# sol1
WITH _python AS (
    SELECT code FROM SKILLCODES WHERE name = 'Python'
), _cs AS (
    SELECT code FROM SKILLCODES WHERE name = 'C#'
), _frontend AS (
    SELECT SUM(code) AS code FROM SKILLCODES WHERE category = 'Front End'
)

SELECT
    (CASE
        WHEN (skill_code & _python.code) AND (skill_code & _frontend.code) THEN 'A'
        WHEN (skill_code & _cs.code) THEN 'B'
        WHEN (skill_code & _frontend.code) THEN 'C'
    END) AS grade,
    id, email
FROM DEVELOPERS, _python, _cs, _frontend
HAVING grade IS NOT NULL
ORDER BY 1, 2;

# sol2
SELECT
    (CASE
        WHEN (skill_code & (SELECT code FROM SKILLCODES WHERE name = 'Python'))
                AND (skill_code & (SELECT SUM(code) AS code FROM SKILLCODES WHERE category = 'Front End')) THEN 'A'
        WHEN (skill_code & (SELECT code FROM SKILLCODES WHERE name = 'C#')) THEN 'B'
        WHEN (skill_code & (SELECT SUM(code) AS code FROM SKILLCODES WHERE category = 'Front End')) THEN 'C'
    END) AS grade,
    id, email
FROM DEVELOPERS
HAVING grade IS NOT NULL
ORDER BY 1, 2;

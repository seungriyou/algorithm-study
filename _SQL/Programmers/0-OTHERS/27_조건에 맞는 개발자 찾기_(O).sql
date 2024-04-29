# https://school.programmers.co.kr/learn/courses/30/lessons/276034
# sol1
SELECT id, email, first_name, last_name
FROM DEVELOPERS
INNER JOIN (SELECT code AS py FROM SKILLCODES WHERE name = 'Python') P ON 1=1
INNER JOIN (SELECT code AS cs FROM SKILLCODES WHERE name = 'C#') C ON 1=1
WHERE skill_code & py OR skill_code & cs
ORDER BY 1;

# sol2
SELECT id, email, first_name, last_name
FROM DEVELOPERS
WHERE skill_code & (
    SELECT SUM(code)
    FROM SKILLCODES
    WHERE name IN ('Python', 'C#')
)
ORDER BY 1;

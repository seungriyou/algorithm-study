# https://school.programmers.co.kr/learn/courses/30/lessons/301651
WITH RECURSIVE T AS (
    (
        SELECT id, parent_id, 1 AS generation
        FROM ECOLI_DATA
        WHERE parent_id IS NULL
    )
    UNION ALL
    (
        SELECT C.id, C.parent_id, T.generation + 1
        FROM ECOLI_DATA C
        INNER JOIN T ON C.parent_id = T.id
    )
)

SELECT COUNT(id) AS count, generation
FROM T
WHERE id NOT IN (
    SELECT DISTINCT parent_id
    FROM ECOLI_DATA
    WHERE parent_id IS NOT NULL # -- parent_id NULL인 것 제외해주지 않으면 안 됨 x_x
)
GROUP BY 2
ORDER BY 2;

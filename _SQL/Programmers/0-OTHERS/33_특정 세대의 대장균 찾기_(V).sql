# https://school.programmers.co.kr/learn/courses/30/lessons/301650
# sol1: subquery
SELECT id
FROM ECOLI_DATA
WHERE parent_id IN (
    # 2세대
    SELECT id
    FROM ECOLI_DATA
    WHERE parent_id IN (
        # 1세대
        SELECT id
        FROM ECOLI_DATA
        WHERE parent_id IS NULL
    )
)
ORDER BY 1;

# sol2: join
SELECT G3.id
FROM ECOLI_DATA G3
INNER JOIN ECOLI_DATA G2 ON G2.id = G3.parent_id
INNER JOIN ECOLI_DATA G1 ON G1.id = G2.parent_id
WHERE G1.parent_id IS NULL
ORDER BY 1;

# sol3: recur cte
WITH RECURSIVE T AS (
    (SELECT id, parent_id, 1 AS gen
    FROM ECOLI_DATA
    WHERE parent_id IS NULL)
    UNION ALL
    (SELECT C.id, C.parent_id, T.gen + 1
    FROM ECOLI_DATA C
    INNER JOIN T ON C.parent_id = T.id)
)
SELECT id FROM T WHERE gen = 3;

# https://leetcode.com/problems/tree-node/

# root: p_id = null
# inner: id IN (DISTINCT p_id)
# leaf: id NOT IN (DISTINCT p_id)

# sol1 (w/ left join, w/ subquery)
SELECT
    id,
    CASE
        WHEN T.p_id IS NULL THEN 'Root'
        WHEN P.p_id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree T
LEFT JOIN (
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
) P ON T.id = P.p_id;


# sol2 (w/ left join, w/o subquery)
SELECT
    DISTINCT T1.id,
    CASE
        WHEN T1.p_id IS NULL THEN 'Root'
        WHEN T2.id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree T1
LEFT JOIN Tree T2 ON T1.id = T2.p_id;


# sol3 (w/o left join)
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;


# ===== (21.12.16) reviewed =====
SELECT
    DISTINCT P.id,
    CASE
        WHEN P.p_id IS NULL THEN 'Root'
        WHEN C.id IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree P
LEFT JOIN Tree C ON P.id = C.p_id;

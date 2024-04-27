# https://school.programmers.co.kr/learn/courses/30/lessons/299305
# w/ subquery
SELECT id, COALESCE(cnt, 0) AS child_count
FROM ECOLI_DATA E1
LEFT JOIN (
    SELECT parent_id, COUNT(id) AS cnt
    FROM ECOLI_DATA
    GROUP BY parent_id
) E2 ON E1.id = E2.parent_id
ORDER BY 1;

# w/o subquery
SELECT P.id, COUNT(C.id) AS child_count
FROM ECOLI_DATA P
LEFT JOIN ECOLI_DATA C ON P.id = C.parent_id
GROUP BY 1
ORDER BY 1;

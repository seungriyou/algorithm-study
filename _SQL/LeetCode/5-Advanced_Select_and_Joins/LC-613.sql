-- https://leetcode.com/problems/shortest-distance-in-a-line/

-- JOIN
SELECT MIN(ABS(p1.x - p2.x)) AS shortest
FROM Point p1
INNER JOIN Point p2 ON p1.x <> p2.x;

-- window function
SELECT MIN(dist) AS shortest
FROM (
    SELECT ABS(x - LEAD(x) OVER (ORDER BY x)) AS dist FROM Point
) T;

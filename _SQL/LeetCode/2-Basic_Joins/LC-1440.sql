-- https://leetcode.com/problems/evaluate-boolean-expression/

SELECT
    left_operand, operator, right_operand,
    (
        CASE
            WHEN operator = "=" THEN IF(v1.value = v2.value, "true", "false")
            WHEN operator = ">" THEN IF(v1.value > v2.value, "true", "false")
            WHEN operator = "<" THEN IF(v1.value < v2.value, "true", "false")
        END
    ) AS value
FROM Expressions e
INNER JOIN Variables v1 ON e.left_operand = v1.name
INNER JOIN Variables v2 ON e.right_operand = v2.name;

-- SELECT
--     left_operand, operator, right_operand,
--     (
--         CASE
--             WHEN operator = "=" AND v1.value = v2.value THEN "true"
--             WHEN operator = ">" AND v1.value > v2.value THEN "true"
--             WHEN operator = "<" AND v1.value < v2.value THEN "true"
--             ELSE "false"
--         END
--     ) AS value
-- FROM Expressions e
-- INNER JOIN Variables v1 ON e.left_operand = v1.name
-- INNER JOIN Variables v2 ON e.right_operand = v2.name;

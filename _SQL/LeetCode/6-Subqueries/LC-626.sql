# https://leetcode.com/problems/exchange-seats/

# === LAG, LEAD ===
SELECT id
    , CASE
        WHEN id % 2 = 0 THEN (LAG(student) OVER (ORDER BY id))
        ELSE IFNULL(LEAD(student) OVER (ORDER BY id), student)
    END AS student
FROM Seat;


# === IF ===
SELECT IF(
        id = (SELECT MAX(id) FROM Seat),
        IF(id % 2 = 0, id - 1, id),
        IF(id % 2 = 0, id - 1, id + 1)
    ) AS id
    , student
FROM Seat
ORDER BY id;


# ===== (23.12.13) reviewed =====
# === LAG & LEAD ===
SELECT
    id,
    CASE
        WHEN id % 2 = 0 THEN (LAG(student) OVER (ORDER BY id))
        ELSE COALESCE(LEAD(student) OVER (ORDER BY id), student)
    END AS student
FROM Seat;

# === IF ===
SELECT
    IF(
        id = (SELECT MAX(id) FROM Seat),
        IF(id % 2 = 0, id - 1, id),
        IF(id % 2 = 0, id - 1, id + 1)
    ) AS id,
    student
FROM Seat
ORDER BY 1;

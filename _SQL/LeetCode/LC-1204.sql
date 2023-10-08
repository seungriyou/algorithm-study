# https://leetcode.com/problems/last-person-to-fit-in-the-bus/

# === SUM() OVER() ===
SELECT person_name
FROM (
    SELECT person_name, SUM(weight) OVER(ORDER BY turn) AS sum
    FROM Queue
    ORDER BY sum DESC
) AS Q
WHERE sum <= 1000
LIMIT 1;

# === JOIN ===
# SELECT Q1.person_name
# FROM Queue Q1, Queue Q2
# WHERE Q1.turn >= Q2.turn
# GROUP BY Q1.turn
# HAVING SUM(Q2.weight) <= 1000
# ORDER BY SUM(Q2.weight) DESC
# LIMIT 1;

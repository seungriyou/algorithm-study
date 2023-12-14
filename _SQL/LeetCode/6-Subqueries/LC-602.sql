# https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

# SELECT R1.id, COUNT(*) AS num
# FROM (
#     SELECT requester_id AS id
#     FROM RequestAccepted
#     UNION
#     SELECT accepter_id AS id
#     FROM RequestAccepted
# ) AS R1
# LEFT JOIN RequestAccepted R2 ON R1.id = R2.requester_id OR R1.id = R2.accepter_id
# GROUP BY id
# ORDER BY num DESC
# LIMIT 1;

SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL   # -- 등장 횟수를 모두 세면 되므로!
    SELECT accepter_id AS id
    FROM RequestAccepted
) AS R
GROUP BY id
ORDER BY num DESC
LIMIT 1;

# ===== (23.12.14) reviewed =====
SELECT id, COUNT(id) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted
) R
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

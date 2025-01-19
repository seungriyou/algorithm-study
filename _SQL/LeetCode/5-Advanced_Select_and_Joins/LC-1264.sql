-- https://leetcode.com/problems/page-recommendations/

-- sol 1
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE page_id NOT IN (
    SELECT page_id
    FROM Likes
    WHERE user_id = 1
) AND user_id IN (
    (SELECT user1_id AS f_id FROM Friendship WHERE user2_id = 1)
    UNION
    (SELECT user2_id FROM Friendship WHERE user1_id = 1)
);

-- sol 2
SELECT DISTINCT page_id AS recommended_page
FROM Likes
INNER JOIN (
    SELECT (
        CASE
            WHEN user1_id = 1 THEN user2_id
            WHEN user2_id = 1 THEN user1_id
        END
    ) AS user_id
    FROM Friendship
) f USING(user_id)
WHERE page_id NOT IN (
    SELECT page_id
    FROM Likes
    WHERE user_id = 1
);

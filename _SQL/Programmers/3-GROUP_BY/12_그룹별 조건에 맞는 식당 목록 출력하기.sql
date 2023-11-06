# https://school.programmers.co.kr/learn/courses/30/lessons/131124

WITH COUNT_T AS (
    SELECT member_id, COUNT(*) AS cnt
    FROM REST_REVIEW
    GROUP BY member_id
    ORDER BY cnt DESC
)
SELECT
    member_name
    , review_text
    , DATE_FORMAT(review_date, '%Y-%m-%d') AS review_date
FROM REST_REVIEW
INNER JOIN MEMBER_PROFILE USING(member_id)
WHERE member_id IN (
    SELECT member_id
    FROM COUNT_T
    WHERE cnt = (
        SELECT MAX(cnt)
        FROM COUNT_T
    )
)
ORDER BY 3, 2;

# https://school.programmers.co.kr/learn/courses/30/lessons/164670

SELECT
    user_id
    , nickname
    , CONCAT_WS(" ", city, street_address1, street_address2) AS '전체주소'
    , CONCAT_WS("-", LEFT(tlno, 3), SUBSTRING(tlno, 4, 4), RIGHT(tlno, 4)) AS '전화번호'
FROM USED_GOODS_USER U
WHERE U.user_id IN (
    SELECT writer_id
    FROM USED_GOODS_BOARD B
    GROUP BY B.writer_id
    HAVING COUNT(board_id) >= 3
)
ORDER BY user_id DESC;

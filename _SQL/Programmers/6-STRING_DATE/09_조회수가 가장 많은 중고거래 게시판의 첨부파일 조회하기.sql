# https://school.programmers.co.kr/learn/courses/30/lessons/164671

SELECT CONCAT_WS('/', '/home/grep/src', board_id, CONCAT(file_id, file_name, file_ext)) AS file_path
FROM USED_GOODS_FILE
# -- LIMIT이 포함된 subquery를 alias로 한 번 감싸야 IN 연산을 사용할 수 있다.
# --- (지금처럼 LIMIT 1인 경우에는 IN 말고 = 을 사용해도 되긴 하다.)
WHERE board_id IN (
    SELECT *
    FROM (
        SELECT board_id
        FROM USED_GOODS_BOARD
        ORDER BY views DESC
        LIMIT 1
    ) AS B
)
# WHERE board_id = (
#     SELECT board_id
#     FROM USED_GOODS_BOARD
#     ORDER BY views DESC
#     LIMIT 1
# )
ORDER BY file_id DESC;

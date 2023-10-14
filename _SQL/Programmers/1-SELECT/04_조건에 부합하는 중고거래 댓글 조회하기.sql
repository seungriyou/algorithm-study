# https://school.programmers.co.kr/learn/courses/30/lessons/164673

SELECT B.title, B.board_id, R.reply_id, R.writer_id , R.contents, DATE_FORMAT(R.created_date, '%Y-%m-%d') AS created_date
FROM USED_GOODS_BOARD B, USED_GOODS_REPLY R
WHERE YEAR(B.created_date) = 2022 AND MONTH(B.created_date) = 10 AND B.board_id = R.board_id
ORDER BY created_date, B.title;

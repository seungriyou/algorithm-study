# https://school.programmers.co.kr/learn/courses/30/lessons/131118

SELECT I.rest_id, rest_name, food_type, favorites, address, ROUND(AVG(R.review_score), 2) AS score
FROM REST_REVIEW R
INNER JOIN (
    SELECT rest_id, rest_name, food_type, favorites, address
    FROM REST_INFO
    WHERE address LIKE '서울%'
) I ON I.rest_id = R.rest_id
GROUP BY I.rest_id
ORDER BY score DESC, favorites DESC;

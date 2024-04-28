# https://school.programmers.co.kr/learn/courses/30/lessons/293261
SELECT id, fish_name, length
FROM FISH_INFO
INNER JOIN FISH_NAME_INFO USING(fish_type)
WHERE (fish_type, length) IN (
    SELECT fish_type, MAX(length) AS max_length
    FROM FISH_INFO
    GROUP BY fish_type
)
ORDER BY 1;

# https://school.programmers.co.kr/learn/courses/30/lessons/298518
SELECT COUNT(id) AS fish_count
FROM FISH_INFO
WHERE fish_type IN (
    SELECT fish_type
    FROM FISH_NAME_INFO
    WHERE fish_name IN ('BASS', 'SNAPPER')
);

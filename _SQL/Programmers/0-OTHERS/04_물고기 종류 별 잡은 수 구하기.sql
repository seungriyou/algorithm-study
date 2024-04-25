# https://school.programmers.co.kr/learn/courses/30/lessons/293257
SELECT COUNT(ID) AS fish_count, fish_name
FROM FISH_INFO FI
INNER JOIN FISH_NAME_INFO FNI ON FI.fish_type = FNI.fish_type
GROUP BY fish_name
ORDER BY fish_count DESC;

# https://school.programmers.co.kr/learn/courses/30/lessons/273711
SELECT item_id, item_name, rarity
FROM ITEM_TREE
INNER JOIN ITEM_INFO USING(item_id)
WHERE parent_item_id IN (
    SELECT item_id
    FROM ITEM_INFO
    WHERE rarity = 'RARE'
)
ORDER BY 1 DESC;

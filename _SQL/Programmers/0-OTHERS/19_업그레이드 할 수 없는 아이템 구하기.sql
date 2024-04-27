# https://school.programmers.co.kr/learn/courses/30/lessons/273712
# subquery
SELECT item_id, item_name, rarity
FROM ITEM_INFO
WHERE item_id NOT IN (
    SELECT DISTINCT parent_item_id
    FROM ITEM_TREE
    WHERE parent_item_id IS NOT NULL
)
ORDER BY 1 DESC;

# join
SELECT I.item_id, I.item_name, I.rarity
FROM ITEM_INFO I
LEFT JOIN ITEM_TREE T ON I.item_id = T.parent_item_id
WHERE T.item_id IS NULL
ORDER BY 1 DESC;

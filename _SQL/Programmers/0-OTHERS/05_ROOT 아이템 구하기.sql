# https://school.programmers.co.kr/learn/courses/30/lessons/273710
SELECT item_id, item_name
FROM ITEM_INFO
WHERE item_id IN (
    SELECT item_id
    FROM ITEM_TREE
    WHERE parent_item_id IS NULL
)
ORDER BY item_id;

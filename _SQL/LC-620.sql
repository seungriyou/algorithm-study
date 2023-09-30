# https://leetcode.com/problems/not-boring-movies/

# (1) id : odd
# (2) description : not 'boring'
SELECT *
FROM Cinema
# WHERE id % 2 = 1 AND description <> 'boring'
WHERE MOD(id, 2) = 1 AND description <> 'boring'
ORDER BY rating DESC;

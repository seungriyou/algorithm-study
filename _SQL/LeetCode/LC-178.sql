# https://leetcode.com/problems/rank-scores/
select score, dense_rank() over (order by score desc) as 'rank'
from Scores;

# select *,
# rank() over (order by score desc) as _rank,
# dense_rank() over (order by score desc) as _dense_rank,
# row_number() over (order by score desc) as _row_number
# from Scores;

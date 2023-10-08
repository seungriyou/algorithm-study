# https://leetcode.com/problems/find-customer-referee/
select name
from customer
# where referee_id is null or referee_id <> 2;
where ifnull(referee_id, 0) <> 2;

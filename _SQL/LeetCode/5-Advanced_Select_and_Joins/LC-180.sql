# https://leetcode.com/problems/consecutive-numbers/
# select distinct L1.num as ConsecutiveNums
# from Logs L1, Logs L2, Logs L3
# where L1.num = L2.num and L1.num = L3.num and L1.id = L2.id + 1 and L1.id = L3.id + 2;

# select distinct num as ConsecutiveNums
# from Logs
# where (id + 1, num) in (select * from Logs) and (id + 2, num) in (select * from Logs);

select D.Num as ConsecutiveNums
from (
    select distinct A.Num
    from Logs A
    left join Logs B on A.Id = B.Id + 1
    left join Logs C on A.Id = C.Id + 2
    where A.Num = B.Num and A.Num = C.Num
) D;

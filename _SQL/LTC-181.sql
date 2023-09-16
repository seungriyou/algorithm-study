# https://leetcode.com/problems/employees-earning-more-than-their-managers/
select E.name as Employee
from Employee E
inner join Employee M on E.managerId = M.id
where E.salary > M.salary;

/* Too large time complexity:
select name as Employee
from Employee E1
where E1.salary > (
    select salary
    from Employee E2
    where E2.id = E1.managerId
);
 */

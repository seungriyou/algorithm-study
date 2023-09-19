# https://leetcode.com/problems/customers-who-never-order/
select name as Customers
from Customers C
left join Orders O
on O.customerId = C.id
where O.id is NULL; # PK라서 더 빠른가..?

/* Slower 1
select name as Customers
from Customers
where id not in (
    select customerId
    from Orders
);
*/

/* Slower 2 (where의 O.customerId가 PK가 아니라서?)
select name as Customers
from Customers C
left join Orders O
on O.customerId = C.id
where O.customerId is NULL;
*/

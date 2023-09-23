# https://leetcode.com/problems/sales-person/
# select name
# from SalesPerson S
# where S.sales_id not in (
#     select sales_id
#     from Orders O
#     left join Company C on O.com_id = C.com_id
#     where C.name = 'RED'
# );

select name
from SalesPerson
where sales_id not in (
    select sales_id
    from Orders
    where com_id = (
        select com_id
        from Company
        where name = 'RED'
    )
);

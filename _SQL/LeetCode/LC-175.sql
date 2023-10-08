# https://leetcode.com/problems/combine-two-tables/
select firstName, lastName, city, state
from Person P left join Address A
on P.personId = A.personId; # using (personId);

# https://leetcode.com/problems/triangle-judgement/
select *, if(x < y + z and y < x + z and z < x + y, "Yes", "No") as triangle
from Triangle;

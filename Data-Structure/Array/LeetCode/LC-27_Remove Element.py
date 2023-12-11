# https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for n in nums:
            if n != val:
                nums[idx] = n
                idx += 1

        return idx

nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums, val))

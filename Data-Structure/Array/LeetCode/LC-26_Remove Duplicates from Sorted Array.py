# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))

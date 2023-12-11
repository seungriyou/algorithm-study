# [LTC] 561 - Array Partition
# https://leetcode.com/problems/array-partition/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

sol = Solution()
nums = [6,2,6,5,1,2]
print(sol.arrayPairSum(nums))

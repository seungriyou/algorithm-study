# [LTC] 136 - Single Number
# https://leetcode.com/problems/single-number/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR = 두 번 등장한 요소는 0으로, 한 번만 등장한 요소는 값을 보존
        result = 0
        for num in nums:
            result ^= num

        return result

sol = Solution()
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))

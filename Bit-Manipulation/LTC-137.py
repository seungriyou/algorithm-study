# [LTC] 137 - Single Number II
# https://leetcode.com/problems/single-number-ii/

from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR => 1인 bit가 짝수번 등장하면 0, 홀수번 등장하면 1
        once, twice = 0, 0
        for num in nums:
            once = once ^ num & ~twice  # -- turn off the bits in twice
            twice = twice ^ num & ~once  # -- turn off the bits in once
            # print(f"=== {num} ({bin(num)}) ===")
            # print(f"{bin(once)=}")
            # print(f"{bin(twice)=}")

        return once

    def singleNumber3(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def singleNumber2(self, nums: List[int]) -> int:

        for num, cnt in Counter(nums).items():
            if cnt == 1:
                return num

        return -1

sol = Solution()
nums = [0,1,0,1,0,1,99]
print(sol.singleNumber(nums))

# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_dict = {}

        for i, num in enumerate(nums):
            if num in sub_dict:
                return [sub_dict[num], i]
            else:
                sub_dict[target - num] = i

# [LTC] 1 - Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find indices of the two numbers
        sub_dict = {}
        for i, n in enumerate(nums):
            if target - n in sub_dict.keys():
                return [sub_dict[target - n], i]
            sub_dict[n] = i

# === 24.02.13 === #
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_dict = {}

        for i, num in enumerate(nums):
            if num in sub_dict:
                return [sub_dict[num], i]
            else:
                sub_dict[target - num] = i

nums = [3,3]
target = 6
solution = Solution()
print(solution.twoSum(nums, target))
solution2 = Solution2()
print(solution2.twoSum(nums, target))

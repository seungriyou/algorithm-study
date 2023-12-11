# [LTC] 167 - Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_val = numbers[l] + numbers[r]
            if sum_val > target:
                r -= 1
            elif sum_val < target:
                l += 1
            else:
                return [l + 1, r + 1]

numbers = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))

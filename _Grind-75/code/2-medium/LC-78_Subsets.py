# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """recursive"""
        result = [[]]

        for num in nums:
            result += [prev + [num] for prev in result]

        return result

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """backtracking w/ global list"""
        result = []
        subset = []

        def backtrack(idx):
            result.append(subset[:])

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)

        return result

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """backtracking w/o global list"""
        result = []

        def backtrack(idx, subset):
            result.append(subset)

            for i in range(idx, len(nums)):
                backtrack(i + 1, subset + [nums[i]])

        backtrack(0, [])

        return result

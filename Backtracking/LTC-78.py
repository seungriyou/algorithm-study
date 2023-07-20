# [LTC] 78 - Subsets
# https://leetcode.com/problems/subsets/

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        if nums = [1, 2, 3], a tree will be:
            1      2     3
           / \    /
          2   3  3
         /
        3
        -> dfs
        """
        result = []

        def dfs(idx: int, path: List[int]) -> None:
            # -- result에 모두 추가
            result.append(path)

            # -- dfs 수행
            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result

sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))

# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result, perm = [], []
        n = len(nums)

        def backtrack():
            # base condition
            if len(perm) == n:
                result.append(perm[:])
                return

            # recur
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    perm.append(num)

                    backtrack()

                    seen.remove(num)
                    perm.pop()

        backtrack()

        return result

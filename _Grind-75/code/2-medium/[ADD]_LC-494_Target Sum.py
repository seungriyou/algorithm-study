# https://leetcode.com/problems/target-sum/

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """backtrack + memo"""
        # from functools import cache
        # ref: https://leetcode.com/problems/target-sum/solutions/455024/dp-is-easy-5-steps-to-think-through-dp-questions

        n = len(nums)
        memo = {}

        # @cache
        def backtrack(tot, idx):
            # from memo (resolve TLE)
            if (tot, idx) in memo:
                return memo[(tot, idx)]

            # base case
            if idx == n:
                if tot == target:
                    return 1
                return 0

            # recur
            pos = backtrack(tot + nums[idx], idx + 1)
            neg = backtrack(tot - nums[idx], idx + 1)

            # memo
            memo[(tot, idx)] = pos + neg

            return memo[(tot, idx)]
            # return pos + neg

        return backtrack(0, 0)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """faster dp (1D)"""
        # ref: https://leetcode.com/problems/target-sum/solutions/97343/python-dp

        from collections import defaultdict

        dp = defaultdict(int)
        dp[0] = 1  # base case

        for num in nums:
            tmp = defaultdict(int)
            for tot, cnt in dp.items():
                tmp[tot + num] += cnt
                tmp[tot - num] += cnt
            dp = tmp

        return dp[target]

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        """backtracking -> TLE"""

        cnt = 0
        n = len(nums)

        def backtrack(tot, idx):
            nonlocal cnt

            # base condition
            if idx == n:
                if tot == target:
                    cnt += 1
                return

            # +
            backtrack(tot + nums[idx], idx + 1)

            # -
            backtrack(tot - nums[idx], idx + 1)

        backtrack(0, 0)

        return cnt
    
# https://leetcode.com/problems/combination-sum-iv/

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[n] = 합이 n인 combination의 개수
        dp = [0] * (target + 1)
        dp[0] = 1  # 초기화

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]

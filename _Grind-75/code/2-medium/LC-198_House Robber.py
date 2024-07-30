# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """O(1) space DP"""

        a, b = 0, 0
        for num in nums:
            a, b = b, max(a + num, b)

        return b

    def rob1(self, nums: List[int]) -> int:
        """O(n) space DP"""
        n = len(nums)

        # dp[i]: nums[i - 1]까지 확인했을 때 훔칠 수 있는 가장 큰 금액
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            # (1) 이전 집을 털 때와 (2) 그 이전 집을 털고 현재 집을 털 때 중 더 큰 값 기록
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[n]

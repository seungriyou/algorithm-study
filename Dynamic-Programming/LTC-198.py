# [LTC] 198 - House Robber
# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob_before(self, nums: List[int]) -> int:
        # === bottom up ===
        n = len(nums)
        dp = [-1] * n

        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[1], dp[0])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        # === bottom up ===
        # dp[i]를 구할 때, dp[i - 1]과 dp[i - 2]만 필요하므로,
        # dp list가 아닌 각각 prev_1 = dp[i - 1], prev_2 = dp[i - 2] 두 변수로 사용
        prev_1, prev_2 = 0, 0
        for n in nums:
            curr = max(prev_2 + n, prev_1)
            prev_2 = prev_1
            prev_1 = curr

        return prev_1

sol = Solution()
nums = [2,7,9,3,1]
print(sol.rob(nums))

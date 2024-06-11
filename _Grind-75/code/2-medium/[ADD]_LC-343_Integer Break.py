# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        # ref: https://leetcode.com/problems/integer-break/solutions/383679/python-dp-solution-with-detailed-explanation-avoids-confusion-about-factors-of-2-or-3

        # dp[i]: sum이 i인 integers의 max product
        dp = [0] * (n + 1)

        for _sum in range(2, n + 1):
            left, right = 1, _sum - 1

            # left와 right를 중앙으로 이동해가며 dp[_sum] 업데이트
            while left <= right:
                dp[_sum] = max(dp[_sum], max(left, dp[left]) * max(right, dp[right]))
                left += 1
                right -= 1

        return dp[n]

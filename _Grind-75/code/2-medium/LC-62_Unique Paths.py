# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """1D DP"""
        dp = [0] * (n + 1)
        dp[1] = 1

        for _ in range(m):
            for i in range(1, n + 1):
                dp[i] += dp[i - 1]

        return dp[n]

    def uniquePaths2(self, m: int, n: int) -> int:
        """2D DP"""
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]

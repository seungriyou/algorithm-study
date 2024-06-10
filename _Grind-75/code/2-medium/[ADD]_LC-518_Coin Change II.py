# https://leetcode.com/problems/coin-change-ii/

from typing import List


class Solution:
    def change2(self, amount: int, coins: List[int]) -> int:
        """2D DP"""

        n = len(coins)
        # dp[i][j]: i번째 coin까지 확인했을 때, j만큼의 amount를 만들 수 있는 combination의 개수
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):  # -- 물건 (coins)
            dp[i][0] = 1
            for j in range(1, amount + 1):  # -- 임시 용량 (amount)
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        """
        1D DP (2D DP에서 dp[i - 1][j], dp[i][j - coins[i - 1]]만 의존하므로 1D로 optimize 가능)
        """

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amnt in range(coin, amount + 1):
                dp[amnt] += dp[amnt - coin]

        return dp[amount]

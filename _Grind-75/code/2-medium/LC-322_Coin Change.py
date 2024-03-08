# https://leetcode.com/problems/coin-change/
from typing import List
import math
from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """BFS"""

        from collections import deque

        q = deque([(0, 0)])  # (curr_amount, coin_num)
        visited = set()

        while q:
            curr_a, coin_n = q.popleft()

            if curr_a == amount:
                return coin_n

            for coin in coins:
                if (next_a := curr_a + coin) <= amount and next_a not in visited:
                    q.append((next_a, coin_n + 1))
                    visited.add(next_a)

        return -1

    def coinChange_t(self, coins: List[int], amount: int) -> int:
        """top down DP"""

        @cache
        def dp(a):
            if a == 0:
                return 0

            if a < 0:
                return math.inf

            return min(dp(a - coin) + 1 for coin in coins)
            # cnt = math.inf
            # for coin in coins:
            #     if a >= coin:
            #         cnt = min(cnt, dp(a - coin) + 1)

            # return cnt

        return dp(amount) if dp(amount) != math.inf else -1

    def coinChange_b(self, coins: List[int], amount: int) -> int:
        """bottom up DP"""

        INF = amount + 1
        dp = [0] + [INF] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != INF else -1

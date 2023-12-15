# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs_on(self, n: int) -> int:
        dp = [0] * 46
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # prev1: 1칸 이전의 값
        # prev2: 2칸 이전의 값
        prev1, prev2 = 2, 1

        for i in range(3, n + 1):
            # 다중 할당으로 트랜잭션 처리
            # prev2 <- prev1
            # prev1 <- prev1 + prev2
            prev2, prev1 = prev1, prev1 + prev2

        return prev1

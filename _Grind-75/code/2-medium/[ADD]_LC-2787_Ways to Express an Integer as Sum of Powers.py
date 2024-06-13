# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution:
    def numberOfWays2(self, n: int, x: int) -> int:
        """2D DP"""
        # ref: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/solutions/3803381/video-dynamic-programming-approach-to-solve-express-integer-as-sum-of-powers

        mod = 10 ** 9 + 7
        max_num = int(n ** (1.0 / x)) + 1
        # dp[i][j]: 1^x ~ i^x 숫자로 이루어진 조합 중, 합쳐서 j가 되는 조합의 개수
        dp = [[0] * (n + 1) for _ in range(max_num + 1)]

        for i in range(max_num + 1):  # -- 물건 (~ i^x)
            dp[i][0] = 1
            for j in range(1, n + 1):  # -- 용량 (~ n)
                if j >= (val := i ** x):
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - val]) % mod
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[max_num][n]

    def numberOfWays(self, n: int, x: int) -> int:
        """1D DP"""
        # ref: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/solutions/3801788/java-c-python-dp

        mod = 10 ** 9 + 7

        # dp[j]: 1^x ~ i^x 숫자로 이루어진 조합 중, 합쳐서 j가 되는 조합의 개수
        dp = [0] * (n + 1)
        dp[0] = 1

        i = 1
        while (val := i ** x) <= n:
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % mod
            i += 1

        return dp[n]

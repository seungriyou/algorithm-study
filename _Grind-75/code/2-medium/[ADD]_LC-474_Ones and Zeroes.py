# https://leetcode.com/problems/ones-and-zeroes/

from typing import List


class Solution:
    # ref: https://leetcode.com/problems/ones-and-zeroes/solutions/95807/0-1-knapsack-detailed-explanation
    def findMaxForm3(self, strs: List[str], m: int, n: int) -> int:
        """
        3D DP
        dp[i][j][k]:
            - strs에서 i번째 원소까지 확인했을 때
            - 최대 j개의 0과
            - 최대 k개의 1로
            구성되도록 만들 수 있는 subset 중 가장 큰 subset의 크기

        =>  (1) dp[i - 1][j][k]                        (not-pick)
            (2) dp[i - 1][j - 0개수][k - 1개수] + 1       (pick)
            중에서 큰 값을 기록하면 된다.
        """
        l = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]

        def count(elem):
            zeros, ones = 0, 0
            for el in elem:
                if el == "0":
                    zeros += 1
                else:
                    ones += 1
            return zeros, ones

        for i in range(1, l + 1):
            zeros, ones = count(strs[i - 1])

            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[l][m][n]

    # ref: https://leetcode.com/problems/ones-and-zeroes/solutions/701736/python-dp-solution-explained-with-example
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        2D DP
        3D DP에서 dp[i - 1][j][k], dp[i - 1][j - 0개수][k - 1개수]만 확인하므로, 2D DP로 space optimize 가능

        dp[j][k]:
            - 최대 j개의 0과
            - 최대 k개의 1로
            구성되도록 만들 수 있는 subset 중 가장 큰 subset의 크기

        =>  (1) dp[j][k]                        (not-pick)
            (2) dp[j - 0개수][k - 1개수] + 1       (pick)
            중에서 큰 값을 기록하면 된다.
        """

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def count(elem):
            zeros, ones = 0, 0
            for el in elem:
                if el == "0":
                    zeros += 1
                else:
                    ones += 1
            return zeros, ones

        for s in strs:
            zeros, ones = count(s)
            # dp table을 업데이트하려면 j >= zeros && k >= ones인 경우를 확인해야 하므로, 거꾸로 순회
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)

        return dp[m][n]

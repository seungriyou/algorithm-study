# https://school.programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    """1D DP (optimized)"""

    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for amnt in range(m, n + 1):
            dp[amnt] += dp[amnt - m]

    return dp[n]


def solution2(n, money):
    """2D DP (knapsack)"""

    m = len(money)

    # dp[i][j]: i번째 화폐까지 봤을 때, j원을 만들 수 있는 방법의 개수
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):  # -- 물건
        dp[i][0] = 1
        for j in range(1, n + 1):  # -- 임시 용량
            dp[i][j] = dp[i - 1][j]
            if j >= money[i - 1]:
                dp[i][j] += dp[i][j - money[i - 1]]

    return dp[m][n]

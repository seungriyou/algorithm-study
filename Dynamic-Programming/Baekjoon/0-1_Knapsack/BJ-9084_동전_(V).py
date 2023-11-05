# https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

# ===== 2D DP =====

T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):       # 동전
        for j in range(M + 1):      # 금액
            dp[i][j] += dp[i - 1][j]
            if j >= coins[i]:
                dp[i][j] += dp[i][j - coins[i]]

    print(dp[N][M])


# ===== 1D DP =====

def dp_coin(M, coins):
    dp = [0] * (M + 1)  # dp[j] = j원을 만드는 방법의 수

    for coin in coins:
        if coin > M:
            continue

        dp[coin] += 1   # coins[i] 값에 해당하는 가격은 해당 coin 하나로도 만들 수 있으므로 +1
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]

    return dp[M]


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    print(dp_coin(M, coins))


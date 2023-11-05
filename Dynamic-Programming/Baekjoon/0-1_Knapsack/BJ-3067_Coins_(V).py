# https://www.acmicpc.net/problem/3067
import sys
input = sys.stdin.readline

# ===== 2D DP =====

T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    M = int(input())

    # dp[i][j]: j 원을 만드는 것을 i 번째 동전까지 판단했을 때, 가능한 경우
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1    # -- 0원을 만드는 것은 동전을 하나도 사용하지 않아도 가능

    for i in range(1, N + 1):       # -- 동전
        for j in range(M + 1):      # -- 임시 가격
            # 현재 동전을 사용하지 않고 j원을 만드는 경우의 수를 base로 시작
            dp[i][j] = dp[i - 1][j]

            # 현재 동전을 사용 가능한 경우 (즉, 만들어야 하는 임시 가격이 coins[i] 보다 작지 않은 경우)
            # 현재 동전을 포함하는 경우를 더해줌
            if j >= coins[i]:
                dp[i][j] += dp[i][j - coins[i]]

    print(dp[N][M])


# ===== 1D DP =====

def dp_coin(M, coins):
    dp = [0] * (M + 1)      # dp[j] = j원을 만드는 방법의 수

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

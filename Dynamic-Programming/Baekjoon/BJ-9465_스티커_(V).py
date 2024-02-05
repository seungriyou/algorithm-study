# https://www.acmicpc.net/problem/9465
import sys; input = sys.stdin.readline


def solve(n, stickers):
    # === dp === #
    # dp[i][j] : stickers[i][j]를 붙이는 경우, 가능한 최대 점수
    dp = [[-1] * n for _ in range(2)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n > 1:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

    for j in range(2, n):
        # 바로 전 col의 대각선과 전전 col의 대각선을 비교해야 한다.
        dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + stickers[0][j]
        dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + stickers[1][j]

    return max(dp[0][n - 1], dp[1][n - 1])

def solve_optim(n, stickers):
    # === space-optimized dp (별 차이는 없는 듯) === #
    if n == 1:
        return max(stickers[0][0], stickers[1][0])

    upper_prev_prev = stickers[0][0]
    lower_prev_prev = stickers[1][0]
    upper_prev = lower_prev_prev + stickers[0][1]
    lower_prev = upper_prev_prev + stickers[1][1]

    for j in range(2, n):
        # 바로 전 col의 대각선과 전전 col의 대각선을 비교해야 한다.
        upper_prev_tmp = max(lower_prev, lower_prev_prev) + stickers[0][j]
        lower_prev_tmp = max(upper_prev, upper_prev_prev) + stickers[1][j]

        upper_prev_prev, lower_prev_prev = upper_prev, lower_prev
        upper_prev, lower_prev = upper_prev_tmp, lower_prev_tmp

    return max(upper_prev, lower_prev)


for _ in range(int(input())):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    print(solve_optim(n, stickers))


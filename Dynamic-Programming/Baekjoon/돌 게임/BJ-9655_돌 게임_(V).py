# https://www.acmicpc.net/problem/9655
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1_001    # dp[i]: i개의 돌이 처리될 때, turn의 횟수 (홀수 = 'SK', 짝수 = 'CY')
dp[1] = 1       # 돌 1개: 'SK'         (turn 1회)
dp[2] = 2       # 돌 2개: 'SK' -> 'CY' (turn 2회)

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)

print('SK' if dp[N] % 2 == 1 else 'CY')

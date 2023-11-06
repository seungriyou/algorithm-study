# https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]

# dp[i]: i번째 계단을 포함할 때, 최대 점수
dp = [0] * N
dp[0] = stairs[0]
if N > 1:
    dp[1] = stairs[0] + stairs[1]
if N > 2:
    dp[2] = max(stairs[1] + stairs[2], dp[0] + stairs[2])

for i in range(3, N):
    # dp[i] 값으로 다음의 두 가지 경우 중 더 큰 값을 넣는다.
    #      i-2 i-1  i
    # ----------------
    # (1)   X   O   O   -> dp[i - 3] + stairs[i - 1] + stairs[i]
    # (2)   O   X   O   -> dp[i - 2] + stairs[i]
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[N - 1])

# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline

# O(N)

N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

max_profit = 0
dp = [0] * (N + 1)    # dp[i]: i일 이후로의 max profit (next_day <= N 조건으로 판단하므로 길이가 N + 1이어야 함)

for i in range(N - 1, -1, -1):
    next_day = i + T[i]    # 해당 상담을 한다면 가능한 다음 상담 일

    if next_day <= N:   # 해당 상담이 가능하다면 (next_day == N 이어도, 상담 종료 일자는 next_day - 1)
        dp[i] = max(max_profit, dp[next_day] + P[i])
        max_profit = dp[i]
    else:
        dp[i] = max_profit

print(max_profit)

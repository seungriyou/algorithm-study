# https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)
max_profit = 0

for i in range(N - 1, -1, -1):
    next_day = i + T[i]     # 현재 보고 있는 상담을 진행한다면, 다음 상담을 할 수 있는 날짜

    if next_day <= N:       # 다음 상담 날짜기 가능하다면
        dp[i] = max(dp[next_day] + P[i], max_profit)
        max_profit = dp[i]
    else:
        dp[i] = max_profit

print(max_profit)

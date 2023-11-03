# https://www.acmicpc.net/problem/12852
import sys
input = sys.stdin.readline

N = int(input())
dp = [-1] * (N + 1)  # dp[i] = i를 만드는 최소 연산 횟수
trace = [-1] * (N + 1)

dp[1] = 0   # 1은 0번의 연산으로 만들 수 있다.

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1                       # (3) 1을 뺀다.
    trace[i] = i - 1

    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:   # (2) 2로 나누어 떨어진다면 2로 나눈다.
        dp[i] = dp[i // 2] + 1
        trace[i] = i // 2

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:   # (1) 3으로 나누어 떨어진다면 3으로 나눈다.
        dp[i] = dp[i // 3] + 1
        trace[i] = i // 3

result = []
prev = N
while prev > 0:
    result.append(prev)
    prev = trace[prev]

print(dp[N])
print(*result)

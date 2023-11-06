# https://www.acmicpc.net/problem/11726
import sys
input = sys.stdin.readline

N = int(input())    # N == 1이면 dp[2] 할당 시 IndexError 발생

dp = [0] * 1_001
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10_007

print(dp[N])

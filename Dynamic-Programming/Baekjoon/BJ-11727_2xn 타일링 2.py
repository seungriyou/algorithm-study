# https://www.acmicpc.net/problem/11727
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1_001    # N == 1이면 dp[2] 할당 시 IndexError 발생

# dp[i]: i 번째까지 타일을 놓는 방법의 개수

dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10_007
    # i - 1 번째까지 타일이 채워져 있을 때, i 번째까지 채울 수 있는 방법은 1가지 (2x1 1개)
    # i - 2 번째까지 타일이 채워져있을 때, i 번째까지 채울 수 있는 방법은 2가지 (2x2 1개, 1x2 2개)

print(dp[N])

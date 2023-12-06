# https://www.acmicpc.net/problem/1699
import sys
input = sys.stdin.readline

N = int(input())

# ==== sol 1 ====
def get_power_num(N):
    dp = [0, 1]     # dp[i]: i를 제곱수의 합으로 나타낼 때, 그 제곱수 항의 최소 개수

    for n in range(2, N + 1):
        min_v = int(1e9)
        s = 1
        while s * s <= n:
            min_v = min(min_v, dp[n - s * s])
            s += 1
        dp.append(min_v + 1)

    return dp[N]

print(get_power_num(N))


# ==== sol 2 ====
dp = [i for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if dp[i] > (new_v := dp[i - j * j] + 1):
            dp[i] = new_v

print(dp[N])

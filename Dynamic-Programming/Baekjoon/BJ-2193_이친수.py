# https://www.acmicpc.net/problem/2193
import sys
input = sys.stdin.readline

N = int(input())
dp0 = [0] * (N + 1)     # i 번째 자리가 0으로 끝나는 이친수의 개수
dp1 = dp0[:]            # i 번째 자리가 1로 끝나는 이친수의 개수

dp0[1], dp1[1] = 0, 1

for i in range(2, N + 1):
    dp0[i] = dp0[i - 1] + dp1[i - 1]
    dp1[i] = dp0[i - 1]

print(dp0[N] + dp1[N])

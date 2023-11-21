# https://www.acmicpc.net/problem/1003
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    # n이 0이면 빠르게 출력
    if n == 0:
        print(1, 0)
        continue
    # n이 0보다 크면 DP 수행
    dp0 = [0] * (n + 1)     # dp0[i] = fib(i) 시 0이 출력되는 횟수
    dp1 = [0] * (n + 1)     # dp1[i] = fib(i) 시 1이 출력되는 횟수
    dp0[0] = 1
    dp1[1] = 1
    for i in range(2, n + 1):
        dp0[i] = dp0[i - 1] + dp0[i - 2]
        dp1[i] = dp1[i - 1] + dp1[i - 2]
    print(dp0[n], dp1[n])
    
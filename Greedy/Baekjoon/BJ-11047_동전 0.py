# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

answer = 0
# while K > 0 and coins:
#     coin = coins.pop()
#     cnt = K // coin
#     answer += cnt
#     K -= cnt * coin

while K > 0 and N > 0:
    cnt = K // coins[N - 1]
    answer += cnt
    K -= cnt * coins[N - 1]
    N -= 1

print(answer)

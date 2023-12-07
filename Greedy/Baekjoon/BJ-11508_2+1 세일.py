# https://www.acmicpc.net/problem/11508
import sys
input = sys.stdin.readline

N = int(input())
prices = [int(input()) for _ in range(N)]
prices.sort(reverse=True)       # 내림차순 정렬

result = 0
for i in range(N):
    if i % 3 == 2:
        continue    # 차례로 3개씩 묶었을 때, 그 안에서 가장 작은 수는 넘어가기
    result += prices[i]
print(result)

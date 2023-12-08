# https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]     # 지나온 도시들의 기름값 중 최소 비용 기록
total_cost = 0

for i in range(N - 1):
    # 최소 비용 업데이트
    if costs[i] < min_cost:
        min_cost = costs[i]
    # i 번째 도시에서 i + 1 번째 도시로 가기 위한 비용 계산 후 total_cost에 더하기
    total_cost += min_cost * roads[i]

print(total_cost)

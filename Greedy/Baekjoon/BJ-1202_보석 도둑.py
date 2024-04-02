# https://www.acmicpc.net/problem/1202
import sys; input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)] # (무게, 가격)
bags = [int(input()) for _ in range(K)]                     # 담을 수 있는 최대 무게

gems.sort(key=lambda x: (x[0], -x[1]))  # 무게 기준 오름차순, 가격 기준 내림차순
bags.sort() # 담을 수 있는 최대 무게 기준 오름차순

# 훔칠 수 있는 보석의 "최대 가격" 구하기
price = 0
tmp = []

for bag in bags:
    # 현재 가방에 넣을 수 있는 보석들의 price를 최대 힙에 저장
    while gems and bag >= gems[0][0]:
        _, _price = heapq.heappop(gems)
        heapq.heappush(tmp, -_price)

    # 최대 힙에 원소가 있다면, 즉, 현재 가방에 넣을 수 있는 보석이 있다면,
    # 최대 가격을 가지는 보석을 빼서 price에 반영
    if tmp:
        price -= heapq.heappop(tmp)

print(price)

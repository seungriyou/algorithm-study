# [LTC] 787 - Cheapest Flights Within K Stops

from typing import List
from collections import defaultdict
import heapq


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for a, b, c in flights:
        graph[a].append((b, c))

    # queue = [(가격, 정점, 남은 가능 경유지 수)]
    queue = [(0, src, k)]

    # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
    while queue:
        price, node, k_tmp = heapq.heappop(queue)
        if node == dst:
            return price
        if k_tmp >= 0:
            for b, c in graph[node]:
                alt = price + c
                heapq.heappush(queue, (alt, b, k_tmp - 1))
    return -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))

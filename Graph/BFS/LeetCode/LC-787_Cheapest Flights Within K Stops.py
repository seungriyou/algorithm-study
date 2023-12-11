# [LTC] 787 - Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List
import heapq
from collections import deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # === BFS ===
        graph = [[] for _ in range(n + 1)]
        for f, t, p in flights:
            graph[f].append((t, p))

        q = deque([(src, 0)])
        INF = int(1e9)
        distance = [INF] * (n + 1)
        stops = -1  # -- stop 횟수

        # -- stop 수 마다 같은 level로 취급
        while q and stops < k:
            for i in range(len(q)):
                now, dist = q.popleft()
                for ngbr, p in graph[now]:
                    cost = dist + p
                    if distance[ngbr] > cost:
                        distance[ngbr] = cost
                        q.append((ngbr, cost))
            stops += 1

        return -1 if distance[dst] == INF else distance[dst]

    def findCheapestPrice_TLE(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # === Dijkstra ===
        graph = [[] for _ in range(n + 1)]
        for f, t, p in flights:
            graph[f].append((t, p))

        heap = [(0, src, -1)]

        while heap:
            dist, now, cnt = heapq.heappop(heap)
            if now == dst:
                return dist
            if cnt < k:
                for t, p in graph[now]:
                    cost = dist + p
                    heapq.heappush(heap, (cost, t, cnt + 1))

        return -1

sol = Solution()
print(sol.findCheapestPrice_TLE(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))

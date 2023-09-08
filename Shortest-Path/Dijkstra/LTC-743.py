# [LTC] 743 - Network Delay Time
# https://leetcode.com/problems/network-delay-time/

from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for x, y, w in times:
            graph[x].append((w, y))

        visited = set()
        heap = [(0, k)]

        while heap:
            time, now = heapq.heappop(heap)
            visited.add(now)

            if len(visited) == n:
                return time

            for i in graph[now]:
                if i[1] not in visited:
                    heapq.heappush(heap, (i[0] + time, i[1]))

        return -1

    def networkDelayTime_2(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        INF = int(1e9)
        distance = [INF] * (n + 1)

        def dijkstra(start):
            q = []
            distance[start] = 0
            heapq.heappush(q, (0, start))

            while q:
                dist, now = heapq.heappop(q)
                if distance[now] < dist:
                    continue
                for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))

        dijkstra(k)

        time, cnt = 0, 0
        for i in range(1, n + 1):
            if distance[i] != INF:
                time = max(time, distance[i])
                cnt += 1
        return time if cnt == n else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
print(sol.networkDelayTime(times, n, k))

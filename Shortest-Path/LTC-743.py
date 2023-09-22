# [LTC] 743 - Network Delay Time
# https://leetcode.com/problems/network-delay-time/

from typing import List
from collections import deque


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        INF = int(1e9)
        distance = [INF] * (n + 1)

        def dijkstra(start):
            q = deque([(0, start)])
            distance[start] = 0

            while q:
                time, node = q.popleft()
                if distance[node] < time:
                    continue
                for i in graph[node]:
                    cost = time + i[1]
                    if cost < distance[i[0]]:
                        q.append((cost, i[0]))
                        distance[i[0]] = cost

        dijkstra(k)

        min_time = max(distance[1:])

        return -1 if min_time == INF else min_time


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
print(sol.networkDelayTime(times, n, k))

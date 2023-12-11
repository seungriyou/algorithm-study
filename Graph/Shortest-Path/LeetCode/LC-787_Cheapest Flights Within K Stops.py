# [LC] 787 - Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List
from collections import deque

class Solution:
    def findCheapestPrice_BF2d(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # === 2D DP (Bellman Ford) ===
        # Bellman Ford는 사실 2D DP의 space optimized version이다.
        # 여기에선 1D version을 사용하면 안 된다.

        INF = int(1e5)
        # -- dp[i][j] = i 개의 edge를 확인했을 때, src로부터 j까지의 shortest distance
        dp = [[INF] * n for _ in range(k + 2)]  # -- k stops => k + 1 edges 이므로 1 edge ~ k + 1 edges 이동 기록하기 위해 k + 2 이용

        # -- src로의 거리는 항상 0
        for i in range(k + 2):
            dp[i][src] = 0

        # -- src로부터 edge를 1개부터 k + 1개까지 이동
        for i in range(1, k + 2):
            for f, t, p in flights:
                if dp[i - 1][f] != INF:
                    dp[i][t] = min(dp[i][t], dp[i - 1][f] + p)

        return -1 if dp[-1][dst] == INF else dp[-1][dst]


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # === Bellman Ford*** ===
        # 매번 모든 edge를 전부 확인하는 방법

        INF = int(1e5)
        distance = [INF] * n

        def bellman_ford(start):
            nonlocal distance
            distance[start] = 0

            # -- k stops => k + 1 edges 이므로 1 edge ~ k + 1 edges 이동
            for _ in range(k + 1):
                # 같은 level(= 같은 edge 개수)에서 최단경로가 발견되더라도 멈추지 않도록 함
                next_distance = distance[:]  # -- edge 개수가 1개 적은 경우의 distance[]를 복사
                for f, t, p in flights:
                    cost = distance[f] + p
                    # 현재 edge를 거쳐 t로 이동하는 거리가 더 짧은 경우, next_distance 업데이트
                    if next_distance[t] > cost:
                        next_distance[t] = cost
                distance = next_distance

        bellman_ford(src)

        return -1 if distance[dst] == INF else distance[dst]


    def findCheapestPrice_bfs(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # === BFS ===
        graph = [[] for _ in range(n)]
        for f, t, p in flights:
            graph[f].append((t, p))  # -- (to, price)

        INF = int(1e5)
        distance = [INF] * n

        q = deque([(src, 0)])
        distance[src] = 0

        cnt = -1

        while q and cnt < k:
            adj_num = len(q)
            for _ in range(adj_num):
                now, dist = q.popleft()

                # 방문했던 노드 확인하지 X
                # --> 확인한다는 것은, 이미 방문했던 노드를 마주친 순간 건너뛰어 해당 노드까지의 최단거리까지만 확인하겠다는 뜻
                # --> dst(node[3]) 까지의 k stops 내로 가능한 path가 꼭 중간 노드(node[2])의 최단경로를 포함하리라는 보장이 없음** (stop 수도 고려해야 하므로!)
                # --> 즉, 지금 확인하고 있는 노드의 인접 노드에 k stop 내에 도달 가능한 dst가 존재할 수도 있음. 그냥 건너뛰면 이러한 경우를 볼 수 없음.
                '''
                n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1 인 경우,

                (1) 방문했던 노드 확인 O    : node[2]에서 node[3](=dst)을 방문하기 전에, node[2]까지 도달하는 최단경로를 이미 찾았으므로 
                                         node[2]에서 더이상 진행하지 X
                    cnt=0
                    q=deque([(1, 1), (2, 5)])
                    distance=[0, 1, 5, 100000]

                    cnt=1
                    q=deque([(2, 2)])
                    distance=[0, 1, 2, 100000]

                (2) 방문했던 노드 확인 X    : node[2]까지의 최단경로는 이미 찾았으나, k stops 내에 node[3](=dst)까지 도달 가능한지도 봐야하므로
                                         이렇게 해야 함
                    cnt=0
                    q=deque([(1, 1), (2, 5)])
                    distance=[0, 1, 5, 100000]

                    cnt=1
                    q=deque([(2, 2), (3, 6)])
                    distance=[0, 1, 2, 6]
                '''
                # if distance[now] < dist:
                #     continue

                for t, p in graph[now]:
                    if distance[t] > (cost := dist + p):
                        distance[t] = cost
                        q.append((t, cost))
            cnt += 1

        return -1 if distance[dst] == INF else distance[dst]

sol = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(sol.findCheapestPrice(n, flights, src, dst, k))
print(sol.findCheapestPrice_bfs(n, flights, src, dst, k))

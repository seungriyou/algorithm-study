# [BOJ] 1504 - 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end, graph):
    distance = [INF] * (n + 1)

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

d_1 = dijkstra(1, v1, graph) + dijkstra(v1, v2, graph) + dijkstra(v2, n, graph)
d_2 = dijkstra(1, v2, graph) + dijkstra(v2, v1, graph) + dijkstra(v1, n, graph)

result = min(d_1, d_2)

if result < INF:
    print(result)
else:
    print(-1)

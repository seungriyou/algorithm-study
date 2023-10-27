# [BOJ] 1753 - 최단 경로
# https://www.acmicpc.net/problem/1753

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

INF = int(1e9)

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1)

q = []
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        # i[0] = next node // i[1] = distance
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

for d in distance[1:]:
    if d >= INF:
        print("INF")
    else:
        print(d)

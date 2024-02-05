# https://www.acmicpc.net/problem/1916
import sys
import heapq
input = sys.stdin.readline

N = int(input())    # 도시 개수 (정점)
M = int(input())    # 버스 개수 (간선)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    # a -> b: 비용 c
    graph[a].append((b, c))
src, dst = map(int, input().split())

INF = int(1e9)
distance = [INF] * (N + 1)

def dijkstra(src):
    q = []

    # 출발 지점 설정
    distance[src] = 0
    heapq.heappush(q, (0, src))

    while q:
        d, pos = heapq.heappop(q)

        if distance[pos] < d:
            continue

        for npos, nd in graph[pos]:
            cost = d + nd
            if distance[npos] > cost:
                distance[npos] = cost
                q.append((cost, npos))

dijkstra(src)
print(distance[dst])

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""

# 거리가 1이므로 BFS 이용도 가능
import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

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

dijkstra(1)

max_node = 0
max_distance = 0
result = []
for i in range(1, n + 1):
    if distance[i] > max_distance:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif distance[i] == max_distance:
        result.append(i)

print(max_node, max_distance, len(result))

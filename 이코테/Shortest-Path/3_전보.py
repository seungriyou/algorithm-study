import heapq

n, m, c = map(int, input().split()) # n = 노드, m = 간선, c = 시작
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

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
        for i in graph[now]: # i = (next_node, cost)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
time = 0
for d in distance:
    if d < INF:
        cnt += 1
        time = max(d, time)

print(cnt - 1, time)

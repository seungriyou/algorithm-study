import heapq

n, m = map(int, input().split()) # n = 노드, m = 간선

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for c in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

res = graph[1][k] + graph[k][x]
if res >= INF:
    print(-1)
else:
    print(res)

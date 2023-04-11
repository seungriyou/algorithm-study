# https://www.acmicpc.net/problem/11404

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 = 0
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b]) # 주의 (같은 노선 여러 개일수도)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

for row in graph[1:]:
    print(" ".join([str(r) if r != INF else str(0) for r in row[1:]]))

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print(0, end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()
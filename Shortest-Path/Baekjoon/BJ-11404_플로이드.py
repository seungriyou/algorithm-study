# [BOJ] 11404 - 플로이드
# https://www.acmicpc.net/problem/11404

# 두 도시를 연결하는 노선은 하나가 아닐 수 있다!!!

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

# 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph[1:]:
    print(" ".join(map(str, [r if r < INF else 0 for r in row[1:]])))

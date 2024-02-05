# https://www.acmicpc.net/problem/11265
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
requests = [list(map(int, input().split())) for _ in range(M)]

# ==== floyd-warshall === #
# floyd-warshall
for k in range(N):
    for a in range(N):
        for b in range(N):
            # CAUTION: min()을 사용하면 TLE
            if (d := graph[a][k] + graph[k][b]) < graph[a][b]:
                graph[a][b] = d

# get answers
for request in requests:
    a, b, c = request
    if graph[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")

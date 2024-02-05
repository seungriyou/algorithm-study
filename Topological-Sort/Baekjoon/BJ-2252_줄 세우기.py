# https://www.acmicpc.net/problem/2252
import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    # a -> b
    graph[a].append(b)
    indegree[b] += 1

def topo_sort():
    q = deque()
    result = []

    # indegree 0인 것부터
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        pos = q.popleft()
        result.append(pos)

        for npos in graph[pos]:
            indegree[npos] -= 1
            if indegree[npos] == 0:
                q.append(npos)

    return result

print(*topo_sort())

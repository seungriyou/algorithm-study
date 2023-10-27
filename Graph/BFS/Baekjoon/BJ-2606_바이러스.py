# [BJ] 2606 - 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)

def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = True

    while q:
        pos = q.popleft()
        for npos in graph[pos]:
            if not visited[npos]:
                visited[npos] = True
                q.append(npos)
                cnt += 1

    return cnt

result = bfs(1)
print(result)

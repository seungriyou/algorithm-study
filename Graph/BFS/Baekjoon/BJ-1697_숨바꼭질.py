# https://www.acmicpc.net/problem/1697
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100_001

def bfs(start, target):
    q = deque([start])
    visited[start] = 0

    while q:
        pos = q.popleft()

        for npos in (pos - 1, pos + 1, pos * 2):
            if 0 <= npos <= 100_000 and visited[npos] == -1:
                visited[npos] = visited[pos] + 1
                q.append(npos)

        if visited[target] != -1:
            return visited[target]


print(bfs(N, K))

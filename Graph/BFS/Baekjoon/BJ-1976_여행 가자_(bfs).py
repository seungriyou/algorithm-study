# https://www.acmicpc.net/problem/1976
import sys; input = sys.stdin.readline
from collections import deque

# union-find로도 풀 수 있다!

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
visited = [False] * (N + 1)

def bfs(src):
    q = deque([src])
    visited[src] = True

    while q:
        pos = q.popleft()

        for npos, is_connected in enumerate(graph[pos - 1], start=1):
            if is_connected and not visited[npos]:
                q.append(npos)
                visited[npos] = True

# plan의 첫 출발지점부터 bfs 수행해서, visited 배열 기록
bfs(plan[0])

answer = "YES"
for i in range(1, M):
    if not visited[plan[i]]:
        answer = "NO"
        break

print(answer)

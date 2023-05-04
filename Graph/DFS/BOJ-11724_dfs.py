# [BOJ] 11724 - 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(graph, start, visited):
    # if visited[start]:
    #     return
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)

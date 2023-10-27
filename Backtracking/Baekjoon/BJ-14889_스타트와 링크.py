# [BJ] 14889 - 스타트와 링크
# https://www.acmicpc.net/problem/14889

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_diff = int(1e9)

def backtrack(depth, idx):
    global min_diff

    # base condition
    if depth == n // 2:
        p1 = p2 = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    p1 += graph[i][j]
                if not visited[i] and not visited[j]:
                    p2 += graph[i][j]

        min_diff = min(min_diff, abs(p1 - p2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth + 1, i + 1)
            visited[i] = False

backtrack(0, 0)
print(min_diff)

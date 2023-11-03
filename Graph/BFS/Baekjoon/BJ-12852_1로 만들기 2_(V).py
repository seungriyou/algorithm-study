# https://www.acmicpc.net/problem/12852
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)

def bfs(start):
    q = deque([(start, [start])])

    while q:
        curr, path = q.popleft()

        if curr == 1:
            return len(path) - 1, path

        if not visited[curr]:
            visited[curr] = True
            if curr % 3 == 0:
                q.append((curr // 3, path + [curr // 3]))
            if curr % 2 == 0:
                q.append((curr // 2, path + [curr // 2]))
            q.append((curr - 1, path + [curr - 1]))

op_num, trace = bfs(N)
print(op_num)
print(*trace)

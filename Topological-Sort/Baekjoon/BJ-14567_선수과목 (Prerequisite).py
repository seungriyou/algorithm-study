# https://www.acmicpc.net/problem/14567
import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    # a -> b 가능
    graph[a].append(b)
    # b의 진입 차수 ++
    indegree[b] += 1

def topo_sort():
    q = deque()
    result = [0] * (N + 1)    # 각 과목을 수강하기 위해 필요한 최소 학기 수 기록

    # indegree == 0인 노드부터 q에 넣기
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append((i, 1))    # i 과목(노드), 1학기에 가능

    while q:
        pos, sem = q.popleft()
        # pos 과목은 sem에 가능
        result[pos] = sem

        for npos in graph[pos]:
            indegree[npos] -= 1
            if indegree[npos] == 0:
                q.append((npos, sem + 1))

    return result[1:]

print(*topo_sort())

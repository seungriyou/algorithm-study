# [BOJ] 1240 - 노드사이의 거리

import sys
from collections import deque
from typing import List, Tuple

sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(N: int, graph: List[List[Tuple]], start_v: int, end_v: int) -> int:
    # 방문한 노드는 1, 미방문한 노드는 0
    visited = [0] * (N + 1)
    # star_v로부터의 거리
    distance = [0] * (N + 1)
    # bfs에서 사용하는 queue (방문할 노드)
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        # 다음 노드가 end_v라면 그대로 반환
        if v == end_v:
            return distance[end_v]
        # 미방문 한 노드라면 방문 후 거리 업데이트
        if not visited[v]:
            visited[v] = 1
            for w in graph[v]:
                queue.append(w[0])
                distance[w[0]] = distance[v] + w[1]
    return distance[end_v]


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    # tree는 undirected graph이므로
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(N, graph, a, b))

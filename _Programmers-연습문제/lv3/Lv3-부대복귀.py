# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # BFS로 (거꾸로**) destination -> 가능한 모든 위치로 이동하는 shortest distance 기록
    # NOTE: src -> dest로 접근하면 TLE 발생
    q = deque([destination])
    distance = [-1] * (n + 1)
    distance[destination] = 0

    while q:
        pos = q.popleft()

        for npos in graph[pos]:
            # not visited 이면
            if distance[npos] == -1:
                q.append(npos)
                distance[npos] = distance[pos] + 1

    return [distance[src] for src in sources]

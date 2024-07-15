# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        # 양방향
        graph[a].append((b, c))
        graph[b].append((a, c))

    INF = 1e9
    distance = [INF] * (N + 1)

    def dijkstra(start):
        distance[start] = 0
        q = [(0, start)]

        while q:
            dist, pos = heapq.heappop(q)

            if distance[pos] < dist:
                continue

            for npos, ndist in graph[pos]:
                if (cost := dist + ndist) < distance[npos]:
                    distance[npos] = cost
                    heapq.heappush(q, (cost, npos))

    dijkstra(1)

    return sum(1 for d in distance if d <= K)

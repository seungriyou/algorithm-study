# [BOJ] 1238 - 파티

import sys
import heapq
from typing import List, Tuple, Optional

sys.stdin = open('input.txt')
input = sys.stdin.readline


def dijkstra(graph: List[List[Optional[Tuple]]], start: int) -> List[int]:
    # 모든 사람에 대해 dijkstra를 수행해야하므로 distance list 초기화
    INF = int(1e9)
    distance = [INF] * (N + 1)
    # 우선순위 큐 (최소 힙)
    queue = []
    # start로 가기 위한 최단 경로는 0
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    # 큐가 비어 있지 않다면
    while queue:
        # 최단 경로가 가장 짧은 node 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # (꺼낸 node로의 기존 경로)가 (꺼낸 경로)보다 짧다면 넘어가기
        if distance[now] < dist:
            continue
        # 꺼낸 node와 연결된 다른 node들 확인
        for n in graph[now]:
            cost = dist + n[1]
            # 꺼낸 node를 거쳐 다른 노드로 이동하는 경로가 더 짧은 경우
            if cost < distance[n[0]]:
                distance[n[0]] = cost
                heapq.heappush(queue, (cost, n[0]))

    return distance


# N: node 개수, M: edge 개수, X: dest
N, M, X = map(int, input().split())
# INF = int(1e9)
# distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

times = []
for i in range(1, N+1):
    if i == X:
        continue
    times.append(dijkstra(graph, i)[X] + dijkstra(graph, X)[i])

print(max(times))

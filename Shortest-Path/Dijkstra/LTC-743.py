# [LTC] 743 - Network Delay Time

from typing import List
from collections import defaultdict
import heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    # 그래프 인접 리스트 구성
    for a, b, c in times:
        graph[a].append((b, c))

    # queue : [(소요 시간, 정점)]
    queue = [(0, k)]

    dist = defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while queue:
        time, node = heapq.heappop(queue)
        if node not in dist:
            dist[node] = time
            for b, c in graph[node]:
                alt = time + c
                heapq.heappush(queue, (alt, b))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == n:
        return max(dist.values())
    return -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))

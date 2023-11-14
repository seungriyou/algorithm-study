# [BOJ] 11657 - 타임머신

import sys

sys.stdin = open('../input.txt')
input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start: int) -> bool:
    # 시작 노드로 가기 위한 최단 경로는 0
    distance[start] = 0
    # 최단 경로 구하기
    for _ in range(n - 1):
        # a번 노드 -> b번 노드 가는 거리가 c
        for a, b, c in graph:
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[a] != INF and distance[a] + c < distance[b]:
                distance[b] = distance[a] + c
    # negative cycle 확인
    for a, b, c in graph:
        if distance[a] != INF and distance[a] + c < distance[b]:
            return True     # negative cycle 존재함
    return False            # negative cycle 존재하지 않음


n, m = map(int, input().split())
distance = [INF] * (n + 1)
graph = []
for _ in range(m):
    graph.append(tuple(map(int, input().split())))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우 -1 출력
        if distance[i] == INF:
            print(-1)
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])

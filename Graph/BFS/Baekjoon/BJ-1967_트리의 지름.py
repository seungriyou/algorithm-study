# [BJ] 1967 - 트리의 지름
# https://www.acmicpc.net/problem/1967
"""
트리의 지름(longest path)을 구하려면,
1. 랜덤한 노드에서 BFS를 수행한 후, 가장 먼 노드를 구한다.
2. 1번에서 구한 노드는 트리의 지름을 구성하는 두 노드 중 하나가 될 것이므로,
    해당 노드에서 다시 BFS를 수행하여 가장 먼 노드까지의 거리를 구한다.
"""

from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start):
    q = deque([(start, 0)])
    distance = [-1] * (n + 1)
    distance[start] = 0
    max_d = max_di = 0
    # max_d: 가장 먼 노드까지의 거리
    # max_di: 가장 먼 노드의 번호

    while q:
        pos, d = q.popleft()

        for npos, nd in graph[pos]:
            if distance[npos] == -1:
                dist = distance[pos] + nd
                distance[npos] = dist
                q.append((npos, dist))
                # 가장 먼 노드까지의 거리 & 번호 트래킹
                if dist > max_d:
                    max_d = dist
                    max_di = npos

    return max_d, max_di

# 1. random 노드에서 BFS 돌리기 -> 가장 먼 노드 찾기
_, max_di = bfs(1)

# 2. 1번에서 찾은 노드에서 다시 가장 먼 노드까지의 거리 찾기
max_d, _ = bfs(max_di)

print(max_d)

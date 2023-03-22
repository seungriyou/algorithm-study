from collections import defaultdict
import heapq

"""
edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G'),
]

visited = [0] * (n + 1) # 노드의 방문 정보 초기화
graph = defaultdict(list)

# 무방향 그래프 생성
for u, v, weight in edges:
    graph[u].append((weight, u, v))
    graph[v].append((weight, v, u))
"""

n, m = map(int, input().split()) # 노드 수, 간선 수
visited = [0] * (n + 1) # 노드의 방문 정보 초기화
graph = defaultdict(list)

# 무방향 그래프 생성
for i in range(m):
    # 간선 정보 입력 받기 (u, v, weight)
    u, v, weight = map(int, input().split())
    graph[u].append((weight, u, v))
    graph[v].append((weight, v, u))

def prim(graph, start_node):
    visited[start_node] = 1
    candidate = graph[start_node] # 인접 간선
    heapq.heapify(candidate) # 우선순위 큐 생성
    mst = list()
    total_weight = 0 # 전체 가중치

    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 작은 간선 추출
        # 방문하지 않은 정점이라면
        if visited[v] == 0:
            visited[v] = 1
            mst.append((u, v)) # mst에 추가
            total_weight += weight

            for edge in graph[v]: # 다음 인접 간선 탐색
                # 방문하지 않은 정점이라면
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge) # 우선순위 큐에 간선 삽입

    return total_weight

print(prim(graph, 1))

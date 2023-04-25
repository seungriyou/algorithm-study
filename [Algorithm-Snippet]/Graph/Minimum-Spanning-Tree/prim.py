import heapq

n, m, start = map(int, input().split()) # 노드 수, 간선 수, 시작 노드
visited = [False] * (n + 1) # 노드의 방문 정보 초기화
graph = [[] for _ in range(n + 1)]

# 무방향 그래프 생성
for i in range(m):
    # 간선 정보 입력 받기 (u, v, weight)
    u, v, weight = map(int, input().split())
    graph[u].append((weight, u, v))
    graph[v].append((weight, v, u))


def prim(start):
    visited[start] = True
    candidate = graph[start] # 인접 간선
    heapq.heapify(candidate) # 우선순위 큐로 변환
    mst = list()
    total_weight = 0 # 전체 가중치

    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 작은 간선 추출

        # 방문하지 않은 정점이라면
        if not visited[v]:
            visited[v] = True
            mst.append((u, v)) # mst에 추가
            total_weight += weight

            for edge in graph[v]: # 다음 인접 간선 탐색
                # 방문하지 않은 정점이라면
                if not visited[edge[2]]:
                    heapq.heappush(candidate, edge) # 우선순위 큐에 간선 삽입

    return total_weight

print(prim(start))

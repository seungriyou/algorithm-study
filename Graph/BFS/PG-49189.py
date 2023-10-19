# [PG] 49189 - 가장 먼 노드 (Lv3)
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

def solution_bfs(n, edge):
    # === BFS ===

    from collections import deque

    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    distance = [-1] * (n + 1)  # -- -1: not visited / >= 0: visited & distance

    def bfs(start):
        q = deque([start])
        distance[start] = 0

        while q:
            curr = q.popleft()
            for ngbr in graph[curr]:
                if distance[ngbr] == -1:  # -- if not visited
                    distance[ngbr] = distance[curr] + 1  # -- 이전 node 까지의 distance에 1을 더해줌
                    q.append(ngbr)

    bfs(1)

    max_distance = max(distance)
    answer = 0
    for d in distance:
        answer += d == max_distance

    return answer


def solution(n, edge):
    # === Dijkstra ===
    import heapq

    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    INF = int(1e9)
    distance = [0] + [INF] * n

    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, curr = heapq.heappop(q)

            if distance[curr] < dist:
                continue

            for ngbr in graph[curr]:
                cost = dist + 1
                if cost < distance[ngbr]:
                    distance[ngbr] = cost
                    heapq.heappush(q, (cost, ngbr))

    dijkstra(1)

    max_distance = max(distance)
    answer = 0

    for d in distance:
        answer += d == max_distance

    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
assert 3 == solution(n, edge) == solution_bfs(n, edge)

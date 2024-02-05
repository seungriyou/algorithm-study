# https://www.acmicpc.net/problem/11265
import sys; input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[0] + list(map(int, input().split())) for _ in range(N)]
graph = [[]] + graph
requests = [list(map(int, input().split())) for _ in range(M)]

# ==== cached-dijkstra === #
cache = [[] for _ in range(N + 1)]

INF = int(1e9)

def dijkstra(src, dst):
    distance = [INF] * (N + 1)

    q = []
    heapq.heappush(q, (0, src))
    distance[src] = 0

    while q:
        d, pos = heapq.heappop(q)
        if distance[pos] < d:
            continue
        for npos in range(1, N + 1):
            cost = d + graph[pos][npos]
            if cost < distance[npos]:
                distance[npos] = cost
                heapq.heappush(q, (cost, npos))

    # src부터 시작했을 때의 dijkstra 결과 distance 배열 caching
    cache[src] = distance

    return distance[dst]

def get_answer(computed_min_time, max_time):
    return "Enjoy other party" if computed_min_time <= max_time else "Stay here"

for request in requests:
    s, d, c = request
    if cache[s]:
        print(get_answer(cache[s][d], c))
    else:
        print(get_answer(dijkstra(s, d), c))

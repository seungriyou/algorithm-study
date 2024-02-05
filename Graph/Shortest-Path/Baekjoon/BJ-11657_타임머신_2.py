# https://www.acmicpc.net/problem/11657
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

INF = int(1e9)
distance = [INF] * (N + 1)

def bellman_ford(src):
    # negative cycle이 존재하면 True 반환

    distance[src] = 0
    # 노드의 개수 N만큼 relaxation 진행
    for i in range(N):
        # 각 과정에서 모든 간선(edges) 확인
        for pos, npos, dist in edges:
            cost = distance[pos] + dist
            if distance[pos] != INF and cost < distance[npos]:
                distance[npos] = cost
                # 만약 N 번째 relaxation에서도 distance 업데이트가 발생한다면, negative cycle 존재
                if i == N - 1:
                    return True
    return False

has_negative_cycle = bellman_ford(1)
if has_negative_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if (d := distance[i]) != INF:
            print(d)
        else:
            print(-1)

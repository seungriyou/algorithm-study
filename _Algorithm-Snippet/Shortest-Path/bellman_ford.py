import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b: 비용 c
    edges.append((a, b, c))

def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 n 번의 라운드 반복
    for i in range(n):
        # 매 반복마다 모든 간선 확인
        for j in range(m):
            now_node, next_node, dist = edges[j]
            # 현재 간선을 거쳐 next_node로 이동하는 거리가 더 짧은 경우
            cost = dist + distance[now_node]
            if distance[now_node] != INF and cost < distance[next_node]: #distance[now_node] + dist:
                distance[next_node] = cost # distance[now_node] + dist
                # n번째 라운드에서드 값이 갱신된다면 음수 순환이 존재하는 것
                if i == n - 1:
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(start) # 시작 노드 = 1

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1): # 시작 노드인 1번 노드 제외
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i], end=" ")

from collections import deque

n, m, k, x = map(int, input().split()) # n = 도시 개수, m = 도로 개수, k = 거리 정보, x = 출발 도시 번호
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)

def bfs(start):
    q = deque([start])
    distance[start] = 0
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1: # if not visited
                q.append(next_node)
                distance[next_node] = distance[now] + 1
bfs(x)

result = [str(i) for i in range(1, n + 1) if distance[i] == k]
if result:
    print("\n".join(result))
else:
    print(-1)

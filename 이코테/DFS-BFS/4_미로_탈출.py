from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, [*input()])))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        # 상하좌우를 모두 살펴보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))

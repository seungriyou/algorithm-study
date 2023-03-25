n, m = map(int, input().split())
ice_container = []
for _ in range(n):
    ice_container.append(list(map(int, [*input()])))

# 특정 노드를 방문한 후, 인접한 모든 노드 확인
def dfs(graph, x, y):
    # 범위를 벗어나면 False
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면 상하좌우로 호출
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 재귀 호출
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return True
    else:
        return False

cnt = 0
# graph 내 모든 위치에서 dfs를 진행해보기
for i in range(n):
    for j in range(m):
        if dfs(ice_container, i, j):
            cnt += 1

print(cnt)

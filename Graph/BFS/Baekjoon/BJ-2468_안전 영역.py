# https://www.acmicpc.net/problem/2468
import sys
from collections import defaultdict, deque
import copy
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# ===== sol1 =====
# 결국 물을 채우는 것 == visited 표시하는 것!

# 각 height 별 좌표 모으기
height_coord = defaultdict(list)
for i in range(N):
    for j in range(N):
        height_coord[graph[i][j]].append((i, j))

# heights를 오름차순 정렬
heights = sorted(height_coord.keys())
max_cnt = 1     # -- 아무 지역도 물에 잠기지 않을 수 있기 때문에 최소 안전 지역의 개수는 1로 설정!


def bfs(x, y, graph):
    q = deque([(x, y)])
    graph[x][y] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != -1:
                graph[nx][ny] = -1
                q.append((nx, ny))


# 등장하는 height의 오름차순 순서대로 물 채워나가기
for h in heights:
    # graph에 물 채우기 (다음 height를 볼 때도 -1로 처리되어 있어야 함)
    for i, j in height_coord[h]:
        graph[i][j] = -1

    # graph 복사 (bfs 과정에서 -1로 visited 표시 해야하므로)
    copied_graph = copy.deepcopy(graph)

    # 물에 잠기지 않은 곳 세기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if copied_graph[i][j] != -1:
                bfs(i, j, copied_graph)
                cnt += 1

    # 안전 영역의 최대 개수 업데이트
    max_cnt = max(max_cnt, cnt)

print(max_cnt)


# ===== sol2 (faster) =====
# height 이하 높이를 visited로 표시하는 것이 아닌 조건 추가!

max_cnt = 1     # -- 아무 지역도 물에 잠기지 않을 수 있기 때문에 최소 안전 지역의 개수는 1로 설정

def count_safe_area(height):    # height 이하 높이는 물에 잠긴다

    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > height:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > height:
                bfs(i, j)
                cnt += 1

    return cnt


# height의 종류를 set()을 이용하여 구하기
# heights = set()
# for row in graph:
#     heights |= set(row)
heights = {r for row in graph for r in row}     # set comprehension
# comprehension에서는 unpacking 불가! 대신에 for 문 한 번 더 사용할 수 있음
# ref: https://stackoverflow.com/questions/37279653/unpacking-tuples-in-a-python-list-comprehension-cannot-use-the-operator

for h in heights:
    # 안전 영역의 최대 개수 업데이트
    max_cnt = max(max_cnt, count_safe_area(h))

print(max_cnt)

# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크 -> 데이터 갱신
def process(x, y, index, union):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))

    # BFS
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당

    population = graph[x][y] # 현재 연합의 전체 인구수
    cnt = 1 # 현재 연합의 국가 수

    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하며 (범위 내 && 아직 연합 할당 X)
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    population += graph[nx][ny]
                    cnt += 1
                    united.append((nx, ny))

    # 연합 국가끼리 인구 분배
    for i, j in united:
        graph[i][j] = population // cnt

    return cnt

total_cnt = 0 # 인구 이동 횟수

# 더이상 인구 이동이 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)] # 연합 새로 정의
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 국가가 아직 처리되지 않았다면
                process(i, j, index, union)
                index += 1 # 인덱스 증가
    # 모든 인구 이동이 끝난 경우
    # (-> 연합이 새로 생성 X -> 각각이 모두 다른 연합에 속합 -> 위의 if문에 모두 걸리게 됨)
    if index == n * n:
        break
    # 인구 이동 횟수 ++
    total_cnt += 1

print(total_cnt)

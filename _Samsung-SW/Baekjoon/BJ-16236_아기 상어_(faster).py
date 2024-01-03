# https://www.acmicpc.net/problem/16236
import sys
import heapq
input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# TIP: 각 단계에서마다 상어가 먹을 수 있는 모든 물고기를 탐색할 필요가 있을까?

def solution(N, space):
    """
    deque와 heapq를 모두 쓸 필요 없이, heapq 하나만으로도 로직을 작성할 수 있다.
    bfs는 어차피 거리가 작은 순으로 방문하게 되기 때문이다.

    이렇게 하면 각 단계에서마다 상어가 먹을 수 있는 모든 물고기들을 확인할 필요가 없이,
    조건에 가장 부합하는 물고기를 하나 만났을 때 곧바로 물고기 탐색이 종료되어
    바로 다음 단계로 진행할 수 있으므로 시간적으로 효율적이다.
    """

    # 상어의 크기 초기화
    size = 2

    # 상어의 현재 크기에서 먹은 물고기의 수
    cnt = 0

    # 구하고자 하는 시간 값
    result = 0

    # 현재 상어의 위치 기록
    q = []
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                space[i][j] = 0
                heapq.heappush(q, (0, i, j))    # (거리, x좌표, y좌표) 순서대로 heap에 저장
                break

    # bfs
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(N)]

    while q:
        d, x, y = heapq.heappop(q)

        # 현재 위치가 (1) 물고기이면서 (2) 먹을 수 있는 물고기(< size)인 경우, 물고기 먹기
        if 0 < space[x][y] < size:
            # 물고기를 먹었으므로 빈칸으로 변경
            space[x][y] = 0

            # 상어 크기 업데이트 검사
            cnt += 1
            if cnt == size:
                size += 1
                cnt = 0

            # 물고기까지의 거리를 시간으로 누적
            result += d

            # 현재 위치부터 다시 bfs 수행해야하므로 초기화
            d = 0       # 최단거리 찾기용 d 초기화
            q.clear()
            visited = [[False] * N for _ in range(N)]

        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 현재 위치가 (1) 범위를 벗어나지 않고 (2) 방문하지 않았으며 (3) 지나갈 수 있는 곳(<= size)인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and space[nx][ny] <= size:
                visited[nx][ny] = True
                # deque를 이용하더라도 bfs에서는 거리순으로 정렬되기는 하지만, x좌표와 y좌표 순서로도 정렬을 한 번에 하도록 heapq 이용
                heapq.heappush(q, (d + 1, nx, ny))  # (거리, x좌표, y좌표) 순으로 우선순위 부여

    return result


print(solution(N, space))

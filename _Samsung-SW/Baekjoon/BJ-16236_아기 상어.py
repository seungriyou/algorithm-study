# https://www.acmicpc.net/problem/16236
import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]


def bfs(sx: int, sy: int, size: int) -> list[tuple[int, int, int]]:
    """
    각 단계마다 상어의 현재 위치에서 각 물고기로의 최단 거리를 구하는 함수
    - BFS + 조건 판단
    - 먹을 수 있는 물고기의 리스트 반환 (필요한 정보: 시간(= 거리), 물고기의 위치)
    """

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * N for _ in range(N)]

    q = deque([(0, sx, sy)])
    visited[sx][sy] = True
    edible_fish = []

    while q:
        d, x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위를 벗어나지 않고 방문하지 않았는지 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 지나갈 수 있는 곳(<= size)이라면 방문하기
                if space[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((d + 1, nx, ny))

                    # 먹을 수 있는 물고기(< size)가 위치해 있었다면 먹기
                    if 0 < space[nx][ny] < size:
                        # 먹을 수 있는 물고기의 (거리, x좌표, y좌표)를 기록
                        # - len(edible_fish) > 1일 때, 우선순위 순서를 고려
                        # - 최소 힙에서는 [0] 인덱스에 위치하는 원소가 최소
                        # - bfs() 호출하는 쪽에서는 (1) 거리를 통해 시간을 계산하고, (2) x, y좌표를 통해 빈칸으로 설정 및 상어 위치 업데이트
                        heapq.heappush(edible_fish, (d + 1, nx, ny))

    return edible_fish


def solution():
    # 상어의 초기 크기
    size = 2

    # 현재 크기에서 먹은 물고기의 수
    fish_cnt = 0

    # 상어의 초기 위치 찾기
    sx, sy = -1, -1
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                space[i][j] = 0  # 빈칸 설정
                sx, sy = i, j  # 상어의 위치
                break

    # 엄마 상어에게 도움 요청 없이 물고기를 잡아 먹을 수 있는 시간
    result = 0

    while True:
        # 1. 상어의 현재 위치에서 먹을 수 있는 모든 물고기의 (거리, x좌표, y좌표) 계산
        edible_fish = bfs(sx, sy, size)

        # 2. 먹을 수 있는 물고기가 없다면 종료
        if not edible_fish:
            return result

        # 3. 먹을 수 있는 물고기가 있다면, 그 중 우선순위가 가장 높은 물고기 추출
        # (edible_fish가 여러 마리라면, 가장 가까운 > 가장 위의 > 가장 왼쪽의 물고기 순서로 우선순위)
        t, x, y = edible_fish[0]

        # 4. 먹은 물고기 수 증가 및 상어 크기 업데이트 검사 (size와 같은 수의 물고기를 먹으면 size++)
        fish_cnt += 1
        if fish_cnt == size:
            size += 1
            fish_cnt = 0

        # 5. 먹은 물고기까지의 거리를 이용하여 시간 업데이트
        result += t

        # 6. 먹은 물고기의 자리를 빈칸으로 바꾸고, 상어의 위치를 해당 위치로 옮겨주기
        space[x][y] = 0
        sx, sy = x, y

    return result


print(solution())

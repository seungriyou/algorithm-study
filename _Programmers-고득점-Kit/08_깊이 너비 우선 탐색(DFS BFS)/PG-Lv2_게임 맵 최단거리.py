# [PG] 1844 - 게임 맵 최단거리 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    """
    최단거리를 찾는다   -> bfs로 접근하면서, visit 하지 않은 곳만을 방문한다.
                    -> 이전 위치의 값에서 1씩 늘려가며 저장한다.
    """
    n, m = len(maps), len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 확인 & 벽인지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m or not maps[nx][ny]:
                continue

            # 방문하지 않았던 곳인지 확인
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    return maps[-1][-1] if maps[-1][-1] > 1 else -1


def solution2(maps):
    answer = 0

    """
    BFS (최단거리)
    - 목표에 도달하면 거리
    - 목표에 도달하지 못하면 -1
    """

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    N, M = len(maps), len(maps[0])

    def bfs():
        q = deque([(0, 0)])
        distance = [[0] * M for _ in range(N)]  # 거리
        maps[0][0] = 0  # visited 처리

        while q:
            r, c = q.popleft()

            if r == N - 1 and c == M - 1:
                return distance[r][c] + 1

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and maps[nr][nc]:
                    q.append((nr, nc))
                    maps[nr][nc] = 0
                    distance[nr][nc] = distance[r][c] + 1

        return -1

    answer = bfs()

    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
assert 11 == solution(maps)

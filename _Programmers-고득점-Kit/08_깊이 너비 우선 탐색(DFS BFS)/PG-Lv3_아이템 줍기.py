# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 모두 2배 늘림
    max_row = 2 * (max(rec[2] for rec in rectangle) + 1)
    max_col = 2 * (max(rec[3] for rec in rectangle) + 1)

    # grid[i][j] = -1: 빈 공간, 1: 합쳐진 공간의 테두리, 0: 합쳐진 공간의 내부
    grid = [[-1] * max_col for _ in range(max_row)]

    def combine_rectangles(rectangle):
        for rec in rectangle:
            x1, y1, x2, y2 = map(lambda x: x * 2, rec)

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    # 어떤 직사각형의 내부라면 먼저 0으로 채우기
                    if x1 < x < x2 and y1 < y < y2:
                        grid[x][y] = 0
                    # 어떤 직사각형의 테두리이면서 다른 직사각형의 내부가 아니라면 1로 채우기
                    elif grid[x][y] != 0:
                        grid[x][y] = 1

    def bfs(x, y, tx, ty):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = deque([(x, y, 0)])
        grid[x][y] = 0  # visited 처리

        dist = 0
        while q:
            x, y, dist = q.popleft()

            # target 발견 시 멈추기
            if x == tx and y == ty:
                break

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 아직 방문하지 않은 테두리라면, q에 넣고 visited 처리
                # 좌표를 2배 했으므로, 좌표가 격자를 벗어나는지 확인하지 않아도 ok
                if grid[nx][ny] == 1:
                    q.append((nx, ny, dist + 1))
                    grid[nx][ny] = 0

        return dist // 2

    combine_rectangles(rectangle)
    result = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2)  # 모든 좌표를 2배 늘려준다!

    return result

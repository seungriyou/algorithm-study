# https://school.programmers.co.kr/learn/courses/30/lessons/159993

def solution(maps):
    from collections import deque

    """
    (1) 시작(S) -> 레버(L) 칸으로 가기 (2) 레버(L) -> 출구(E) 칸으로 가기
        (1) 통로(O) & 출구(E) 칸 지날 수 있음
        (2) 통로(O) 칸 지날 수 있음
    각 칸은 여러 번 지날 수 있음
    """

    row, col = len(maps), len(maps[0])
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    def min_time(start, end):
        r, c = start
        q = deque([(r, c, 0)])

        visited = [[False] * col for _ in range(row)]
        visited[r][c] = True

        while q:
            r, c, time = q.popleft()

            # end에 도달했다면 현재 time 반환
            if (r, c) == end:
                return time

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                # (1) 범위를 벗어나지 않고 (2) 방문하지 않았으며 (3) 벽이 아닌 곳이라면 이동
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and maps[nr][nc] != "X":
                    q.append((nr, nc, time + 1))
                    visited[nr][nc] = True

        # end에 도달하지 못하는 경우 -1 반환
        return -1

    # S, L, E 좌표 구하기
    S, L, E = None, None, None
    for r in range(row):
        if S and L and E:
            break
        for c in range(col):
            if maps[r][c] == "S":
                S = (r, c)
            elif maps[r][c] == "L":
                L = (r, c)
            elif maps[r][c] == "E":
                E = (r, c)

    # S -> L 또는 L -> E 중에서 -1이 있다면 탈출할 수 X
    if (first_pass := min_time(S, L)) == -1 or (second_pass := min_time(L, E)) == -1:
        return -1
    else:
        return first_pass + second_pass

# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def solution(board):
    """BFS"""

    from collections import deque

    row, col = len(board), len(board[0])
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = deque()
    visited = [[False] * col for _ in range(row)]

    # 시작 위치 구하기
    for r in range(row):
        if q:
            break
        for c in range(col):
            if board[r][c] == "R":
                q.append((r, c, 0))
                visited[r][c] = True
                break

    def is_valid(r, c):
        return 0 <= r < row and 0 <= c < col

    def move(r, c, d):
        """
        (r, c): 시작 좌표
        d: 방향
        """

        nr, nc = r + dr[d], c + dc[d]

        # 방향 d로 (1) 맨 끝이나 (2) 장애물에 부딪힐 때까지 미끄러져 이동
        while is_valid(nr, nc) and board[nr][nc] != "D":
            r, c = nr, nc
            nr, nc = r + dr[d], c + dc[d]

        return (r, c)


    while q:
        r, c, cnt = q.popleft()

        if board[r][c] == "G":
            return cnt

        for d in range(4):
            # d 방향으로 미끄러져 이동
            nr, nc = move(r, c, d)

            # (1) 이동한 위치가 범위 내이고 (2) 이전에 방문한 적이 없으면 이동
            if is_valid(nr, nc) and not visited[nr][nc]:
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = True

    return -1

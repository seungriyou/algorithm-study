# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution2(maps):
    """DFS"""
    import sys
    sys.setrecursionlimit(10001)

    answer = []

    row, col = len(maps), len(maps[0])
    visited = [[False] * col for _ in range(row)]

    def dfs(r, c):
        if not (0 <= r < row and 0 <= c < col) or maps[r][c] == "X" or visited[r][c]:
            return 0

        visited[r][c] = True

        return int(maps[r][c]) + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

    for r in range(row):
        for c in range(col):
            if maps[r][c] != "X" and not visited[r][c]:
                answer.append(dfs(r, c))

    return sorted(answer) if answer else [-1]


def solution3(maps):
    """DFS"""
    import sys
    sys.setrecursionlimit(10001)

    answer = []

    new_maps = []
    for map in maps:
        tmp = []
        for m in map:
            if m == "X":
                tmp.append(-1)
            else:
                tmp.append(int(m))
        new_maps.append(tmp)

    row, col = len(maps), len(maps[0])

    def dfs(r, c):
        if not (0 <= r < row and 0 <= c < col) or new_maps[r][c] == -1:
            return 0

        val = int(maps[r][c])
        new_maps[r][c] = -1

        return val + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

    for r in range(row):
        for c in range(col):
            if new_maps[r][c] != -1:
                answer.append(dfs(r, c))

    return sorted(answer) if answer else [-1]


def solution(maps):
    """BFS"""
    from collections import deque

    answer = []

    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    row, col = len(maps), len(maps[0])
    visited = [[False] * col for _ in range(row)]

    def bfs(r, c):
        q = deque([(r, c)])

        val = int(maps[r][c])
        visited[r][c] = True

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] != "X" and not visited[nr][nc]:
                    val += int(maps[nr][nc])
                    visited[nr][nc] = True
                    q.append((nr, nc))

        return val

    for r in range(row):
        for c in range(col):
            if maps[r][c] != "X" and not visited[r][c]:
                answer.append(bfs(r, c))

    return sorted(answer) if answer else [-1]


def solution1(maps):
    """BFS"""
    from collections import deque

    answer = []

    new_maps = []
    for map in maps:
        tmp = []
        for m in map:
            if m == "X":
                tmp.append(-1)
            else:
                tmp.append(int(m))
        new_maps.append(tmp)

    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    row, col = len(maps), len(maps[0])

    def bfs(r, c, maps):
        q = deque([(r, c)])

        val = maps[r][c]
        maps[r][c] = -1

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] != -1:
                    val += maps[nr][nc]
                    maps[nr][nc] = -1
                    q.append((nr, nc))

        return val

    for r in range(row):
        for c in range(col):
            if new_maps[r][c] != -1:
                answer.append(bfs(r, c, new_maps))

    return sorted(answer) if answer else [-1]

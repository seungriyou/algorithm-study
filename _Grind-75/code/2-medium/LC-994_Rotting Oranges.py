# https://leetcode.com/problems/rotting-oranges/

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        mins = 0
        m, n = len(grid), len(grid[0])

        rotten, fresh = deque(), set()

        # not changing the input
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        while rotten and fresh:
            mins += 1

            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) in fresh:
                        rotten.append((nr, nc))
                        fresh.remove((nr, nc))

        return mins if not fresh else -1


    def orangesRotting1(self, grid: List[List[int]]) -> int:
        from collections import deque

        mins = 0
        m, n = len(grid), len(grid[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0)) # (r, c, sec)
                    grid[i][j] = 0      # visited 처리

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        while q:
            r, c, sec = q.popleft()
            mins = sec

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # 범위를 벗어나지 않고 fresh orange 이면
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    # queue에 넣기
                    q.append((nr, nc, sec + 1))
                    # visited 처리
                    grid[nr][nc] = 0

        # fresh orange가 남아있다면 -1 반환
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return mins


    def orangesRotting2(self, grid: List[List[int]]) -> int:
        from collections import deque

        mins = 0
        m, n = len(grid), len(grid[0])

        q = deque()
        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    grid[i][j] = 0      # visited 처리

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        while q and fresh_oranges:
            mins += 1

            for _ in range(len(q)):
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    # 범위를 벗어나지 않고 fresh orange 이면
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        # queue에 넣기
                        q.append((nr, nc))
                        # visited 처리
                        grid[nr][nc] = 0
                        # fresh orange 1 감소
                        fresh_oranges -= 1

        return mins if not fresh_oranges else -1

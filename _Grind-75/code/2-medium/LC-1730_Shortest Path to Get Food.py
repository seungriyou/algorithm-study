# https://leetcode.com/problems/shortest-path-to-get-food/

from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        """
        any food cell에 도달할 수 있는 shortest path의 length 반환
        food에 도달할 수 없다면 -1 반환
        -> BFS

        - TC: O(m * n) (every cell)
        - SC: O(m * n) (deque)
        """
        from collections import deque

        dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
        row, col = len(grid), len(grid[0])

        # 현재 위치 찾기
        r, c = None, None
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "*":
                    r, c = i, j
                    break
            if r and c:
                break

        # BFS
        q = deque([(r, c, 0, grid[r][c])])
        grid[r][c] = "X"

        while q:
            r, c, _len, _type = q.popleft()

            if _type == "#":
                return _len

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != "X":
                    q.append((nr, nc, _len + 1, grid[nr][nc]))
                    grid[nr][nc] = "X"

        return -1

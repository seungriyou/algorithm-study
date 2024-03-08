# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """BFS"""
        from collections import deque

        m, n = len(grid), len(grid[0])
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        cnt = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

            return 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += bfs(i, j)

        return cnt

    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        """DFS"""

        m, n = len(grid), len(grid[0])
        cnt = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1

        return cnt

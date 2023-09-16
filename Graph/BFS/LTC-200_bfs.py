# [LTC] 200 - Number of Islands (BFS)
# https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # === BFS ===
        row = len(grid)
        col = len(grid[0])

        dr = [-1, 1, 0, 0, ]
        dc = [0, 0, -1, 1]

        """
        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))

        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    bfs(r, c)
                    cnt += 1
        """

        def bfs(r, c):
            if grid[r][c] == '0':
                return 0

            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))

            return 1

        cnt = 0
        for r in range(row):
            for c in range(col):
                cnt += bfs(r, c)

        return cnt

sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))

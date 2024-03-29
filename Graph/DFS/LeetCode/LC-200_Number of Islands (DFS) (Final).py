# [LTC] 200 - Number of Islands (DFS)
# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # === DFS ===
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    cnt += 1

        return cnt

sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))

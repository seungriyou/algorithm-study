# [LTC] 200 - Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(x, y):
            # 범위를 벗어났거나 땅이 아닌 경우 종료
            if (x < 0 or x >= row or y < 0 or y >= col
                    or grid[x][y] != "1"):
                return

            # 방문하지 않은 경우(if grid[x][y] == "1")
            # -- 방문 처리
            grid[x][y] = "0"
            # -- 인접 노드 확인
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1

        return cnt

sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid))

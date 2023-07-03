# [LTC] 200 - Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            row = len(grid)
            col = len(grid[0])

            # 범위 확인
            if x < 0 or x >= row or y < 0 or y >= col:
                return False

            # 방문하지 않은 경우(= 육지, 1),
            if grid[x][y] == "1":
                # 방문 처리
                grid[x][y] = "0"
                # 인접 노드 확인
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
                return True
            else:
                return False

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if dfs(grid, i, j):
                #     cnt += 1
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

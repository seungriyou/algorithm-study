# [LTC] 417 - Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # === DFS ===
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        rows, cols = len(heights), len(heights[0])
        visited_p, visited_a = set(), set()

        def dfs(x, y, visited):
            if (x, y) in visited:
                return

            visited.add((x, y))

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= heights[x][y]:  # -- 가장자리부터 거꾸로 찾아나가므로
                    dfs(nx, ny, visited)

        for r in range(rows):
            dfs(r, 0, visited_p)
            dfs(r, cols - 1, visited_a)

        for c in range(cols):
            dfs(0, c, visited_p)
            dfs(rows - 1, c, visited_a)

        return list(visited_p & visited_a)

sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))

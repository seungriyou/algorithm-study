# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]

        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        r = c = d = 0

        for val in range(n * n):
            grid[r][c] = val + 1

            nr, nc = r + dr[d], c + dc[d]
            # (1) grid를 벗어났거나 (2) 이미 visited 라면, 방향을 시계방향 90도 틀기
            if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc]:
                d = (d + 1) % 4
                nr, nc = r + dr[d], c + dc[d]

            r, c = nr, nc

        return grid

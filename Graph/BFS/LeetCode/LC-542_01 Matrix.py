# [LC] 542 - 01 Matrix
# https://leetcode.com/problems/01-matrix/

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # === DP & BFS (w/o visited) ===
        m = len(mat)
        n = len(mat[0])
        q = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1  # -- mark as not visited yet

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or nx >= m or ny < 0 or ny >= n or mat[nx][ny] != -1:
                    continue

                mat[nx][ny] = mat[x][y] + 1
                q.append((nx, ny))

        return mat

    def updateMatrix_1(self, mat: List[List[int]]) -> List[List[int]]:
        # === DP & BFS ===
        m = len(mat)
        n = len(mat[0])
        q = deque([])
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in visited:
                    continue

                visited.add((nx, ny))
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx, ny))

        return mat

sol = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(sol.updateMatrix(mat))

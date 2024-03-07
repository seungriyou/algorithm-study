# https://leetcode.com/problems/01-matrix/

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """DP"""
        m, n = len(mat), len(mat[0])
        INF = int(1e4)

        # left, top
        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    top = mat[i - 1][j] if i > 0 else INF
                    left = mat[i][j - 1] if j > 0 else INF
                    mat[i][j] = min(top, left) + 1

        # right, bottom
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] > 0:
                    bottom = mat[i + 1][j] if i < m - 1 else INF
                    right = mat[i][j + 1] if j < n - 1 else INF
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

        return mat

    def updateMatrix_bfs(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS -> 모든 0인 cell에서 0이 아닌 cell로 수행 (w/o visited)
        """

        from collections import deque

        m, n = len(mat), len(mat[0])

        # 0인 cell에서 시작
        q = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1  # 방문하지 않은 cell은 -1로 표시

        # BFS
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # 범위를 벗어났거나 이미 방문한 곳이면 넘어가기
                if nr < 0 or nr >= m or nc < 0 or nc >= n or mat[nr][nc] != -1:
                    continue

                # mat에 거리 업데이트 및 visited 처리
                mat[nr][nc] = mat[r][c] + 1

                # q에 넣기
                q.append((nr, nc))

        return mat

    def updateMatrix_bfs_w_vis(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS -> 모든 0인 cell에서 0이 아닌 cell로 수행
        """

        from collections import deque

        m, n = len(mat), len(mat[0])

        # 0인 cell에서 시작
        q = deque([])
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        # BFS
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # 범위를 벗어났거나 이미 방문한 곳이면 넘어가기
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited:
                    continue

                # mat에 거리 업데이트
                mat[nr][nc] = mat[r][c] + 1

                # q에 넣고 visited 처리
                q.append((nr, nc))
                visited.add((nr, nc))

        return mat

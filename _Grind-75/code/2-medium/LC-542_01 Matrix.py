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


###### review ######
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """dp"""
        m, n = len(mat), len(mat[0])
        INF = int(1e4)

        # top & left 부터
        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    top = mat[i - 1][j] if i > 0 else INF
                    left = mat[i][j - 1] if j > 0 else INF
                    mat[i][j] = min(top, left) + 1

        # bottom & right 부터
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] > 0:
                    bottom = mat[i + 1][j] if i < m - 1 else INF
                    right = mat[i][j + 1] if j < n - 1 else INF
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

        return mat

    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        """bfs w/o visited"""
        from collections import deque

        m, n = len(mat), len(mat[0])

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # not visited 표시

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat

    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        """bfs w/ visited"""
        from collections import deque

        m, n = len(mat), len(mat[0])
        visited = [[False] * n for _ in range(m)]

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        q = deque([])
        for r in range(m):
            for c in range(n):
                # zero cell에서 시작하기
                if not mat[r][c]:
                    q.append((r, c, 0))  # (r, c, distance)
                    visited[r][c] = True

        while q:
            r, c, d = q.popleft()

            # mat[r][c] == 1이라면 distance 기록
            if mat[r][c] == 1:
                mat[r][c] = d

            # 상하좌우
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    q.append((nr, nc, d + 1))
                    visited[nr][nc] = True

        return mat

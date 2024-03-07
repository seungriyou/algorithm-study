# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    # DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]

        def dfs(r, c):
            # 범위를 벗어나면 종료
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            # (1) not visited 이고 (2) original_color와 같은 색상이면
            if (r, c) not in visited and image[r][c] == original_color:
                # color로 색칠하고 visited 표시
                image[r][c] = color
                visited.add((r, c))

                # 인접한 칸 확인
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)

        dfs(sr, sc)

        return image

    # BFS
    def floodFill_bfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        visited = set()
        m, n = len(image), len(image[0])

        original_color = image[sr][sc]

        q = deque([(sr, sc)])
        image[sr][sc] = color
        visited.add((sr, sc))

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위를 벗어나면 넘어가기
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # (1) not visited이면서 (2) original_color와 같은 색깔인 경우
                if (nr, nc) not in visited and image[nr][nc] == original_color:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    image[nr][nc] = color

        return image

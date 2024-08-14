# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        [BFS]
        반대로, ocean에 맞닿아있는 edge에서부터 더 큰 수를 가진 칸 쪽으로 이동
        pacific & atlantic 각각 진행 후, 둘다 해당되는 좌표 반환
        시작 지점을 edge에 해당하는 좌표들로 지정
        """
        from collections import deque

        row, col = len(heights), len(heights[0])
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

        def bfs(start):
            visited = set(start)
            q = deque(start)

            while q:
                r, c = q.popleft()

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    # 범위를 벗어나지 않고, 방문하지 않았으며, 값이 이전 값보다 크거나 같은 경우
                    if (0 <= nr < row and 0 <= nc < col
                            and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        # get edges (start)
        start_p, start_a = [], []
        for c in range(col):
            start_p.append((0, c))
            start_a.append((row - 1, c))
        for r in range(row):
            start_p.append((r, 0))
            start_a.append((r, col - 1))

        # get locations
        visited_p = bfs(start_p)
        visited_a = bfs(start_a)

        # get intersection
        return visited_p & visited_a

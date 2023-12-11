# [LTC] 417 - Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # === BFS ===
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        rows, cols = len(heights), len(heights[0])
        visited_p, visited_a = set(), set()
        queue_p, queue_a = [], []

        def bfs(queue, visited):
            q = deque(queue)

            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue

                visited.add((x, y))

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= heights[x][y]:  # -- 가장자리부터 거꾸로 찾아나가므로
                        q.append((nx, ny))

        for r in range(rows):
            queue_p.append((r, 0))
            queue_a.append((r, cols - 1))

        for c in range(cols):
            queue_p.append((0, c))
            queue_a.append((rows - 1, c))

        bfs(queue_p, visited_p)
        bfs(queue_a, visited_a)

        return list(visited_p & visited_a)

sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))

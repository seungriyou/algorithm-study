# [LTC] 886 - Possible Bipartition (BFS)
# https://leetcode.com/problems/possible-bipartition/

from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # === BFS ===
        # dislikes -> edge
        # bipartite graph
        # 두 가지 color로 coloring 해보자 (color = -1, 1)
        if n == 1 or not dislikes:
            return True

        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = [0] * (n + 1)

        def bfs(start):
            q = deque([(start, 1)]) # -- (색칠하려는 node, color)
            while q:
                pos, color = q.popleft()
                # 색칠 가능한지 확인
                # -- 이미 coloring 된 경우
                if colors[pos] != 0:
                    # -- 색칠하려는 color와 다르다면 return False
                    if colors[pos] != color:
                        return False
                    # -- 색칠하려는 color가 이미 색칠된 경우 넘어가기
                    continue
                # -- coloring이 되어있지 않다면 coloring
                colors[pos] = color
                for npos in graph[pos]:
                    q.append((npos, -color))

            return True

        for i in range(1, n + 1):
            if not colors[i]:   # -- colors[i] == 0인, 즉 coloring이 안된 node에 대해서만 bfs 수행해야 함
                if not bfs(i):
                    return False
        return True

sol = Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(sol.possibleBipartition(n, dislikes))

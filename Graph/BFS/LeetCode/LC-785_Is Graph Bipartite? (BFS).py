# [LTC] 785 - Is Graph Bipartite? (BFS)
# https://leetcode.com/problems/is-graph-bipartite/

from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # === BFS ===
        # bipartite -> 2가지 색(1, -1)만으로 모든 node에 대해 서로 인접한 node는 다른 색으로 coloring 가능하다면!
        n = len(graph)
        colors = [0] * n

        def bfs(start):
            q = deque([(start, 1)])  # -- 두 가지 color를 1, -1로 하기 위해 초기 color를 1로 부여
            while q:
                pos, color = q.popleft()
                if colors[pos] != 0:  # -- 이미 1, -1 중 하나로 coloring 된 경우
                    if colors[pos] != color:  # -- 잘못된 color가 이미 coloring 된 경우, False
                        return False
                    continue  # -- 알맞은 color가 이미 coloring 된 경우, 그냥 넘어가기
                colors[pos] = color  # -- 아직 coloring이 되지 않은 경우
                for npos in graph[pos]:
                    q.append((npos, -color))  # -- 다른 color로 넣어주기

            return True

        # -- 모든 위치에 대해서, coloring이 안된 node임을 확인(colors[i] == 0)하고 coloring 수행해야 함 *** ("The graph may not be connected")
        for i in range(n):
            if not colors[i]:
                if not bfs(i):
                    return False

        return True

sol = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(sol.isBipartite(graph))

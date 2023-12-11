# [LTC] 785 - Is Graph Bipartite? (DFS)
# https://leetcode.com/problems/is-graph-bipartite/

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # === DFS (정리) ===
        # 2개의 color로 색칠 -> 1, -1

        def coloring(pos, color):
            # pos에 색칠하기
            colors[pos] = color

            for npos in graph[pos]:
                # npos의 color가 이미 정해져있고, 그 color가 pos의 color와 같으면 False
                if colors[npos] == color:
                    return False

                # npos의 color가 정해져있지 않으나, 그 반대 color로 npos를 coloring 할 수 없으면 False
                if not colors[npos] and not coloring(npos, -color):
                    return False

            # 그 외 경우에는 True
            return True

        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if not colors[i]:  # -- colors[i] == 0, 즉 i가 coloring이 되지 않은 node일 때
                if not coloring(pos=i, color=1):  # -- default 시작 color는 1
                    return False
        return True

    def isBipartite_dfs(self, graph: List[List[int]]) -> bool:
        # === DFS ===
        n = len(graph)
        colors = [0] * n

        def dfs(pos):
            for npos in graph[pos]:
                # -- npos를 이미 coloring 한 경우
                if colors[npos] != 0:
                    # -- pos와 color가 같다면 인접한 두 node가 같은 color라는 것이므로 False
                    if colors[npos] == colors[pos]:
                        return False
                else:
                    # -- 다른 color 기록
                    colors[npos] = -colors[pos]
                    if not dfs(npos):
                        return False
            return True

        # -- 모든 위치에 대해서, coloring이 안된 node임을 확인(colors[i] == 0)하고 coloring 수행해야 함 *** ("The graph may not be connected")
        for i in range(n):
            if not colors[i]:
                colors[i] = 1
                if not dfs(i):
                    return False

        return True


sol = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(sol.isBipartite(graph))

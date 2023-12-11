# [LTC] 886 - Possible Bipartition (DFS)
# https://leetcode.com/problems/possible-bipartition/

from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # === DFS (정리) ===
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

        if n == 1 or not dislikes:
            return True

        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = [0] * (n + 1)

        for i in range(1, n + 1):
            if not colors[i]:
                if not coloring(i, 1):  # -- default 시작 color는 1
                    return False

        return True

    def possibleBipartition_dfs(self, n: int, dislikes: List[List[int]]) -> bool:
        # === DFS ===
        if n == 1 or not dislikes:
            return True

        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colors = [0] * (n + 1)

        def dfs(pos):
            # 이미 coloring 된 pos에 대해 인접 node들 순회
            for npos in graph[pos]:
                # npos가 이미 coloring 되었으면
                if colors[npos] != 0:
                    # pos와 npos의 color가 같다면 return False
                    if colors[npos] == colors[pos]:
                        return False
                # npos가 coloring 되어 있지 않다면
                else:
                    colors[npos] = -colors[pos]
                    if not dfs(npos):
                        return False

            return True

        for i in range(1, n + 1):
            if not colors[i]:  # -- colors[i] == 0
                colors[i] = 1  # -- default 시작 color는 1로
                if not dfs(i):
                    return False
        return True

sol = Solution()
n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(sol.possibleBipartition(n, dislikes))

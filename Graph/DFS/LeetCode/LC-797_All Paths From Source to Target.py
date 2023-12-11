# [LC] 797 - All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DAG이므로 visited 확인하지 않아도 ok

        result = []

        def dfs(i, path):
            if i == len(graph) - 1:  # -- dst = len(graph) - 1
                result.append(path)
                return

            for j in graph[i]:
                dfs(j, path + [j])

        dfs(0, [0])  # -- src = 0
        return result

sol = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(sol.allPathsSourceTarget(graph))

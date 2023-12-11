# [LTC] 547 - Number of Provinces
# https://leetcode.com/problems/number-of-provinces/

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = [False] * n

        def dfs(start):
            visited[start] = True
            for i in graph[start]:
                if not visited[i]:
                    dfs(i)

        cnt = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                cnt += 1

        return cnt

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
sol = Solution()
print(sol.findCircleNum(isConnected))

# [LTC] 684 - Redundant Connection
# https://leetcode.com/problems/redundant-connection/

from typing import List


class Solution:
    # === union-find ===
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(len(edges) + 1)]
        answer = None

        for a, b in edges:
            # -- cycle이 발생한 경우 (root node가 서로 같은 경우)
            if self.find(a) == self.find(b):
                answer = [a, b]
            # -- cycle이 발생하지 않았다면 union
            else:
                self.union(a, b)

        return answer

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

sol = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(sol.findRedundantConnection(edges))

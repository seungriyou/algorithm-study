# [LTC] 310 - Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # graph 구축 시 set -> element remove 시 time complexity 더 좋아질 수 있음
        #
        # base case 설명 시 -> node 개수 1, 2일 때
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        node_cnt = n

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = [node for node in range(n) if len(graph[node]) == 1]

        while node_cnt > 2:
            node_cnt -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(sol.findMinHeightTrees(n, edges))

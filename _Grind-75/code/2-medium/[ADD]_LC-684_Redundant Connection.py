# https://leetcode.com/problems/redundant-connection/

from typing import List


class Solution:
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        """dfs"""
        # https://leetcode.com/problems/redundant-connection/solutions/123819/from-dfs-to-union-find
        # https://leetcode.com/problems/redundant-connection/solutions/1295991/python-easy-to-understand-graph-dfs
        # https://leetcode.com/problems/redundant-connection/solutions/3876792/python3-dfs-with-clear-explanation

        graph = [[] for _ in range(len(edges) + 1)]

        def is_cyclic(u, v):
            if u == v:
                return True

            for nu in graph[u]:
                if nu not in visited:
                    visited.add(nu)
                    if is_cyclic(nu, v):
                        return True

            return False

        for u, v in edges:
            visited = set()

            if is_cyclic(u, v):
                # ** cycle detected! **
                # n vertices and n edges, there can be only one cycle
                return [u, v]

            graph[u].append(v)
            graph[v].append(u)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """union-find"""
        # https://leetcode.com/problems/redundant-connection/solutions/123819/from-dfs-to-union-find

        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]

        def union_parent(parent, a, b):
            parent_a, parent_b = find_parent(parent, a), find_parent(parent, b)
            if parent_a < parent_b:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b

        parent = [i for i in range(len(edges) + 1)]  # node 개수 == edge 개수 (node: 1 ~ n번)

        for a, b in edges:
            if find_parent(parent, a) == find_parent(parent, b):
                # cycle detected!
                # n vertices and n edges, there can be only one cycle
                return [a, b]
            else:
                union_parent(parent, a, b)


###### review ######
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """dfs"""

        n = len(edges)

        graph = [[] for _ in range(n + 1)]

        def has_cycle(u, v, visited):
            # base condition
            if u == v:
                return True

            # recur
            for nu in graph[u]:
                if nu not in visited:
                    visited.add(nu)
                    if has_cycle(nu, v, visited):
                        return True

            return False

        for u, v in edges:
            # u ~ v edge로 인해 cycle이 생긴다면, 반환
            if has_cycle(u, v, set()):
                return [u, v]

            # u ~ v edge를 graph에 추가하기
            graph[u].append(v)
            graph[v].append(u)

    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        """union find"""

        n = len(edges)

        def find_parent(x):
            if x != parent[x]:
                parent[x] = find_parent(parent[x])

            return parent[x]

        def union_parent(x, y):
            x, y = find_parent(x), find_parent(y)

            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        parent = list(range(n + 1))

        for u, v in edges:
            if find_parent(u) == find_parent(v):
                return [u, v]
            union_parent(u, v)

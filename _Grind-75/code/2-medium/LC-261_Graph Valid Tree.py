# https://leetcode.com/problems/graph-valid-tree/

from typing import List


class Solution:
    def validTree_bfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        tree = acyclic & connected graph
        [bfs]

        - TC: O(V+E) == O(N) (E가 N에 bounded)
        - SC: O(N)
        """
        from collections import deque

        # early checking (connected & acyclic)
        if len(edges) != n - 1:
            return False

        # bfs
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = {0}
        q = deque([0])

        while q:
            pos = q.popleft()
            for npos in graph[pos]:
                if npos not in visited:
                    visited.add(npos)
                    q.append(npos)

        return len(visited) == n

    def validTree_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        tree = acyclic & connected graph
        [dfs]

        - TC: O(V+E) == O(N) (E가 N에 bounded)
        - SC: O(N)
        """

        # early checking (connected & acyclic)
        if len(edges) != n - 1:
            return False

        # dfs
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(start):
            # base condition
            if start in visited:
                return

            visited.add(start)

            # recur
            for ngbr in graph[start]:
                dfs(ngbr)

        # should visit all nodes
        dfs(0)

        return len(visited) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        tree = acyclic & connected graph
        -> union-find

        - TC: O(N*α(N)) (path compression)
        - SC: O(N)
        """

        # early checking (connected & acyclic)
        if len(edges) != n - 1:
            return False

        # union-find for cycle detection
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union_parent(x, y):
            px, py = find_parent(x), find_parent(y)

            # if cyclic, return False
            if px == py:
                return False

            if px < py:
                parent[py] = px
            else:
                parent[px] = py

            return True

        parent = [i for i in range(n)]

        for a, b in edges:
            if not union_parent(a, b):
                return False

        return True

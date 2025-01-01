# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        [union find 2]

        - TC: O(V + E*α(V))
            (* α(V) = 경로 압축 시 find 연산의 복잡도)
        - SC: O(V)
        """

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        parent = [i for i in range(n)]

        res = n
        for a, b in edges:
            pa, pb = find_parent(a), find_parent(b)
            if pa != pb:
                parent[pa] = pb
                res -= 1

        return res

    def countComponents_uf(self, n: int, edges: List[List[int]]) -> int:
        """
        [union find]

        union-find 모두 수행한 후, parent 종류의 개수 반환

        - TC: O(V + E*α(V))
            (* α(V) = 경로 압축 시 find 연산의 복잡도)
        - SC: O(V)
        """

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union_parent(x, y):
            px, py = find_parent(x), find_parent(y)
            if px < py:
                parent[py] = parent[px]
            else:
                parent[px] = parent[py]

        parent = [i for i in range(n)]

        for a, b in edges:
            union_parent(a, b)

        return len(set(find_parent(i) for i in range(n)))

    def countComponents_b(self, n: int, edges: List[List[int]]) -> int:
        """
        [bfs]

        - TC: O(V+E)
            - 모든 V 한 번씩 방문 & 해당 V 마다 인접한 E 방문
        - SC: O(V+E)
            - E = graph (adjacency list)
            - V = visited
        """
        from collections import deque

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def bfs(start):
            q = deque([start])
            visited.add(start)

            while q:
                pos = q.popleft()

                for npos in graph[pos]:
                    if npos not in visited:
                        q.append(npos)
                        visited.add(npos)

        cnt = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                cnt += 1

        return cnt

    def countComponents_d(self, n: int, edges: List[List[int]]) -> int:
        """
        [dfs]

        - TC: O(V+E)
            - 모든 V 한 번씩 방문 & 해당 V 마다 인접한 E 방문
        - SC: O(V+E)
            - E = graph (adjacency list)
            - V = visited
        """

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def dfs(start):
            visited.add(start)
            for ngbr in graph[start]:
                if ngbr not in visited:
                    dfs(ngbr)

        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1

        return cnt

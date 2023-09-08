# [LTC] 399 - Evaluate Division
# https://leetcode.com/problems/evaluate-division/

from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # === BFS ===
        graph = defaultdict(set)  # -- weighted directed graph
        for (a, b), v in zip(equations, values):
            graph[a].add((b, v))  # -- a->b : a/b
            graph[b].add((a, 1 / v))  # -- b->a : b/a

        def bfs(s, e):
            if s not in graph or e not in graph:
                return -1.0
            if s == e:
                return 1.0

            q = deque([(s, 1.0)])
            visited = set()  # -- s는 visited에 넣으면 X (-> edge: / 연산)

            while q:
                ns, pv = q.popleft()
                if ns == e:
                    return pv
                for n, v in graph[ns]:
                    if n not in visited:
                        q.append((n, pv * v))
                        visited.add(n)

            return -1.0

        return [bfs(s, e) for s, e in queries]

    def calcEquation_dfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[
        float]:
        # === DFS ===
        graph = defaultdict(set)  # -- weighted directed graph
        for (a, b), v in zip(equations, values):
            graph[a].add((b, v))  # -- a->b : a/b
            graph[b].add((a, 1 / v))  # -- b->a : b/a

        def solve(s, e, visited):
            if s not in graph or e not in graph:
                return -1.0
            if s == e:
                return 1.0

            visited.add(s)

            for n, v in graph[s]:
                if n == e:
                    return v
                if n not in visited:
                    if (nv := solve(n, e, visited)) != -1.0:
                        return v * nv

            return -1.0

        result = []

        for s, e in queries:
            visited = set()
            result.append(solve(s, e, visited))

        return result

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
sol = Solution()
print(sol.calcEquation(equations, values, queries))

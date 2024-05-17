# https://leetcode.com/problems/minimum-height-trees/

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        (topo sort와 비슷) leaf node removal
            -> node가 1개 or 2개 남을 때까지 leaf(= degree가 1인 node)를 잘라나가기
        """
        # ref: https://leetcode.com/problems/minimum-height-trees/solutions/1631179/c-python-3-simple-solution-w-explanation-brute-force-2x-dfs-remove-leaves-w-bfs
        # ref: https://leetcode.com/problems/minimum-height-trees/solutions/76055/share-some-thoughts

        # edge case
        if n == 1:
            return [0]

        # graph 생성
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # leaves(degree가 1인 node) 초기화
        leaves = [node for node in range(n) if len(graph[node]) == 1]

        # 남은 node가 1개 or 2개일 때까지 leaf node 제거하기 (tree = acyclic connected graph)
        while n > 2:
            # 현재 단계에서 새롭게 찾을 leaves 담을 list 선언
            new_leaves = []

            for leaf in leaves:
                # len(graph[leaf]) == 1이다! 따라서 ngbr도 1개이다.
                # 따라서 for ngbr in graph[leaf] 할 필요 X. graph[leaf].pop() 하면 된다.
                ngbr = graph[leaf].pop()
                graph[ngbr].remove(leaf)

                # ngbr의 degree가 1이 되었다면, new_leaves에 추가
                if len(graph[ngbr]) == 1:
                    new_leaves.append(ngbr)

            # node 수 업데이트
            n -= len(leaves)

            # leaves를 new_leaves로 업데이트
            leaves = new_leaves

        return leaves

    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        """longest path(diameter of tree) (2 dfs) (bad TC & SC)"""
        # ref: https://leetcode.com/problems/minimum-height-trees/solutions/923071/python-find-diameter-using-2-dfs-explained

        graph = [set() for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(start):
            if visited[start]:
                return []

            longest_path = []
            visited[start] = True

            for ngbr in graph[start]:
                if not visited[ngbr]:
                    path = dfs(ngbr)
                    if len(path) > len(longest_path):
                        longest_path = path

            longest_path.append(start)
            visited[start] = False

            return longest_path

        # 2 dfs
        max_di = dfs(0)[0]  # (1) dfs(0) 결과로 얻은 path의 첫 번째 원소 == 랜덤 node(0번 node)로부터 가장 먼 거리에 위치한 node 번호
        path = dfs(max_di)  # (2) (1)번에서 찾은 node로부터 출발하는 longest path를 찾기 -> diameter of tree에 해당하는 path가 됨

        # path의 길이가 홀수이면 중간의 1개 원소, 짝수이면 중간의 2개 원소 반환
        np = len(path)
        return [path[np // 2]] if np & 1 else [path[np // 2 - 1], path[np // 2]]

    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        """longest path(diameter of tree) (2 bfs) (better TC & SC)"""
        # ref: https://github.com/lydxlx1/LeetCode/blob/master/src/_310.java
        from collections import deque

        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            visited = [False] * n
            dist = [0] * n
            prev = [0] * n

            visited[start] = True
            q = deque([start])
            prev[start] = -1

            while q:
                pos = q.popleft()

                for npos in graph[pos]:
                    if not visited[npos]:
                        q.append(npos)
                        visited[npos] = True
                        dist[npos] = dist[pos] + 1
                        prev[npos] = pos

            # max dist
            max_d, max_di = -1, -1
            for idx, d in enumerate(dist):
                if d > max_d:
                    max_di = idx
                    max_d = d

            # max_di: start로부터 가장 먼 거리에 위치한 node 번호
            # prev: start로부터 출발한 최장 경로의 정보 (각 node의 이전 node 정보)
            return max_di, prev

        # 2 bfs
        u, _ = bfs(0)  # (1) 랜덤 node(0번 node)로부터 가장 먼 거리에 위치한 node 번호 찾기
        v, prev = bfs(u)  # (2) (1)번에서 찾은 node로부터 가장 먼 거리에 위치한 node 번호 및 경로 정보 찾기 (u ~ v == diameter of tree)

        # prev 정보를 통해 node v로부터 거슬러 올라가며 longest path 찾기
        path = []
        while v != -1:
            path.append(v)
            v = prev[v]

        # path의 길이가 홀수이면 중간의 1개 원소, 짝수이면 중간의 2개 원소 반환
        np = len(path)
        return [path[np // 2]] if np & 1 else [path[np // 2 - 1], path[np // 2]]

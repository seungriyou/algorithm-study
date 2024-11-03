# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        [ DFS ]
        - TC: O(n)
        - SC: O(n)
        """

        from collections import defaultdict

        graph, res, visited = defaultdict(list), [], set()

        # 1. 양방향 graph 구축 (DFS)
        def dfs1(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs1(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs1(node.right)

        dfs1(root)

        # 2. target node로부터 k 만큼 떨어진 node의 값 반환 (DFS)
        def dfs2(node, k):
            if k == 0:
                res.append(node.val)
            elif k > 0:
                visited.add(node)
                for ngbr in graph[node]:
                    if ngbr not in visited:
                        dfs2(ngbr, k - 1)

        dfs2(target, k)

        return res

    def distanceK1(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        [ BFS ]
        - TC: O(n)
        - SC: O(n)

        1. hash map으로 양방향 graph 구축 {node val: [neighbor val]} -> BFS
        2. target node로부터 k 만큼 떨어진 node의 값 반환 -> BFS

        (tree의 val이 unique 함을 이용함)
        """
        from collections import defaultdict, deque

        # 1. 양방향 graph 구축 (BFS)
        q = deque([root])
        graph = defaultdict(list)

        while q:
            curr = q.popleft()

            # 양방향 graph 구축
            if curr.left:
                graph[curr.left.val].append(curr.val)
                graph[curr.val].append(curr.left.val)
                q.append(curr.left)
            if curr.right:
                graph[curr.right.val].append(curr.val)
                graph[curr.val].append(curr.right.val)
                q.append(curr.right)

        # 2. target node로부터 k 만큼 떨어진 node의 값 반환 (BFS)
        q = deque([(target.val, 0)])  # (val, dist)
        visited = set()
        res = []

        while q:
            val, dist = q.popleft()
            visited.add(val)

            if dist > k:
                break
            if dist == k:
                res.append(val)
                continue

            for nval in graph[val]:
                if nval not in visited:
                    q.append((nval, dist + 1))

        return res

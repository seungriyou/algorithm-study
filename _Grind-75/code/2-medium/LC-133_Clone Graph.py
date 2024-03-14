# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph_BFS(self, node: Optional['Node']) -> Optional['Node']:
        """BFS"""

        from collections import deque

        if not node:
            return

        q = deque([node])
        node_copy = Node(val=node.val)  # first node (for return)
        copy_table = {node.val: node_copy}  # visited 처리 및 caching

        while q:
            node = q.popleft()

            # 현재 노드의 이웃 순회
            for ngbr in node.neighbors:
                # hash table에 저장되어 있다면(caching O), 해당 복사본 사용
                if ngbr.val in copy_table:
                    copy_table[node.val].neighbors.append(copy_table[ngbr.val])
                # hash table에 저장되어 있지 않다면(caching X), 새롭게 생성, visited 처리, 이어서 방문
                else:
                    ngbr_copy = Node(val=ngbr.val)
                    copy_table[ngbr.val] = ngbr_copy
                    copy_table[node.val].neighbors.append(ngbr_copy)
                    q.append(ngbr)

        return node_copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """DFS"""

        if not node:
            return

        copy_table = {}

        def dfs(node):
            # 이미 node의 복사본이 caching 되어 있다면, 해당 복사본 반환
            if node.val in copy_table:
                return copy_table[node.val]

            # 주어진 node의 복사본을 만들고, hash table에 저장 (caching)
            node_copy = Node(val=node.val)
            copy_table[node.val] = node_copy

            # 주어진 노드의 이웃 순회
            for ngbr in node.neighbors:
                node_copy.neighbors.append(dfs(ngbr))

            # 복사본 반환
            return node_copy

        return dfs(node)

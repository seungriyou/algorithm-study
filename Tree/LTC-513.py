# [LTC] 513 - Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # === BFS (right -> left) ===
        q = deque([root])
        result = None

        while q:
            n = q.popleft()
            result = n.val
            if n.right:
                q.append(n.right)
            if n.left:
                q.append(n.left)

        return result

    def findBottomLeftValue_bfs(self, root: Optional[TreeNode]) -> int:
        # === BFS ===
        q = [root]
        result = None

        while q:
            result = q[0].val
            q = [c for n in q for c in (n.left, n.right) if c]  # -- level 별로

        return result

    def findBottomLeftValue_dfs(self, root: Optional[TreeNode]) -> int:
        # === DFS ===
        self.result = None
        self.max_depth = -1  # -- root의 depth = 0 이므로 초기값은 -1로..!

        def dfs(node, depth):
            if node is None:
                return

            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return self.result

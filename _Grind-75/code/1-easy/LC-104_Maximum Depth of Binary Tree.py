# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth_iter(self, root: Optional[TreeNode]) -> int:
        """w/ deque"""

        if not root:
            return 0

        depth = 0
        q = deque([root])

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """w/o deque"""

        depth = 0
        q = [root] if root else []

        while q:
            depth += 1
            level = []

            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            q = level

        return depth

    def maxDepth_recur(self, root: Optional[TreeNode]) -> int:
        """recursive version"""

        # base condition
        if not root:
            return 0

        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)

        return max(left_max_depth, right_max_depth) + 1

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


###### review ######
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """iterative"""

        level = [root] if root else []
        depth = 0

        while level:
            _level = []
            depth += 1

            for node in level:
                if node.left:
                    _level.append(node.left)
                if node.right:
                    _level.append(node.right)

            level = _level

        return depth

    def maxDepth_r(self, root: Optional[TreeNode]) -> int:
        """recursive"""

        def max_depth(node):
            if node is None:
                return 0

            left = max_depth(node.left)
            right = max_depth(node.right)

            return max(left, right) + 1

        return max_depth(root)

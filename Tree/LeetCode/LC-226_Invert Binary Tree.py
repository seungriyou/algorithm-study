# [LTC] 226 - Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # === BFS ===
        queue = deque([root])

        while queue:  # -- top에서부터
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    def invertTree_recur(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # === recursive ===
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

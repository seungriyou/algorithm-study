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

    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # from top (bfs)
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                # switch
                node.left, node.right = node.right, node.left

                # add next nodes to deque
                q.append(node.left)
                q.append(node.right)

        return root

    def invertTree_r(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # from bottom
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root

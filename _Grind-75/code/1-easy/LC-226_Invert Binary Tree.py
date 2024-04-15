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


###### review ######
class Solution:
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """bottom-up"""

        def invert(node):
            if node is None:
                return None

            # left와 right의 subtree를 바꿔버린다!
            node.left, node.right = invert(node.right), invert(node.left)

            return node

        return invert(root)

    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """bottom-up"""

        def invert(node):
            # 더 줄여서 다음과 같이 작성할 수 있다!
            if node:
                node.left, node.right = invert(node.right), invert(node.left)
            return node

        return invert(root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """top-down"""
        from collections import deque

        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)

        return root

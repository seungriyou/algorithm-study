# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional['TreeNode'], k: int) -> int:
        """w/ generator"""

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        for i, node in enumerate(inorder(root)):
            if i == k - 1:
                return node.val

    def kthSmallest2(self, root: Optional['TreeNode'], k: int) -> int:
        # BST -> inorder traversal -> sorted!

        cnt = k
        res = None

        def inorder(node):
            nonlocal cnt, res

            if node is None or res:
                return

            inorder(node.left)

            cnt -= 1
            if not cnt:
                res = node.val
                return

            inorder(node.right)

        inorder(root)

        return res

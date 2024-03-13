# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_in_range(node, floor, ceil):
            if node is None:
                return True
            if not floor < node.val < ceil:
                return False
            return is_in_range(node.left, floor, node.val) and is_in_range(node.right, node.val, ceil)

        return is_in_range(root, -float("inf"), float("inf"))

    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        inorder_path = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inorder_path.append(node.val)
            inorder(node.right)

        def is_asc_sorted(lst):
            for i in range(len(lst) - 1):
                if lst[i] >= lst[i + 1]:
                    return False
            return True

        inorder(root)

        return is_asc_sorted(inorder_path)

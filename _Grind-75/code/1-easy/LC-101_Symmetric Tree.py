# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional['TreeNode']) -> bool:
        def check_mirror(node1, node2):
            # base condition
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            # check symmetric (recur)
            return node1.val == node2.val and check_mirror(node1.left, node2.right) and check_mirror(node1.right, node2.left)

        return check_mirror(root.left, root.right)

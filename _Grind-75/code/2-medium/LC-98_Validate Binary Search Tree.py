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


###### review ######
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import math

        def in_valid_range(node, floor, ceil):
            # node가 아니면 True 반환
            if not node:
                return True

            # 현재 node가 알맞은 범위 내에 있다면, left와 right에 대해서 재귀 호출
            if floor < node.val < ceil:
                return in_valid_range(node.left, floor, node.val) and in_valid_range(node.right, node.val, ceil)

            # 현재 node가 알맞은 범위 내에 있지 않다면, False 반환
            else:
                return False

        return in_valid_range(root, -math.inf, math.inf)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        path = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            path.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(len(path) - 1):
            if path[i] >= path[i + 1]:
                return False

        return True

# [LTC] 543 - Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: TreeNode) -> int:
            nonlocal diameter

            # -- empty tree의 height = -1로 설정
            if not node:
                return -1

            left, right = dfs(node.left), dfs(node.right)  # -- left와 right의 leaf ~ 현재 node 까지의 거리

            diameter = max(left + right + 2, diameter)  # -- diameter 기록

            return max(left, right) + 1  # -- leaf ~ 현재 node 까지의 거리 업데이트

        dfs(root)

        return diameter
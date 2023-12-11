# [LTC] 129 - Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node: Optional[TreeNode], prev_val: int) -> None:
            val = prev_val * 10 + node.val

            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)

            if node.left is None and node.right is None:
                values.append(val)

        dfs(root, 0)

        return sum(values)

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: Optional[TreeNode], prev_val: int) -> None:
            nonlocal result
            val = prev_val * 10 + node.val

            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)

            if node.left is None and node.right is None:
                result += val

        dfs(root, 0)

        return result

    def sumNumbers3(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], prev_val: int) -> None:
            if node is None:
                return 0

            val = prev_val * 10 + node.val

            # -- leaf node라면
            if node.left is None and node.right is None:
                return val
            # -- leaf node가 아니라면, left & right child (재귀)
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)

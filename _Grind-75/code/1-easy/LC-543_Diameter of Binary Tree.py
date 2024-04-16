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
        """
        longest path between any two nodes -> `root`를 지나지 않을 수도 있으므로, 모든 node에 대해 찾아야 함
        """

        diameter = 0

        def max_depth(root):
            nonlocal diameter

            # base condition
            if not root:
                return 0

            # 1. left subtree와 right subtree의 max depth 구하기 (recur)
            left_max_depth, right_max_depth = max_depth(root.left), max_depth(root.right)

            # 2. 현재의 root 노드에 대해 diameter 업데이트
            diameter = max(diameter, left_max_depth + right_max_depth)

            # 3. 현재 tree의 max depth 반환
            return max(left_max_depth, right_max_depth) + 1

        max_depth(root)

        return diameter


###### review ######
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def max_depth(node):
            nonlocal max_length

            # base condition
            if not node:
                return 0

            # recur
            left = max_depth(node.left)
            right = max_depth(node.right)

            # max_length 업데이트
            max_length = max(max_length, left + right)

            # 현재 노드의 max depth 반환
            return max(left, right) + 1

        max_depth(root)

        return max_length

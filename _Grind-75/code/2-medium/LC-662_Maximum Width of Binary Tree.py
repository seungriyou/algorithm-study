# https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        """
        - 각 level 마다 왼쪽에서부터 0번부터 번호 부여-> BFS by level
            parent node가 0, 1, ~ 이라면
            left/right child node는 각각 parent * 2, parent * 2 + 1
        - 해당 level을 확인할 때마다 max width 기록
        """
        from collections import deque

        max_width = 0
        level = deque([(0, root)])

        while level:
            # update max_width
            max_width = max(max_width, level[-1][0] - level[0][0] + 1)

            # assign number(0~) to child nodes
            next_level = []
            for i, node in level:
                if node.left:
                    next_level.append((i * 2, node.left))
                if node.right:
                    next_level.append((i * 2 + 1, node.right))
            level = next_level

        return max_width

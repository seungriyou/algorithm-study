# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        zigzag level order
            - bfs level search
            - node와 함께 reversed 여부 기록하기
        """

        if not root:
            return []

        res, level = [], [root]
        is_reversed = False

        while level:
            tmp_level, tmp_res = [], []

            for node in level:
                tmp_res.append(node.val)

                if node.left:
                    tmp_level.append(node.left)
                if node.right:
                    tmp_level.append(node.right)

            if is_reversed:
                tmp_res.reverse()

            res.append(tmp_res)

            is_reversed = not is_reversed

            level = tmp_level

        return res

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        zigzag level order
            - bfs level search
            - node와 함께 reversed 여부 기록하기
        """
        from collections import deque

        if not root:
            return []

        res, q = [], deque([root])
        is_reversed = False

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if is_reversed:
                level.reverse()

            res.append(level)

            is_reversed = not is_reversed

        return res

# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result, level = [], [root]

        while level:
            # result에 level 내 val 추가
            result.append([node.val for node in level])

            # level을 다음 level 노드로 변경
            level = [child for node in level for child in (node.left, node.right) if child]

        return result

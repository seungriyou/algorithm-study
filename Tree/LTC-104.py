# [LTC] 104 - Maximum Depth of Binary Tree

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    return depth


root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(
    val=20, left=TreeNode(val=15), right=TreeNode(val=7)
))
print(maxDepth(root))

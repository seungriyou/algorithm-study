# [LTC] 104 - Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        # === DFS ===
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # === BFS ===
        if not root:
            return 0

        depth, q = 0, deque([root])

        while q:
            depth += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth


root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(
    val=20, left=TreeNode(val=15), right=TreeNode(val=7)
))
sol = Solution()
print(sol.maxDepth(root))

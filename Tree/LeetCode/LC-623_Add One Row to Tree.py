# [LC] 623 - Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # === BFS ===
        if depth == 1:
            return TreeNode(val=val, left=root, right=None)

        q = deque([root])
        level = 1
        while level != depth - 1:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1

        for n in q:
            n.left, n.right = TreeNode(val=val, left=n.left), TreeNode(val=val, right=n.right)

        return root

    def addOneRow_bfs(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # === BFS ===
        dummy = TreeNode(val=val, left=root, right=None)
        q = [dummy]
        for _ in range(depth - 1):
            q = [c for n in q for c in (n.left, n.right) if c]
        for n in q:
            n.left, n.right = TreeNode(val=val, left=n.left), TreeNode(val=val, right=n.right)
        return dummy.left

    def addOneRow_dfs(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # === DFS ===
        if not root:
            return None
        if depth == 1:
            return TreeNode(val=val, left=root, right=None)
        if depth == 2:
            root.left = TreeNode(val=val, left=root.left, right=None)
            root.right = TreeNode(val=val, left=None, right=root.right)
        else:
            root.left = self.addOneRow(root=root.left, val=val, depth=depth - 1)
            root.right = self.addOneRow(root=root.right, val=val, depth=depth - 1)
        return root

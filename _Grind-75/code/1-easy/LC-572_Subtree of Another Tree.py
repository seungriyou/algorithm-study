# https://leetcode.com/problems/subtree-of-another-tree/
"""
similar to
- [Same Tree - LeetCode](https://leetcode.com/problems/same-tree/)
- [Symmetric Tree - LeetCode](https://leetcode.com/problems/symmetric-tree/)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """recursion + iterative"""
        from collections import deque

        def check(s, t):
            # base condition
            if not s or not t:
                return s == t

            # recur
            return s.val == t.val and check(s.left, t.left) and check(s.right, t.right)

        q = deque([root])

        while q:
            node = q.popleft()

            if check(node, subRoot):
                return True

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False

    def isSubtree1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """recursion + dfs"""

        def check(s, t):
            # base condition
            if not s or not t:
                return s == t
            # if not s and not t:
            #     return True
            # if not s or not t:
            #     return False

            # recur
            return s.val == t.val and check(s.left, t.left) and check(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False

            return check(s, t) or dfs(s.left, t) or dfs(s.right, t)

        return dfs(root, subRoot)

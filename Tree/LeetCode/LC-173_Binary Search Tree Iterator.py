# [LTC] 173 - Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder_val = []
        self._inorder(root)
        self.idx = -1

    def next(self) -> int:
        # next() calls will be always valid
        self.idx += 1
        return self.inorder_val[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.inorder_val)

    def _inorder(self, node: TreeNode) -> None:
        if node is None:
            return
        self._inorder(node.left)
        self.inorder_val.append(node.val)
        self._inorder(node.right)


class BSTIterator_stack:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._inorder(root)

    def next(self) -> int:
        # next() calls will be always valid
        leftmost = self.stack.pop()
        if leftmost.right:
            self._inorder(leftmost.right)
        return leftmost.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _inorder(self, node: TreeNode) -> None:
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

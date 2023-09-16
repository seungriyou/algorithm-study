# [LTC] 230 = Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest_gen(self, root: Optional[TreeNode], k: int) -> int:
        # === generator ===
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        k -= 1
        for i, node in enumerate(inorder(root)):
            if i == k:
                return node.val

    def kthSmallest_recur(self, root: Optional[TreeNode], k: int) -> int:
        # === inorder (recur) ===
        # inorder_path = []
        self.cnt = k
        self.result = None

        def inorder(node):
            if not node or self.result:  # -- if node: ... 보다 faster
                return

            inorder(node.left)

            # inorder_path.append(node.val)
            self.cnt -= 1
            if not self.cnt:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)

        return self.result
        # return inorder_path[k - 1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # === inorder (stack) ===
        # 우선 root의 left child를 모두 stack에 넣어두고, 하나씩 pop 해가면서 cnt
        # pop 한 node가 right child를 가진 경우, 그 right child의 모든 left child를 root에서 했던 것처럼 모두 stack에 넣기 (nested while문)
        # pop 한 node가 right child가 없다면 root = None이 될 것이므로 nested while문은 건너뛰게 될 것

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if not k:
                return root.val
            root = root.right

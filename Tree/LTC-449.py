# [LTC] 449 - Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []

        def preorder(node: Optional[TreeNode]) -> None:
            if node:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        result_str = ','.join(result)

        return result_str

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # (1) preorder -> 맨 첫 번째 원소가 root.val
        # (2) binary search tree -> left subtree 원소는 node.val 보다 작고, right subtree 원소는 node.val 보다 크다.
        #     즉, node.val은 left subtree의 upper bound, right subtree의 lower bound가 된다.

        vals = deque(int(v) for v in data.split(',') if v)
        INF = int(1e5)

        def bst(vals: deque, lb: int, ub: int) -> Optional[TreeNode]:
            if vals and lb < vals[0] < ub:
                v = vals.popleft()
                return TreeNode(v, bst(vals, lb, v), bst(vals, v, ub))

        return bst(vals=vals, lb=-INF, ub=INF)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

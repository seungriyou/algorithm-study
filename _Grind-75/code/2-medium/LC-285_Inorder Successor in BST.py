# https://leetcode.com/problems/inorder-successor-in-bst/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        [BST 활용]
        - TC: O(n) (balanced BST라면 O(logn))
        - SC: O(1)
        """

        successor = None

        while root:
            # p.val이 root.val보다 크거나 같다면, successor 후보를 찾기 위해 right subtree로
            if root.val <= p.val:
                root = root.right
            # p.val이 root.val보다 작다면, 현재 보고있는 root가 successor 후보가 됨
            else:
                successor = root
                root = root.left

        return successor

    def inorderSuccessor1(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        [inorder traverse -> p 이후에 나오는 노드]
        - TC: O(n)
        - SC: O(n)
        """
        _inorder = []

        def inorder(node):
            # base condition
            if node is None:
                return

            # inorder recur
            inorder(node.left)
            _inorder.append(node)
            inorder(node.right)

        inorder(root)

        if (idx := _inorder.index(p)) == len(_inorder) - 1:
            return None
        else:
            return _inorder[idx + 1]

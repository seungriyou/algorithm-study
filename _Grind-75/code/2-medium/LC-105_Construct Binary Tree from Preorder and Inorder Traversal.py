# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder.pop(0) (O(n)) 대신 preorder.pop() (O(1))
        preorder.reverse()

        def solve(preorder, inorder):
            if inorder:
                root_idx = inorder.index(preorder.pop())
                root = TreeNode(inorder[root_idx])
                root.left = solve(preorder, inorder[:root_idx])
                root.right = solve(preorder, inorder[root_idx + 1:])

                return root

        return solve(preorder, inorder)

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root_idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_idx])
            root.left = self.buildTree(preorder, inorder[:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx + 1:])

            return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base condition
        if not preorder:
            return None

        if len(preorder) == 1:  # leaf node
            return TreeNode(preorder[0])

        # find root (= preorder[0])
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])

        # recur (w/o root)
        root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])

        return root

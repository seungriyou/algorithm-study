# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor_iter(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        BST에서는 어떤 node에 대해...
        - left subtree: node.val 보다 작은 값들만 존재
        - right subtree: node.val 보다 큰 값들만 존재
        """
        while root:
            # (1) p, q가 모두 root.val 보다 작으면, LCA는 left subtree에 위치
            if p.val < root.val > q.val:
                root = root.left

            # (2) p, q가 모두 root.val 보다 크면, LCA는 right subtree에 위치
            elif p.val > root.val < q.val:
                root = root.right

            # (1), (2)에 해당하지 않으면 현재 root가 LCA
            else:
                return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """recursive 버전"""
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

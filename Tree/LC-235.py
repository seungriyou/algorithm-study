# [LC] 235 - Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor_recur(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # === recursive ===
        # nroot = None
        # if p.val < root.val > q.val and root.left:  # -- 앞 조건 만족 시 root.left, 만족 X 시 False
        #     nroot = root.left
        # elif p.val > root.val < q.val and root.right:   # -- 앞 조건 만족 시 root.right, 만족 X 시 False
        #     nroot = root.right

        nroot = ((p.val < root.val > q.val and root.left) or  # -- 앞 조건 만족 시 root.left, 만족 X 시 False
                 (p.val > root.val < q.val and root.right))  # -- 앞 조건 만족 시 root.right, 만족 X 시 False

        return self.lowestCommonAncestor(nroot, p, q) if nroot else root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # === iterative ===
        # tree의 root부터 시작해서 내려가기
        while root:
            # -- p와 q가 root 보다 작으면 LCA는 left subtree에 위치할 것
            if p.val < root.val > q.val:
                root = root.left
            # -- p와 q가 root 보다 크면 LCA는 right subtree에 위치할 것
            elif p.val > root.val < q.val:
                root = root.right
            # -- 그 외의 경우, 현재 root가 LCA가 됨
            else:
                return root

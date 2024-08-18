# https://leetcode.com/problems/path-sum-ii/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """iterative"""

        res, stack = [], []

        if root:
            stack.append((root, targetSum - root.val, [root.val]))

        while stack:
            node, remaining_val, tmp_path = stack.pop()

            if not node.left and not node.right and not remaining_val:
                res.append(tmp_path[:])

            if node.left:
                stack.append((node.left, remaining_val - node.left.val, tmp_path + [node.left.val]))

            if node.right:
                stack.append((node.right, remaining_val - node.right.val, tmp_path + [node.right.val]))

        return res

    def pathSum1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        DFS (backtracking)
        - complexity: https://leetcode.com/problems/path-sum-ii/solutions/1382332/c-python-dfs-clean-concise-time-complexity-explained
        """
        res = []
        tmp_path = []

        def get_path_sum(node, remaining_val):
            # base condition
            if not node:
                return

            # common work
            remaining_val -= node.val
            tmp_path.append(node.val)

            # <1> if given node is leaf node, record
            if not node.left and not node.right:
                # targetSum과 현재까지의 sum_val이 같다면(= remaining_val이 0이라면), tmp_path 기록
                if not remaining_val:
                    res.append(tmp_path[:])
            # <2> else, recur
            else:
                get_path_sum(node.left, remaining_val)
                get_path_sum(node.right, remaining_val)

            # common work
            tmp_path.pop()

        get_path_sum(root, targetSum)

        return res

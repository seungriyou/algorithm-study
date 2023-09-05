# [LTC] 199 - Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # === BFS ===
        result = []
        if not root:
            return result

        level = [root]
        while level:
            result.append(level[-1].val)
            level = [c for n in level for c in (n.left, n.right) if c]

        return result

    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        # === DFS ===
        result = []  # -- 각 level 마다 값 하나씩 저장됨

        def solve(node, depth):
            if not node:
                return

            # -- right 부터 찾다가, 탐색 대상 depth 내에서 가장 먼저 발견되는 값을 넣게 됨
            # -- 같은 depth에서 이미 이전에 발견된 값이 저장되었다면 len(result) > depth일 것이므로
            if len(result) == depth:
                result.append(node.val)

            # -- right 부터 찾기
            solve(node.right, depth + 1)
            solve(node.left, depth + 1)

        solve(root, 0)

        return result

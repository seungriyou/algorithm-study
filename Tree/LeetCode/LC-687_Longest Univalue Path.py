# [LTC] 687 - Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest_len = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal longest_len

            # (1) 빈 node 처리
            if not node:
                return 0
            # (2) left, right 각각에 대하여 leaf ~ 해당 node 까지의 longest length 구하기
            left, right = dfs(node.left), dfs(node.right)
            # (3) 현재 node.val과 left, right의 val을 비교하여 left, right 값 업데이트
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0  # -- 초기화
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0  # -- 초기화
            # (4) longest length 업데이트
            longest_len = max(longest_len, left + right)
            # (5) leaf ~ 현재 node 까지의 longest length 반환
            return max(left, right)

        dfs(root)

        return longest_len

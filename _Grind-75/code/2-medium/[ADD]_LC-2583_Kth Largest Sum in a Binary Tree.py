# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional['TreeNode'], k: int) -> int:
        import heapq

        level = [root]
        level_sums = []

        while level:
            next_level, level_sum = [], 0
            for node in level:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            heapq.heappush(level_sums, level_sum)
            if len(level_sums) > k:
                heapq.heappop(level_sums)

            level = next_level

        return -1 if len(level_sums) < k else level_sums[0]

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        ascending order로 주어짐
        - mid 위치의 값을 node로 만들고
        - 나머지에 대해서 left, right subtree로
        """

        def construct_tree(lo, hi):
            # base condition
            if lo > hi:
                return None

            # recur: mid 위치의 값을 node로 만들기 & 나머지에 대해 left, right subtree로 구성하기
            mid = lo + (hi - lo) // 2
            node = TreeNode(
                val=nums[mid],
                left=construct_tree(lo, mid - 1),
                right=construct_tree(mid + 1, hi)
            )

            return node

        return construct_tree(0, len(nums) - 1)

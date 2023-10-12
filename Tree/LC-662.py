# [LC] 662 - Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        """
        번호 i를 가지고 있는 어떤 node에 대해, left child에는 (i * 2), right child에는 (i * 2 + 1)을 부여하자.
        이렇게 하면 해당 level 내에서 왼쪽에서부터 해당 node의 순서를 알 수 있다.
        해당 level의 width를 구하려면, q 내부에 있는 양 끝의 node의 번호 간의 차이를 구해 1을 더하면 된다.

                            width   q [(node, node number in that level)]
                            -----   -------------------
                 1          1       [(1, 0)]            => 0 - 0 + 1 = 1
               /   \
             3       2      2       [(3, 0), (2, 1)]    => 1 - 0 + 1 = 2
           /           \
          5             9   4       [(5, 0), (9, 3)]    => 3 - 0 + 1 = 4
         /             /
        6             7     7       [(6, 0), (7, 6)]    => 6 - 0 + 1 = 7
        """

        q = deque([(root, 0)])
        max_width = 0

        while q:
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)

            for _ in range(len(q)):
                n, i = q.popleft()
                if n.left:
                    q.append((n.left, i * 2))
                if n.right:
                    q.append((n.right, i * 2 + 1))

        return max_width

# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional['TreeNode']) -> bool:
        def check(node):
            # None이라면 return 0
            if node is None:
                return 0

            # left / right subtree에 대해 recursive call
            left, right = check(node.left), check(node.right)

            # (1) left와 right 중 하나라도 -1이거나 (2) left와 right의 차이가 1보다 큰 경우, return -1
            # recursion 과정에서 두 subtree의 height 차이가 1보다 큰 경우를 만나면, -1을 flag로 사용하여 기록
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # 위의 경우에 해당하지 않았다면, node가 속한 subtree의 height return
            # height = left와 right 중 큰 값에 1을 더한 값
            return max(left, right) + 1

        # return 값이 flag 값이 아니라면 True
        return check(root) != -1


###### review ######
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balanced(node):
            if node is None:
                return 0

            left, right = check_balanced(node.left), check_balanced(node.right)

            # balanced가 아닌지 확인
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # 현재까지의 depth
            return max(left, right) + 1

        return check_balanced(root) != -1


###### review ######
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        - TC: O(n)
        - SC: O(height)
        """

        def get_max_height(node):
            """
            양쪽 subtree의 height를 비교해서 차이가 1보다 크면 -1 반환
            """
            # base condition
            if node is None:
                return 0

            # recur
            left, right = get_max_height(node.left), get_max_height(node.right)

            # check if -1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # 현재 보고 있는 tree의 height 반환
            return max(left, right) + 1

        return get_max_height(root) != -1

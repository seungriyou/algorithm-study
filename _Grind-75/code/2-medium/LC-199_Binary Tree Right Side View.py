# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS
        right child를 우선으로 탐색
        """

        res = []

        def dfs(node, depth):
            if not node:
                return

            # 현재까지 모은 res의 길이가 depth의 길이와 같아야
            # 현재 depth에서 가장 먼저 발견된 node라는 의미이므로
            if len(res) == depth:
                res.append(node.val)

            # right child 부터 우선으로 탐색
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return res

    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS
        right side -> level 별로 모으고, 가장 마지막 원소를 모아서 반환하면 된다
        """

        if root is None:
            return []

        level = [root]
        res = []

        while level:
            # level의 가장 오른쪽 원소의 값 기록
            res.append(level[-1].val)

            # 다음 level의 노드 찾고, 다음 level로 업데이트
            level = [child for node in level for child in (node.left, node.right) if child]

        return res

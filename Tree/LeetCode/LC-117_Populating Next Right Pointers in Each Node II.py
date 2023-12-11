# [LTC] 117 - Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque([root])

        # -- level 별로
        while q:
            # print(f"== {[node.val for node in q]} ==")
            prev_node = None
            for _ in range(len(q)):  # -- len(q)는 for 문 진입 시 evaluated 된 값 사용 (내부에서 q 바꾸더라도)
                # for i in range(len(q)):
                # print(f"<{i}> {len(q)=}")

                cur_node = q.popleft()

                if prev_node:
                    prev_node.next = cur_node
                prev_node = cur_node

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

                # print(f"\t{[node.val for node in q]}")

        return root

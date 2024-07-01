# https://leetcode.com/problems/next-greater-node-in-linked-list/

from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional['ListNode']) -> List[int]:
        res, stack = [], []
        # stack: monotonic stack (non-increasing) -> [(idx, val)]
        # head.val 보다 strictly 작은 값에 대해서 res에 head.val 기록하기

        i = 0

        while head:
            res.append(0)

            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val  # stack.pop()[0] = idx
            stack.append((i, head.val))

            i += 1
            head = head.next

        return res

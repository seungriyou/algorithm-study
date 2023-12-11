# [LTC] 206 - Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_recur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # === recursive ===
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # === iterative ===
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
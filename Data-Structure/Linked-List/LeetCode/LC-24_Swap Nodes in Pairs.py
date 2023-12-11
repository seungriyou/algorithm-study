# [LTC] 24 - Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs_recur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # === recursive ===
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # === iterative ===
        root = prev = ListNode(val=0)
        prev.next = p1 = head
        while p1 and p1.next:
            # -- swap pair
            p2 = p1.next
            p1.next = p2.next
            p2.next = p1

            prev.next = p2  # -- 이전 노드가 p2를 가리키도록 함

            p1 = p1.next  # -- 전진
            prev = prev.next.next

        return root.next
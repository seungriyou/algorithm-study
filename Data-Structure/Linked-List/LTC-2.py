# [LTC] 2 - Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # === carry ===
        carry = 0
        res = n = ListNode(val=0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val=val)  # -- n.next에 새로운 Node 추가 & n 전진
        return res.next

    def addTwoNumbers_mine(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        num1, num2, d = 0, 0, 1

        while n1:
            num1 += n1.val * d
            d *= 10
            num1 = num1 * 10 + n1.val
            n1 = n1.next
        d = 1
        while n2:
            num2 += n2.val * d
            d *= 10
            n2 = n2.next

        num, next = str(num1 + num2), None

        for n in num:
            node = ListNode(val=int(n))
            if next:
                node.next = next
            next = node

        return next

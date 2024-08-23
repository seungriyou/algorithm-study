# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        간결한 코드로 작성한 버전
        """
        carry = 0
        prev = head = ListNode()

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, new_val = divmod(carry, 10)

            prev.next = ListNode(val=new_val)
            prev = prev.next

        return head.next

    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1, l2, carry가 모두 없을 때까지 ListNode를 만들어서 연결해나가야 한다!
        코드를 더 간결하게 쓰도록 하자..
        """
        carry = 0
        prev = head = ListNode()

        while l1 and l2:
            # 새로운 node 만들기
            carry, new_val = divmod(l1.val + l2.val + carry, 10)
            node = ListNode(val=new_val)

            # prev와 연결 및 전진
            prev.next = node
            prev = prev.next

            # l1, l2 전진
            l1, l2 = l1.next, l2.next

        while l1:
            # 새로운 node 만들기
            carry, new_val = divmod(l1.val + carry, 10)
            node = ListNode(val=new_val)

            # prev와 연결 및 전진
            prev.next = node
            prev = prev.next

            # l1 전진
            l1 = l1.next

        while l2:
            # 새로운 node 만들기
            carry, new_val = divmod(l2.val + carry, 10)
            node = ListNode(val=new_val)

            # prev와 연결 및 전진
            prev.next = node
            prev = prev.next

            # l2 전진
            l2 = l2.next

        if carry:
            node = ListNode(val=carry)
            # prev와 연결
            prev.next = node

        return head.next

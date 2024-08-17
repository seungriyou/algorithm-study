# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional['ListNode']) -> Optional['ListNode']:
        """
        [recursive]
        """
        # base condition
        if not head or not head.next:
            return head

        # 시작 node의 next에 대한 pointer
        p = head.next
        # 기존 head의 next는 p.next부터 swap 한 결과를 가리키도록
        head.next = self.swapPairs(p.next)
        # p의 next는 기존 head로
        p.next = head
        # 시작지점 반환
        return p

    def swapPairs1(self, head: Optional['ListNode']) -> Optional['ListNode']:
        """
        [iterative]
        - 현재 보고 있는 두 node에 대한 pointer p1, p2가 필요
        - p1 이전 원소의 next를 수정해야 하므로, p1 이전 원소를 가리키는 prev도 필요
        """
        root = prev = ListNode(next=head)
        p1 = head

        while p1 and p1.next:
            # get p2
            p2 = p1.next

            # swap p1 <-> p2
            p1.next, p2.next = p2.next, p1

            # change prev.next from p1 to p2
            prev.next = p2

            # go ahead
            p1 = p1.next
            prev = prev.next.next

        return root.next

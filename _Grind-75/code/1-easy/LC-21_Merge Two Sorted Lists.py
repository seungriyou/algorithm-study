# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1, node = list1.next, node.next
            else:
                node.next = list2
                list2, node = list2.next, node.next

        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        return head.next


###### review ######
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head는 반환용, node는 포인터용
        head = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                # 결과에 기록
                node.next = list1
                # 전진
                list1, node = list1.next, node.next
            else:
                # 결과에 기록
                node.next = list2
                # 전진
                list2, node = list2.next, node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return head.next

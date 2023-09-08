# [LTC] 21 - Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # === recursive ===
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


    def mergeTwoLists_iter(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # === iterative ===
        result = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1, result = list1.next, result.next
            else:
                result.next = list2
                list2, result = list2.next, result.next

        if list1 or list2:
            result.next = list1 if list1 else list2

        return head.next

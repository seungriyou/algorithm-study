# https://leetcode.com/problems/sort-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        TC: O(nlogn)
            -> merge sort (tree에 비유)
                (1) logn : 절반씩 범위를 줄여나가면서 확인하므로, height는 logn이다.
                (2) n    : 각 level 마다, 재정렬 시 소요되는 전체 시간은 n이다.
        SC: O(logn)
            -> recursion stack은 height에 해당하는 logn이 된다.
        """

        def merge(l1, l2):
            # merging two linked lists (w/ iteration)

            if l1.val > l2.val:
                l1, l2 = l2, l1

            head = prev = l1
            l1 = l1.next

            while l1 and l2:
                # [sol1]
                # if l1.val > l2.val:
                #     l1, l2 = l2, l1

                # prev.next = l1
                # l1 = l1.next

                # [sol2]
                if l1.val > l2.val:
                    prev.next, l2 = l2, l2.next
                else:
                    prev.next, l1 = l1, l1.next

                prev = prev.next

            prev.next = l1 or l2

            return head

        ##############################
        # base condition
        if not (head and head.next):
            return head

        # recursion
        # (1) slow / fast runner를 이용하여 linked list 절반 나누기
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        slow.next = None

        # (2) 나눈 부분에 대해 linked list sorting
        l1 = self.sortList(head)
        l2 = self.sortList(half)

        # (3) 정렬한 linked list 합치기
        return merge(l1, l2)

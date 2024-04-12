# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_iter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            # 1. next에 node.next 저장
            next = node.next
            # 2. node.next에 prev 저장
            node.next = prev
            # 3. prev와 node를 한 칸씩 옆으로 move
            prev, node = node, next

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 위의 풀이에서 3번을 재귀 함수로 수행
        def reverse(prev, node):
            if not node:
                return prev

            # 1,2번 수행: next -> node.next, node.next -> prev
            next, node.next = node.next, prev

            # 3번 수행: prev -> node, node -> next (한 칸씩 옆으로)
            return reverse(node, next)

        return reverse(None, head)


###### review ######
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            # base condition
            if not curr:
                return prev

            # next 얻어놓기
            next = curr.next

            # curr.next를 prev로 변경
            curr.next = prev

            # prev & curr를 모두 한 칸씩 전진
            return reverse(curr, next)

        return reverse(None, head)

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # next 얻어놓기
            next = curr.next

            # curr.next를 prev로 변경
            curr.next = prev

            # prev & curr를 모두 한 칸씩 전진
            prev, curr = curr, next

        return prev

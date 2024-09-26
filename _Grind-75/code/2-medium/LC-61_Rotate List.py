# https://leetcode.com/problems/rotate-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base condition
        if not head:
            return None

        # 주어진 list의 length 구하기
        length = 1
        last = head
        while last.next:
            length += 1
            last = last.next

        # 맨 마지막 노드의 next를 head로 연결
        last.next = head

        # 끊어야 하는 지점까지 이동해야 하는 횟수 구하고 이동
        num = length - k % length
        curr = head
        while num:
            num -= 1
            last, curr = curr, curr.next

        # 끊어야 할 지점 끊기
        last.next = None

        # 시작 지점 반환
        return curr

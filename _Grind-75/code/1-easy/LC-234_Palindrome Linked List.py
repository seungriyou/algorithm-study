# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional['ListNode']) -> bool:
        """runner 기법 w/ reversed linked list"""

        slow = fast = head
        rev = None  # reversed linked list
        while fast and fast.next:
            # fast 전진
            fast = fast.next.next
            # rev 구성 & slow 전진
            rev, rev.next, slow = slow, rev, slow.next

        # 길이가 홀수라면, slow 한 칸 더 전진
        if fast:
            slow = slow.next

        # rev와 slow를 비교하며 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev  # 팰린드롬이라면 rev & slow 모두 None일 것

    def isPalindrome2(self, head: Optional['ListNode']) -> bool:
        """deque"""
        from collections import deque

        if not head:
            return True

        node = head
        q = deque()
        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    def isPalindrome1(self, head: Optional['ListNode']) -> bool:
        """
        runner 기법: slow, fast pointer
        - slow: list에 값을 저장해가기
        - fast가 끝에 도달하면, slow는 이전까지 저장했던 list에서 pop 해가며 확인 & 한 칸 전진
        """

        slow = fast = head
        half = []

        # 런너 기법
        while fast and fast.next:
            # half list에 값 저장
            half.append(slow.val)
            # 전진
            slow, fast = slow.next, fast.next.next

        # 길이가 홀수라면 slow 한 칸 더 전진(**)
        if fast:
            slow = slow.next

        # half에 가장 최근 추가된 원소부터 비교해가며 slow 전진
        while half and half.pop() == slow.val:
            slow = slow.next

        return not slow

        # while half and slow:
        #     # 다르면 False 반환
        #     if half.pop() != slow.val:
        #         return False
        #     # 같으면 한 칸 전진
        #     slow = slow.next

        # return True

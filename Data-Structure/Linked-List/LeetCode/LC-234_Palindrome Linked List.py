# [LTC] 234 - Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional, Deque
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # [sol 1] deque를 이용한 풀이
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = deque()

        if not head:
            return True

        node = head
        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop() != q.popleft():
                return False

        return True

    # [sol 2] runner 기법을 이용한 풀이
    def isPalindrome_runner(self, head: Optional[ListNode]) -> bool:
        # - 빠른 런너가 끝에 다다를 때 느린 런너는 중간 지점 도달
        # - 느린 런너는 중간까지 이동하며 역순으로 연결 리스트 rev를 만들어 나감
        # - 느린 런너가 나머지 경로를 이동할 때, rev의 값들과 일치하는지 확인

        # 런너 기법을 이용하여 역순 연결리스트 rev 구성
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next # 두 칸씩 이동 (if None: 길이가 짝수)
            rev, rev.next, slow = slow, rev, slow.next # 역순 연결리스트

        # 연결 리스트의 길이가 홀수라면, slow 런너를 한 칸 더 앞으로 (중간은 제외)
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인 (rev와 남은 느린 런너 앞에 남은 연결리스트 비교)
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        # 팰린드롬이라면 slow와 rev 모두 None에 도달했을 것이므로
        return not rev


linked_list = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(
            val=2,
            next=ListNode(
                val=1
            )
        )
    )
)
sol = Solution()
print(sol.isPalindrome(linked_list))
print(sol.isPalindrome_runner(linked_list))

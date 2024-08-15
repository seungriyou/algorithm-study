# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        slow = fast = head

        # fast를 n 번째 node 까지 이동
        for _ in range(n):
            fast = fast.next

        # fast가 끝에 도달했다면, 맨 첫 node를 remove 해야 하므로 head.next 반환
        if not fast:
            return head.next

        # fast와 slow를 함께 이동하면, fast가 끝에 도달할 때 slow는 뒤에서부터 n + 1 번째 node에서 멈춤
        while fast.next:
            slow, fast = slow.next, fast.next

        # 뒤에서부터 n + 1 번째 node의 next가 n - 1 번째 node를 가리키도록 함
        slow.next = slow.next.next

        return head

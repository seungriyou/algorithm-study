# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - odd는 첫 원소부터 2칸 간격, even은 두 번째 원소부터 2칸 간격
        - odd와 even을 따로 구성하고, odd.next = even_head로 연결
        - 로직
            - odd와 even 모두 두 칸 뒤의 node를 연결하고
            - 한 칸씩 전진
        - while loop에서 even and even.next를 확인하는 이유
            - even이 존재하면 odd도 존재함이 자명함
            - 전체 길이가 짝수라면, even이 마지막 node를 가리키게 되어 even.next가 None
            - 전체 길이가 홀수라면, odd가 마지막 node를 가리키게 되어 even이 None
        """

        if not head:
            return None

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            # odd와 even -> 두 칸 뒤의 node를 next로 연결
            odd.next, even.next = odd.next.next, even.next.next

            # odd와 even 모두 next로 전진
            odd, even = odd.next, even.next

        # odd와 even_head 연결
        odd.next = even_head

        return head

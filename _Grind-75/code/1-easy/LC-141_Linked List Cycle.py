# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hash table (O(N) space)
        p = head
        visited = set()

        while p is not None:
            if p in visited:
                return True
            visited.add(p)
            p = p.next

        return False

    def hasCycle_floyd(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Detection (O(1) space)
        slow = fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # print("cycle detected!")
                return True

        return False


###### review ######
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """O(N)"""
        visited = set()

        node = head

        while node:
            # visited에 현재 node가 있으면 cycle 발생!
            if node in visited:
                return True

            # 새로운 node면 visited 처리
            visited.add(node)

            # 다음 node로 이동
            node = node.next

        return False

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        """O(1)"""

        # slow pointer, fast pointer를 시작지점에 위치
        slow = fast = head

        # fast와 fast.next가 존재하는 동안
        while fast and fast.next:
            # slow는 한 칸, fast는 두 칸 이동
            slow = slow.next
            fast = fast.next.next

            # slow와 fast가 만난다면 cycle 발생!
            if slow == fast:
                return True

        # fast가 None에 도달했다면 cycle 발생 X
        return False

# https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                # slow를 head로 옮기기
                slow = head
                # slow와 fast가 다시 만날 때까지 한 칸씩 이동
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

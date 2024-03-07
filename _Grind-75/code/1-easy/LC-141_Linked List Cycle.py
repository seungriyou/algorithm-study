# https://leetcode.com/problems/linked-list-cycle/

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

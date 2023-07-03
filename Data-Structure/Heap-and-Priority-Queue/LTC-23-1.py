# [LTC] 23 - Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        root = result = ListNode(None) # -- 결과 연결 리스트
        # root는 시작점, result는 node를 점차 추가해나갈 때 사용

        # 각 연결 리스트의 시작 노드를 heap에 넣기
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) # -- (값, 리스트 번호, 해당 노드)

        # heap에서 하나씩 꺼내기
        while heap:
            node = heapq.heappop(heap)
            idx = node[1] # -- 리스트 번호
            result.next = node[2] # -- 해당 노드

            result = result.next # -- 다음 노드로 이동
            if result.next: # -- 다음 노드가 존재한다면, 그 노드를 heap에 넣기
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [ListNode(val=1, next=ListNode
    (val=4, next=ListNode(
        val=5))), ListNode(val=1, next=ListNode(
        val=3, next=ListNode(
            val=4))), ListNode(val=2, next=ListNode(
        val=6))]

sol = Solution()
print(sol.mergeKLists(lists=lists))

# [LTC] 23 - Merge k Sorted Lists

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # heapq 는 최소 힙 지원 -> 값이 작은 순서대로 pop() 가능
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 heap에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))  # 첫 번째 원소 = 우선순위 결정

    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]   # i
        result.next = node[2]   # 해당 list의 다음 노드를 이어서 저장하기 위함

        result = result.next    # 다음 노드로 이동
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next


# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [ListNode(val=1, next=ListNode
    (val=4, next=ListNode(
        val=5))), ListNode(val=1, next=ListNode(
        val=3, next=ListNode(
            val=4))), ListNode(val=2, next=ListNode(
        val=6))]

print(mergeKLists(lists=lists))

# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1. 각 linked list 마다 앞에서부터 node를 min heap에 넣기
        2. 가장 작은 node를 pop & res에 추가
        3. 그 다음 노드를 min heap에 넣기

        * node의 다음 node를 찾기 위해 min heap에 ListNode를 저장해야 하는데, 다음을 주의해야 한다.
            <1> q = [(head.val, head) for head in lists if head]
            <2> q = [(head.val, i, head) for i, head in enumerate(lists) if head]

            파이썬에서 tuple과 같은 자료형끼리의 비교는 앞에서부터 이루어진다! (min heap 구성 시 연산 필요)
            이때, <1> 처럼 넣으면 head.val이 같은 상황에서 head를 비교하는데, 이때 ListNode는 '<'로 비교가 불가능하다.
            따라서 <2> 처럼 head.val이 같은 상황에서도 무조건 다른 숫자형 값인 index i를 넣어줌으로써 ListNode를 비교하는 상황을 방지해야 한다.
        """
        import heapq

        # 1. 각 linked list의 맨 앞 node 저장
        # min heap에 ListNode도 저장해야하지만 이는 비교가 불가능하므로 index 추가
        q = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(q)

        # 결과 linked list
        res = head = ListNode()

        while q:
            # 2-1. 가장 작은 node pop
            val, i, node = heapq.heappop(q)
            # 2-2. res에 pop 한 node 추가하기
            head.next = node
            head = head.next

            # 3. pop 한 node의 다음 노드를 min heap에 넣기
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))

        return res.next

# https://leetcode.com/problems/top-k-frequent-words/

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        min heap (w/ __lt__ custom)
        (이때 min이란, (1) freq가 작거나 (2) freq가 같으면서 사전순으로 뒤에 오는 것)
        - TC: O(nlogk)
        - SC: O(n)
        """
        import heapq
        from collections import Counter

        class Node:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            def __lt__(self, other):
                # freq가 같다면, 사전순으로 뒤에 오면 lt
                if self.freq == other.freq:
                    return self.word > other.word
                # freq가 같지 않다면, freq가 작으면 lt
                return self.freq < other.freq

        pq = []
        for word, freq in Counter(words).items():
            node = Node(word, freq)
            # min heap의 크기가 k라면 push & pop
            if len(pq) == k:
                heapq.heappushpop(pq, node)
            # min heap의 크기가 k보다 작다면 push
            else:
                heapq.heappush(pq, node)

        # pq에서 word를 pop 한 후, top freq 순으로 반환
        res = [heapq.heappop(pq).word for _ in range(k)]
        return res[::-1]

    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        """
        max heap
        - TC: O(klogn)
        - SC: O(n)
        """
        import heapq
        from collections import Counter

        # pq에 넣기 (-frequency, word) -- O(n)
        pq = [(-v, k) for k, v in Counter(words).items()]
        heapq.heapify(pq)

        # top frequency k개 추출하기 -- O(klogn)
        res = [heapq.heappop(pq)[1] for _ in range(k)]

        return res

# [LTC] 347 - Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import Counter
import heapq

class Solution:
    # sol 1
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = Counter(nums)
    #     heap = []
    #     for n, c in counter.items():
    #         heapq.heappush(heap, (-c, n)) # -- 최소 힙이므로
    #
    #     return [heapq.heappop(heap)[1] for _ in range(k)]

    # sol 2
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return list(list(zip(*counter.most_common(k)))[0])

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))
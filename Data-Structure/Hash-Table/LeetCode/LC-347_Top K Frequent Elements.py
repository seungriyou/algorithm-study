# [LTC] 347 - Top K Frequent Elements

from collections import Counter
from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # 방법 1 - heapq 사용
    freqs = Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))  # count 수가 큰 것부터 내림차순으로 되도록

    topk = []
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk

    # 방법 2 - Pythonic way
    # return list(list(zip(*(Counter(nums).most_common(k))))[0])


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

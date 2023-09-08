# [LTC] 215 - Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k):
            result = heapq.heappop(heap)
        return -result

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)

        for _ in range(n - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums, k))

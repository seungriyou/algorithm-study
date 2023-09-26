# [LC] 215 - Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import heapq


class Solution:
    def findKthLargest_3(self, nums: List[int], k: int) -> int:
        # === quick select ===
        pivot = nums[0]
        larger, same, smaller = [], [], []
        for n in nums:
            if n > pivot:
                larger.append(n)
            elif n < pivot:
                smaller.append(n)
            else:
                same.append(n)

        L, S = len(larger), len(same)

        if k <= L:  # -- larger 쪽에 kth largest가 있는 경우
            return self.findKthLargest(larger, k)
        elif k > L + S:  # -- smaller 쪽에 kth largest가 있는 경우 (smaller에서 k-L-S 번째 largest 찾기)
            return self.findKthLargest(smaller, k - L - S)
        else:  # -- same 쪽에 kth largest가 있는 경우 (same에는 모두 pivot과 같은 원소가 들어있음)
            return pivot

    def findKthLargest_tle(self, nums: List[int], k: int) -> int:
        # === quick select ===
        def partition(left, right, arr):
            p = left  # -- pivot보다 작은 원소들 이후의 첫 번째 index를 가리키게 되므로, 마지막에 pivot과 swap 되면 pivot의 index를 나타냄
            pivot = arr[right]  # -- 배열의 맨 오른쪽 값을 pivot으로 설정
            for i in range(left, right):
                if arr[i] <= pivot:
                    arr[i], arr[p] = arr[p], arr[i]
                    p += 1
            arr[p], arr[right] = arr[right], arr[p]
            return p

        def quick_select(low, high, arr, k):
            pivot_index = partition(low, high, arr)
            if pivot_index > k:  # -- left part
                return quick_select(low, pivot_index - 1, arr, k)
            elif pivot_index < k:  # -- right part
                return quick_select(pivot_index + 1, high, arr, k)
            else:  # -- find kth element
                return arr[pivot_index]

        n = len(nums)
        return quick_select(0, n - 1, nums, n - k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

    def findKthLargest_1(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            heapq.heappush(q, -n)
        for _ in range(k):
            result = -heapq.heappop(q)
        return result

sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(sol.findKthLargest(nums, k))

# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        k-th largest element in an array w/o sorting
        => heap

        - TC: O(nlogk)
        - SC: O(k)
        """
        import heapq

        # min heap 구성
        heapq.heapify(nums)

        # min heap이므로 거꾸로 len(nums) - k + 1 번째 smallest element 구하기
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def findKthLargest_qs_TLE(self, nums: List[int], k: int) -> int:
        """
        k-th largest element in an array w/o sorting
        => quick select -> TLE

        - TC: O(n) (worst O(n^2) 때문에 TLE 발생하는 듯)
        - SC: O(1) (iteration 적용. recursion stack X)
        """

        def partition(left, right):
            # pivot(맨 오른쪽 원소)을 기준으로 pivot 보다 작은 원소는 왼쪽에, pivot 보다 큰 원소는 오른쪽에 위치하도록 함
            p = left
            pivot = nums[right]

            # pivot의 위치가 될 인덱스인 p 업데이트
            for i in range(left, right):
                if nums[i] < pivot:  # -- **주의** <=가 아니라 <인 이유는, 거꾸로 k-th largest를 찾기 때문임!
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            return p

        left, right = 0, len(nums) - 1

        # iteration
        while True:
            pivot_idx = partition(left, right)
            if pivot_idx < len(nums) - k:
                left = pivot_idx + 1
            elif pivot_idx > len(nums) - k:
                right = pivot_idx - 1
            else:
                return nums[pivot_idx]

    def findKthLargest_qs_noTLE(self, nums: List[int], k: int) -> int:
        """
        k-th largest element in an array w/o sorting
        => 다른 방법으로 구현한 quick select -> TLE 발생 X

        - TC: O(n) (worst O(n^2) 때문에 TLE 발생하는 듯)
        - SC: O(1) (iteration 적용. recursion stack X)
        """
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

        # larger 쪽에 kth largest가 있는 경우
        if k <= L:
            return self.findKthLargest(larger, k)
        # smaller 쪽에 kth largest가 있는 경우 (smaller에서 k-L-S 번째 largest 찾기)
        elif k > L + S:
            return self.findKthLargest(smaller, k - L - S)
        # same 쪽에 kth largest가 있는 경우 (same에는 모두 pivot과 같은 원소가 들어있음)
        else:
            return pivot

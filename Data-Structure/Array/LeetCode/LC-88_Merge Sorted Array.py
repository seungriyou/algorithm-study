# [LTC} 88 - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums2가 비어있다면 동작 필요 X
        if not nums2:
            return

        # nums1의 last 부분이 0으로 비워져있으므로, last 부분부터 거꾸로 큰 값 채워나가기 위한 pointer
        p1, p2 = m - 1, n - 1

        # -- p2 >= 0 일 때만 돌아가도록
        for i in range(m + n - 1, -1, -1):
            if p1 >= 0 and nums1[p1] > nums2[p2]:  # -- p2 == -1 인 상황
                nums1[i] = nums1[p1]
                p1 -= 1
            elif p2 >= 0:
                nums1[i] = nums2[p2]
                p2 -= 1

sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)

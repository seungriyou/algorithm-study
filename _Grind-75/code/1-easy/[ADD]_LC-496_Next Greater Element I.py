# https://leetcode.com/problems/next-greater-element-i/

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """monotonic stack"""

        stack = []
        mapping = {}

        for n in nums2:
            while stack and stack[-1] < n:
                mapping[stack.pop()] = n
            stack.append(n)

        while stack:
            mapping[stack.pop()] = -1

        return [mapping[n] for n in nums1]

    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """monotonic stack"""

        # create idx mapping of nums2
        idx2 = {n: i for i, n in enumerate(nums2)}

        # make next_greater list of nums2 w/ monotonic stack
        stack = []
        next_greater = [-1] * len(nums2)

        for i, n in enumerate(nums2):
            while stack and nums2[stack[-1]] <= n:
                next_greater[stack.pop()] = n
            stack.append(i)

        # create result list w/ next_greater
        res = [next_greater[idx2[n]] for n in nums1]
        return res

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """brute-force"""

        idx_2 = {n: i for i, n in enumerate(nums2)}
        res = [-1] * len(nums1)

        for i, n in enumerate(nums1):
            for idx in range(idx_2[n] + 1, len(nums2)):
                if n < nums2[idx]:
                    res[i] = nums2[idx]
                    break

        return res

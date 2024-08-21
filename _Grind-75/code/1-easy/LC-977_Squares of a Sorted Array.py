# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        TC: O(n) / SC: O(1) (except res)
        non-decreasing 순서로 이루어져 있으므로, two pointer를 양쪽에서부터 좁혀오며 abs() 값이 더 큰 값의 제곱을
        res 배열의 맨 뒤에서부터 채워나가면 된다!
        """
        res = [-1] * len(nums)
        lo, hi = 0, len(nums) - 1
        i = hi

        # while lo <= hi:
        while i >= 0:
            left, right = abs(nums[lo]), abs(nums[hi])
            if left <= right:
                res[i] = right * right
                hi -= 1
            else:
                res[i] = left * left
                lo += 1
            i -= 1

        return res

    def sortedSquares1(self, nums: List[int]) -> List[int]:
        """O(n)"""
        # early return
        if nums[-1] <= 0:
            res = [num * num for num in nums]
            return res[::-1]

        if nums[0] >= 0:
            res = [num * num for num in nums]
            return res

        # 양수 + 0 / 음수 나누는 기준 찾기
        p, _len, res = 0, len(nums), []
        while nums[p] < 0:
            p += 1
        n = p - 1

        while n >= 0 and p < _len:
            neg, pos = nums[n], nums[p]
            if -neg <= pos:
                res.append(neg * neg)
                n -= 1
            else:
                res.append(pos * pos)
                p += 1

        while n >= 0:
            res.append(nums[n] * nums[n])
            n -= 1

        while p < _len:
            res.append(nums[p] * nums[p])
            p += 1

        return res

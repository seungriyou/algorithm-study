# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        condition(divisor): (divisor로 나눈 몫의 합)이 threshold 이하인지 여부
            -> 위를 만족하는 값 중 smallest divisor 구하기

        - lo: 1 (-> sum이 sum(nums)가 될 것)
        - hi: max(nums) (-> sum이 1이 될 것)
        """

        def condition(divisor):
            # division의 결과는 rounded to the nearest integer "greater than or equal" to that element ***
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        lo, hi = 1, max(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if condition(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo  # return smallest divisor

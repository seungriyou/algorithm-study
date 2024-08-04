# https://leetcode.com/problems/split-array-largest-sum/

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        (1011. Capacity To Ship Packages Within D Days 와 비슷한 문제)

        k개의 non-empty subarrays 중 largest sum 값이 minimized 되도록 할 때,
        minimized largest sum of split 구하기

        minimized largest sum of split:
            - lo: max(nums)
            - hi: sum(nums)

        feasible(sum_value): largest sum 값이 sum_value가 되도록 split 했을 때, subarray 개수가 k 이하인지 여부 반환
        """

        def feasible(sum_value):
            cnt, curr_sum = 1, 0

            for n in nums:
                curr_sum += n
                if curr_sum > sum_value:
                    cnt += 1
                    curr_sum = n
                    if cnt > k:
                        return False

            return True

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if feasible(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo

    def splitArray1(self, nums: List[int], k: int) -> int:
        """
        (1011. Capacity To Ship Packages Within D Days 와 비슷한 문제)

        k개의 non-empty subarrays 중 largest sum 값이 minimized 되도록 할 때,
        minimized largest sum of split 구하기

        minimized largest sum of split:
            - lo: max(nums)
            - hi: sum(nums)

        get_number_of_split(sum_value): largest sum 값이 sum_value가 되도록 split 했을 때, subarray의 개수 반환
        """

        def get_number_of_split(sum_value):
            cnt, curr_sum = 1, 0

            for n in nums:
                curr_sum += n
                if curr_sum > sum_value:
                    cnt += 1
                    curr_sum = n

            return cnt

        lo, hi = max(nums), sum(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if get_number_of_split(mid) > k:
                lo = mid + 1
            else:
                hi = mid  # look for left

        return lo

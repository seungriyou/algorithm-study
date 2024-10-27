# https://leetcode.com/problems/subarray-product-less-than-k/

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        [ two-pointer & sliding window ]
        - prefix sum 과 유사한 prefix product 이용
            -> 모든 원소는 양수이므로 non-decreasing 순서로 정렬됨
        - sliding window를 통해 product가 strictly less than k인 interval을 트래킹해나가며 동시에 res 세기
            -> prod 변수가 그 valid한 product 값이 되므로, list 전체를 가져갈 필요가 없음 (O(1) space

        > TC: O(n)
        > SC: O(1)
        """

        left, prod, res = 0, 1, 0

        for right, num in enumerate(nums):
            prod *= num

            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1

            res += right - left + 1

        return res

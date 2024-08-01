# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [ Kadane's Algorithm (DP) ]
        기존 풀이에서 max_product와 min_product를 구할 때 세 가지 값을 비교하는 로직을 줄이기 위해서
        nums[i]가 음수인 경우에 max_product와 min_product를 swap 한다.
        (음수를 곱해야 하는 경우에는 min_product에 곱해야 더 큰 값을 얻을 수 있으므로)
        """

        max_product = min_product = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(max_product * num, num)
            min_product = min(min_product * num, num)

            result = max(result, max_product)

        return result

    def maxProduct1(self, nums: List[int]) -> int:
        """
        [ Kadane's Algorithm (DP) ]
        현재 nums[i]를 보고 있고, nums[i - 1]까지의 max product subarray를 max_product, min product subarray를 min_product라고 하자.

        이때, (1) nums[i]가 양수 및 음수일 때와 (2) 현재 값부터 시작하는 subarray를 채택하는 경우를 모두 고려하여
        nums[i]에서의 max_product, min_product 값으로 업데이트 하려면, 다음과 같은 식을 이용하면 된다.
            max_product = max(max_product * nums[i], min_product * nums[i], nums[i])
            min_product = min(max_product * nums[i], min_product * nums[i], nums[i])
        """

        max_product = min_product = result = nums[0]

        for num in nums[1:]:
            max_product_tmp, min_product_tmp = max_product * num, min_product * num

            max_product = max(max_product_tmp, min_product_tmp, num)
            min_product = min(max_product_tmp, min_product_tmp, num)

            result = max(result, max_product)

        return result

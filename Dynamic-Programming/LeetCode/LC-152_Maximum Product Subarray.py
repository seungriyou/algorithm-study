# [LTC] 152 - Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        nums를 순차적으로 순회한다고 할 때, i-th 원소(nums[i])까지의 max_prod 값은
        - nums[i]가 양수라면, (nums[i-1]까지의 max_prod에 nums[i]를 곱한 값)과 (nums[i])를 비교하여,
        - nums[i]가 음수라면, (nums[i-1]까지의 min_prod에 nums[i]를 곱한 값)과 (nums[i])를 비교하여
        구할 수 있다.
        따라서 (nums[i-1]까지의 max_prod) 뿐만 아니라 (nums[i-1]까지의 min_prod)도 트래킹한다.
        """

        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:  # -- nums[1:] -> copy가 됨..!
            max_prod_num, min_prod_num = max_prod * num, min_prod * num
            max_prod = max(max_prod_num, min_prod_num, num)
            min_prod = min(max_prod_num, min_prod_num, num)
            result = max(result, max_prod)

        return result

nums = [2,3,-2,4]
sol = Solution()
print(sol.maxProduct(nums))

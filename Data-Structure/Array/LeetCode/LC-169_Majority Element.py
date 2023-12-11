# [LC] 169 - Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List


class Solution:
    """
    (1) boyer-moore majority vote algorithm (O(n) time & O(1) space)
    (2) sorting
    (3) divide-conquer
    (4) bit
    """

    def majorityElement(self, nums: List[int]) -> int:
        # === boyer-moore majority vote algorithm (O(n) time & O(1) space) ===
        # 과반수 이상 등장하는 원소가 있다는 가정하에, 해당 원소를 찾음
        major = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if major == nums[i]:
                cnt += 1
            elif cnt == 0:
                major, cnt = nums[i], 1
            else:
                cnt -= 1
        return major

    def majorityElement_dc(self, nums: List[int]) -> int:
        # === divide and conquer ===
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return a if nums.count(a) > half else b

    def majorityElement_dc2(self, nums: List[int]) -> int:
        # === divide and conquer (w/o copying array) ===
        def count_subarray(l, r, n1, n2):
            cnt_1 = cnt_2 = 0
            for i in range(l, r + 1):
                if nums[i] == n1:
                    cnt_1 += 1
                if nums[i] == n2:
                    cnt_2 += 1
            return cnt_1, cnt_2

        def helper(l, r):
            if l == r:
                return nums[l]

            # mid = l + (r - l) // 2
            mid = l + ((r - l) >> 2)
            left = helper(l, mid)
            right = helper(mid + 1, r)

            if left == right:
                return left

            cnt_l, cnt_r = count_subarray(l, r, left, right)
            return left if cnt_l > cnt_r else right
            # return left if cnt_l > (r - l + 1) // 2 else right  # -- 비둘기집 원리 이용

        return helper(0, len(nums) - 1)

    def majorityElement_bm(self, nums: List[int]) -> int:
        # === bit manipulation ===
        # It swipes all numbers 32 times checking for fixed bit every time.
        # If this bit is set more than half times it means that in the result this bit should be set.

        major = 0
        mask = 1
        OFFSET = int(1e9)  # -- testcase
        for i in range(32):
            bits = 0
            for num in nums:
                if (num + OFFSET) & mask:
                    bits += 1
            if bits > len(nums) / 2:
                major |= mask
            mask <<= 1

        return major - OFFSET

    def majorityElement_bm2(self, nums: List[int]) -> int:
        # === bit manipulation ===
        OFFSET = int(1e9)  # -- testcase
        bits = [0] * 32
        for i in range(len(nums)):
            for j in range(32):
                bits[j] += ((nums[i] + OFFSET) >> j) & 1
        major = 0
        for j in range(32):
            bits[j] = bits[j] > len(nums) / 2
            major += bits[j] << j

        return major - OFFSET

    def majorityElement_sr(self, nums: List[int]) -> int:
        # === sorting ===
        # 정렬 후 중간 위치 == 과반수 이상 등장하는 원소
        nums.sort()
        return nums[len(nums) // 2]

sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))

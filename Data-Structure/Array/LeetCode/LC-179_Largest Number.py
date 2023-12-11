# [LTC] 179 - Largest Number
# https://leetcode.com/problems/largest-number/

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge_sort(nums):
            if len(nums) < 2:
                return nums

            mid = len(nums) // 2
            l_nums = merge_sort(nums[:mid])
            r_nums = merge_sort(nums[mid:])

            merged_arr = []
            l = r = 0
            while l < len(l_nums) and r < len(r_nums):
                # print(f"{str(l_nums[l]) + str(r_nums[r])=} / {str(r_nums[r]) + str(l_nums[l])=}")
                if str(l_nums[l]) + str(r_nums[r]) < str(r_nums[r]) + str(l_nums[l]):
                    # -- 순차적으로 unicode 값을 비교하므로 int() 안해도 ok
                    merged_arr.append(r_nums[r])
                    r += 1
                else:
                    merged_arr.append(l_nums[l])
                    l += 1

            merged_arr += l_nums[l:]
            merged_arr += r_nums[r:]
            # while l < len(l_nums):
            #     merged_arr.append(l_nums[l])
            #     l += 1
            # while r < len(r_nums):
            #     merged_arr.append(r_nums[r])
            #     r += 1

            return merged_arr

        sorted_nums = merge_sort(nums)

        return ''.join(map(str, sorted_nums)).lstrip('0') or '0'

sol = Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))

# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement_sort(self, nums: List[int]) -> int:
        """
        sort 후 정 가운데에 위치한 원소 == 과반수 이상 등장하는 원소
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_bm1(self, nums: List[int]) -> int:
        """
        boyer-moore majority vote algorithm (O(n) time & O(1) space)
        """
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

    def majorityElement(self, nums: List[int]) -> int:
        """
        boyer-moore majority vote algorithm (O(n) time & O(1) space)
        """
        cnt = major = 0

        for num in nums:
            if cnt == 0:
                major = num

            if major == num:
                cnt += 1
            else:
                cnt -= 1

        return major


###### review ######
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_cnt, m_elem = 1, nums[0]

        for i in range(1, len(nums)):
            c_elem = nums[i]

            if m_elem == c_elem:
                m_cnt += 1
            elif m_cnt == 0:
                m_cnt, m_elem = 1, c_elem
            else:
                m_cnt -= 1

        return m_elem

    def majorityElement2(self, nums: List[int]) -> int:
        """O(1) space"""
        m_cnt, m_elem = 0, nums[0]

        for c_elem in nums:
            # 현재까지의 m_elem과 현재 c_elem이 같다면, m_cnt ++
            if m_elem == c_elem:
                m_cnt += 1

            # 현재까지의 m_elem과 현재 c_elem이 다르다면,
            else:
                # m_cnt --
                m_cnt -= 1

                # m_cnt이 0에 도달하면, m_elem을 c_elem으로 변경하고 m_cnt ++
                if m_cnt == 0:
                    m_elem = c_elem
                    m_cnt += 1

        return m_elem

    def majorityElement1(self, nums: List[int]) -> int:
        """O(N) space"""
        nums.sort()
        return nums[len(nums) // 2]

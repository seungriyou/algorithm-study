# [LC] 287 - Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # === bit manipulation ===
        result = 0
        n = len(nums)

        # 0이 아닌 첫 번째 bit 찾기
        bit_max = 31
        while (n - 1) >> bit_max == 0:
            bit_max -= 1

        for p in range(bit_max + 1):
            a = b = 0  # a: [1 ~ n]에서 bit 세기, b: nums에서 bit 세기
            bit = 1 << p  # 오른쪽부터 왼쪽까지 32개 bit 확인하기 위함
            for i in range(n):
                # 1 ~ n 까지 bit 세면 되므로 i > 0
                if i > 0 and (i & bit):
                    a += 1
                # nums에서 bit 세야 하므로
                if nums[i] & bit:
                    b += 1
            # b > a인 경우, 해당 bit가 1인 수가 중복된 것임
            if b > a:
                result += bit
        return result

    def findDuplicate_floyd(self, nums: List[int]) -> int:
        # === floyd's cycle detection (runner) ===
        # -- linked list 처럼 간주 (pointer가 가리키는 값을 index로 사용) ([1, n] 내의 숫자 n + 1개)
        # -- duplicate number가 존재한다는 것이 보장되어 있으므로, cycle은 항상 발생함

        # start at the first element
        slow = fast = nums[0]

        # slow(1칸)와 fast(2칸)를 진행하다가 slow == fast 만나는 지점이 있으면 stop
        # 해당 지점은 cycle 내에 존재하는 지점이 됨
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # slow는 다시 처음으로 옮기고 fast는 그대로 둔 후, slow와 fast를 모두 1칸씩 진행시킴
        # 이렇게 하면, slow와 fast가 만나는 지점이 cycle의 시작지점이 됨
        # --> 원리..?
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def findDuplicate_bs(self, nums: List[int]) -> int:
        # === binary search ===
        """
        1 ~ n 까지의 수가 존재하고, 그 중 단 하나의 수만 두 번 등장하여 총 n + 1 개의 숫자가 nums에 존재함
        비둘기집 원리를 이용하자.
        - 현재 보고있는 값(mid)과 비교했을 때 작거나 같은 값들의 개수를 세었을 때 mid 보다 크다면 중복되는 값이 [left, mid]에 있는 것이다.
        - ... mid 보다 작거나 같다면 중복되는 값이 [mid + 1, right]에 있는 것이다.
        이때, [left, mid]와 [mid + 1, right]는 index의 범위가 아닌, 중복되는 숫자 값의 범위라고 생각하면 된다.
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            cnt = 0

            for n in nums:
                if n <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            else:
                left = mid + 1

        return left

sol = Solution()
nums = [1,3,4,2,2]
print(sol.findDuplicate(nums))

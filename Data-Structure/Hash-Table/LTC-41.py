# [LTC] 41 - First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        주어진 nums의 길이를 n이라고 할 때, first missing positive는 [1, 2, ..., n, n + 1] 내에 존재할 것이다.
        우선, nums 중 first missing positive가 [1, ..., n] 내에 있는지 살펴보고,
        없다면 n + 1을 반환한다.

        ex) [3, 4, -1, 1]
        """

        n = len(nums)

        # 1 이상 n 이하인 값만 남겨두고, 나머지는 0으로 바꾼다.
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
        # -- [3, 4, 0, 1]

        # nums[i] : (i + 1)이 nums에 존재할 때마다 (n + 1) 씩 더한다. (1 <= i + 1 <= n)
        # (n + 1) 씩 더해야 %(n + 1) 연산 시 원래의 nums[i] 값이 유지되며,
        # %(n + 1) 연산을 하는 이유는 순회 시, 복원해야 하는 원래의 nums[i] 값의 최대 값이 n이기 때문이다.
        for i in range(n):
            if (tmp := nums[i] % (n + 1)) != 0:  # -- 1 <= tmp <= n
                idx = tmp - 1  # -- 0 <= idx <= n - 1
                nums[idx] += n + 1
        # -- [8, 4, 5, 6]

        for i in range(n):
            # (i + 1)이 한 번이라도 등장했다면 nums[i] >= n + 1 일 것이므로,
            # nums[i] < n + 1라면 (i + 1)가 nums에 존재하지 않는 것이다.
            if nums[i] < n + 1:
                return i + 1

        # first missing positive가 [1, ..., n] 내에 없으므로,
        # 즉, nums가 [1, ..., n] 이므로
        # first missing positive는 n + 1이다.
        return n + 1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(1, n):
            if nums[i] // n == 0:
                return i

        return n

nums = [3,4,-1,1]
sol = Solution()
print(sol.firstMissingPositive(nums))

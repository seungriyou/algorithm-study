# https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex1(self, nums: List[int]) -> int:
        """
        pivot index = 해당 위치를 기준으로 왼쪽의 sum == 오른쪽의 sum이어야 함
        -> prefix sum을 양방향으로 구하고, 값이 같은 leftmost index를 구하면 됨

        1   7   3   6   5   6
        ----------------------
        1   8  11  17  22  28   -> (ps1)
        28 27  20  17  11   6   <- (ps2)

        2   1  -1
        ----------
        2   3   2   ->  (ps1)
        2   0  -1   <-  (ps2)

        - TC: O(n)
        - SC: O(n)
        """

        ps1, ps2, n = [0], [0], len(nums)

        for i in range(n):
            ps1.append(ps1[-1] + nums[i])
            ps2.append(ps2[-1] + nums[n - i - 1])

        for i in range(1, n + 1):
            if ps1[i] == ps2[n + 1 - i]:
                return i - 1

        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        """
        SC: O(1)로 optimize
        """

        lsum, rsum = 0, sum(nums)

        for i, num in enumerate(nums):
            # **순서 주의**
            rsum -= num

            if lsum == rsum:
                return i

            lsum += num

        return -1

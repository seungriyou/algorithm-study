# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        # 제곱해서 x보다 큰 leftmost 찾고, 거기에서 -1
        lo, hi = 0, x + 1  # -> x + 1임에 주의!!

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if x < mid * mid:
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo - 1

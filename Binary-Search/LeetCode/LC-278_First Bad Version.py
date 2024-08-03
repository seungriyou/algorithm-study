# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # find leftmost
        lo, hi = 1, n

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if isBadVersion(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo

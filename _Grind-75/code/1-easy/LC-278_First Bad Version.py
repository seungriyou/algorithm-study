# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s, e = 1, n

        while s < e:
            mid = s + (e - s) // 2
            if isBadVersion(mid):
                e = mid
            else:
                s = mid + 1

        return e

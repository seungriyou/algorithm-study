# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight1(self, n: int) -> int:
        """Bit Manipulation"""
        cnt = 0
        # 오른쪽 비트부터 확인
        while n:
            cnt += n & 1
            n >>= 1
        return cnt

    def hammingWeight2(self, n: int) -> int:
        """Brian Kernighan's Algorithm
        ref: https://leetcode.com/problems/number-of-1-bits/solutions/4341511/faster-lesser-3-methods-simple-count-brian-kernighan-s-algorithm-bit-manipulation-explained
        """
        cnt = 0
        # 오른쪽부터 1인 비트 없애기 (drops the lowest set bit)
        while n:
            n &= n - 1
            cnt += 1
        return cnt
    
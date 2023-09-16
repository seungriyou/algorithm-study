# [LTC] 191 - Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight1(self, n: int) -> int:
        cnt = 0

        for i in range(32):
            cnt += (n >> i) & 1

        return cnt

    def hammingWeight2(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1  # -- n에서 1을 빼면, rightmost bit 1이 0으로 바뀌고, 그 bit의 오른쪽 bit들이 1로 변한다.
            # --- 따라서 n 과 (n - 1)을 & 연산하면 rightmost bit 1을 0으로 지우는 효과가 있다.
            cnt += 1

        return cnt

    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += (n & 1)
            n >>= 1

        return cnt

sol = Solution()
n = int(0b00000000000000000000000000001011)
print(sol.hammingWeight(n))

# [LTC] 190 - Reverse Bits
# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(16):
            left = (n >> (31 - i)) & 1
            right = (n >> i) & 1
            # answer |= left << i
            # answer |= right << (31 - i)
            answer |= (left << i) | (right << (31 - i))
        return answer

    def reverseBits_2(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


sol = Solution()
n = int("0b00000010100101000001111010011100", 2)
print(sol.reverseBits(n))

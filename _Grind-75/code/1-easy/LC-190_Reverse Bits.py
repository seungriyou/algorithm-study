# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        32bit를 모두 순회하지 않고 한 번에 2bit 씩 16번 확인하기 (양끝에서부터)
        """

        res = 0
        for i in range(16):
            left = (n >> (31 - i)) & 1
            right = (n >> i) & 1
            res |= (left << i) | (right << (31 - i))

        return res

    def reverseBits1(self, n: int) -> int:
        """
        n의 LSB부터 bit 값을 가져와서 오른쪽에 붙여나가기
        """

        res = 0
        for i in range(32):
            res |= ((n >> i) & 1) << (31 - i)

        return res

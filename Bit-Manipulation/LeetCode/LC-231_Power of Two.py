# [LC] 231 - Power of Two
# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n = 0 인 경우, output = False여야 함
        # n & (n - 1) == 0만 있으면 True 이므로 조건 추가 필요
        return n != 0 and n & (n - 1) == 0

n = 16
sol = Solution()
print(sol.isPowerOfTwo(n))

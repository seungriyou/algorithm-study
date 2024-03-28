# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        p = 0
        number = ""

        # 1. ignore leading whitespace
        s = s.lstrip()

        # s가 비어있으면 0 반환
        if not s:
            return 0

        # 2. negative / positive
        if s[0] == "-":
            sign = -1
            p = 1
        elif s[0] == "+":
            p = 1

        # 3. read characters until the next non-digit character / end of the input is reached
        for i in range(p, len(s)):
            if s[i] in set("0123456789"):
                number += s[i]
            else:
                break

        # number가 비어있으면 0 반환
        if not number:
            return 0

        # 4. convert digits into an integer & change the sign as necessary
        number = sign * int(number)

        # 5. clamp the integer to remain in [-2^31, 2^31-1] range
        number = min(number, 2 ** 31 - 1)
        number = max(-(2 ** 31), number)

        return number

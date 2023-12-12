# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )
        answer = 0

        for i in range(len(s)):
            if i < len(s) - 1 and symbols[s[i]] < symbols[s[i + 1]]:
                answer -= symbols[s[i]]
            else:
                answer += symbols[s[i]]

        return answer

    def romanToInt1(self, s: str) -> int:
        symbols = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )
        pre = dict(
            I={"V", "X"},
            X={"L", "C"},
            C={"D", "M"}
        )
        i = answer = 0

        while i < len(s):
            if s[i] in pre and i < len(s) - 1 and s[i + 1] in pre[s[i]]:
                answer += symbols[s[i + 1]] - symbols[s[i]]
                i += 2
            else:
                answer += symbols[s[i]]
                i += 1

        return answer

sol = Solution()
s = "MCMXCIV"
print(sol.romanToInt(s))

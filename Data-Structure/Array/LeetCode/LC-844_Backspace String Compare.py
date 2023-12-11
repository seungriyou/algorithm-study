# [LC] 844 - Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i1, i2 = len(s) - 1, len(t) - 1
        cnt1, cnt2 = 0, 0

        while i1 >= 0 or i2 >= 0:
            while i1 >= 0:
                if s[i1] == "#":
                    cnt1 += 1
                    i1 -= 1
                elif s[i1] != "#" and cnt1 > 0:
                    cnt1 -= 1
                    i1 -= 1
                else:
                    break

            while i2 >= 0:
                if t[i2] == "#":
                    cnt2 += 1
                    i2 -= 1
                elif t[i2] != "#" and cnt2 > 0:
                    cnt2 -= 1
                    i2 -= 1
                else:
                    break

            if (i1 < 0 and i2 >= 0) or (i1 >= 0 and i2 < 0):
                return False
            if i1 >= 0 and i2 >= 0 and s[i1] != t[i2]:
                return False

            i1 -= 1
            i2 -= 1

        return True


class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for c in s:
            if c == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(c)

        stack2 = []
        for c in t:
            if c == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(c)

        return stack1 == stack2


s = "ab##"
t = "c#d#"
sol1 = Solution()
sol2 = Solution2()
print(sol1.backspaceCompare(s, t))
print(sol2.backspaceCompare(s, t))

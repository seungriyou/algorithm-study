# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """O(1) space"""

        p1, p2 = len(s) - 1, len(t) - 1  # s, t의 pointer (뒤에서부터 확인!)
        b1, b2 = 0, 0  # 어떤 문자 뒤에 등장하는 backspace #의 개수

        while p1 >= 0 or p2 >= 0:
            # text editor에 남을 문자에서 stop
            while p1 >= 0:
                if s[p1] == "#":
                    b1 += 1
                    p1 -= 1
                elif b1 > 0:
                    b1 -= 1
                    p1 -= 1
                else:
                    break
            while p2 >= 0:
                if t[p2] == "#":
                    b2 += 1
                    p2 -= 1
                elif b2 > 0:
                    b2 -= 1
                    p2 -= 1
                else:
                    break

            # 동일하지 않은 경우 판단
            if (p1 < 0 and p2 >= 0) or (p1 >= 0 and p2 < 0):
                return False
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False

            # pointer 이동
            p1 -= 1
            p2 -= 1

        return True

    def backspaceCompare2(self, s: str, t: str) -> bool:
        """O(n) space"""

        st1, st2 = [], []

        for _s in s:
            if _s == "#":
                if st1:
                    st1.pop()
            else:
                st1.append(_s)

        for _t in t:
            if _t == "#":
                if st2:
                    st2.pop()
            else:
                st2.append(_t)

        return st1 == st2

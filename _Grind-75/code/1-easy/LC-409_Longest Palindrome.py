# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        appears_odd = set()

        for c in s:
            if c in appears_odd:
                appears_odd.remove(c)
            else:
                appears_odd.add(c)

        return len(s) - len(appears_odd) + 1 if appears_odd else len(s)

    def longestPalindrome1(self, s: str) -> int:
        from collections import Counter

        cnt = Counter(s)
        result = 0

        for i, c in cnt.items():
            result += c // 2

        return result * 2 + (len(s) > result * 2)  # len(s) > result * 2 라면 s에 홀수 번 등장하는 문자가 하나 이상이라는 것이기 때문

    def longestPalindrome2(self, s: str) -> int:
        from collections import Counter

        cnt = Counter(s)

        result = 0
        contains_odd_cnt = False

        for i, c in cnt.items():
            if c & 1:
                if not contains_odd_cnt:
                    contains_odd_cnt = True

                result += c - 1
            else:
                result += c

        return result + 1 if contains_odd_cnt else result

###### review ######
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        appeared_odd = False
        res = 0

        for c, cnt in counter.items():
            # 홀수라면
            if cnt & 1:
                res += cnt - 1
                appeared_odd = True

            # 짝수라면
            else:
                res += cnt

        return res + 1 if appeared_odd else res

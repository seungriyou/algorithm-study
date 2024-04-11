# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        from collections import defaultdict

        if len(s) != len(t):
            return False

        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1

        for c in t:
            cnt[c] -= 1

        for i in cnt.values():
            if i != 0:
                return False

        return True

    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        return s == t

    def isAnagram3(self, s: str, t: str) -> bool:
        from collections import Counter

        if len(s) != len(t):
            return False

        s_cnt = Counter(s)
        t_cnt = Counter(t)
        return s_cnt == t_cnt

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt = [0] * 26

        for ss, tt in zip(s, t):
            cnt[ord(ss) - ord('a')] += 1
            cnt[ord(tt) - ord('a')] -= 1

        for c in cnt:
            if c != 0:
                return False

        return True

###### review ######
class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        _s = sorted(s)
        _t = sorted(t)

        return _s == _t

    def isAnagram1(self, s: str, t: str) -> bool:
        # 훨씬 빠르다..!

        from collections import Counter

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0] * 26
        for _s in s:
            counter[ord(_s) - ord('a')] += 1
        for _t in t:
            counter[ord(_t) - ord('a')] -= 1

        return not any(counter)

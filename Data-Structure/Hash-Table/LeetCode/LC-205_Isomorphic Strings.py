# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_seen = dict()
        t_seen = dict()

        for i in range(len(s)):
            if s[i] in s_seen:
                # t[i]가 동일하지 않다면 불가
                if t[i] != s_seen[s[i]]:
                    return False
            else:
                if t[i] in t_seen and s[i] != t_seen[t[i]]:
                    return False
                s_seen[s[i]] = t[i]
                t_seen[t[i]] = s[i]

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        s_seen = dict()
        t_seen = dict()

        for i in range(len(s)):
            if s[i] in s_seen and s_seen[s[i]] != t[i]:
                return False
            if t[i] in t_seen and t_seen[t[i]] != s[i]:
                return False

            s_seen[s[i]] = t[i]
            t_seen[t[i]] = s[i]

        return True

s = "paper"
t = "title"
sol = Solution()
print(sol.isIsomorphic(s, t))

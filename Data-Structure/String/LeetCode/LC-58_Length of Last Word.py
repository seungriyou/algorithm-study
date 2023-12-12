# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split()[-1])

        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            elif length > 0:
                return length

        return length

s = "luffy is still joyboy"
sol = Solution()
print(sol.lengthOfLastWord(s))

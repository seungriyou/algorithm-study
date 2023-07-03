# [LTC] 3 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appeared = {}
        max_length = start = 0
        for i, char in enumerate(s):
            # char 가 이미 등장했던 문자인 경우, idx 업데이트
            if char in appeared and start <= appeared[char]:
                start = appeared[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            # 현재 문자열의 위치 업데이트
            appeared[char] = i

        return max_length

s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring((s)))

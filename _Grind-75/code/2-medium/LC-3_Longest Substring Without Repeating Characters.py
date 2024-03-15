# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appeared = {}  # {c: 문자 c가 등장하는 마지막 인덱스}
        max_len = start = 0

        for i, end in enumerate(s):
            # 현재 보고 있는 범위 (start~end) 내에 end가 이미 등장했었다면, (등장했었던 위치 + 1)로 start 업데이트
            if end in appeared:
                start = max(start, appeared[end] + 1)

            # max_len 업데이트
            max_len = max(max_len, i - start + 1)

            # 현재 문자 end가 마지막으로 등장한 위치 업데이트
            appeared[end] = i

        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        appeared = {}  # {c: 문자 c가 등장하는 마지막 인덱스}
        max_len = start = 0

        for i, end in enumerate(s):
            # end가 이미 등장했던 문자인 경우
            if end in appeared and start <= appeared[end]:
                start = appeared[end] + 1  # start를 end가 마지막으로 등장했던 인덱스의 한 칸 옆으로 옮기기
            # end가 처음 보는 문자인 경우
            else:
                max_len = max(max_len, i - start + 1)  # max_len 업데이트

            # 현재 문자 end가 마지막으로 등장한 위치 업데이트
            appeared[end] = i

        return max_len

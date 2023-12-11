# [LTC] 3 - Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for idx, char in enumerate(s):
        # 이미 등장했던 문자라면 start 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1  # start는 여기에서만 조작
        # 최대 부분 문자열 길이 갱신
        else:
            max_length = max(max_length, idx - start + 1)
        # 현재 문자의 위치 삽입
        used[char] = idx

    return max_length


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

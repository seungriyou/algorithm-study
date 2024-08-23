# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        [ two-pointer ]
        - left, right pointer -> longest substring containing the same letter를 가리킴
        - right pointer를 왼쪽에서부터 점차 늘려가면서 확인
        - cost for replace: substring 길이 - substring 내 가장 많이 등장한 문자의 등장 횟수
        - cost <= k: 가능하므로, max_len 업데이트
        - cost > k: 불가능하므로, left pointer 한 칸 이동 & freq 값 업데이트
        """
        from collections import defaultdict

        left = max_len = max_freq = 0
        cnts = defaultdict(int)

        for right in range(len(s)):
            # freq 업데이트
            cnts[s[right]] += 1
            max_freq = max(max_freq, cnts[s[right]])

            # cost for replacement 계산
            sub_len = right - left + 1
            cost = sub_len - max_freq

            # cost와 k 비교
            # (1) replacement 가능한 경우, max_len 업데이트 후 넘어가기
            if cost <= k:
                max_len = max(max_len, sub_len)
            # (2) replacement 불가능한 경우, cnts 값 업데이트 후 left pointer 이동
            else:
                cnts[s[left]] -= 1
                left += 1

        return max_len

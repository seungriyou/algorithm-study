# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """w/ list"""

        n = len(p)
        res = []

        # Counter 대신 len 26 짜리 list (lowercase Eng)
        target = [0] * 26
        in_wnd = [0] * 26

        # target, in_wnd 채우기
        base = ord("a")
        for _p in p:
            target[ord(_p) - base] += 1
        for _s in s[:n - 1]:  # 하나 부족하게 채우기
            in_wnd[ord(_s) - base] += 1

        # sliding window
        for i, _s in enumerate(s[n - 1:]):
            """
            i = 현재 window의 첫 원소의 인덱스
            _s = 현재 window에 새롭게 추가할 원소
            """

            # 새롭게 window에 원소 추가
            in_wnd[ord(_s) - base] += 1

            # target과 in_wnd가 같으면 anagram이므로 res에 window의 첫 인덱스 추가
            if target == in_wnd:
                res.append(i)

            # window의 첫 인덱스 삭제
            in_wnd[ord(s[i]) - base] -= 1

        return res

    def findAnagrams1(self, s: str, p: str) -> List[int]:
        """w/ Counter"""
        from collections import Counter

        n = len(p)
        res = []

        # create counters
        target = Counter(p)
        in_wnd = Counter(s[:n - 1])  # 하나 모자란 채로 시작

        # sliding window
        for i, _s in enumerate(s[n - 1:]):
            """
            i = 현재 window의 첫 원소의 인덱스
            _s = 현재 window에 새롭게 추가할 원소
            """

            # 새롭게 window에 원소 추가
            in_wnd[_s] += 1

            # target과 in_wnd가 같으면 anagram이므로 res에 window의 첫 인덱스 추가
            if target == in_wnd:
                res.append(i)

            # window의 첫 인덱스 삭제
            in_wnd[s[i]] -= 1

            # Counter를 사용하니 안 해도 된다! (rich comparison)
            # ref: https://docs.python.org/3/library/collections.html#collections.Counter
            # if not in_wnd[s[i]]:
            #     del in_wnd[s[i]]

        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        """w/ normal dict"""

        if len(s) < len(p):
            return []

        cnt_p = {_p: 0 for _p in p}
        for _p in p:
            cnt_p[_p] += 1

        cnt_s = {}
        for i in range(len(p)):
            if s[i] in cnt_s:
                cnt_s[s[i]] += 1
            else:
                cnt_s[s[i]] = 1

        res = []
        if cnt_s == cnt_p:
            res.append(0)

        for i in range(1, len(s) - len(p) + 1):
            # sliding window 벗어난 원소 cnt_s에서 빼기
            cnt_s[s[i - 1]] -= 1
            if not cnt_s[s[i - 1]]:
                del cnt_s[s[i - 1]]

            # sliding window에 새롭게 포함된 원소 cnt_s에 더하기
            added = s[i + len(p) - 1]
            if added in cnt_s:
                cnt_s[added] += 1
            else:
                cnt_s[added] = 1

            # cnt_p와 같은지 확인
            if cnt_s == cnt_p:
                res.append(i)

        return res

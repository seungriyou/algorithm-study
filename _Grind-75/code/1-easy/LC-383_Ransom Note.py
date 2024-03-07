# https://leetcode.com/problems/ransom-note/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_cnt = Counter(magazine)

        for rc in ransomNote:
            if (mc := magazine_cnt.get(rc)) and mc > 0:
                magazine_cnt[rc] -= 1
            else:
                return False

        return True

    def canConstruct_cnt(self, ransomNote: str, magazine: str) -> bool:
        # 1. counter 생성
        ransomNote_cnt = Counter(ransomNote)
        magazine_cnt = Counter(magazine)

        # 2. ransomNote의 count 값 <= magazine의 count 값인지 확인
        for r_key, r_val in ransomNote_cnt.items():
            if (m_val := magazine_cnt.get(r_key)) and r_val <= m_val:
                continue
            else:
                return False

        return True
    
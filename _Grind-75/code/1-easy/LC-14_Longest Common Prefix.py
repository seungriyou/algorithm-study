# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        사전순으로 정렬 -> first & last 만 확인하면 된다!
        """
        # 정렬
        strs.sort()

        # first & last
        first, last = strs[0], strs[-1]

        prefix = []
        for f, l in zip(first, last):
            if f != l:
                break
            else:
                prefix.append(f)

        return "".join(prefix)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        # 정렬
        strs.sort()
        # strs[0] 포인터 설정
        p = len(strs[0])

        while p:
            prefix = strs[0][:p]

            for s in strs:
                if not s.startswith(prefix):
                    p -= 1
                    break
            else:
                break

        return strs[0][:p]

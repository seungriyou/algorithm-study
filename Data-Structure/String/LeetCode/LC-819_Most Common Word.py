# [LTC] 819 - Most Common Word
# https://leetcode.com/problems/most-common-word/

import re
from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [
            word for word in re.sub(r"[\W]", " ", paragraph.lower()).split()
            if word not in banned
        ]
        counter = Counter(words)
        return counter.most_common(1)[0][0]

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
paragraph = "a."
banned = []

sol = Solution()
print(sol.mostCommonWord(paragraph, banned))
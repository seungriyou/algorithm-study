# [LTC] 937 - Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # -- letter log와 digit log 분리
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            elif log.split()[1].isalpha():
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

sol = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(sol.reorderLogFiles(logs))

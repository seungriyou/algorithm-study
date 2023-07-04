# [LTC] 17 - Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 백트래킹 w/ dfs
        def dfs(index, path):
            # print(f"dfs: index={index}, path={path}")

            # 끝까지 탐색하면 result에 추가 및 백트래킹
            if len(digits) == len(path):
                result.append(path)
                return

            # digits의 자릿수만큼 반복
            for i in range(index, len(digits)):
                # 해당 숫자에 해당하는 문자 반복
                for j in num_mapping[digits[i]]:
                    dfs(i + 1, path + j)

        result = []

        if not digits:
            return result

        num_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        dfs(0, "")

        return result

sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))

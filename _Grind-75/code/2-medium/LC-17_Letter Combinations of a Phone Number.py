# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        comb = [""] if digits else []

        for d in digits:
            comb = [p + q for p in comb for q in letters[d]]

        return comb

    def letterCombinations2(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        res = []

        if not digits:
            return []

        def dfs(idx, comb):
            # base condition
            if idx == n:
                res.append(comb)
                return

            # recur
            for c in letters[digits[idx]]:
                dfs(idx + 1, comb + c)

        dfs(0, "")

        return res

    def letterCombinations1(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        res = []
        tmp = []

        if not digits:
            return []

        def dfs(idx):
            # base condition
            if idx == n:
                res.append("".join(tmp))
                return

            # recur
            for c in letters[digits[idx]]:
                tmp.append(c)
                dfs(idx + 1)
                tmp.pop()

        dfs(0)

        return res

# [LTC] 17 - Letter Combination of a Phone Number

from typing import List


def letterCombinations(digits: str) -> List[str]:
    def dfs(index: int, path: str) -> None:
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        # 입력값 자릿수 단위 반복
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    # 예외 처리
    if not digits:
        return []

    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    dfs(0, "")
    return result


digits = "23"
print(letterCombinations(digits))

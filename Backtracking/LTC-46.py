# [LTC] 46 - Permutations

from typing import List
import itertools


def permute(nums: List[int]) -> List[List[int]]:
    # 방법 1
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])
            # print('>> results:', results)

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            # print(prev_elements)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

    # 방법 2
    # return list(map(list, itertools.permutations(nums)))


nums = [1, 2, 3]
print(permute(nums))


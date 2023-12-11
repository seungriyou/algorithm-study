# [LTC] 433 - Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        q = deque([(startGene, 0)])

        while q:
            gene, cnt = q.popleft()
            if gene == endGene:
                return cnt
            for i in range(8):
                for s in "ACGT":
                    mutation = gene[:i] + s + gene[i + 1:]  # -- 문자 하나씩 다 바꿔보기
                    if mutation in bank:
                        bank.remove(mutation)
                        q.append((mutation, cnt + 1))

        return -1

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
sol = Solution()
print(sol.minMutation(startGene, endGene, bank))

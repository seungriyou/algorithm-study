# [LTC] 128 - Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        a_start = self.find(a)
        b_start = self.find(b)

        # -- a와 b가 다른 집합에 속한다면, length가 긴 쪽이 parent가 되도록 한다
        if a_start != b_start:
            if self.length[a_start] < self.length[b_start]:
                self.parent[a_start] = self.parent[b_start]
                self.length[b_start] += self.length[a_start]
            else:
                self.parent[b_start] = self.parent[a_start]
                self.length[a_start] += self.length[b_start]

    def longestConsecutive(self, nums: List[int]) -> int:
        # -- nums가 비어있다면 빠르게 0 반환
        if not nums:
            return 0

        # -- parent, length 리스트
        self.parent = [i for i in range(len(nums))]
        self.length = [1] * len(nums)

        # -- num - idx mapping 딕셔너리
        idx_mapping = {}

        # -- set을 통해 중복을 제거한다
        for i, num in enumerate(set(nums)):
            idx_mapping[num] = i

            # -- 양옆 숫자가 존재한다면 합쳐나간다 (union)
            if num - 1 in idx_mapping:
                self.union(i, idx_mapping[num - 1])
            if num + 1 in idx_mapping:
                self.union(i, idx_mapping[num + 1])

        return max(self.length)

sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))

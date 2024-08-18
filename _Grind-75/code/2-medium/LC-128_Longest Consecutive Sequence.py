# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """hash table"""

        if not nums:
            return 0

        # hash table for O(1) lookup
        _set = set(nums)
        # max length of consecutive sequence
        res = 0

        for num in nums:
            # num의 양 옆 값 구하기
            left, right = num - 1, num + 1

            # left 및 right가 _set에 존재할 때까지 삭제 & 확장
            while left in _set:
                _set.remove(left)
                left -= 1
            while right in _set:
                _set.remove(right)
                right += 1

            # res 값 업데이트
            res = max(res, right - left - 1)

            # hash table이 비었다면 더 이상 확인할 필요가 없으므로 종료
            if not _set:
                break

        return res

    def longestConsecutive1(self, nums: List[int]) -> int:
        """
        union-find & hash table
            - 현재 보고 있는 값 num과 1 차이 나는 값(num - 1, num + 1)을 발견하면 union
            - 전체 TC가 O(n)이어야 하므로, num - 1, num + 1이 존재하는지 O(1)에 찾아야 함 -> hash table
            - union 할때마다 length 값 업데이트 & length가 긴 쪽으로 모으도록 함
        """

        n = len(nums)

        # early stop
        if not nums:
            return 0

        # for union-find
        parent = [i for i in range(n)]
        length = [1] * n
        # for hash table (O(1) lookup)
        num_idx = {}

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union_parent(a, b):
            # a, b의 parent 찾기
            a_parent, b_parent = find_parent(a), find_parent(b)

            # a와 b의 parent가 다르다면, length가 긴 쪽으로 모으도록 함
            if a_parent != b_parent:
                if length[a_parent] < length[b_parent]:
                    parent[a_parent] = parent[b_parent]
                    length[b_parent] += length[a_parent]
                else:
                    parent[b_parent] = parent[a_parent]
                    length[a_parent] += length[b_parent]

        # remove duplicate w/ set
        for i, num in enumerate(set(nums)):
            # hash table에 저장
            num_idx[num] = i

            # num - 1, num + 1이 존재한다면 union
            if (left := num - 1) in num_idx:
                union_parent(i, num_idx[left])
            if (right := num + 1) in num_idx:
                union_parent(i, num_idx[right])

        return max(length)

# https://leetcode.com/problems/contiguous-array/

from typing import List


class Solution:
    def findMaxLength1(self, nums: List[int]) -> int:
        """
        [ hash table & prefix sum ]
        - 1이 나오면 +1, 0이 나오면 -1 하며 cnt 값 트래킹 (prefix sum 응용)
          -> 이렇게 하면, cnt 값이 같은 idx 사이는 0과 1의 개수가 동일함
        - 따라서 cnt를 트래킹함과 동시에 hash table에 해당 cnt 값이 처음으로 등장한 idx 기록 & max length 트래킹
          -> cnt 값이 0이라면 처음부터 지금까지의 0과 1의 개수가 같다는 것에 주의!!
        """

        # hash table = {cnt: 해당 cnt 값이 나타난 첫 idx}
        first_idx = {}

        # prefix sum 응용
        cnt = max_length = 0

        for i, num in enumerate(nums):
            # cnt 값 업데이트
            if num == 1:
                cnt += 1
            elif num == 0:
                cnt -= 1

            # (1) cnt 값이 0이라면, 처음부터 지금까지의 0과 1의 개수가 같다는 것 **
            if cnt == 0:
                max_length = i + 1
            # (2) hash table에서 현재 cnt 값이 이전에도 나타났었다면, 나타난 첫 idx 찾고 max_length 업데이트
            elif cnt in first_idx:
                max_length = max(max_length, i - first_idx[cnt])
            # (3) 처음 보는 cnt 값이라면 hash table에 기록
            else:
                first_idx[cnt] = i

        return max_length

    def findMaxLength(self, nums: List[int]) -> int:
        """
        [ hash table & prefix sum ] - concise version
        """

        # hash table = {cnt: 해당 cnt 값이 나타난 첫 idx + 1}
        first_idx = {0: 0}  # cnt 값이 0일 때 처리

        # prefix sum 응용
        cnt = max_length = 0

        for i, num in enumerate(nums, start=1):
            # cnt 값 업데이트
            if num == 1:
                cnt += 1
            elif num == 0:
                cnt -= 1

            # (1) hash table에서 현재 cnt 값이 이전에도 나타났었다면, 나타난 첫 idx 찾고 max_length 업데이트
            if cnt in first_idx:
                max_length = max(max_length, i - first_idx[cnt])
            # (2) 처음 보는 cnt 값이라면 hash table에 기록
            else:
                first_idx[cnt] = i

        return max_length

# https://leetcode.com/problems/intervals-between-identical-elements/

from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """
        TC: O(n)
        SC: O(n)
        """
        # [ pass 1 ]
        # ps = {num: 해당 값의 idx의 prefix sum}
        # idxs[i] = arr[i]가 ps[num]의 몇 번째 idx에 반영되는지
        ps = {}
        idxs = [0] * len(arr)
        for i, num in enumerate(arr):
            # ps 기록
            if num not in ps:
                ps[num] = [0]
            ps[num].append(ps[num][-1] + i)
            # idxs 기록
            idxs[i] = len(ps[num]) - 1

        # [ pass 2 ]
        res = []
        for i, num in enumerate(arr):
            """
            arr에서 원소 num의 idx가 [1, 2, 3, 5, 6, 7] 인 경우를 가정해보자.

            - 이 경우, ps[num] = [1, 3, 6, 11, 17, 24] 이다.
            - i = 3, 즉 ps_idx = 2인 경우, 해당 원소를 기준으로 왼쪽과 오른쪽의 interval sum을 각각 구해보자.
              이처럼 왼쪽과 오른쪽에서 각각 interval sum을 구하는 식(= sum(|j - i|))을 순서를 같은 부호끼리 재구성하면
              연속된 원소의 합을 이용하는 식으로 바꿀 수 있다는 것을 알 수 있다.
                                v
                 i  |   1   2   3   5   6   7
                ps  |   1   3   6   11  17  24
             ======= ===========================
               left |   <----                       : [3(v) * 2(왼쪽 원소 개수)] - [3](prefix sum)
              right |               --------->      : [24 - 6](prefix sum) - [3(v) * 3(오른쪽 원소 개수)]

            """
            # 현재 보고 있는 arr[i]가 ps[num]에서 위치한 idx 확인
            ps_idx = idxs[i]

            # 현재 보고 있는 num 기준으로, 왼쪽의 interval sum과 오른쪽의 interval sum 구하기 (w/ prefix sum)
            left = (i * ps_idx) - ps[num][ps_idx - 1]
            right = (ps[num][-1] - ps[num][ps_idx]) - (i * (len(ps[num]) - ps_idx))

            # res에 기록
            res.append(left + right)

        return res

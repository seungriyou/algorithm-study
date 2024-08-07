# https://leetcode.com/problems/find-a-peak-element-ii/

from typing import List

class Solution:
    def findPeakGrid1(self, mat: List[List[int]]) -> List[int]:
        """
        ref: https://leetcode.com/problems/find-a-peak-element-ii/solutions/1276556/java-python-c-clear-explanation-with-images-m-log-n-very-short-code
        2D array이므로 binary search를 하나의 원소가 아닌 하나의 column에 대해서 수행하자!
            - 이전 문제와 동일한 아이디어
            - mid column 내의 원소 중 최댓값을 찾은 후
                - 상하좌우 값과 비교했을 때 peak인 곳이라면 return
                - 더 큰 값이 있었던 곳으로 탐색 범위 이동
            - 더 직관적으로 peak를 발견할 때 반환하기 위해 lo <= hi 조건 이용
        """

        row, col = len(mat), len(mat[0])

        lo_col, hi_col = 0, col - 1

        while lo_col <= hi_col:
            mid_col = (lo_col + hi_col) // 2

            # [상하] mid_col 내에서 가장 큰 값을 가지는 row 번호 찾기
            max_row = 0
            for r in range(row):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r

            # [좌우] mid_col 내에서 가장 큰 값을 기준으로, 왼쪽 col과 오른쪽 col 비교하기 (boundary 및 크기)
            left_is_big = lo_col <= mid_col - 1 and mat[max_row][mid_col - 1] > mat[max_row][mid_col]
            right_is_big = mid_col + 1 <= hi_col and mat[max_row][mid_col + 1] > mat[max_row][mid_col]

            # left와 right 모두 mid 보다 크지 않거나, 더이상 비교할 원소가 없다면 peak 발견
            if not left_is_big and not right_is_big:
                return [max_row, mid_col]
            # peak를 발견하지 못했다면, 더 큰 값이 있는 구간으로 이동
            elif right_is_big:
                lo_col = mid_col + 1
            else:
                hi_col = mid_col - 1

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        ref: https://leetcode.com/problems/find-a-peak-element-ii/solutions/1275904/java-clean-code-with-explanation-o-nlgm
        2D array이므로 binary search를 하나의 원소가 아닌 하나의 column에 대해서 수행하자!
            - 이전 문제와 동일한 아이디어
            - mid column 내의 원소 중 최댓값을 찾은 후
                - 상하좌우 값과 비교했을 때 peak인 곳이라면 return
                - 더 큰 값이 있었던 곳으로 탐색 범위 이동
            - 더 직관적으로 peak를 발견할 때 반환하기 위해 lo <= hi 조건 이용
        """

        row, col = len(mat), len(mat[0])

        lo_col, hi_col = 0, col - 1

        def get_max_row_idx(c):
            """column index가 c인 column 내에서 최댓값의 row index 반환"""
            max_row = 0
            for r in range(row):
                if mat[r][c] > mat[max_row][c]:
                    max_row = r
            return max_row

        while lo_col < hi_col:
            mid_col = (lo_col + hi_col) // 2  # lower mid

            # [상하] mid_col 내에서 가장 큰 값을 가지는 row 번호 찾기
            max_row = get_max_row_idx(mid_col)

            # [좌우] mid_col의 값이 오른쪽 값보다 크면, 해당 값까지 포함하여 왼쪽 탐색
            if mat[max_row][mid_col] > mat[max_row][mid_col + 1]:
                hi_col = mid_col  # include mid_col & look for left
            else:
                lo_col = mid_col + 1

        # 직전에 lo_col이 업데이트 된 경우를 위해, 현재 lo_col 내에서 max_row index 구하기(***)
        max_row = get_max_row_idx(lo_col)

        return [max_row, lo_col]

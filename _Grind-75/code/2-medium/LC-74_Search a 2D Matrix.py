# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        binary search
            - 2D array를 1D array로 펼친다고 생각하면, 해당 array는 non-decreasing order로 정렬되어 있음

        TC: O(log(m * n))
        """

        row, col = len(matrix), len(matrix[0])
        lo, hi = 0, row * col - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if matrix[mid // col][mid % col] < target:
                lo = mid + 1
            else:
                hi = mid

        return matrix[lo // col][lo % col] == target

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """
        각 row의 첫 값은 이전 row의 마지막 값보다 큼
        -> top right corner에서 시작
            - 현재 위치의 값이 target 보다 작다면, 다음 row로 이동
            - 현재 위치의 값이 target 보다 크다면, 이전 col 확인

        TC: O(m + n)
        """

        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            # 현재 위치의 값이 target 보다 작다면, 다음 row로 이동
            if matrix[r][c] < target:
                r += 1
            # 현재 위치의 값이 target 보다 크다면, 이전 col 확인
            elif matrix[r][c] > target:
                c -= 1
            # 현재 위치의 값이 target과 같다면, True 반환
            else:
                return True

        return False

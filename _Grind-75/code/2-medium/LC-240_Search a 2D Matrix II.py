# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        row & column -> 각각 모두 ascending order로 sorted -> top right corner에서 시작
            - 현재 보고 있는 값이 target 보다 작으면, row 증가
            - 현재 보고 있는 값이 target 보다 크면, col 감소

        TC: O(m + n)
        """

        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            # 현재 보고 있는 값이 target 보다 작으면, row 증가
            if matrix[r][c] < target:
                r += 1
            # 현재 보고 있는 값이 target 보다 크면, col 감소
            elif matrix[r][c] > target:
                c -= 1
            # target 값 발견
            else:
                return True

        return False

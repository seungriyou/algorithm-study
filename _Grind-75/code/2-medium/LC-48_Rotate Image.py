# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        [ clockwise rotation (in-place) ]
            1. matrix reverse
            2. matrix transpose
        """

        n = len(matrix)

        # (1) reverse
        for r in range(n // 2):
            matrix[r], matrix[n - r - 1] = matrix[n - r - 1], matrix[r]

        # (2) transpose
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    def rotate_counterclockwise(self, matrix: List[List[int]]) -> None:
        """
        [ counterclockwise rotation (in-place) ]
            1. matrix row 별 reverse
            2. matrix transpose
        """

        n = len(matrix)

        # (1) row reverse
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][n - c - 1] = matrix[r][n - c - 1], matrix[r][c]

        # (2) transpose
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

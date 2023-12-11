# [LC] 240 - Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        맨 위 오른쪽 코너에서 시작하면,
        - 해당 값 < target이라면, target은 해당 row에 있을 수 없음 -> row를 늘려나가기
        - 해당 값 > target이라면, target은 해당 col에 있을 수 없음 -> col을 줄여나가기
        """
        if not matrix:
            return False

        # first row's last element (top right)
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True

        return False

sol = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(sol.searchMatrix(matrix, target))

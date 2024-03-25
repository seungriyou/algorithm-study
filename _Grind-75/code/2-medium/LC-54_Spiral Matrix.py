# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]  # counter-clockwise rotation

        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # d: 0, 1, 2, 3 / 우, 하, 좌, 상
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

        m, n = len(matrix), len(matrix[0])
        r, c, d = 0, 0, 0
        res = [matrix[r][c]]
        matrix[r][c] = "#"

        # res에 m * n개의 숫자가 저장될 때까지
        while len(res) < m * n:
            nr, nc = r + dr[d], c + dc[d]

            # 범위를 벗어났거나 이미 방문했으면 방향 바꾸기
            if nr < 0 or nr >= m or nc < 0 or nc >= n or matrix[nr][nc] == "#":
                d = (d + 1) % 4
                nr, nc = r + dr[d], c + dc[d]

            res.append(matrix[nr][nc])
            matrix[nr][nc] = "#"
            r, c = nr, nc

        return res

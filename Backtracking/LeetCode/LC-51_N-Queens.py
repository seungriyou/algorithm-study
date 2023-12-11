# [LTC] 51 - N-Queens
# https://leetcode.com/problems/n-queens/

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # row 0부터 n - 1까지
        visited_col = set()  # -- 하나의 col에는 하나의 queen 만 가능
        visited_diag_ur = set()  # -- upper right를 향하는 대각선 -> 같은 대각선에 속하면 (r + c) 같음
        visited_diag_lr = set()  # -- lower right를 향하는 대각선 -> 같은 대각선에 속하면 (r - c) 같음
        board = [['.'] * n for _ in range(n)]
        result = []

        def dfs(r):
            # -- 종료 조건
            if r == n:
                result.append([''.join(row) for row in board])
                return

            for c in range(n):
                diag_ur = r + c  # -- upper right diag
                diag_lr = r - c  # -- lower right diag

                if not (c in visited_col or diag_ur in visited_diag_ur or diag_lr in visited_diag_lr):
                    # place the queen
                    visited_col.add(c)
                    visited_diag_ur.add(diag_ur)
                    visited_diag_lr.add(diag_lr)
                    board[r][c] = 'Q'

                    dfs(r + 1)  # -- 다음 row에 대해 dfs

                    # remove the queen
                    visited_col.remove(c)
                    visited_diag_ur.remove(diag_ur)
                    visited_diag_lr.remove(diag_lr)
                    board[r][c] = '.'

        dfs(0)  # -- 0th row 부터 시작

        return result

sol = Solution()
n = 4
print(sol.solveNQueens(n))

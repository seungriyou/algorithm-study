# https://leetcode.com/problems/n-queens/

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        [Complexity]
            - TC: O(n!)
            - SC: O(n^2)
        [Approach]
            no two queens attach each other인 n-queens puzzle
                -> queens가 서로 같은 row, col, diag(upper_right, lower_right)에 위치하면 안 된다.
            따라서 dfs로 row를 하나씩 늘려가면서, 이전에 방문하지 않았던 col, ur_diag, lr_diag에 해당하는 칸에만 표시한다.
                - col, ur_diag, lr_diag는 set으로 트래킹한다.
                - 같은 ur_diag 끼리는 row + col 값이 같다.
                - 같은 lr_diag 끼리는 row - col 값이 같다.
        """

        visited_col = set()
        visited_ur_diag = set()
        visited_lr_diag = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(row):
            # base condition
            if row == n:
                res.append(["".join(_row) for _row in board])
                return

            # column
            for col in range(n):
                # ur_diag, lr_diag
                ur_diag, lr_diag = row + col, row - col

                # 이전에 방문하지 않았던 col, ur_diag, lr_diag에 해당한다면, recur
                if not (col in visited_col or ur_diag in visited_ur_diag or lr_diag in visited_lr_diag):
                    # 해당 자리에 queen 놓기
                    visited_col.add(col)
                    visited_ur_diag.add(ur_diag)
                    visited_lr_diag.add(lr_diag)
                    board[row][col] = "Q"

                    dfs(row + 1)  # 다음 row에 대해서도 실행

                    # 놓았던 queen 다시 빼기
                    visited_col.remove(col)
                    visited_ur_diag.remove(ur_diag)
                    visited_lr_diag.remove(lr_diag)
                    board[row][col] = "."

        # 0번 row 부터 시작
        dfs(0)

        return res

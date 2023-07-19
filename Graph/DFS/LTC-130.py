# [LTC] 130 - Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        r, c = len(board), len(board[0])

        # -- border에 인접한 O region -> B (w/ dfs)
        def dfs(i: int, j: int) -> None:
            # -- 범위 검사
            if i < 0 or j < 0 or i >= r or j >= c:
                return

            # -- border에 인접한 O region -> B로 표시
            if board[i][j] == "O":
                board[i][j] = "B"

                # -- 상하좌우
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

            return

        # -- (1) 왼쪽 & 오른쪽 border 확인
        for i in range(r):
            dfs(i, 0)
            dfs(i, c - 1)
        # -- (2) 위쪽 & 아래쪽 border 확인
        for j in range(c):
            dfs(0, j)
            dfs(r - 1, j)

        # -- 전체 순회하며 수정
        for i in range(r):
            for j in range(c):
                # -- 남은 O region은 내부에 위치할 것이므로 -> X region
                if board[i][j] == "O":
                    board[i][j] = "X"
                # -- B region -> O region
                elif board[i][j] == "B":
                    board[i][j] = "O"

sol = Solution()
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["X"]]
sol.solve(board)
print(board)

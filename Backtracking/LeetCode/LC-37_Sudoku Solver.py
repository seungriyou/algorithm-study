# [LTC] 37 - Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

from typing import List
import heapq

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # === decision space 줄이는 방법 ===
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        empty_cells = []
        heap = []

        for r in range(9):
            for c in range(9):
                s = (r // 3) * 3 + (c // 3)
                if (k := board[r][c]) != ".":
                    rows[r].add(k)
                    cols[c].add(k)
                    squares[s].add(k)
                else:
                    empty_cells.append((r, c, s))

        nums = set("123456789")
        for r, c, s in empty_cells:
            heapq.heappush(heap, (len(nums - (rows[r] | cols[c] | squares[s])), r, c, s))

        def dfs():
            if not heap:
                return True

            p, r, c, s = heapq.heappop(heap)

            for k in (nums - (rows[r] | cols[c] | squares[s])):
                board[r][c] = k
                rows[r].add(k)
                cols[c].add(k)
                squares[s].add(k)

                if dfs():
                    return True
                else:
                    # board[r][c] = "."   # -- 안해도 ok ("." 여부로 판단하지 X)
                    rows[r].remove(k)
                    cols[c].remove(k)
                    squares[s].remove(k)

            heapq.heappush(heap, (p, r, c, s))
            # return False

        dfs()

    def solveSudoku1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(r, c, k):
            for i in range(9):
                # (1) 해당 column에서 k와 같은 숫자가 있으면 False
                if board[i][c] == k:
                    return False
                # (2) 해당 row에서 k와 같은 숫자가 있으면 False
                if board[r][i] == k:
                    return False
                # (3) 해당 3x3 square에서 k와 같은 숫자가 있으면 False
                #     - 3x3 square의 upper-left 좌표 = (r // 3, c // 3)
                #     - row offset = i // 3
                #     - col offset = i % 3
                if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == k:
                    return False
            return True

        def solve(r, c):
            # -- 하나의 row를 왼쪽 column 부터 확인
            if r == 9:
                return True
            if c == 9:
                return solve(r + 1, 0)

            if board[r][c] == ".":
                for k in "123456789":
                    if is_valid(r, c, k):
                        board[r][c] = k

                        if solve(r, c + 1):
                            return True
                        else:
                            board[r][c] = "."
                return False
            else:
                return solve(r, c + 1)

        solve(0, 0)

    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in "123456789":
                        if self.is_valid(board, i, j, k):
                            board[i][j] = k
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def is_valid(self, board, r, c, k):
        # (1) 해당 column에서 k와 같은 숫자가 있으면 False
        for i in range(9):
            if board[i][c] == k:
                return False
        # (2) 해당 row에서 k와 같은 숫자가 있으면 False
        for j in range(9):
            if board[r][j] == k:
                return False
        # (3) 해당 3x3 square에서 k와 같은 숫자가 있으면 False
        for i in range(3):
            for j in range(3):
                if board[(r // 3) * 3 + i][(c // 3) * 3 + j] == k:
                    return False
        return True

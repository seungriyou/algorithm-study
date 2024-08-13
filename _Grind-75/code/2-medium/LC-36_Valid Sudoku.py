# https://leetcode.com/problems/valid-sudoku/

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        row: 0 ~ 8까지 (i)
        col: 0 ~ 8까지 (j)
        square: 0,0 ~ 2,2까지 (i // 3, j // 3)
        """
        row, col, square = set(), set(), set()

        for i, r in enumerate(board):
            for j, n in enumerate(r):
                if n != ".":
                    if (i, n) in row or (j, n) in col or (i // 3, j // 3, n) in square:
                        return False

                    row.add((i, n))
                    col.add((j, n))
                    square.add((i // 3, j // 3, n))

        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            elem = [r for r in row if r != "."]
            if len(elem) != len(set(elem)):
                return False

        # col
        for col in zip(*board):
            elem = [c for c in col if c != "."]
            if len(elem) != len(set(elem)):
                return False

        # square
        for r in (0, 3, 6):
            for c in (0, 3, 6):
                elem = [board[r + dr][c + dc] for dr in range(3) for dc in range(3) if board[r + dr][c + dc] != "."]
                if len(elem) != len(set(elem)):
                    return False

        return True

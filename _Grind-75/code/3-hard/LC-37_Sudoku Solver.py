# https://leetcode.com/problems/sudoku-solver/

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        [ decision space 줄이기 ]
            - 칸에 가능한 숫자를 모두 넣어보는 것이 아니라, <같은 row, col, square에 없는 숫자들> 중에서만 넣어본다!
            - 이때, 사람이 푸는 것처럼 <같은 row, col, square에 이미 숫자가 많이 채워진 빈 칸> 부터 채워나간다! (-> heapq 사용)
        """
        import heapq

        rows = [set() for _ in range(9)]  # rows[r] = board의 각 row 별로, 이미 채워진 숫자들의 set
        cols = [set() for _ in range(9)]  # cols[c] = board의 각 col 별로, 이미 채워진 숫자들의 set
        squares = [set() for _ in range(9)]  # squares[s] = board의 각 square 별로, 이미 채워진 숫자들의 set
        empty_cells = []  # 빈 칸의 rows, cols, squares에서 해당하는 index ((r, c, s))

        # board의 초기 상태 반영
        for r in range(9):
            for c in range(9):
                s = (r // 3) * 3 + (c // 3)
                if (k := board[r][c]) != ".":
                    rows[r].add(k)
                    cols[c].add(k)
                    squares[s].add(k)
                else:
                    empty_cells.append((r, c, s))

        # 같은 row, col, square에 채워져있는 숫자가 많은 빈 칸부터 채워나갈 수 있도록, heapq 사용
        nums = set("123456789")
        q = [(len(nums - (rows[r] | cols[c] | squares[s])), r, c, s) for r, c, s in empty_cells]
        heapq.heapify(q)

        def dfs():
            # base condition
            if not q:
                return True

            # recur
            n, r, c, s = heapq.heappop(q)
            # 같은 row, col, square에 채워져있는 숫자를 제외한 수만 넣어보기 (decision space 축소)
            for k in (nums - (rows[r] | cols[c] | squares[s])):
                board[r][c] = k
                rows[r].add(k)
                cols[c].add(k)
                squares[s].add(k)

                # backtrack
                if dfs():
                    return True

                board[r][c] = "."  # -- 필요 없음 (빈 칸을 "."으로 판단하지 않으므로)
                rows[r].remove(k)
                cols[c].remove(k)
                squares[s].remove(k)

            # 현재 보고 있는 빈 칸에서 숫자 채우기가 실패했으므로, 다시 q에 넣어주기 ***
            heapq.heappush(q, (n, r, c, s))
            return False

        dfs()


    def solveSudoku1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # ref: https://leetcode.com/problems/sudoku-solver/editorial/comments/385377

        from collections import defaultdict

        n = len(board)
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(n):
            for c in range(n):
                if (k := board[r][c]) != ".":
                    rows[r].add(k)
                    cols[c].add(k)
                    squares[(r // 3) * 3 + c // 3].add(k)

        def is_valid(r, c, k):
            s = (r // 3) * 3 + c // 3
            return k not in rows[r] and k not in cols[c] and k not in squares[s]

        def dfs(r, c):
            """
            board의 왼쪽 맨 위 코너부터 확인
            """
            # base condition
            if r == n - 1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1

            # current grid has been filled
            if board[r][c] != ".":
                return dfs(r, c + 1)

            # recur
            s = (r // 3) * 3 + c // 3
            for k in "123456789":
                if not is_valid(r, c, k):
                    continue

                board[r][c] = k
                rows[r].add(k)
                cols[c].add(k)
                squares[s].add(k)

                # backtrack
                if dfs(r, c + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(k)
                cols[c].remove(k)
                squares[s].remove(k)

            return False

        dfs(0, 0)


    def solveSudoku_tle(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        예전에는 아니었는데... TLE 발생
        """

        def is_valid(r, c, k):
            """
            board[r][c]와
                - 같은 row
                - 같은 col
                - 같은 3x3 square
            에 하나라도 k와 같은 값이 있으면 False, 없으면 True 반환
            """
            # board[r][c]가 속하는 3x3 square의 upper left corner의 좌표
            sq_r, sq_c = r // 3 * 3, c // 3 * 3

            for i in range(9):
                # 같은 row에 k와 같은 값이 있으면 False 반환
                if board[i][c] == k:
                    return False
                # 같은 col에 k와 같은 값이 있으면 False 반환
                if board[r][i] == k:
                    return False
                # 같은 square에 k와 같은 값이 있으면 False 반환
                if board[sq_r + (i // 3)][sq_c + (i % 3)] == k:
                    return False
            return True

        def dfs(r, c):
            """
            board를 맨 위 row부터, 맨 왼쪽 col부터 하나씩 확인
            """
            # base condition
            if r == 9:
                return True
            if c == 9:
                return dfs(r + 1, 0)

            # recur
            # (1) 현재 칸이 빈칸이라면, 들어갈 수 있는 모든 숫자 넣어보기
            if board[r][c] == ".":
                # 현재 칸에 들어갈 수 있는 값 모두 넣어보기
                for k in "123456789":
                    if is_valid(r, c, k):
                        board[r][c] = k
                        # backtrack (현재 칸에 k를 넣었을 때, 다음 칸 확인)
                        # (1) 현재 칸에 k를 넣는 것이 올바르면 True 반환
                        if dfs(r, c + 1):
                            return True
                        # (2) 현재 칸에 k를 넣는 것이 올바르지 않으면 원상복구
                        else:
                            board[r][c] = "."

                # 현재 칸에 모든 수를 넣어봤는데 성립하지 않으면 False 반환
                return False

            # (2) 현재 칸이 빈칸이 아니라면, 다음 칸으로 넘어가기
            else:
                return dfs(r, c + 1)

        # 첫 번째 칸부터 시작
        dfs(0, 0)

# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # NOTE: 왜 BFS는 안 됐는지 생각해보기...!

        # early stop (3106ms -> 486ms으로 대폭 감소!)
        if set(word).difference(set(c for row in board for c in row)):
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def backtrack(r, c, idx):
            # base condition
            if idx == len(word):
                return True

            # (1) 범위를 벗어나거나, (2) 이미 방문했거나, (3) word[i]와 같은 문자가 아니라면 false
            if not (0 <= r < m and 0 <= c < n) or visited[r][c] or board[r][c] != word[idx]:
                return False

            visited[r][c] = True

            if (
                    backtrack(r - 1, c, idx + 1) or
                    backtrack(r + 1, c, idx + 1) or
                    backtrack(r, c - 1, idx + 1) or
                    backtrack(r, c + 1, idx + 1)
            ):
                return True

            visited[r][c] = False

            return False

        for i in range(m):
            for j in range(n):
                # if word[0] == board[i][j] and backtrack(i, j, 0):
                if backtrack(i, j, 0):
                    return True

        return False

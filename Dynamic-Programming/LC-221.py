# [LC] 221 - Maximal Square
# https://leetcode.com/problems/maximal-square/

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # === space optimized DP ===
        m, n = len(matrix), len(matrix[0])

        dp = [0] * (n + 1)
        max_s = upper_left = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    tmp = dp[c + 1]  # -- 다음 c에서 사용할 upper_left 값을 dp[c + 1] 값이 바뀌기 전에 미리 저장
                    dp[c + 1] = min(upper_left, dp[c], dp[c + 1]) + 1  # -- min(upper_left, left, upper) + 1
                    max_s = max(max_s, dp[c + 1])
                    upper_left = tmp  # -- upper_left 업데이트
                else:
                    dp[c + 1] = upper_left = 0

        return max_s * max_s

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        """
        어떠한 좌표 (r, c)가 1x1 보다 큰 square의 lower right 지점이 될 수 있는지의 여부는
            (1) 본인이 '1' 이고
            (2) upper, upper left, left 가 모두 square에 속하면
        가능하다고 정해진다.
        이때, 한 변의 길이가 s인 square에 해당 좌표가 속한다는 것을 나타내는 dp 테이블을 만들 수 있다.
            (1) matrix의 첫 번째 row & column을 위해, dp 테이블의 upper와 left에는 0으로 초기화한 padding을 넣는다.
            (2) 현재 보고있는 좌표가 '1' 값을 가진다면, upper, upper left, left에 기록되어 있는 s 값의 최솟값을 구한 후 1을 더한 값을 기록한다.
        따라서 dp에 기록된 값 중 가장 큰 값이 가능한 square의 변의 최대 길이가 된다.
        """
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_s = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r][c + 1], dp[r + 1][c]) + 1
                    max_s = max(max_s, dp[r + 1][c + 1])

        return max_s * max_s


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol = Solution()
print(sol.maximalSquare(matrix))

# [LTC] 279 - Perfect Squares
# https://leetcode.com/problems/perfect-squares/

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # TODO: perfect number 부터 역으로 level by level로도!
        """
        === BFS solution ===
        n에서부터 1^2, 2^2, ..., int(sqrt(n))^2 를 뺀 값을 queue에 넣어가면서 cnt++
        """
        q = deque([(n, 0)])  # -- (num, cnt)
        visited = {n}

        while q:
            num, cnt = q.popleft()

            # -- num이 square number 라면 return cnt + 1
            if int(num ** 0.5) == num ** 0.5:
                return cnt + 1

            for i in range(1, int(num ** 0.5) + 1):
                if (prev_num := num - (i * i)) not in visited:
                    q.append((prev_num, cnt + 1))
                    visited.add(prev_num)

    def numSquares_DP(self, n: int) -> int:
        """
        === DP solution ===
        dp[i] = min(dp[i - 1^2], dp[i - 2^2], ..., dp[i - int(sqrt(i))^2]) + 1
        """
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1
            # -- (j ** 2) 보다 (j * j)가 훨씬 빠르다..!

        return dp[-1]

sol = Solution()
n = 12
print(sol.numSquares(n))

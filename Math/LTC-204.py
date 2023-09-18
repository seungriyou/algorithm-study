# [LTC] 204 - Count Primes
# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        # === 에라토스테네스의 체 ===
        if n < 3:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:  # -- 아직 남아있는 수
                for j in range(i * i, n, i):  # -- faster!
                    is_prime[j] = False
                """
                왜 i에 2부터 곱해나가는 것이 아니라 i부터 곱해나갈까?
                i   j
                --- --- --- --- ---
                2   2*2 2*3 2*4 2*5 ...
                3   3*3 3*4 3*5 3*6 ... -> (3*2)는 i=2에서 처리함
                4   4*4 4*5 4*6 4*7 ... -> (4*2)는 i=2에서, (4*3)은 i=3에서 처리함
                => 더 빠른 속도 가능!
                """
                # j = 2
                # while i * j < n:
                #     is_prime[i * j] = False
                #     j += 1

        return sum(is_prime)

sol = Solution()
n = 10
print(sol.countPrimes(n))

# https://leetcode.com/problems/ugly-number-iii/

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        ugly(num): num 이하인 ugly number의 개수가 n개 이하인지 여부 반환 (최소공배수 lcm 이용***)
            num 이하 ugly number 개수
            = num // a + num // b + num // c - num // lcm(a, b) - num // lcm(b, c) - num // lcm(c, a) + num // lcm(a, b, c)

        -> ugly를 만족하는 가장 작은 num을 구하면 된다!
        """

        def gcd(p, q):
            while q:
                p, q = q, p % q
            return p

        # lcm 구하기
        ab, bc, ca = a * b // gcd(a, b), b * c // gcd(b, c), c * a // gcd(c, a)
        abc = a * bc // gcd(a, bc)

        def ugly(num):
            return (
               num // a + num // b + num // c
               - (num // ab + num // bc + num // ca)
               + num // abc
            ) >= n

        lo, hi = 1, 2 * 10 ** 9

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ugly(mid):
                hi = mid  # look for left
            else:
                lo = mid + 1

        return lo

# https://school.programmers.co.kr/learn/courses/30/lessons/92335

import re


def solution(n, k):
    # k진수로 변환하기
    def k_base(n, k):
        if k == 10:
            return str(n)

        result = ""
        while n > 0:
            n, m = divmod(n, k)
            result += str(m)

        return result[::-1]

    def is_prime(n):
        if n == 1:
            return False

        if n == 2 or n == 3:
            return True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    nums = k_base(n, k).split("0")
    cnt = 0
    for num in nums:
        if num:  # 빈 문자열
            cnt += is_prime(int(num))

    return cnt

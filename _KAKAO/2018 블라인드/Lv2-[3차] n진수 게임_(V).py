# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    # 진법 변환 함수
    def n_base(n, num):
        DIGITS = '0123456789ABCDEF'
        if num == 0:
            return DIGITS[0]

        result = ''
        while num > 0:
            d, m = divmod(num, n)
            result += DIGITS[m]
            num = d
        return result[::-1]

    digits = []
    turn = 0
    # last = m * (t - 1) + p # 마지막 turn의 튜브 순서까지 불리는 숫자 개수 (m * (t - 1) + p * 1 이라고 생각하면 됨)
    while len(digits) < m * t:  # 마지막 turn의 끝까지 둘러보기
        digits.extend(list(n_base(n, turn)))
        turn += 1

    return "".join(digits[p - 1:m * t:m])  # m * t 대신 last를 사용하지 않고, 그냥 이렇게 해도 된다! 어차피 해당 turn에 튜브의 순서는 단 한 번이므로..


# 이렇게 복잡하게 풀 필요가 없다..... x_x
def solution2(n, t, m, p):
    from math import ceil

    answer = ''

    # 진법 변환 함수
    def n_base(n, num):
        result = ''
        lookup = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }

        if num == 0:
            return '0'

        while num > 0:
            d, q = divmod(num, n)
            if q > 9:
                result += lookup[q]
            else:
                result += str(q)
            num = d
        return result[::-1]

    def get_last_num(n, target_digit):
        d = prev = 1
        while True:
            tmp = n ** (d - 1) * (n - 1) * d
            if prev + tmp > target_digit:
                break
            prev += tmp
            d += 1
        return prev - 1 + ceil((target_digit - prev) / d)

    target_digit = m * (t - 1) + p
    last_num = get_last_num(n, target_digit)

    nums = ''
    for i in range(last_num + 1):
        nums += n_base(n, i)

    i = p - 1
    for _ in range(t):
        answer += nums[i]
        i += m

    return answer

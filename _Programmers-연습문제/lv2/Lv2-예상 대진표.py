# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2

        answer += 1

    return answer


def solution1(n, a, b):
    answer = 0

    while a != b:
        # a = (a // 2) + (a % 2)
        # b = (b // 2) + (b % 2)
        a = sum(divmod(a, 2))
        b = sum(divmod(b, 2))

        answer += 1

    return answer

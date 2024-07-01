# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        answer += a * b

    return answer

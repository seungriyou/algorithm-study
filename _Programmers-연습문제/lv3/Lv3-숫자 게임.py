# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    i = 0
    for b in B:
        if A[i] < b:
            i += 1
            answer += 1

    return answer


def solution1(A, B):
    from collections import deque

    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    if A[-1] > B[0]:
        return answer

    B = deque(B)

    for a in A:
        if a >= B[0]:
            B.pop()
        else:
            B.popleft()
            answer += 1

    return answer

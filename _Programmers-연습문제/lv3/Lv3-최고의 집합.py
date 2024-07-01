# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]

    answer = []

    r, q = divmod(s, n)
    for _ in range(n - q):
        answer.append(r)
    for _ in range(q):
        answer.append(r + 1)

    return answer

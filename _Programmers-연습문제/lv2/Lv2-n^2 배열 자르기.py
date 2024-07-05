# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []

    # row, col 중 더 큰 값으로 채워야 함
    for i in range(left, right + 1):
        r, c = divmod(i, n)
        answer.append(max(r, c) + 1)

    return answer

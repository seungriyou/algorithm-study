# https://www.acmicpc.net/problem/17140
import sys; input = sys.stdin.readline
from collections import defaultdict

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]


# === 함수 === #
def r_op(prev_A):
    new_A = []
    max_len = 0

    # 1. 새롭게 정렬한 row 추가하기
    for row in prev_A:
        # row에 대해 counter 생성
        counter = defaultdict(int)
        for r in row:
            if r != 0:
                counter[r] += 1

        # 새로운 row
        nrow = []
        for n, c in sorted(list(counter.items()), key=lambda x: (x[1], x[0])):
            nrow += [n, c]

        # result에 새로운 row 추가
        new_A.append(nrow)
        max_len = max(max_len, len(nrow))

    # 2. 가장 긴 row를 기준으로 0 채우기
    for row in new_A:
        row += [0] * (max_len - len(row))

    # 3. row의 길이가 100을 넘어간다면 자르기
    if max_len > 100:
        for i in range(len(new_A)):
            new_A[i] = new_A[i][:100]

    return new_A


def c_op(prev_A):
    # 1. row 기준으로 변경
    _prev_A = []
    for col in zip(*prev_A):
        _prev_A.append(list(col))

    # 2. r_op 수행
    _new_A = r_op(_prev_A)

    # 3. 연산 결과를 다시 col 기준으로 변경
    new_A = []
    for col in zip(*_new_A):
        new_A.append(list(col))

    return new_A


def solve():
    global A

    seconds = 0
    while seconds <= 100:
        # 1. 조건에 부합하면 seconds 반환
        if r - 1 < len(A) and c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
            return seconds

        # 2. R 연산 혹은 C 연산 수행
        if len(A) >= len(A[0]):
            A = r_op(A)
        else:
            A = c_op(A)

        # 3. seconds 증가
        seconds += 1

    return -1

print(solve())

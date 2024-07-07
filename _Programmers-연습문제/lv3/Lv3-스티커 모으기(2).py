# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    n = len(sticker)

    if n <= 3:
        return max(sticker)

    # dp #1: 마지막 원소 제외
    a1 = b1 = 0
    for i in range(n - 1):
        curr = max(a1 + sticker[i], b1)
        a1, b1 = b1, curr

    # dp #2: 첫 번재 원소 제외
    a2 = b2 = 0
    for i in range(1, n):
        curr = max(a2 + sticker[i], b2)
        a2, b2 = b2, curr

    return max(b1, b2)

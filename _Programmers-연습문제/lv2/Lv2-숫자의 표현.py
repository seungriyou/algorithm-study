# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    lo, hi = 1, 2
    val = 1
    answer = 0

    while lo < hi:
        if val < n:
            val += hi
            hi += 1
        elif val > n:
            val -= lo
            lo += 1
        else:
            answer += 1
            lo, hi = lo + 1, hi + 1
            val -= lo
            val += hi

    return answer

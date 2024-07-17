# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0

    # 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # S_i 구하고, 누적하여 bitwise XOR
    for i in range(row_begin, row_end + 1):
        answer ^= sum(n % i for n in data[i - 1])

    return answer

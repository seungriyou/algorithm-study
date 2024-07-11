# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    target = bin(n).count("1")

    # for num in range(n + 1, int(bin(n)[2:] + "0", 2) + 1):
    #     if bin(num).count("1") == target:
    #         return num

    while True:
        n += 1
        if bin(n).count("1") == target:
            break

    return n

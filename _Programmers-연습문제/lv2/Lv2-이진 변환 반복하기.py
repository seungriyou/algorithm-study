# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]

    while s != "1":
        num = s.count("1")

        answer[0] += 1
        answer[1] += len(s) - num

        s = bin(num)[2:]

    return answer

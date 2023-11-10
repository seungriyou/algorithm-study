# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    d = {chr(i + 65): i + 1 for i in range(26)}
    l = r = 0  # 현재 입력으로 볼 substring의 left, right pointer
    end_val = 27
    n = len(msg)

    while l < n:
        while r < n:
            if msg[l:r + 1] not in d:
                break
            r += 1

        answer.append(d[msg[l:r]])

        d[msg[l:r + 1]] = end_val

        end_val += 1
        l = r

    return answer

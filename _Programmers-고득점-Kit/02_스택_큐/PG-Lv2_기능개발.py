# [PG] 42586 - 기능개발 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# from math import ceil

def solution(progresses, speeds):
    answer = []
    days = []

    for p, s in zip(progresses, speeds):
        # days.append(ceil((100 - p) / s))
        days.append(-((p - 100) // s))

    max_day = 0
    for d in days:
        if d > max_day:
            max_day = d
            answer.append(1)
        else:
            answer[-1] += 1

    return answer


from math import ceil


def solution2(progresses, speeds):
    answer = []

    days = []
    for p, s in zip(progresses, speeds):
        days.append(ceil((100 - p) / s))

    stack = []
    for day in days:
        if stack and stack[-1] >= day:
            answer[-1] += 1
        else:
            stack.append(day)
            answer.append(1)

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
assert [1, 3, 2] == solution(progresses, speeds)

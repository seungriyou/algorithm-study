# [PG] 42748 - K번째수 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
assert [5, 6, 3] == solution(array, commands)

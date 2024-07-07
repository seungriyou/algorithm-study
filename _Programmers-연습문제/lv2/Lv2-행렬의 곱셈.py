# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []

    # 굳이 list comprehension으로 one-line 할 필요는 없을 듯
    for row in arr1:
        _row = []
        for col in zip(*arr2):
            _row.append(sum(r * c for r, c in zip(row, col)))
        answer.append(_row)

    return answer

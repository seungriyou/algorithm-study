# [PG] 12906 - 같은 숫자는 싫어 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    curr = -1
    answer = []
    for a in arr:
        if curr != a:
            answer.append(a)
            curr = a
    return answer


assert [1,3,0,1] == solution([1,1,3,3,0,1,1])

# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    from collections import Counter

    answer = 0

    left = set()  # left는 set()을 이용하여 토핑 종류만 트래킹해도 ok
    right = Counter(topping)  # right에 우선 전체 topping 몰아주기

    for t in topping:
        # left에 추가
        left.add(t)

        # right에서 제거
        right[t] -= 1
        if right[t] == 0:
            right.pop(t)  # del right[t]

        # left 개수와 right 개수가 같으면 answer++
        answer += (len(left) == len(right))

    return answer

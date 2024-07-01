# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    stack = []  # 뒷큰수가 없는 원소의 index
    answer = [-1] * len(numbers)

    # 뒷큰수가 있는 원소에 대해서는 answer 채우기
    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)

    # 뒷큰수가 없는 원소에 대해서는 -1로 두기

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution2(order):
    answer = 0
    stack = []

    for i, o in enumerate(order, start=1):
        # i = 컨테이너 벨트에서 순서대로 받는 상자 번호
        stack.append(i)
        # print(stack)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1
        # print(stack)
        # print()

    return answer


def solution(order):
    answer = 0

    stack = []

    # 컨테이너 벨트 (1번부터 오름차순)
    i = 1

    # order 순서대로
    for o in order:
        # (1) stack이 비어있거나, stack에서 가장 큰 값이 o 보다 작으면 stack 채우기
        if not stack or stack[-1] < o:
            while i != o:
                stack.append(i)
                i += 1
            answer += 1
            i += 1

        # (2) 현재 컨테이너 벨트 상자를 가져갈 수 있으면 바로 가져가기
        elif i == o:
            i += 1
            answer += 1

        # (3) stack에서 가져올 수 있으면 stack에서 가져오기
        elif stack[-1] == o:
            stack.pop()
            answer += 1

        # (4) 불가능하면 멈추기
        else:
            break

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/67257

def solution(expression):
    from itertools import permutations
    from collections import deque

    # expression 파싱
    num = ""
    exp = []
    operations = set()

    for e in expression:
        if e.isdigit():
            num += e
        else:
            exp.append(int(num))
            exp.append(e)
            operations.add(e)
            num = ""
    exp.append(int(num))

    # 각 연산자에 대해 연산 동작 정의
    def operate(n1, o, n2):
        if o == "*":
            return n1 * n2
        elif o == "-":
            return n1 - n2
        elif o == "+":
            return n1 + n2

    # 하나의 operation 우선순위 조합에 대해 결과 계산
    def calculate(ops, exp):
        q = deque(exp)  # 연산의 대상

        for op in ops:  # 연산자 우선순위 순서대로 확인
            stack = []  # 연산 결과 저장
            while q:
                e = q.popleft()
                if e == op:  # 현재 보고 있는 연산자이면 바로 계산 후 stack에 추가
                    stack.append(operate(stack.pop(), e, q.popleft()))
                else:  # 아니라면 stack에 추가
                    stack.append(e)
            q = deque(stack)  # 현재까지 계산한 결과를 다음 연산 대상으로 설정

        return abs(q[0])  # 절댓값

    max_val = 0  # 최대 상금 금액
    for ops in permutations(operations):
        max_val = max(max_val, calculate(ops, exp))

    return max_val

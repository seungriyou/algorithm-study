# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    n = len(s)

    def is_valid(start):
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for d in range(n):
            i = (start + d) % n

            # 여는 괄호라면, stack에 추가
            if (p := s[i]) not in mapping:
                stack.append(p)

            # 닫는 괄호이고, 남은 여는 괄호가 없거나 짝이 맞지 않는 경우 False 반환
            elif not stack or stack.pop() != mapping[p]:
                return False

        # stack에 남은 원소가 없어야 True
        return len(stack) == 0

    cnt = 0
    for i in range(n):
        cnt += is_valid(i)

    return cnt

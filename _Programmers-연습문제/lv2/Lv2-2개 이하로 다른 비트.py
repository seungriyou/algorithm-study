# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    def func(num):
        # 홀수
        if num & 1:
            # 맨 왼쪽에 0 붙이기
            lst = list("0" + bin(num)[2:])
            # 맨 오른쪽에 있는 0 찾기 (num보다 큰 수 중에서 제일 작은 수를 찾아야 하므로)
            idx = "".join(lst).rfind("0")
            # 찾은 0을 1로 바꾸고, 그 오른쪽 수를 0으로 바꾸기
            lst[idx] = "1"
            lst[idx + 1] = "0"
            return int("".join(lst), 2)
        # 짝수
        else:
            return num + 1

    return [func(num) for num in numbers]

# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    # 3진법으로 변환하면서, 뒤에서부터 해당 자리가 0이 되면 (1) 4로 바꾸고 (2) 앞에서 1 빌려오기
    nums = []

    while n > 0:
        r = n % 3

        if r == 0:
            r = 4
            n -= 1

        nums.append(str(r))

        n //= 3

    return "".join(nums[::-1])

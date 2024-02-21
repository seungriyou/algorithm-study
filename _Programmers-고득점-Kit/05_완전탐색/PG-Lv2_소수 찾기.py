# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
    n = len(numbers)

    # 1. 만들 수 있는 모든 숫자 찾기 (permutation)
    possible_numbers = set()
    curr_number = []
    seen = [False] * n

    def backtrack():
        if curr_number:
            possible_numbers.add(int("".join(curr_number)))

        # recur
        for i in range(n):
            if not seen[i]:
                curr_number.append(numbers[i])
                seen[i] = True

                backtrack()

                curr_number.pop()
                seen[i] = False

    backtrack()

    # 2. 소수인 숫자만 세기
    def is_prime(num):
        if num == 0 or num == 1:
            return False

        if num == 2 or num == 3:
            return True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    return sum(is_prime(num) for num in possible_numbers)


numbers = "17"
print(solution(numbers))    # should print 3

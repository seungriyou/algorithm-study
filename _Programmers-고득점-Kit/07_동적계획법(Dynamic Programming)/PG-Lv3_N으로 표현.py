# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    """
    dp[i] = N을 i번 사용하여 만들 수 있는 숫자

    즉, dp[3]이란 N을 3번 사용하여 만들 수 있는 숫자들의 집합이다.
    따라서
        (1) int(NNN)
        (2) dp[1]과 dp[2]에 속하는 숫자들로 사칙연산을 수행한 결과
        (3) dp[2]와 dp[1]에 속하는 숫자들로 사칙연산을 수행한 결과
    를 모두 모은 것이 dp[3]이 된다.

    dp[4]의 경우에는
        (1) int(NNNN)
        (2) dp[1], dp[3]
        (3) dp[2], dp[2]
        (4) dp[3], dp[1]
    ...

    이때, N 사용횟수의 최솟값을 구해야하므로, 각 단계마다 number가 존재하는지 확인한다.
    """

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 * num2)
                    dp[i].add(num1 - num2)

                    if num2 != 0:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            return i

    return -1

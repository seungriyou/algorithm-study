# https://school.programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    """
    O(1) DP (점화식 최적화)

    최적화된 점화식은 f(n) = 4 * f(n - 1) - f(n - 2) 인데,
    f(n)을 구하기 위해서는 이전의 2개 값만 보면 된다.
    """
    # n이 홀수이면 0 반환
    if n % 2:
        return 0

    a, b = 1, 3
    idx = n // 2

    for i in range(2, idx + 1):
        a, b = b, (4 * b - a) % 1_000_000_007

    return b


def solution1(n):
    """
    1D DP (점화식 최적화)

    이전에 구한 점화식은 다음과 같다.
        f(n) = 3 * f(n - 1) + [[ 2 * f(n - 2) + ... + 2 ]]      -- (1)

    점화식 (1)을 통해 다음과 같은 식 (2)를 얻을 수 있다.
        f(n) - f(n - 1) = 2 * (f(n - 1) + f(n - 2) + ... + 1)   -- (2)

    식 (2)의 n에 n - 1을 대입하면 다음과 같은 식 (3)을 얻을 수 있다.
        [[ f(n - 1) - f(n - 2) ]] = 2 * (f(n - 2) + f(n - 3) + ... + 1) -- (3)

    점화식 (1)의 [[ ]] 부분 == 식 (3)의 우변이므로, 점화식 (1)의 [[ ]] 부분에 식 (3)의 [[ ]] 부분을 대입할 수 있다.
        f(n) = 3 * f(n - 1) + f(n - 1) - f(n - 2) = 4 * f(n - 1) - f(n - 2) -- (4)

    따라서 최적화된 점화식은 f(n) = 4 * f(n - 1) - f(n - 2) 이다.
    """
    # n이 홀수이면 0 반환
    if n % 2:
        return 0

    # 짝수 n만 살펴보기 위해서 홀수 인덱스 제거
    dp = [0, 3, 11]
    idx = n // 2

    if idx < 3:
        return dp[idx]

    for i in range(3, idx + 1):
        dp.append((4 * dp[i - 1] - dp[i - 2]) % 1_000_000_007)

    return dp[idx]


def solution2(n):
    """
    1D DP
    ref: https://s2choco.tistory.com/24
    """
    # n이 홀수이면 0 반환
    if n % 2:
        return 0

    # 짝수 n만 살펴보기 위해서 홀수 인덱스 제거
    dp = [0, 3, 11]
    idx = n // 2

    if idx < 3:
        return dp[idx]

    for i in range(3, idx + 1):
        """
        점화식: f(n)
            = f(n - 1) * 3  : <1> 바로 이전 단계에서 가로 2칸 짜리 경우 = 3가지
            + f(n - 2) * 2  : <2> 그 이전 단계에서 새롭게 추가된 종류 반영 = 2가지
            + ...
            + 2             : <3> 매 단계마다 새롭게 추가되는 종류(= 가로 n짜리) = 2가지
        """
        dp.append((dp[i - 1] * 3 + sum(dp[:i - 1]) * 2 + 2) % 1_000_000_007)

    return dp[idx]

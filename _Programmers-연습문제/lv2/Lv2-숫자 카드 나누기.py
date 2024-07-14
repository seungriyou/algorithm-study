# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def solution(arrayA, arrayB):
    """
    각 조건을 두 파트로 나누어보면 다음과 같다.
        - A가 가진 카드들에 적힌 모든 숫자를 나눌 수 있다 => A의 최대공약수 (이 부분 조건을 만족하는 가장 큰 수)
        - B가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없다 => A의 최대공약수가 B의 모든 원소를 나누지 못하는지 여부를 확인하면 된다.
    """
    answer = 0

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def arr_gcd(arr):
        _gcd = arr[0]
        for a in arr:
            _gcd = gcd(_gcd, a)
        return _gcd

    def is_divisible(arr, num):
        return any(a % num == 0 for a in arr)
        # for a in arr:
        #     if a % num == 0:
        #         return True
        # return False

    # arrayA와 arrayB의 최대공약수 구하기
    gcd_a, gcd_b = arr_gcd(arrayA), arr_gcd(arrayB)

    # 조건 1번
    if not is_divisible(arrayB, gcd_a):
        answer = max(answer, gcd_a)

    # 조건 2번
    if not is_divisible(arrayA, gcd_b):
        answer = max(answer, gcd_b)

    return answer

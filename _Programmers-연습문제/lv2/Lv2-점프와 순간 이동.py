# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    return bin(n).count("1")


def solution2(n):
    ans = 1

    while n > 1:
        ans += n % 2
        n //= 2

    return ans


def solution1(n):
    """
    아이언 슈트
    - K칸 앞으로 점프: K만큼 건전지 사용
    - (현재까지 온 거리) * 2 위치로 순간이동: 건전지 사용 X

    거리 N만큼 떨어진 장소로 가려 하며, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최소로
    건전지 사용량의 최솟값
    """

    ans = 0

    while n > 0:
        # 홀수인 경우
        if n & 1:
            n -= 1
            ans += 1
        # 짝수인 경우
        else:
            n //= 2

    return ans

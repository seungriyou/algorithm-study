# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    # 순차적으로 최소공배수를 구해나가면 됨
    lcm = 1
    for a in arr:
        # lcm(a, b) = (a * b) / gcd(a, b)
        lcm = (lcm * a) / gcd(lcm, a)

    return lcm


def solution1(arr):
    arr.sort(reverse=True)

    # 제일 큰 수를 기준으로, 다른 나머지 수로 나누어떨어지는지 확인
    m, n = 1, len(arr)
    max_val = arr[0]
    while True:
        is_stopped = False
        candidate = max_val * m

        for i in range(1, n):
            # 나누어떨어지지 않으면, 곱할 값 m을 늘리고 빠르게 continue
            if candidate % arr[i]:
                m += 1
                is_stopped = True
                break

        if not is_stopped:
            return candidate

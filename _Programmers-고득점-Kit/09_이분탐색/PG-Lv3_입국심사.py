# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0

    left, right = 1, max(times) * n  # 모든 사람을 심사하는 데에 걸리는 시간의 최솟값, 최댓값

    while left <= right:
        mid = (left + right) // 2

        capacity = 0
        for time in times:
            capacity += mid // time  # 모든 심사관들이 mid분 동안 심사한 사람의 수

            # 모든 심사관을 거치지 않아도 모든 사람을 심사할 수 있다면 빠르게 멈추기
            if capacity >= n:
                break

        # capacity가 n 이상이라면, 값을 저장하고 시간을 줄임
        if capacity >= n:
            answer = mid
            right = mid - 1

        # capacity가 n보다 작다면, 시간을 더 늘려야 함
        elif capacity < n:
            left = mid + 1

    return answer

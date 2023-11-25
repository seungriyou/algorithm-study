# https://school.programmers.co.kr/learn/courses/30/lessons/64062

# binary search (parameteric search)

def solution(stones, k):
    left, right = 0, 200_000_000  # 다리를 건널 수 있는 친구의 수가 속하는 범위

    while left <= right:
        # while left < right:
        mid = left + (right - left) // 2
        cnt = 0  # 연속해서 등장하는, 건널 수 없는 징검다리의 개수

        for stone in stones:
            if stone - mid <= 0:  # 건널 수 없는 경우
                cnt += 1
            else:
                cnt = 0  # 건널 수 있는 경우, cnt 초기화

            # cnt가 k 조건에 도달하면 빠르게 break
            if cnt == k:
                break

        if cnt == k:
            right = mid - 1
            # right = mid
        else:
            left = mid + 1

    return left

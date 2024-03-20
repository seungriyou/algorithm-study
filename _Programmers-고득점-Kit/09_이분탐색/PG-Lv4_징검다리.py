# https://school.programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance

    while left <= right:
        mid = (left + right) // 2  # 각 지점 사이의 거리의 최솟값

        start_rock = removed = 0
        min_dist = float('inf')

        for rock in rocks:
            # start_rock 까지의 거리가 최솟값이어야 하는 mid 보다 작은 경우, rock을 제거해야 함
            if (dist := rock - start_rock) < mid:
                removed += 1
            # 아니라면, min_dist 및 start_rock 업데이트
            else:
                start_rock = rock
                min_dist = min(min_dist, dist)

            # removed 개수가 n보다 커지면 빠르게 중단
            if removed > n:
                break

        # 제거된 바위가 너무 많다면, 거리의 최솟값을 줄여야 함
        if removed > n:
            right = mid - 1
        # 아니라면, 거리의 최솟값을 늘려야 함
        else:
            answer = min_dist
            left = mid + 1

    return answer

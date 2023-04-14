# https://school.programmers.co.kr/learn/courses/30/lessons/42891

"""
소요 시간이 작은 음식부터 그리디하게 처리
우선순위 큐 말고 sort 써도 되지 않을까?
"""

import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    sorted_time_food = [(t, i + 1) for i, t in enumerate(food_times)]
    heapq.heapify(sorted_time_food)

    remaining_food = len(food_times)
    passed_time = 0
    prev_time = 0

    while True:
        time, food = heapq.heappop(sorted_time_food)
        next_passed_time = passed_time + (time - prev_time) * remaining_food
        if next_passed_time > k:
            heapq.heappush(sorted_time_food, (time, food))
            break
        passed_time = next_passed_time
        remaining_food -= 1
        prev_time = time

    result = sorted(sorted_time_food, key=lambda x: x[1])
    return result[(k - passed_time) % remaining_food][1]

food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))
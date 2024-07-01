# [PG] 42583 - 다리를 지나는 트럭 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    # bridge를 만들어서 1초가 지날 때마다 shifting 되는 효과를 구현한다.

    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0  # bridge 위의 truck 무게의 합
    cnt = 0

    while bridge:
        cnt += 1
        total_weight -= bridge.popleft()

        if truck_weights:
            if truck_weights[0] + total_weight <= weight:
                truck_weight = truck_weights.popleft()
                bridge.append(truck_weight)
                total_weight += truck_weight
            else:
                bridge.append(0)

    return cnt

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
assert 8 == solution(bridge_length, weight, truck_weights)


##### review #####
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = truck_weights[::-1]
    total_weight = sec = 0

    while truck_weights:
        total_weight -= bridge.pop()

        if total_weight + truck_weights[-1] <= weight:
            new_truck = truck_weights.pop()
            bridge.appendleft(new_truck)
            total_weight += new_truck
        else:
            bridge.appendleft(0)

        sec += 1

    return sec + bridge_length

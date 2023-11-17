# https://www.acmicpc.net/problem/13335
import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * W)

time = 0
total_weights = 0

# TIP: bridge의 원소들을 계속 shift -> deque로 popleft & append!
while bridge:
    time += 1
    # bridge의 맨 앞 원소 pop 하고, bridge 위의 전체 truck 무게에서 뺀다
    total_weights -= bridge.popleft()

    # 남은 truck이 존재한다면
    if trucks:
        # bridge의 최대하중을 견딜 수 있어야 truck을 올릴 수 있다
        if total_weights + trucks[0] <= L:
            next_truck = trucks.popleft()
            bridge.append(next_truck)
            total_weights += next_truck
        # truck을 올릴 수 없다면 0을 추가한다
        else:
            bridge.append(0)

print(time)

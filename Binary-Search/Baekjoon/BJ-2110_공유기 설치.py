# [BJ] 2110 - 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append((int(input())))

houses.sort()

start = 0   # min gap
end = houses[-1] - houses[0]    # max gap (인접 공유기 간 거리)
result = 0

while start <= end:
    mid = start + (end - start) // 2
    prev_house = houses[0]
    cnt = 1 # 첫 집에 공유기 설치

    for i in range(1, n):   # 첫 집 제외
        if prev_house + mid <= houses[i]:
            prev_house = houses[i]
            cnt += 1

    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

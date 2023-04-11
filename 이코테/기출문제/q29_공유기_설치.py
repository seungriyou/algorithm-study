# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

start = 1 # 최소 gap
end = houses[-1] - houses[0] # 최대 gap
result = 0

while start <= end:
    mid = (start + end) // 2
    val = houses[0]
    cnt = 1 # 맨 첫 집에는 공유기 설치

    # 두 번째 집부터 검사
    for i in range(1, n):
        if houses[i] >= val + mid:
            cnt += 1
            val = houses[i]
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

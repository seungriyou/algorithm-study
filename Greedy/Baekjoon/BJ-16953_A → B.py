# [BOJ] 16953 - A → B
# https://www.acmicpc.net/problem/16953

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1
while a < b:
    if b % 2 == 0:
        b //= 2
    else:
        if b % 10 == 1:
            b //= 10
        else:
            cnt = -1
            break
    cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)

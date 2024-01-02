# https://www.acmicpc.net/problem/13458
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N

for a in A:
    # 총감독관
    a -= B
    # 부감독관
    if a > 0:
        if a % C:
            cnt += (a // C) + 1
        else:
            cnt += (a // C)

print(cnt)

# https://www.acmicpc.net/problem/2170
import sys
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()    # 정렬 -> ll > r 일 때, l, r을 새롭게 셋팅하면 됨

l, r = lines[0]
total = r - l

for i in range(1, N):
    ll, lr = lines[i]   # 현재 보고 있는 선의 왼쪽, 오른쪽

    # ll이 r보다 작거나 같으면, 기존에 보고있던 total에 이어서
    if ll <= r:
        if lr > r:
            total += lr - r
            r = lr
    # ll이 r보다 크면, l, r로 tracking 하는 line을 새롭게 셋팅
    else:
        l, r = ll, lr
        total += r - l

print(total)

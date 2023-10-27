# [BOJ] 1931 - 회의실 배정

import sys

sys.stdin = open('../input.txt')
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    meeting = tuple(map(int, input().split()))
    meetings.append(meeting)

# 마치는 시간 -> 시작 시간 순서로 오름차순 정렬
# 마치는 시간이 빠를수록 뒤에 더 많은 회의 가능하므로
meetings.sort(key=lambda x: (x[1], x[0]))

cnt, last_end = 0, 0
for s, e in meetings:
    if s >= last_end:
        cnt += 1
        last_end = e

print(cnt)

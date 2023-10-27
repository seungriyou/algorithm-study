# [BOJ] 1931 - 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

meetings = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 오름차순 정렬 우선 순위: (끝나는 시각, 시작 시각)
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last_end = 0
for s, e in meetings:
    if s >= last_end:
        cnt += 1
        last_end = e

print(cnt)

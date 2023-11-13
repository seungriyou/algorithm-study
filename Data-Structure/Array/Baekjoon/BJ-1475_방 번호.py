# https://www.acmicpc.net/problem/1475
import sys
from math import ceil
input = sys.stdin.readline

N = list(input().rstrip())
cnt = [0] * 10
for n in N:
    cnt[int(n)] += 1

max_cnt = max(cnt)
if max_cnt == cnt[6] or cnt[9]:
    cnt[6] = cnt[9] = ceil((cnt[6] + cnt[9]) / 2)
    print(max(cnt))
else:
    print(max_cnt)

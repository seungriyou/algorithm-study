# https://www.acmicpc.net/problem/19598
import sys; input = sys.stdin.readline
import heapq

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)] # (s, t) = (시작 시각, 완료 시각)

# (시작 시각, 완료 시각) 순서로 오름차순 정렬
meetings.sort()
# 회의의 완료 시각을 오름차순으로 확인하기 위한 heap
q = []

for s, t in meetings:
    # 현재 확인하고 있는 회의의 완료 시각을 q에 넣기
    heapq.heappush(q, t)

    # q에 존재하는 가장 빠른 완료 시각 <= s라면, 가장 빠른 완료 시각을 가지는 회의실에서 이어서 회의 진행 가능
    if q[0] <= s:
        heapq.heappop(q)

# 필요한 최소 회의실 개수는 q의 길이와 같음
print(len(q))
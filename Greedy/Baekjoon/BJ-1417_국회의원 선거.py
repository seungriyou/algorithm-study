# https://www.acmicpc.net/problem/1417
import sys; input = sys.stdin.readline
import heapq

N = int(input())
votes = [int(input()) for _ in range(N)]

dasom = votes[0]
votes = [-votes[i] for i in range(1, N)]
heapq.heapify(votes)
cnt = 0

while votes:
    if dasom + cnt > -votes[0]:
        break

    top = heapq.heappop(votes)
    heapq.heappush(votes, top + 1)
    cnt += 1

print(cnt)
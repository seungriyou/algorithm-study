# https://www.acmicpc.net/problem/10451
import sys
input = sys.stdin.readline


def bfs(start, nums, visited):
    visited[start] = True
    npos = nums[start]

    while not visited[npos]:
        visited[npos] = True
        npos = nums[npos]

    return


T = int(input())
for _ in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i, nums, visited)
            cnt += 1

    print(cnt)

# https://www.acmicpc.net/problem/2696
import sys; input = sys.stdin.readline
import heapq

def solve(nums, M):
    # left: mid 보다 작은 값을 담는 최대힙 / right: mid 보다 큰 값을 담는 최소힙
    left, right, ans = [], [], [nums[0]]
    mid = nums[0]

    for i in range(1, M):
        num = nums[i]

        # left, right 업데이트
        if num < mid:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        # 홀수 번째 수
        if i % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            # else 라면 mid 값은 그대로

            ans.append(mid)

    return ans


T = int(input())
for _ in range(T):
    M = int(input())

    nums = []
    for _ in range(M // 10 + 1):
        nums.extend(list(map(int, input().split())))

    res = solve(nums, M)
    print(len(res))
    print(*res)

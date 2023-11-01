# https://www.acmicpc.net/problem/12738
import bisect
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

memo = [nums[0]]

# memo[i] = 길이가 (i + 1)인 LIS의 맨 마지막 원소가 될 수 있는 값 중 가장 작은 값
for i in range(N):
    if memo[-1] < nums[i]:
        memo.append(nums[i])
    else:
        idx = bisect.bisect_left(memo, nums[i])
        memo[idx] = nums[i]

print(len(memo))

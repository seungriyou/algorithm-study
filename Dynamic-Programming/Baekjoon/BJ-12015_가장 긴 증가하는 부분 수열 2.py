# https://www.acmicpc.net/problem/12015
import bisect
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# memo[i] = 길이가 (i + 1)인 LIS의 맨 마지막 원소가 될 수 있는 값 중 가장 작은 값
# memo는 오름차순으로 정렬된 리스트 -> 이분 탐색!
memo = [nums[0]]

# ===== w/ bisect =====
for i in range(N):
    if memo[-1] < nums[i]:
        memo.append(nums[i])
    else:
        idx = bisect.bisect_left(memo, nums[i])   # memo에 nums[i]가 들어갈 수 있는 위치 찾기
        memo[idx] = nums[i]                       # 해당 위치의 값을 nums[i]로 업데이트  (nums[i] <= memo[idx] 일 것이므로 min()으로 구할 필요 X)

print(len(memo))


# ===== w/o bisect =====
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = l + (r - l) // 2
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid

    return l    # r

for i in range(N):
    if memo[-1] < nums[i]:
        memo.append(nums[i])
    else:
        idx = binary_search(memo, nums[i])   # memo에 nums[i]가 들어갈 수 있는 위치 찾기
        memo[idx] = nums[i]                  # 해당 위치의 값을 nums[i]로 업데이트  (nums[i] <= memo[idx] 일 것이므로 min()으로 구할 필요 X)

print(len(memo))
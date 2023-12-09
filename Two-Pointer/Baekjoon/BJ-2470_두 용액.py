# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

N = int(input())

# ==== [sol1] 단순 two pointer ====
nums = sorted(list(map(int, input().split())))

left, right = 0, N - 1
val = int(1e10)
result = None

while left < right:
    new_val = nums[left] + nums[right]

    if abs(new_val) < val:
        val = abs(new_val)
        result = nums[left], nums[right]

    if new_val < 0:
        left += 1
    elif new_val > 0:
        right -= 1
    else:
        result = nums[left], nums[right]
        break

print(*result)


# ==== [sol2] 절댓값 기준 정렬 ====
nums = sorted(list(map(int, input().split())), key=lambda x: abs(x))
min_dist = 2 * int(1e9)
result = None

for i in range(N - 1):
    if (new_dist := abs(nums[i] + nums[i + 1])) < min_dist:
        min_dist = new_dist
        result = [nums[i], nums[i + 1]]

print(*sorted(result))

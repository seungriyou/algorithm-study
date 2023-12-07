# https://www.acmicpc.net/problem/1789
import sys
input = sys.stdin.readline

S = int(input())

# ==== greedy ====
# 가장 많은 자연수를 가지고 S라는 합을 만들려면, 1부터 차례대로 더해나가야 한다.
num, cnt, sum_v = 1, 0, 0

while True:
    sum_v += num
    cnt += 1
    if sum_v > S:
        cnt -= 1
        break
    num += 1

print(cnt)

# ==== binary search ====
left, right = 0, S
while left <= right:
    mid = left + (right - left) // 2
    sum_v = mid * (mid + 1) // 2    # 1 ~ mid 까지의 합

    if sum_v > S:
        right = mid - 1
    else:
        left = mid + 1

print(right)

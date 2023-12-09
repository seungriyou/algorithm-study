# https://www.acmicpc.net/problem/20922
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
left = right = 0

counter = {num: 0 for num in nums}
max_len = 0

# ==== sol1 =====
while right < N:
    if counter[nums[right]] == K:
        counter[nums[left]] -= 1
        left += 1
    else:
        counter[nums[right]] += 1
        right += 1
        # max_len 갱신
        max_len = max(max_len, right - left)

print(max_len)

# ==== sol2 =====
for right in range(N):
    # right 위치의 값 counter에 반영
    counter[nums[right]] += 1
    # 만약 해당 값의 개수가 K 초과라면, 그 개수가 K 이하로 바뀔 때까지 left를 오른쪽으로 옮기기
    while counter[nums[right]] > K:
        counter[nums[left]] -= 1
        left += 1
    # max_len 갱신
    max_len = max(max_len, right - left + 1)

print(max_len)

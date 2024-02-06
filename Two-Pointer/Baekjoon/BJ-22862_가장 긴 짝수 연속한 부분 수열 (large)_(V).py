# https://www.acmicpc.net/problem/22862
import sys; input = sys.stdin.readline

# 최대 K번 삭제를 할 수 있다 -> 최대 K개의 홀수가 들어있는 가장 긴 길이의 부분 수열을 찾자!
N, K = map(int, input().split())
nums = list(map(int, input().split()))

left = right = 0    # 부분 수열의 시작과 끝 index
max_len = 0         # 가장 긴 짝수 연속한 부분 수열의 길이
even_cnt = 0        # 현재 보고 있는 임시 부분 수열의 짝수 연속한 부분 길이
odd_cnt = 0         # 현재 보고 있는 임시 부분 수열의 홀수 개수

def is_odd(num):
    return num & 1

# === sol 1 ==== #
while True:
    if right == N:
        break

    if odd_cnt <= K:
        # right ++
        if is_odd(nums[right]):
            odd_cnt += 1
        else:
            even_cnt += 1
        right += 1
    else:
        # left ++
        if is_odd(nums[left]):
            odd_cnt -= 1
        else:
            even_cnt -= 1
        left += 1

    if odd_cnt <= K:
        max_len = max(max_len, even_cnt)

print(max_len)


# === sol 2 ==== #
for left in range(N):
    # right ++
    while right < N and odd_cnt <= K:
        if is_odd(nums[right]):
            odd_cnt += 1
        else:
            even_cnt += 1
        right += 1

    # (주의) 전체 수열에 K개 이하의 홀수만 들어있는 경우
    if left == 0 and right == N:
        max_len = even_cnt
        break

    if odd_cnt == K + 1:
        max_len = max(max_len, even_cnt)

    # left ++
    if is_odd(nums[left]):
        odd_cnt -= 1
    else:
        even_cnt -= 1

print(max_len)

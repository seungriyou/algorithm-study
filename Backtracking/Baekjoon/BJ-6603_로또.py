# https://www.acmicpc.net/problem/6603
import sys
input = sys.stdin.readline

# kC6

while True:
    tmp = list(map(int, input().split()))
    if tmp == [0]:
        break
    k, nums = tmp[0], tmp[1:]

    lotto_nums = []
    def backtrack(idx):
        # base case
        if len(lotto_nums) == 6:
            print(*lotto_nums)
            return

        for i in range(idx, k):
            lotto_nums.append(nums[i])
            backtrack(i + 1)
            lotto_nums.pop()

    backtrack(0)
    print()

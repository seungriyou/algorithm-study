# [PG] 1845 - 폰켓몬 (Lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import defaultdict

def solution(nums):
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1

        if len(cnt) <= len(nums) // 2:
            return len(cnt)
        else:
            return len(nums) // 2

def solution2(nums):
    return min(len(set(nums)), len(nums) // 2)


nums = [3,3,3,2,2,4]
assert 3 == solution(nums) == solution2(nums)

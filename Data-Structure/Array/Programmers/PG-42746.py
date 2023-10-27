# [PG] 42746 - 가장 큰 수 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# === cmp_to_key ===
from functools import cmp_to_key

def compare(x, y):  # -- 굳이 int() 변환할 필요 없음 (순차적으로 unicode 값을 비교하므로)
    t1 = x + y
    t2 = y + x
    if t1 > t2:
        return -1  # -- x < y 순서
    elif t1 < t2:
        return 1  # -- y < x 순서
    else:
        return 0

def compare1(x, y):  # -- 굳이 int() 변환할 필요 없음 (순차적으로 unicode 값을 비교하므로)
    t1 = x + y
    t2 = y + x
    return (t1 < t2) - (t1 > t2)  # -- t1이 크면 -1, t2가 크면 1, 같으면 0

def solution1(numbers):
    nums = [str(n) for n in numbers]
    nums.sort(key=cmp_to_key(compare))
    return ''.join(nums).lstrip('0') or '0'


# === merge sort ====
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])

    l = r = 0
    merged_arr = []
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] + r_arr[r] > r_arr[r] + l_arr[l]:  # -- 굳이 int() 변환할 필요 없음 (순차적으로 unicode 값을 비교하므로)
            merged_arr.append(l_arr[l])
            l += 1
        else:
            merged_arr.append(r_arr[r])
            r += 1

    # merged_arr += l_arr[l:]
    # merged_arr += r_arr[r:]
    while l < len(l_arr):
        merged_arr.append(l_arr[l])
        l += 1
    while r < len(r_arr):
        merged_arr.append(r_arr[r])
        r += 1

    return merged_arr


def solution(numbers):
    nums = [str(n) for n in numbers]

    return ''.join(merge_sort(nums)).lstrip('0') or '0'


numbers = [3, 30, 34, 5, 9]
assert '9534330' == solution(numbers) == solution1(numbers)

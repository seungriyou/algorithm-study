# https://www.acmicpc.net/problem/2331
import sys
input = sys.stdin.readline

A, P = map(int, input().split())
nums = {A}  # set 이용
prev = A
is_rep = False  # 반복되는 수가 나오기 시작한 경우, True로 바꾸기

def get_number(num, power):
    # num의 각 자릿수를 power-제곱햐여 더한 값을 계산하는 함수
    result = 0
    i = 1
    while i <= num:
        result += (num // i % 10) ** power
        i *= 10
    return result

while True:
    prev = get_number(prev, P)
    if is_rep:
        if prev in nums:
            nums.remove(prev)
        else:               # 반복되는 수가 더이상 nums에 남아있지 않다면 종료
            break
    else:
        if prev in nums:    # 이전에 발견했던 수가 다시 발견되는 경우
            is_rep = True
            nums.remove(prev)
        else:
            nums.add(prev)

print(len(nums))

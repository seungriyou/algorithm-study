# https://www.acmicpc.net/problem/14916
import sys
input = sys.stdin.readline

N = int(input())

def count_min_coin(N):
    remainder = N
    cnt = 0

    # 5원짜리 동전으로 나누어 떨어질 때까지 2원짜리 동전 사용하기
    while remainder % 5 != 0:
        remainder -= 2
        cnt += 1
        # 2원짜리, 5원짜리 동전을 사용해서 거슬러 줄 수 없는 경우
        if remainder < 0:
            return -1

    cnt += remainder // 5
    return cnt

print(count_min_coin(N))

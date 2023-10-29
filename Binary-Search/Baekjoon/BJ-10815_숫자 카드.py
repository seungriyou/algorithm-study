# https://www.acmicpc.net/problem/10815
import sys
input = sys.stdin.readline

# ===== binary search =====
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

cards.sort()

def binary_search(card):
    left, right = 0, N - 1

    while left <= right:
        mid = left + (right - left) // 2
        if card < cards[mid]:
            right = mid - 1
        elif card > cards[mid]:
            left = mid + 1
        else:
            return "1"

    return "0"


result = [binary_search(c) for c in compare]
print(' '.join(result))

# ===== set =====
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

for c in compare:
    if c in cards:
        print("1", end=" ")
    else:
        print("0", end=" ")

# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))


# ===== dict =====
from collections import defaultdict
cards_dict = defaultdict(int)
for c in cards:
    cards_dict[c] += 1

for c in compare:
    print(cards_dict.get(c, 0), end=" ")


# ===== counter =====
from collections import Counter

cards_dict = Counter(cards)

for c in compare:
    print(cards_dict.get(c, 0), end=" ")


# ===== binary search =====
from bisect import bisect_left, bisect_right

cards.sort()

def binary_search(num):
    return bisect_right(cards, num) - bisect_left(cards, num)

for c in compare:
    print(binary_search(c), end=" ")

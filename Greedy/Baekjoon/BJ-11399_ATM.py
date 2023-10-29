# https://www.acmicpc.net/problem/11399
import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
p.sort()

answer = acc = 0
for pi in p:
    answer += (acc + pi)
    acc += pi

print(answer)

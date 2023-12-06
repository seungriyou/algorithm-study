# https://www.acmicpc.net/problem/21921
import sys
input = sys.stdin.readline

X, N = map(int, input().split())
visitors = list(map(int, input().split()))
max_visitor = cnt = 0

# prefix sum
sum_v = 0
p_sum = [0]
for i in range(X):
    sum_v += visitors[i]
    p_sum.append(sum_v)

for i in range(N, X + 1):
    v = p_sum[i] - p_sum[i - N]
    if v > max_visitor:
        max_visitor = v
        cnt = 1
    elif v == max_visitor:
        cnt += 1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(cnt)

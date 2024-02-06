# https://www.acmicpc.net/problem/14929
import sys; input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

# === p_sum array 이용 === #
p_sum = [0]
for x in X:
    p_sum.append(p_sum[-1] + x)

result = 0
for i in range(2, N + 1):
    result += (X[i - 2] * (p_sum[N] - p_sum[i - 1]))

print(result)

# === p_sum array 이용 X === #
# (i >= 2) sum(X_i ~ X_N) 까지의 값이 필요하므로 굳이 p_sum array를 가져가지 않아도 된다.
_sum = sum(X)
result = 0
for x in X:
    _sum -= x
    result += x * _sum

print(result)

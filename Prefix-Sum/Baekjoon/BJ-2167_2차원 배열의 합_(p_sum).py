# https://www.acmicpc.net/problem/2167
import sys; input = sys.stdin.readline

# DP로도 가능

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

# 배열의 row 마다 p_sum 구하기
p_sums = [[]]
for num in nums:
    p_sum = [0]
    for n in num:
        p_sum.append(p_sum[-1] + n)
    p_sums.append(p_sum)

def get_sum(i, j, x, y):
    result = 0
    # row i ~ x 까지, p_sum을 이용하여 col j ~ y 까지의 구간 합 구해서 누적
    for m in range(i, x + 1):
        result += (p_sums[m][y] - p_sums[m][j - 1])
    return result

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(get_sum(i, j, x, y))

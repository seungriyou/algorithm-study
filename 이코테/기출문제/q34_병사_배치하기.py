# https://www.acmicpc.net/problem/18353

n = int(input())
array = list(map(int, input().split()))
# "순서를 뒤집어 가장 긴 감소하는 부분 수열 구하기" 문제로 바꿈
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))

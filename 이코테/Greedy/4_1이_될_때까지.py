n, k = map(int, input().split())
cnt = 0

# while True:
#     if n == 1:
#         break
#     if n % k == 0:
#         n /= k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1
#
# print(cnt)

while True:
    # 나누어 떨어질 때까지 1 빼기 (한 번에 구하기)
    tmp = n // k * k
    cnt += n - tmp
    n = tmp
    if n < k:
        break
    # n >= k라면 k로 나누기
    n //= k
    cnt += 1

# 남은 수에서 1이 남을 때까지 1을 빼는 횟수 더하기
cnt += (n - 1)
print(cnt)

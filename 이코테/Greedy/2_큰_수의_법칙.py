n, m, k = map(int, input().split()) # (연속 최대 k번) m 번 더하여 최대
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

# first 덧셈 횟수 계산
cnt = m // (k + 1) * k
cnt += m % (k + 1)

result = first * cnt
result += second * (m - cnt)

print(result)

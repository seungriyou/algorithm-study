n, m = map(int, input().split())
balls = list(map(int, input().split()))
nums = [0] * (m + 1) # 각 볼링공 별 무게 저장

for b in balls:
    nums[b] += 1

result = 0
for i in range(1, m + 1):
    n -= nums[i]
    result += nums[i] * n

print(result)

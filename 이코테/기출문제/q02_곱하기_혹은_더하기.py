nums = list(map(int, list(input())))

result = nums[0]

# 주의: result 조건도 잊지 않기 (왼, 오 둘다 확인)
for n in nums[1:]:
    d = n
    if d <= 1 or result <= 1:
        result += d
    else:
        result *= d

print(result)

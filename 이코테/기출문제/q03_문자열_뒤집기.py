nums = list(map(int, list(input())))

# 전부 0으로 바꾸는 경우와 1로 바꾸는 경우 중 min 값

cnt_0 = 0 # 0으로 바꾸는 경우
cnt_1 = 0 # 1로 바꾸는 경우

if nums[0] == 1:
    cnt_0 += 1
else:
    cnt_1 += 1

for i in range(len(nums) - 1):
    if nums[i] != nums[i + 1]:
        if nums[i + 1] == 1:
            cnt_0 += 1
        else:
            cnt_1 += 1

print(min(cnt_0, cnt_1))

# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# prefix sum 배열 계산
sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산 (ex. 3번째 수 ~ 4번째 수)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])

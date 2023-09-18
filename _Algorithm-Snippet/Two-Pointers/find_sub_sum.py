n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0 # 합이 M인 부분 연속 수열 개수
interval_sum = 0
end = 0

# start를 차례대로 증가시키면서 반복
for start in range(n):
    # end를 가능한 만큼 이동
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m: # interval_sum >= m인 상황 중, ==인 경우에만 count++
        count += 1
    interval_sum -= data[start] # start를 1 증가할 것이므로

print(count)

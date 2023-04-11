# https://www.acmicpc.net/problem/14501

n = int(input())
t = []
p = []
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

dp = [0] * (n + 1)
max_val = 0 # 최대 이익

for i in range(n - 1, -1, -1):
    time = i + t[i] # 지금으로부터 완료할 때까지 걸리는 시간
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 지금 선택한 상담을 한다면,
        # {(지금 상담의 이익) + (지금 상담이 완료된 시점에서의 최대 이익)} 과 (지금까지의 최대 이익) 중에서
        # 최댓값을 선택해야 함
        dp[i] = max(p[i] + dp[time], max_val)
        max_val = dp[i]
    # 상담이 기간을 법어나는 경우
    else:
        dp[i] = max_val

print(max_val)

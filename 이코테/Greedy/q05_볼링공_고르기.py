"""
두 개를 고를 때, 무게가 달라야 함 -> 무게를 인덱스로 하는 리스트를 만들어 count
볼링공 "무게"의 조합이 아닌, 볼링공 "번호"의 조합임을 주의
"""

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

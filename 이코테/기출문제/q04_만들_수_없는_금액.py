"""
정렬을 이용한 그리디 알고리즘 (한정적인 동전 개수)
1.  오름차순 정렬
2.  1부터 target-1 까지의 모든 금액을 만들 수 있다고 가정하고,
    현재 확인하는 동전을 이용해 target 금액 또한 만들 수 있는지 확인
    (== 현재 확인하는 동전의 단위가 target 이하인지)
3.  만들 수 있다면 target 값 업데이트
"""

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

target = 1
for n in nums:
    if target < n:
        break
    target += n

print(target)

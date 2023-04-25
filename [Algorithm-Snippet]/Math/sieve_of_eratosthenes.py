import math

n = 1000 # 2부터 1000까지의 모든 수에 대해 소수 판별
array = [True for _ in range(n + 1)] # 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2 ~ n의 제곱근까지 모든 수 확인
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end= " ")

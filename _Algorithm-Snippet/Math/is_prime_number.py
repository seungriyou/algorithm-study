import math

# 소수 판별 함수
def is_prime_number(x):
    # 2 ~ x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 i로 나누어 떨어진다면 소수가 아님
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))
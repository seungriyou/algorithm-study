n = 10    # 2부터 n까지의 모든 수에 대해 소수 판별
is_prime = [True] * (n + 1)     # 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)
is_prime[0] = is_prime[1] = False   # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for i in range(2, int(n ** 0.5) + 1):   # 2 ~ n의 제곱근까지 모든 수 확인
    if is_prime[i]:  # 아직 남아있는 수
        for j in range(i * i, n + 1, i):  # 2부터 곱하면서 모든 배수를 확인하는 것보다 빠르다!
            is_prime[j] = False
            """
            왜 i에 2부터 곱해나가는 것이 아니라 i부터 곱해나갈까?
            i   j
            --- --- --- --- ---
            2   2*2 2*3 2*4 2*5 ...
            3   3*3 3*4 3*5 3*6 ... -> (3*2)는 i=2에서 처리함
            4   4*4 4*5 4*6 4*7 ... -> (4*2)는 i=2에서, (4*3)은 i=3에서 처리함
            => 더 빠른 속도 가능!
            """

# 모든 소수 출력
for i in range(2, n + 1):
    if is_prime[i]:
        print(i, end=' ')
print()

# 소수의 개수 출력
print(sum(is_prime))

# https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers/
# https://app.codility.com/demo/results/trainingTRCVDZ-NB4/

def solution(N, M):
    # N과 M의 gcd를 구하고,
    # 0부터 N까지의 수 중 gcd의 배수의 개수를 계산하면 된다.

    def gcd(n, m):
        if (r := n % m) == 0:
            return m
        else:
            return gcd(m, r)

    return N // gcd(N, M)

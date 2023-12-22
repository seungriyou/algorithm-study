# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
# https://app.codility.com/demo/results/trainingPX3ETK-TXD/

def solution(N):
    i = 2
    min_perimeter = 2 * (1 + N)

    while i * i <= N:
        if N % i == 0:
            min_perimeter = min(min_perimeter, 2 * (i + N // i))
        i += 1

    return min_perimeter

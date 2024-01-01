# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# https://app.codility.com/demo/results/trainingR9J54J-2V2/

def solution(A):
    # A 오름차순 정렬
    A.sort()

    # set a default value for smallest positive integer that does not occur in A
    spi = 1

    # A를 순회하면서, spi와 a 값이 같은 경우에 spi++ 해나가기
    for a in A:
        if spi == a:
            spi += 1

    return spi

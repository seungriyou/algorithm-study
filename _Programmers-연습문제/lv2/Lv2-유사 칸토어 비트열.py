# https://school.programmers.co.kr/learn/courses/30/lessons/148652

def solution(n, l, r):
    """
    - 매 번째마다 길이가 5배가 된다.
    - 유사 칸토어 비트열에서 5 * m + 2 번째의 비트는 무조건 0이다. (1 -> 11011, 0 -> 00000)
        - k 번째(0-based)의 비트를 5로 나누었을 때 나머지가 2이면, 그 자리는 0이다.
        - k < 5가 될 때까지 k를 5로 나누다가, k가 2가 아니라면 1, 2라면 0이다.
    """
    # l ~ r 번째 비트가 모두 1이라고 가정
    answer = r - l + 1

    for k in range(l - 1, r):
        while k > 0:
            k, r = divmod(k, 5)
            # k를 5로 나누었을 때 나머지가 2이면 그 자리는 0이므로 answer--
            if r == 2:
                answer -= 1
                break

    return answer

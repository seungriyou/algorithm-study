# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0

    # x = 0부터 d까지 +k씩 해가면서 확인
    for x in range(0, d + 1, k):
        # 현재 x에서, 피타고라스의 정리를 이용하여 가능한 가장 큰 y 값(= b*k, 정수) 구하기
        max_y = int((d * d - x * x) ** 0.5)
        # b(= max_y // k) 값을 구하고, b = 0도 가능하므로 + 1하여 answer 기록
        answer += max_y // k + 1

    return answer

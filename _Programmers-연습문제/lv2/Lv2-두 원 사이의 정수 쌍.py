# https://school.programmers.co.kr/learn/courses/30/lessons/181187

def solution(r1, r2):
    """
    r1^2 <= x^2 + y^2 <= r2^2 여야하므로, 다음의 방법으로 한 사분원(1사분면)에 속하는 정수 쌍 수를 구한다.
        (1) x = 1 ~ r2까지 살펴보며 해당 x 값과 두 원의 교점의 y좌표 y1, y2를 구한 뒤
            (x는 1부터 시작함으로써 y축 위의 정수 쌍은 세지 X, x축 위의 정수 쌍까지만 센다!)
        (2) y1 ~ y2 에 속하는 y 값 중 정수의 개수를 더해나감

    이렇게 구한 값에 4를 곱해준다.
    """
    answer = 0

    r12, r22 = r1 * r1, r2 * r2

    # x = 1 ~ r2 수직선을 그었을 때, 두 원과의 교점을 구하고 그 사이의 정수인 y값 개수 더하기
    # x = 1부터 시작해야 4 곱했을 때 중복 X
    for x in range(1, r2 + 1):
        # y1 & y2 값 구하기
        y1 = (r12 - x * x) ** 0.5 if x < r1 else 0
        y2 = (r22 - x * x) ** 0.5

        # y1는 ceil, y2는 floor 값 구하기
        y1 = int(y1) + 1 if y1 > int(y1) else int(y1)
        y2 = int(y2)

        # 사분원 내에 속하는 정수 쌍 수 더하기
        answer += y2 - y1 + 1

    return answer * 4

# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0

    while storey > 0:
        # 오른쪽 수부터 확인
        storey, move = divmod(storey, 10)

        # (1) 오른쪽 수가 5 초과이거나 (2) 5이면서 그 왼쪽 수가 5 이상이라면
        # 왼쪽 자리로 1 넘기기
        if move > 5 or (move == 5 and storey % 10 >= 5):
            move = 10 - move
            storey += 1
        answer += move

    return answer

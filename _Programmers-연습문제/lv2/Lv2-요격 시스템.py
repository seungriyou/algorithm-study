# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0
    bound = 0  # 현재의 요격 미사일로 격추 가능한 가장 오른쪽 경계값

    # targets의 end 기준으로 정렬(***)
    for start, end in sorted(targets, key=lambda x: x[1]):
        # start가 bound 범위를 벗어난다면 새로운 요격 미사일 추가
        if bound <= start:
            answer += 1
            bound = end

    return answer


def solution2(targets):
    answer = 0
    bound = 0  # 현재의 요격 미사일로 격추 가능한 가장 오른쪽 경계값

    for start, end in sorted(targets):
        # bound 범위 내에 start가 들어온다면, bound 값 업데이트
        if start < bound:
            bound = min(bound, end)
        # start가 bound 범위를 벗어난다면, 새로운 요격 미사일 추가
        else:
            bound = end
            answer += 1

    return answer

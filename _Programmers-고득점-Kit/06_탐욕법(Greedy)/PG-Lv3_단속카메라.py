# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준으로 오름차순 정렬
    answer = 0
    camera = -30_001  # 카메라의 현재 위치 초기화

    for s, e in routes:
        if camera < s:
            answer += 1  # 카메라의 현재 위치가 진입 지점보다 이전이면 새로운 카메라 필요
            camera = e

    return answer


def solution2(routes):
    routes.sort()
    intersections = []  # 교집합 구간을 모으는 리스트

    for route in routes:
        # 이전의 결과와 교집합을 구할 수 없는 경우
        if not intersections or intersections[-1][1] < route[0]:
            intersections.append(route)
        # 교집합을 구할 수 있는 경우, 업데이트
        else:
            intersections[-1] = [route[0], min(intersections[-1][1], route[1])]

    return len(intersections)

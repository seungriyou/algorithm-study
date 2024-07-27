# https://school.programmers.co.kr/learn/courses/30/lessons/169198

def solution(m, n, startX, startY, balls):
    """
    - 선대칭 활용
    - 꼭짓점에 부딪히는 경우에는 최소 거리가 될 수 없으므로 고려 X (ref: https://school.programmers.co.kr/questions/46119)
    """
    answer = []

    def get_powered_distance(p, q):
        return (startX - p) ** 2 + (startY - q) ** 2

    for p, q in balls:
        dist = 1e9
        # startX == p && startY > q: down 방향 불가
        if not (startX == p and startY > q):
            dist = min(dist, get_powered_distance(p, -q))
        # startX == p && startY < q: up 방향 불가
        if not (startX == p and startY < q):
            dist = min(dist, get_powered_distance(p, 2 * n - q))
        # startY == q && startX > p: left 방향 불가
        if not (startY == q and startX > p):
            dist = min(dist, get_powered_distance(-p, q))
        # startY == q && startX < p: right 방향 불가
        if not (startY == q and startX < p):
            dist = min(dist, get_powered_distance(2 * m - p, q))

        answer.append(dist)

    return answer

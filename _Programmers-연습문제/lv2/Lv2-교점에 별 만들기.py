# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    # ==== 정수 좌표인 교점 구하기 ====
    def get_int_intersection():
        for a, b, e in line:
            for c, d, f in line:
                g = a * d - b * c
                if g:
                    x, r1 = divmod(b * f - e * d, g)
                    y, r2 = divmod(e * c - a * f, g)
                    if not r1 and not r2:
                        yield (x, y)

    points = set(get_int_intersection())

    # ==== 별 찍기 ====
    xs, ys = list(zip(*points))

    def print_line(y):
        return "".join("*" if (x, y) in points else "." for x in range(min(xs), max(xs) + 1))

    return [print_line(y) for y in range(max(ys), min(ys) - 1, -1)]


def solution1(line):
    """for 문"""
    n = len(line)

    # ==== 정수 좌표인 교점 구하기 ====
    int_points = set()  # 정수 교점 좌표

    def get_int_intersection(i1, i2):
        a, b, e = line[i1]
        c, d, f = line[i2]

        # 교점 좌표 구하는 식의 분모로 들어갈 수
        dv = a * d - b * c

        # ZeroDivisonError인 경우에는 return
        if dv == 0:
            return

        # 교점의 좌표 구하기
        x, y = (b * f - e * d) / dv, (e * c - a * f) / dv

        # x, y가 모두 정수인 경우에만 기록
        if int(x) == x and int(y) == y:
            int_points.add((int(x), int(y)))

    for i in range(n - 1):
        for j in range(i + 1, n):
            get_int_intersection(i, j)

    # ==== 별 찍기 ====
    # 좌표의 최대/최소값 구하기
    borders = [[min(points), max(points)] for points in zip(*int_points)]
    x_min, x_max = borders[0]
    y_min, y_max = borders[1]

    # 별찍기용 2d list 만들기
    w, h = (x_max - x_min + 1), (y_max - y_min + 1)
    res = [["."] * w for _ in range(h)]

    # 각 좌표에서 (x_min, y_min)을 빼서 이동 후 res에 기록
    for x, y in int_points:
        res[h - (y - y_min + 1)][x - x_min] = "*"

    return ["".join(row) for row in res]


def solution2(line):
    """backtracking"""

    n = len(line)
    int_points = set()  # 정수 교점 좌표

    def get_int_intersection(i1, i2):
        a, b, e = line[i1]
        c, d, f = line[i2]

        # 교점 좌표 구하는 식의 분모로 들어갈 수
        dv = a * d - b * c

        # ZeroDivisonError인 경우에는 return
        if dv == 0:
            return

        # 교점의 좌표 구하기
        x, y = (b * f - e * d) / dv, (e * c - a * f) / dv

        # x, y가 모두 정수인 경우에만 기록
        if int(x) == x and int(y) == y:
            int_points.add((int(x), int(y)))

    # nC2 조합 -> 교점 좌표 구하기 -> 정수 좌표만 기록
    lines = []

    def backtrack(idx):
        # base condition
        if len(lines) == 2:
            get_int_intersection(*lines)
            return

        # recur
        for i in range(idx, n):
            lines.append(i)
            backtrack(i + 1)
            lines.pop()

    # ==== 정수 좌표인 교점 구하기 ====
    backtrack(0)

    # ==== 별 찍기 ====
    # 좌표의 최대/최소값 구하기
    borders = [[min(points), max(points)] for points in zip(*int_points)]
    x_min, x_max = borders[0]
    y_min, y_max = borders[1]

    # 별찍기용 2d list 만들기
    w, h = (x_max - x_min + 1), (y_max - y_min + 1)
    res = [["."] * w for _ in range(h)]

    # 각 좌표에서 (x_min, y_min)을 빼서 이동 후 res에 기록
    for x, y in int_points:
        res[h - (y - y_min + 1)][x - x_min] = "*"

    return ["".join(row) for row in res]

# https://school.programmers.co.kr/learn/courses/30/lessons/118670

def solution(rc, operations):
    from collections import deque

    nr, nc = len(rc), len(rc[0])

    center_rows = deque(deque(row[1:-1]) for row in rc)     # 양 side column을 제외한 rows
    side_rows = [deque(rc[i][0] for i in range(nr)),        # 양 side column (side_rows[0]: 왼쪽, side_rows[1]: 오른쪽)
                 deque(rc[i][-1] for i in range(nr))]

    for op in operations:
        if op == "ShiftRow":
            # center_rows
            center_rows.appendleft(center_rows.pop())
            # side_rows
            for side_row in side_rows:
                side_row.appendleft((side_row.pop()))

        elif op == "Rotate":
            center_rows[0].appendleft(side_rows[0].popleft())
            side_rows[1].appendleft(center_rows[0].pop())
            center_rows[-1].append(side_rows[1].pop())
            side_rows[0].append(center_rows[-1].popleft())

    result = []
    for ls, rs, cr in zip(side_rows[0], side_rows[1], center_rows):
        result.append([ls, *cr, rs])

    return result

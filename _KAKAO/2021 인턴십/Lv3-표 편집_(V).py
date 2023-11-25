# https://school.programmers.co.kr/learn/courses/30/lessons/81303

# TIP: linked list를 딕셔너리를 사용하여 쉽게 구현할 수 있다!!
def solution(n, k, cmd):
    table = {i: [i - 1, i + 1] for i in range(n)}  # [prev, next] -> linked list로 사용
    table[0][0] = table[n - 1][1] = None

    deleted = []
    answer = ["O"] * n
    curr = k  # 현재 선택된 행 위치

    for c in cmd:
        if c == "C":
            # delete
            p_pos, n_pos = table[curr]
            deleted.append((p_pos, curr, n_pos))
            answer[curr] = "X"

            # 현재 선택된 행 위치 변경 & table 업데이트
            if n_pos is None:       # (1) 맨 마지막 행 삭제
                curr = p_pos
                table[p_pos][1] = None
            else:
                curr = n_pos
                if p_pos is None:   # (2) 맨 처음 행 삭제
                    table[n_pos][0] = None
                else:               # (3) 중간 행 삭제
                    table[n_pos][0] = p_pos
                    table[p_pos][1] = n_pos


        elif c == "Z":
            # stack에서 가장 최근에 삭제된 행 복구
            p_pos, row, n_pos = deleted.pop()
            answer[row] = "O"

            # table 업데이트
            if p_pos is None:       # (1) 맨 처음 행 복구
                table[n_pos][0] = row
            elif n_pos is None:     # (2) 맨 마지막 행 복구
                table[p_pos][1] = row
            else:                   # (3) 중간 행 복구
                table[n_pos][0] = table[p_pos][1] = row


        else:  # 현재 선택된 행 위치 변경
            c1, c2 = c.split()

            if c1 == "U":
                for _ in range(int(c2)):
                    curr = table[curr][0]

            elif c1 == "D":
                for _ in range(int(c2)):
                    curr = table[curr][1]

    return "".join(answer)


def solution_tle(n, k, cmd):
    table = list(range(n))
    deleted = []

    for command in cmd:
        comm = command.split()
        op = comm[0]

        if op == "U":
            m = int(comm[1])
            k = max(0, k - m)

        elif op == "D":
            m = int(comm[1])
            k = min(len(table) - 1, k + m)

        elif op == "C":
            deleted.append((k, table.pop(k)))
            if k == len(table):
                k -= 1

        elif op == "Z":
            i, val = deleted.pop()
            table.insert(i, val)
            if k >= i:
                k += 1

    answer = ["O"] * len(table)

    while deleted:
        i, val = deleted.pop()
        answer.insert(i, "X")

    return "".join(answer)

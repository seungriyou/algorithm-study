# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0

    direc = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }
    visited = set()

    r, c = 0, 0

    for d in dirs:
        dr, dc = direc[d]
        nr, nc = r + dr, c + dc

        # nr, nc가 범위 넘어가지 않으면
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            # 해당 "길"이 이전에 방문되었으면 중복처리가 되어야 하므로, 양방향(A->B, A<-B)을 모두 visited에 넣기
            visited.add((r, c, nr, nc))
            visited.add((nr, nc, r, c))
            r, c = nr, nc

    return len(visited) // 2

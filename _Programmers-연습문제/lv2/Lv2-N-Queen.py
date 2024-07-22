# https://school.programmers.co.kr/learn/courses/30/lessons/12952
# https://leetcode.com/problems/n-queens/

def solution(n):
    """
    queen: 서로 같은 row / col / diag에 위치해서는 X

    - row 별로 진행함으로써, 같은 row에 겹치지 않도록 함
    - col, diag_lr(lower right), diag_ur(upper right)는 visited로 관리함으로써 겹치지 않도록 함
        - diag_lr: (r - c)가 같음
        - diag_ur: (r + c)가 같음
    """
    answer = 0

    visited_col = set()
    visited_diag_lr = set()  # (r - c) 같음
    visited_diag_ur = set()  # (r + c) 같음

    def dfs(r):
        nonlocal answer

        # base condition
        if r == n:
            answer += 1
            return

        # recur
        for c in range(n):
            diag_lr, diag_ur = r - c, r + c

            if not (c in visited_col or diag_lr in visited_diag_lr or diag_ur in visited_diag_ur):
                # col, diag_lr, diag_ur 기록
                visited_col.add(c)
                visited_diag_lr.add(diag_lr)
                visited_diag_ur.add(diag_ur)

                # 다음 row에 대해 dfs 수행
                dfs(r + 1)

                # col, diag_lr, diag_ur 기록 삭제
                visited_col.remove(c)
                visited_diag_lr.remove(diag_lr)
                visited_diag_ur.remove(diag_ur)

    dfs(0)

    return answer

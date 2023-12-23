# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/
# https://app.codility.com/demo/results/trainingJDFNQQ-3EA/

def solution(K, A):
    tied_rope = cnt = 0

    # 인접한 rope 끼리 묶을 수 있으므로, 정렬 없이 있는 순서 그대로
    for a in A:
        tied_rope += a
        if tied_rope >= K:
            cnt += 1
            tied_rope = 0

    return cnt

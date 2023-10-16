# [PG] 87946 - 피로도 (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution_bf(k, dungeons):
    # dungeons의 idx -> permutation 구하기
    # 각 permutation 순서대로 확인
    # 1. p = k에서 시작하여, permutation 내 idx 순서대로 순회하며 다음을 반복
    # 2. p >= d[0]이면
    # 3. p -= d[1] & num ++

    n = len(dungeons)
    pers = list(permutations(range(n)))  # -- dungeons의 idx로 만든 permutation
    max_num = 0  # -- 최대 던전 수

    for per in pers:
        p = k  # 이번 permutation에서의 시작 피로도 setting
        num = 0  # 이번 permutation에서의 탐험 던전수 초기화
        for i in range(n):
            d = dungeons[per[i]]  # 현재 idx가 가리키는 dungeon
            if p >= d[0]:  # 현재 피로도 >= 최소 필요 피로도이면
                p -= d[1]  # 현재 피로도에서 소모 피로도를 빼고
                num += 1  # 탐험 던전수 ++
        max_num = max(max_num, num)  # permutation 하나를 마쳤으므로, 해당 permutation의 순서대로 던전을 탐험했을 때의 탐험 던전수를 통해 최대 던전수 업데이트

    return max_num


def solution(k, dungeons):
    # === DFS (Backtracking) ===

    max_num = 0
    n = len(dungeons)
    visited = [False] * n

    def dfs(k, cnt):
        nonlocal max_num

        if cnt > max_num:
            max_num = cnt

        for i in range(n):
            if dungeons[i][0] <= k and not visited[i]:
                visited[i] = True
                dfs(k - dungeons[i][1], cnt + 1)
                visited[i] = False

    dfs(k, 0)

    return max_num


k = 80
dungeons = [[80,20],[50,40],[30,10]]
assert 3 == solution(k, dungeons) == solution_bf(k, dungeons)

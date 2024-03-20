# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    """
    어떤 선수의 순위를 알기 위해서는 다른 모든 선수들과의 경기 결과를 알면 된다!
    """

    match = [[None] * n for _ in range(n)]

    # 알고 있는 경기 결과
    for win, lose in results:
        match[win - 1][lose - 1] = 1  # 이김
        match[lose - 1][win - 1] = -1  # 짐

    # floyd-warshall 응용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # (i+1, k+1) 사이, 혹은 (k+1, j+1) 사이의 결과를 알 수 없다면, 넘어가기
                if match[i][k] is None or match[k][j] is None:
                    continue

                # (i+1, k+1) 사이와 (k+1, j+1) 사이의 결과가 동일하다면, (i+1, j+1) 사이의 결과를 알 수 있음
                if match[i][k] == match[k][j]:
                    match[i][j] = match[i][k]
                    match[j][i] = -match[i][k]

    # match에서 각 선수별로 다른 선수들과의 경기 결과를 보며 자신이 이기는지(row), 지는지(col) 여부를 확인했을 때,
    # 결과를 알 수 없는 경우(None)가 단 하나도 없어야 해당 선수의 순위를 정확하게 매길 수 있다.
    answer = 0
    for i in range(n):
        if not None in set(match[i][:i] + match[i][i + 1:]):
            answer += 1

    return answer

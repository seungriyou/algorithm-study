# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    """
    1. 조이스틱을 좌우로 이동하는 것과 상하로 이동하는 것을 각각 구한다.
    2. 좌우 이동의 경우, 방향은 한 번 이하로 변경해야 최소 조작으로 변경할 수 있다.
        - 가장 처음으로 등장하는 'A'로만 이루어진 부분 문자열을 기준으로, 왼쪽의 문자 개수(left)와 오른쪽의 문자 개수(right)를 구하자.
        - 다음의 세 가지 경우 중 최솟값을 구하면 된다.
            (1) 방향 변경 없이 한 방향으로만 이동     : _len - 1
            (2) 오른쪽으로 가다가 왼쪽으로 변경       : left * 2 + right
            (3) 왼쪽으로 가다가 오른쪽으로 변경       : right * 2 + left
    3. 상하 이동의 경우, ascii 코드를 사용한다.
    """

    _len = len(name)
    min_cnt = _len - 1

    # <1> 좌우 이동
    i = 1  # 첫 번째 문자는 좌우 이동 없이 가능하므로 인덱스 1부터 시작
    while i < _len:
        if name[i] == 'A':
            left = i - 1  # 'A'로 이루어진 부분 문자열의 왼쪽 부분의 길이
            while i < _len and name[i] == 'A':
                i += 1
            right = _len - i  # 'A'로 이루어진 부분 문자열의 오른쪽 부분의 길이

            min_cnt = min(min_cnt, left * 2 + right, right * 2 + left)

        else:
            i += 1

    # <2> 상하 이동
    for n in name:
        min_cnt += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)

    return min_cnt

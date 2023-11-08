# https://school.programmers.co.kr/learn/courses/30/lessons/17677

# import re
from collections import Counter


def solution(str1, str2):
    """
    자카드 유사도 = J(A, B) = 교집합 크기 / 합집합 크기
    A와 B가 모두 공집합일 때는 나눗셈 정의 X -> J(A, B) = 1
    다중집합에 대해서도 확장 가능
    문자열에 대해서는, 두 글자씩 끊어서 다중집합 구성 후 자카드 유사도 구할 수 있음
    두 글자 중 공백/숫자/특수문자 있는 경우 버림
    case-sensitive X
    """

    # c = re.compile('[^a-z]+')

    # 영문 소문자로만 이루어진 다중집합 만드는 함수
    def get_multi_set(s):
        multi_set = []
        for i in range(1, len(s)):
            substr = s[i - 1:i + 1].lower()
            # if not re.search(c, substring):
            if substr.isalpha():    # -- isalpha() 까먹지 말자~
                multi_set.append(substr)
        return multi_set

    ms1 = get_multi_set(str1)
    ms2 = get_multi_set(str2)
    if not ms1 and not ms2:
        return 65536

    cnt1 = Counter(ms1)
    cnt2 = Counter(ms2)

    substrs = set(ms1 + ms2)
    inter = union = 0
    for k in substrs:
        v1 = cnt1.get(k, 0)
        v2 = cnt2.get(k, 0)
        if v1 < v2:
            inter += v1
            union += v2
        else:
            inter += v2
            union += v1
        # inter += min(v1, v2)
        # union += max(v1, v2)

    return int(inter / union * 65536)

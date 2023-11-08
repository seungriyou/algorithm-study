# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    """
    길이가 작은 것부터 확인해나가면 된다.
    """
    answer = []
    str_sets = s[2:-2].split("},{")
    sets = [set(map(int, str_set.split(","))) for str_set in str_sets]
    sets.sort(key=len)

    prev = set()
    for se in sets:
        answer.extend(se - prev)
        prev = se

    return answer

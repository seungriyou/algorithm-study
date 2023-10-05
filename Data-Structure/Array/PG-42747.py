# [PG] 42747 - H-Index (Lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for c in citations:
        if c > h_index:
            h_index += 1
    return h_index


def solution1(citations):
    """
    citations = [3, 0, 6, 1, 5] 일 때,
    enumerate(citations, start=1)
    -> 	(1, 6)
        (2, 5)
        (3, 3)
        (4, 1)
        (5, 0)
    ->  idx 부분은 citations[idx-1] 이상인 값의 개수를 나타내고,
        value 부분은 citations[idx-1:]의 최댓값을 나타낸다.
    ->  따라서 이것의 min 값을 구하면 각 위치에서 가능한 h 값을 구할 수 있다.
        [1, 2, 3, 1, 0]
    ->  여기에서 max를 구해 h의 최대값을 구한다.
    """
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))


def solution2(citations):
    citations.sort(reverse=True)

    for h in range(min(citations[0], len(citations)), -1, -1):
        if h == len(citations) and citations[h - 1] >= h:
            break

        if citations[h - 1] >= h and citations[h] <= h:
            break

    return h


citations = [3, 0, 6, 1, 5]
assert 3 == solution(citations) == solution1(citations) == solution2(citations)

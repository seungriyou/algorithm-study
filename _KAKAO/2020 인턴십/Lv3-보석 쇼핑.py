# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    from collections import defaultdict

    gem_type_n = len(set(gems))  # 보석 종류의 개수
    gem_n = len(gems)  # gems의 길이
    cnt = defaultdict(int)  # gems[lo:hi] 구간 내에 속하는 보석 종류와 그 개수

    lo = hi = 0
    min_len = 100_001
    min_range = None

    while lo < gem_n:
        # [lo:hi] 구간에 모든 종류의 보석이 존재한다면, gems[lo]를 cnt에서 빼고 lo++
        if len(cnt) == gem_type_n:
            # 조건을 만족하는 가장 짧은 구간 업데이트
            if hi - lo < min_len:
                min_range = [lo + 1, hi]  # 진열대는 1-based index이므로, [lo:hi]에 해당하는 범위가 (lo, hi - 1)가 아닌 (lo + 1, hi)
                min_len = hi - lo

            if cnt[gems[lo]] > 1:
                cnt[gems[lo]] -= 1
            else:
                del cnt[gems[lo]]
            lo += 1

        # [lo:hi] 구간에 모든 종류의 보석이 존재하지 않고 hi가 gems를 벗어나지 않는다면, gems[hi]를 cnt에 넣고 hi++
        elif hi < gem_n:
            cnt[gems[hi]] += 1
            hi += 1

        # 위의 두 조건을 모두 만족하지 않는다면 빠르게 종료
        else:
            break

    return min_range

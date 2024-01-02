# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

# 첫 번째 풀이(66%, O(N * M)): https://app.codility.com/demo/results/training89UMB8-DGJ/
def solution(S, P, Q):
    result = []
    mapping = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    for p, q in zip(P, Q):
        min_impact = 5

        for i in range(p, q + 1):
            min_impact = min(min_impact, mapping[S[i]])
        result.append(min_impact)

    return result


# 두 번째 풀이(100%, O(N + M)): https://app.codility.com/demo/results/trainingDTMWBK-EZP/
# ref: https://jackjeong.tistory.com/entry/Codility%EC%BD%94%EB%94%9C%EB%A6%AC%ED%8B%B0-Lesson5-GenomicRangeQuery-100
def solution(S, P, Q):
    # i를 0 ~ N까지 늘려가며 S[:i]에 등장하는 각 타입 별로 카운트 수행
    # prefix sum의 아이디어를 활용하면, substring의 카운트 결과를 쉽게 구할 수 있음 (이중 for문 없이)

    # cnt 리스트에서 각 문자가 해당하는 index 값 (= impact factor - 1)
    mapping = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    result = []

    # cnt 값은 [A, C, G, T] 형태로
    cnt = [0, 0, 0, 0]
    cnts = [cnt[:]]
    for s in S:
        cnt[mapping[s]] += 1
        cnts.append(cnt[:])

    for p, q in zip(P, Q):
        # O(N) * O(1) = O(N)
        for i in range(4):
            # prefix sum 아이디어 적용
            if cnts[q + 1][i] - cnts[p][i] > 0:
                # impact factor는 mapping 값(= cnt 내 해당하는 index 값)에 1을 더한 값이므로
                result.append(i + 1)
                break

    return result

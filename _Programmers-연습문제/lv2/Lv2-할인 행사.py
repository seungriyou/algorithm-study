# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    want_cnt = {w: n for w, n in zip(want, number)}

    # first window
    cnt = {}
    for i in range(10):
        if discount[i] in cnt:
            cnt[discount[i]] += 1
        else:
            cnt[discount[i]] = 1

    answer += (cnt == want_cnt)

    for i in range(10, len(discount)):
        # left
        j = i - 10
        cnt[discount[j]] -= 1
        if cnt[discount[j]] == 0:
            del cnt[discount[j]]

        # right
        if discount[i] in cnt:
            cnt[discount[i]] += 1
        else:
            cnt[discount[i]] = 1

        answer += (cnt == want_cnt)

    return answer


def solution1(want, number, discount):
    answer = 0
    want_cnt = {w: n for w, n in zip(want, number)}

    for i in range(len(discount) - 9):
        cnt = {}
        for j in range(10):
            if discount[i + j] not in cnt:
                cnt[discount[i + j]] = 1
            else:
                cnt[discount[i + j]] += 1

        answer += (cnt == want_cnt)

    return answer

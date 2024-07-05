# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    """
    멈추는 경우
    (1) 이전에 나온 단어가 다시 나올 때 -> seen set()
    (2) 바로 앞 단어의 끝 글자로 시작하지 않을 때
    """
    _len = len(words)
    seen = {words[0]}

    for i in range(1, _len):
        turn, order = divmod(i, n)

        # (1) 이전에 나온 단어가 다시 나올 때 (2) 바로 앞 단어의 끝 글자로 시작하지 않을 때
        if (words[i] in seen) or (words[i - 1][-1] != words[i][0]):
            return [order + 1, turn + 1]

        seen.add(words[i])

    return [0, 0]


def solution1(n, words):
    """
    멈추는 경우
    (1) 이전에 나온 단어가 다시 나올 때 -> seen set()
    (2) 바로 앞 단어의 끝 글자로 시작하지 않을 때
    """

    turns = len(words) // n + (1 if len(words) % n else 0)
    seen = set()

    for turn in range(turns):
        for i in range(n):
            idx = turn * n + i

            # (1) 이전에 나온 단어가 다시 나올 때 (2) 바로 앞 단어의 끝 글자로 시작하지 않을 때
            if (words[idx] in seen) or (idx > 0 and words[idx - 1][-1] != words[idx][0]):
                return [i + 1, turn + 1]

            seen.add(words[idx])

    return [0, 0]

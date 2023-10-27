# [PG] 43163 - 단어 변환 (Lv3)
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    from collections import deque

    def get_neighbor(curr):
        for word in words:
            cnt = 0
            for i, j in zip(curr, word):
                cnt += i != j
            if cnt == 1:
                yield word

    q = deque([(begin, 0)])
    visited = set([begin])

    while q:
        curr, cnt = q.popleft()

        if curr == target:
            return cnt

        for ngbr in get_neighbor(curr):
            if ngbr not in visited:
                visited.add(ngbr)
                q.append((ngbr, cnt + 1))

    return 0


def solution2(begin, target, words):
    from collections import deque

    def get_neighbor(curr):
        # 비교할 word와 한 글자만 다른 단어
        for word in words:
            cnt = 0

            for i, j in zip(curr, word):
                cnt += i != j

            if cnt == 1:
                yield word

    q = deque([begin])
    result = {begin: 0}

    while q:
        curr = q.popleft()

        if curr == target:
            break

        for ngbr in get_neighbor(curr):
            if ngbr not in result:  # ngbr가 not visited
                q.append(ngbr)
                result[ngbr] = result[curr] + 1

    return result.get(target, 0)


def solution1(begin, target, words):
    from collections import deque

    n = len(begin)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    words_set = set(words)

    q = deque([(begin, 0)])

    while q:
        word, cnt = q.popleft()

        if word == target:  # target으로 변환 완료되면 return
            return cnt

        for i in range(n):  # 첫 자리부터
            for l in letters:  # 알파벳 하나씩 넣어보기
                temp = word[:i] + l + word[i + 1:]
                if temp in words_set:  # 만약 words에 있는 단어였다면
                    words_set.remove(temp)  # 해당 단어 삭제 (다시 방문할 필요 X)
                    q.append((temp, cnt + 1))  # cnt++ 하여 q에 넣기

    return 0

begin = "hit"
target = "cog"
words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]

assert 4 == solution(begin, target, words1) == solution1(begin, target, words1) == solution2(begin, target, words1)
assert 0 == solution(begin, target, words2) == solution1(begin, target, words2) == solution2(begin, target, words2)

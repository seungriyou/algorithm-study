# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer, word = [], ""

    for i in s:
        # 공백 문자와 마주치면, 현재까지 모은 word를 추가 후 word 초기화
        if i == " ":
            answer.append(word.capitalize())
            word = ""
        # 공백 문자가 아니라면, word 모으기
        else:
            word += i

    answer.append(word.capitalize())

    return " ".join(answer)


def solution1(s):
    answer = []
    i, n = 0, len(s)

    while i < n:
        if s[i] == " ":
            answer.append(s[i])
            i += 1
            continue

        tmp = []
        while i < n and s[i] != " ":
            tmp.append(s[i])
            i += 1

        answer.append("".join(tmp).capitalize())

    return "".join(answer)
